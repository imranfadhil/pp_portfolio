# Summary of Petrophysical Analysis for Block 30/7

The analysis follows a comprehensive petrophysical workflow, starting from data loading and quality control, moving through lithology, porosity, permeability, and saturation modeling, and concluding with reservoir summary and visualization. The quick-pp library is central to the entire process.

Here is a step-by-step breakdown of the workflow:

## 1. Data Loading and Preparation (`01_data_handler.ipynb`)

*   **Data Aggregation**: Well log data from multiple LAS files, core analysis data (`.xls`), formation tops (`.xlsx`), and deviation surveys are loaded.
*   **Project Creation**: A `Project` object from the `quick_pp` library is created to manage all the well data.
*   **Data Cleaning**:
    *   Depth units are converted from feet to meters.
    *   Neutron Porosity (`NPHI`) is scaled from percent to a fractional value.
    *   Composite curves for Gamma Ray (`GR`) and Resistivity (`RT`) are created by coalescing different tool measurements (e.g., `GRL`, `ILD`, `LLD`).
*   **Data Merging**:
    *   Core data (porosity and permeability) is depth-matched to the log data using `pandas.merge_asof`.
    *   Formation tops are merged to assign geological zones to the log data.
    *   Deviation surveys are processed using the `wellpathpy` library to calculate True Vertical Depth (`TVD`) and True Vertical Depth Sub-Sea (`TVDSS`) for each well.
*   **Saving**: The consolidated and cleaned dataset is saved back into the `.qppp` project file for use in subsequent steps.

## 2. Exploratory Data Analysis (EDA) (`01b_EDA.ipynb`)

*   **Data Profiling**: The `ydata-profiling` library is used to generate detailed statistical and visual reports for the entire dataset and for each well individually. This helps in understanding data completeness, distributions, and potential outliers.
*   **Distribution Analysis**: Key petrophysical logs (`GR`, `RT`, `NPHI`, `RHOB`) are plotted as Kernel Density Estimates (KDE) to compare their distributions across different wells, highlighting variations in reservoir properties throughout the field.

## 3. Lithology and Porosity Estimation (`02_lithology_porosity.ipynb` & `02b_lithology_multi_mineral.ipynb`)

The analysis is performed separately on clastic (sandshale) and carbonate intervals, as defined by a pre-existing model column.

*   **Sand-Shale & Carbonate Models**: A two-mineral (sand-shale) and a three-mineral (calcite-dolomite-shale) model are used.
*   **Hydrocarbon Correction**: Neutron-Density logs are corrected for hydrocarbon effects using standard cross-plot techniques before being used for lithology and porosity calculations.
*   **Porosity Calculation**: Total Porosity (`PHIT`) is primarily derived from the Neutron-Density cross-plot. Density Porosity (`PHID`) is also calculated and used to fill gaps.
*   **Effective Porosity (`PHIE`)**: Calculated by subtracting the clay-bound water volume (`VCLB`) from the total porosity (`PHIT`).
*   **Core-to-Log Depth Shifting**:
    *   A significant mismatch was observed between the calculated log porosity (`PHIT`) and core porosity (`CPORE`).
    *   **Dynamic Time Warping (DTW)** is employed to find the optimal depth shift for core data by aligning the `CPORE` and `PHIT` curves. This significantly improves the correlation.
    *   The core data (`CPORE`, `CPERM`) is shifted to its new, corrected depth in the final dataset.
*   **Multi-Mineral Analysis**: An alternative approach using a multi-mineral solver (`MultiMineral`) is explored in `02b_lithology_multi_mineral.ipynb`. This solver uses `GR`, `NPHI`, `RHOB`, `PEF`, and `DTC` logs to estimate mineral and fluid volumes simultaneously, providing a more detailed lithological breakdown.

## 4. Rock Typing and Permeability Modeling (`03_rock_typing_perm.ipynb`)

*   **Rock Typing**:
    *   The **Flow Zone Indicator (FZI)** method is used for rock typing based on core porosity and permeability.
    *   Statistical methods like the **Modified Lorenz plot** are used to determine the optimal number of rock types and their corresponding FZI cutoffs.
*   **Machine Learning for Prediction**: Two machine learning models are trained on the core data:
    *   A classification model to predict the rock type (`ROCK_FLAG`) from log data (`VCLAY`, `PHIE`, etc.).
    *   A regression model to predict the `FZI` value itself from log data and the predicted rock type.
*   **Permeability Estimation**:
    *   The predicted `FZI` is used to calculate a continuous permeability curve (`PERM`) for all wells, including non-cored intervals. This method is chosen over traditional porosity-permeability transforms for better accuracy.
    *   The final permeability curve shows a good match with the depth-shifted core permeability data.

## 5. Water Saturation Modeling (`04_saturation.ipynb`)

*   **Parameter Estimation**:
    *   A **Pickett plot** is used to interactively determine the cementation exponent (`m`).
    *   Formation water resistivity (`Rw`) is estimated based on formation temperature and a given water salinity (100,000 ppm).
*   **Saturation Calculation**:
    *   The **Waxman-Smits model** is chosen to calculate water saturation (`SWT`) because it accounts for the conductivity of shale. Key parameters like the equivalent counter-ion concentration (`Qv`) and the shale term (`B`) are estimated from log data.
    *   The calculated `SWT` is clipped between 0 and 1 and applied to all wells.

## 6. Reservoir Summary and Final Plots (`05_ressum_plot.ipynb`)

*   **Final Computations**: Net pay flags, hydrocarbon pore volume (`BVW`, `VHC`), and other summary properties are calculated.
*   **Reservoir Summary (ResSum)**: A zone-by-zone summary of key reservoir properties (Gross, Net, Net/Gross, Avg Porosity, Avg Sw, etc.) is computed for each well using defined petrophysical cutoffs (e.g., `VSHALE` < 0.7, `PHIT` > 0.2).
*   **Visualization**:
    *   Comprehensive multi-track log plots are generated for each well, displaying input logs, interpreted lithology, porosity, permeability, and saturation curves.
    *   A field-wide stick plot is created to visualize fluid contacts (e.g., `ODT`, `WUT`) and their consistency across the wells.

This structured workflow ensures that the final petrophysical properties are well-calibrated to core data and consistently applied across the entire field, providing a robust basis for subsequent reservoir modeling and volumetric analysis.

`TODO`
1. Add insights from each sections.
2. Add summary of results.
3 ...