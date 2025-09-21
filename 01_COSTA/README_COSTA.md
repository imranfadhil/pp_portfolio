# Summary of Petrophysical Analysis

This project performs a complete petrophysical analysis of the COSTA dataset, which appears to be a carbonate reservoir. The workflow starts with data loading and preparation, moves through detailed petrophysical calculations and machine learning model development, and concludes with volume estimation and uncertainty analysis.

Here is a summary of each notebook in order:

*   **01_data_handler.ipynb:** This notebook initializes the project by finding and loading all the well data (`.las` files) into a `quick_pp` Project object. This creates a centralized data repository for the subsequent analysis.

*   **02_EDA.ipynb:** This notebook performs Exploratory Data Analysis (EDA) on the loaded data. It generates comprehensive profiling reports for the entire dataset and for individual wells, allowing for a first look at the data quality and distribution of petrophysical properties. It also compares wells and visualizes log distributions.

*   **03_lithology_porosity.ipynb:** This notebook details the process of estimating lithology and porosity for a single well. It explains the challenges of carbonate reservoirs and uses neutron-density crossplots and hydrocarbon correction to determine the rock composition (calcite, dolomite, clay) and porosity. The results are validated against core data.

*   **04_rock_typing_fzi.ipynb:** This notebook focuses on classifying the reservoir rock into different types based on the Flow Zone Indicator (FZI). It determines FZI cutoffs from core data and then trains machine learning models to predict both the rock type (`ROCK_FLAG`) and the FZI value from well logs. It also develops permeability-porosity relationships for each rock type.

*   **05_saturation_j_fzi.ipynb:** This notebook tackles water saturation estimation. It calculates water saturation using the Archie equation from logs (`SWT`) and also develops a saturation-height function (SHF) based on capillary pressure data (Leverett J-function) for each rock type. This allows for a more geologically consistent water saturation model.

*   **06_a_single.ipynb:** This notebook consolidates the entire workflow for a single well. It applies the developed models and methods to calculate a full suite of petrophysical properties: lithology, porosity, permeability, rock type, and water saturation. It serves as a template for the batch processing.

*   **06_b_batch.ipynb:** This notebook automates the petrophysical interpretation for all wells in the project. It iterates through each well, applies the complete workflow developed in the previous notebooks, and saves the results. It then performs a comprehensive QC of the results, comparing the estimated properties with core data and across all wells, and generates numerous plots and error metrics.

*   **07_volume_uncertainty.ipynb:** This final notebook uses the petrophysical results to estimate the hydrocarbon volume in place. It uses a Monte Carlo simulation to perform an uncertainty analysis, providing a probabilistic range of the estimated volumes. It also includes a sensitivity analysis to understand which parameters have the most significant impact on the final volume calculation.

In short, the notebooks represent a complete petrophysical evaluation workflow, from raw data to uncertainty analysis, leveraging both traditional petrophysical methods and machine learning.
