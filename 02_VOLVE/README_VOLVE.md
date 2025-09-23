# Petrophysical Analysis on the Volve Dataset

This project presents a quick petrophysical analysis of the Volve dataset, leveraging the `quick-pp` library. The workflow spans from initial data ingestion and preparation to petrophysical property estimation, including lithology, porosity, permeability, and water saturation. The analysis is structured across several Jupyter notebooks, each tackling a specific stage of the interpretation process.

### Geological Background

###  Focused Wells


### 1. Data Ingestion and Preparation (`01_data_handler.ipynb`)

The initial phase focused on consolidating various data sources into a unified project structure.

*   **Data Loading**: Well log data from multiple LAS files were read and aggregated.
*   **Core Data Integration**: Routine core analysis (RCA) data (porosity and permeability) from Excel files for wells `15-9-19-A` and `15-9-19-BT2` were loaded and merged with the log data based on depth.
*   **Facies Data Integration**: Lithofacies information from Excel files was processed and merged with the log data, providing geological context for subsequent analysis.
*   **Project Creation**: All consolidated data was saved into a single `quick-pp` project file (`VOLVE.qppp`) for streamlined access in later stages.

### 2. Lithology and Porosity Estimation (`02_lithology_porosity.ipynb`)

This notebook demonstrates the fundamental petrophysical evaluation for a single well (`15-9-19-A`).

*   **Log Conditioning**: The log data was pre-processed, which included badhole flagging and hydrocarbon correction on neutron (NPHI) and density (RHOB) logs to ensure accurate lithology and porosity calculations.
*   **Lithology Estimation**: A Sand-Shale (`ss`) model was used to estimate the volume of sand and clay (`VSAND`, `VCLAY`) from the corrected NPHI and RHOB logs.
*   **Porosity Calculation**: Total porosity (`PHIT`) was calculated using the neutron-density crossplot method. The results were benchmarked against available core porosity (`CPORE`), showing a good correlation with an R² score of 0.81.

### 3. Rock Typing and Permeability Prediction (`03_rock_typing_fzi.ipynb`)

This stage focused on classifying the reservoir into rock types to better characterize permeability.

*   **Rock Type Definition**: The Flow Zone Indicator (FZI) method was used on core data to define hydraulic flow units. Cutoffs were determined using cumulative probability and Lorenz plots, resulting in 12 distinct rock types (`ROCK_FLAG`).
*   **Machine Learning for Rock Typing**:
    *   A classification model was trained to predict `ROCK_FLAG` from standard well logs (`GR`, `NPHI`, `RHOB`, `RT`). This allows rock type prediction in uncored intervals and wells.
    *   A regression model was trained to predict `log(FZI)` using the same logs plus the predicted `ROCK_FLAG`.
*   **Permeability Modeling**:
    *   The predicted FZI was used to calculate a continuous permeability curve (`PERM`). This method proved superior to traditional porosity-permeability transforms.
    *   The final permeability model, when benchmarked against core permeability (`CPERM`) on well `15-9-19-A`, achieved a high R² score of 0.81.

### 4. Full Petrophysical Interpretation (`05_a_qpp_ss_single.ipynb` & `05_b_qpp_ss_batch.ipynb`)

These notebooks apply the developed workflows to deliver a complete petrophysical interpretation, first for a single well and then in batch mode for all wells in the project.

*   **Single-Well Workflow (`05_a`)**: This notebook provides a detailed, step-by-step interpretation for well `15-9-19-A`, integrating all previous steps:
    *   Lithology and porosity estimation.
    *   Permeability estimation using various methods (Coates, Kozeny-Carman, etc.).
    *   Water Saturation (`SWT`) calculation using the Waxman-Smits model.
    *   Generation of a comprehensive log plot and a reservoir summary (`ressum`).

*   **Batch Processing Workflow (`05_b`)**: This notebook automates the entire interpretation process for all wells in the Volve project.
    *   It iteratively loads each well, applies the standardized workflow for log conditioning, lithology, porosity, and water saturation.
    *   It uses the pre-trained machine learning models from notebook `03` to predict rock type and permeability for all wells.
    *   The final results, including calculated curves and reservoir summaries, are saved back to the `quick-pp` project.
    *   Log plots for each well are generated and saved, and a cross-well comparison plot is created for quality control.

### Summary

This analysis successfully demonstrates an end-to-end petrophysical workflow on the Volve dataset. By integrating core data, log data, and machine learning, it produces a robust and consistent reservoir characterization across multiple wells. The use of the FZI-based rock typing model was critical for achieving accurate permeability predictions, a key parameter for reservoir simulation and development planning.