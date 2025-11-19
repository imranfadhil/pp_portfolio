import pandas as pd
import hashlib
import matplotlib.pyplot as plt
import numpy as np


from quick_pp.rock_type import estimate_pore_throat


def restructure_scal_data(df_wide):
    """
    Restructures a SCAL dataset from a wide format (multiple Pc/Sw columns per depth)
    to a long format (one Pc/Sw pair per row).

    Args:
        df_wide (pd.DataFrame): The input DataFrame in wide format.

    Returns:
        pd.DataFrame: The restructured DataFrame in long format.
    """
    # Identify columns to rename
    columns = df_wide.columns
    new_columns = {}
    for col in columns:
        if col.startswith("Pc") or col.startswith("Sw"):
            new_col = col.split("_")[0]
            new_col = f"{new_col[:2]}.{new_col[-1]}"
            new_columns[col] = new_col

    df_temp = df_wide.rename(columns=new_columns)

    # 2. Apply the wide_to_long function
    cols = ["Well", "Sample ID", "Depth_m", "K_mD", "PHI_frac"]
    df_long = pd.wide_to_long(
        df_temp,
        # The 'stubnames' are the prefixes we want to turn into columns
        stubnames=["Pc", "Sw"],
        # 'i' is the column that identifies the groups/rows (Depth)
        i=cols,
        # 'j' is the new column that holds the suffix (the measurement index)
        j="Measurement_Index",
        # The separator used between the stubname and the suffix (e.g., Pc.1 uses '.')
        sep=".",
    ).reset_index()

    # 3. Clean up the resulting data

    # Remove rows where all the newly created measurement columns are NaN (if any exist)
    df_long.dropna(subset=["Pc", "Sw"], how="all", inplace=True)

    # Sort by Depth and Measurement_Index for clean viewing (optional)
    df_long.sort_values(
        by=["Well", "Sample ID", "Depth_m", "Measurement_Index"], inplace=True
    )

    # Finalize columns for output
    df_final = df_long[cols + ["Pc", "Sw"]].copy()

    # Reset index and return
    df_final.reset_index(drop=True, inplace=True)

    return df_final


def string_to_int_hash(s):
    if pd.isna(s):  # Handle NaN values
        return None
    # Use SHA256 for stability across runs
    hash_obj = hashlib.sha256(s.encode("utf-8"))
    # Convert first 8 bytes to integer (fits in 64-bit)
    return int.from_bytes(hash_obj.digest()[:4], "big", signed=False)


def ptsd(df, ift, theta):
    copy_df = df.copy()

    # It's better to calculate on a sorted temporary dataframe
    # to ensure np.gradient works as expected.
    temp_dfs = []
    for sample, data in copy_df.groupby("Sample"):
        # Sort by PC to ensure monotonic change in R and LOG_R
        data = data.sort_values("PC", ascending=True).copy()
        r = estimate_pore_throat(data["PC"], ift, theta)
        log_r = np.log10(r)
        # dSw/dLogR should be negative. We plot -dSw/dLogR.
        dsw = -np.gradient(data["SW"], log_r)
        data["R"] = r
        data["LOG_R"] = log_r
        data["DSW"] = dsw
        temp_dfs.append(data)

    if not temp_dfs:
        print("No data to plot.")
        return

    processed_df = pd.concat(temp_dfs)

    fig, axes = plt.subplots(4, 3, figsize=(15, 17))
    axes = axes.flatten()
    for i in range(5):
        rock = i + 1
        data = processed_df[processed_df.ROCK_FLAG == rock]
        if data.empty:
            continue  # Skip rock types with no data
        ax = axes[i]
        for sample, sample_data in data.groupby("Sample"):
            ax.plot(
                sample_data["LOG_R"],
                sample_data["DSW"],
                label=f"Sample {sample}",
                zorder=-1,
            )
            color = ax.lines[-1].get_color()
            ax.fill_between(
                sample_data["LOG_R"], sample_data["DSW"], color=color, alpha=0.9
            )

        ax.set_title(f"PRT {int(rock)}")
        ax.set_xlabel("Log Pore Throat Radius (microns)")
        ax.set_xlim(-2, 2)
        ax.set_ylabel("-dSw/dLogR")
        ax.legend(loc=2, prop={"size": 5})

    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    fig.set_facecolor("aliceblue")
    plt.tight_layout()

    processed_df.to_excel("ptsd.xlsx")
    return processed_df
