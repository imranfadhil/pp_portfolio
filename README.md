# pp_portfolio

Welcome to my Petrophysical Portfolio! This repository showcases a collection of hands-on petrophysical analysis projects, demonstrating a complete workflow from raw data processing to reservoir characterization and volume estimation.

The primary tool used for these analyses is the `quick_pp` Python package, supplemented by other data science libraries for machine learning and data visualization.

## Projects

### 1. COSTA Dataset - Carbonate Reservoir Analysis

This project performs a complete petrophysical evaluation of the COSTA dataset, which represents a carbonate reservoir. The workflow is broken down into a series of Jupyter notebooks, each tackling a specific stage of the analysis.

*   **01_data_handler:** Loads well data (`.las` files) into a centralized `quick_pp` Project.
*   **02_EDA:** Performs Exploratory Data Analysis (EDA) with `ydata-profiling` to assess data quality and distributions.
*   **03_lithology_porosity:** Estimates lithology (calcite, dolomite, clay) and porosity using neutron-density crossplots and hydrocarbon correction, validated against core data.
*   **04_rock_typing_fzi:** Classifies the reservoir using the Flow Zone Indicator (FZI). It involves training ML models to predict rock types and developing permeability-porosity relationships.
*   **05_saturation_j_fzi:** Calculates water saturation using both the Archie equation and a saturation-height function derived from capillary pressure data (Leverett J-function).
*   **06_a_single & 06_b_batch:** Consolidates the workflow for a single well and then applies it in batch mode to all wells in the project.
*   **07_volume_uncertainty:** Estimates hydrocarbon volume in place (STOIIP) and performs a Monte Carlo simulation for uncertainty and sensitivity analysis.

For a detailed summary of this project, please see the [COSTA Project README](01_COSTA/README.md).

---

### 2. Volve Dataset - Clastic Reservoir Analysis

This project presents a comprehensive petrophysical analysis of the public Volve dataset, representing a shallow marine sandstone reservoir from the North Sea. The workflow demonstrates an end-to-end process from data ingestion and quality control to advanced rock typing and permeability modeling using machine learning.

*   **01_data_handler.ipynb**: Data loading, cleaning, and consolidation from various sources (LAS, Excel) into a unified project file.
*   **02_lithology_porosity.ipynb**: Log conditioning and calculation of fundamental petrophysical properties like lithology (VCLAY) and porosity (PHIT).
*   **03_rock_typing_perm.ipynb**: Advanced reservoir characterization using the Flow Zone Indicator (FZI) for rock typing and machine learning to predict permeability.
*   **04_saturation.ipynb**: Estimation of water saturation using the Normalized Waxman-Smits equation.
*   **05_ressum_plot.ipynb**: Generation of final reservoir summary reports and interactive log plots.

For a detailed summary of this project, please see the [Volve Project README](02_VOLVE/README.md).

---

*(More projects will be added here as they are completed.)*

## Tech Stack

*   **Language:** Python 3.11
*   **Core Petrophysics Package:** `quick-pp`
*   **Data Analysis & ML:** `pandas`, `scikit-learn`, `ydata-profiling`
*   **Visualization:** `plotly`, `matplotlib`, `seaborn`
*   **Environment:** Jupyter Notebooks

## Installation

To run these notebooks, you can clone the repository and install the required packages:

```bash
git clone https://github.com/imranfadhil/pp_portfolio.git
cd pp_portfolio

# Create and activate a virtual environment
uv venv --python 3.11
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate

# Install the dependencies
uv pip install -r requirements.txt
```
