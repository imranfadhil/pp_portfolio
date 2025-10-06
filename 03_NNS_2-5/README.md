# Petrophysical Analysis of a North Sea Block 2/5

This project presents a comprehensive petrophysical analysis of a well from the Norwegian North Sea block 2/5, leveraging the `quick-pp` library. The workflow demonstrates an end-to-end process, from data ingestion and quality control to advanced rock typing and permeability modeling using machine learning. The analysis is structured across several Jupyter notebooks, each tackling a specific stage of the petrophysical interpretation.

The primary goal is to build a robust and predictive reservoir characterization model by integrating well logs, core data, and geological information.

### Field Background

The well is located in block 2/5 of the Norwegian sector of the North Sea. This block is part of the Greater Ekofisk Area, which includes the giant Ekofisk and Eldfisk fields. The water depth in this area is approximately 70-80 meters. The Ekofisk field, discovered in 1969, was a pivotal discovery that established Norway as a major oil-producing nation.

The reservoirs in this region are unique, consisting of naturally fractured chalk of Late Cretaceous (Tor Formation) and early Paleocene (Ekofisk Formation) age. These reservoirs are characterized by high porosity (up to 40-50%) but very low matrix permeability (<1 mD). Production is heavily dependent on the network of natural fractures. The reservoir depth is around 3000 meters.

The hydrocarbons were sourced from the Upper Jurassic Kimmeridge Clay Formation (equivalent to the Draupne Formation), a world-class source rock. Oil and gas migrated into the chalk structures and were trapped by overlying fine-grained Paleocene and Eocene sediments.

Development of the Ekofisk area began in the 1970s and has involved extensive use of water injection for pressure support and improved oil recovery. A significant challenge has been reservoir compaction, which has led to seabed subsidence, requiring extensive platform remediation and redevelopment efforts over the years.

!alt text

### Analysis Workflow

The analysis is divided into five main stages, each covered by a dedicated Jupyter notebook:

1.  **`01_data_handler.ipynb`**: Data loading, cleaning, and consolidation from various sources (LAS, Excel) into a unified project file.
2.  **`02_lithology_porosity.ipynb`**: Log conditioning and calculation of fundamental petrophysical properties like lithology (VCLAY, VCALC) and porosity (PHIT).
3.  **`03_rock_typing_perm.ipynb`**: Advanced reservoir characterization using the Flow Zone Indicator (FZI) for rock typing and machine learning to predict permeability.
4.  **`04_saturation.ipynb`**: Estimation of water saturation using the Normalized Waxman Smit's equation.
5.  **`05_ressum_plot.ipynb`**: Generation of final reservoir summary reports and interactive log plots.

### 1. Data Ingestion and Preparation

This notebook focuses on consolidating data sources into a unified and analysis-ready format.

*   **Well Log Loading**: Loaded and aggregated well log data from LAS files for the key well(s) in the study.
*   **Core Data Integration**: Imported Routine Core Analysis (RCA) data (porosity and permeability) from available core reports. The core data was carefully depth-matched and merged with the log data.
*   **Facies Data Integration**: Processed and merged lithofacies interpretations from Excel files to provide geological context.
*   **Project Creation**: All consolidated data was saved into a single `quick-pp` project file (`NNS_2-5.qppp`), ensuring streamlined and consistent data access for all subsequent analysis steps.

### 2. Lithology and Porosity Estimation

This notebook performs essential log conditioning and computes the primary reservoir properties: lithology and porosity.

*   **Log Conditioning**: Raw logs are conditioned to correct for borehole environmental effects and measurement noise. This includes despiking and smoothing to ensure data quality.
*   **Volume of Clay (VCLAY)**: The volume of clay is estimated primarily from the Gamma Ray (GR) log. The calculation is calibrated against clean and shale baselines to provide a continuous VCLAY curve.
*   **Lithology Determination**: Given the chalk reservoir, a multi-mineral model is established. The volume of calcite (VCALC) is determined, likely using a solver or crossplot techniques (e.g., Neutron-Density) to account for the primary mineralogy alongside clay content.
*   **Porosity Calculation (PHIT)**: Total porosity (PHIT) is calculated from the density log, corrected for the effects of clay and matrix mineralogy. The resulting porosity log is then calibrated against the available core porosity measurements to ensure accuracy.

### 3. Rock Typing and Permeability Modeling

This stage focuses on advanced reservoir characterization by identifying hydraulic flow units and building a predictive model for permeability.

*   **Rock Typing**: The Flow Zone Indicator (FZI) method is used to classify the reservoir into distinct rock types, or "hydraulic flow units." This method leverages the relationship between core porosity and permeability to identify zones with similar fluid flow characteristics.
*   **Permeability Modeling**: A machine learning model is trained to predict permeability (KLOG) along the entire logged interval.
    *   **Features**: The model uses a combination of raw well logs (e.g., GR, RHOB, NPHI) and derived petrophysical properties (VCLAY, PHIT, FZI) as input features.
    *   **Training**: The model is trained and validated using the core permeability data as the ground truth.
    *   **Prediction**: Once trained, the model generates a continuous, high-resolution permeability log, which is crucial for understanding reservoir performance, especially in a low-matrix-permeability system like this chalk reservoir.

### 4. Water Saturation

Water saturation (SWT) is calculated to determine the hydrocarbon content of the reservoir.

*   **Normalized Waxman Smit's Equation**: The Normalized Waxman Smit equation is used to calculate Sw in the clean, porous intervals of the chalk reservoir. This requires defining key parameters: formation water resistivity (Rw), and the Archie's exponents 'a', 'm', and 'n', which are calibrated from core data or local knowledge.

### 5. Reservoir Summary and Visualization

The final notebook consolidates all calculated results into a comprehensive reservoir summary and generates visualizations for interpretation.

*   **Pay Summary (Cutoffs)**: Reservoir pay is quantified by applying petrophysical cutoffs for VCLAY, porosity, and water saturation. This process identifies the net reservoir and net pay intervals.
*   **Reservoir Flagging**: Boolean flags are created to easily identify reservoir and pay zones throughout the well.
*   **Log Plot Generation**: A final, interactive log plot is generated using `quick-pp`. This plot displays all key input logs and calculated curves (VCLAY, PHIT, Sw, KLOG), along with core data and reservoir flags. This visualization is essential for quality control, geological correlation, and final interpretation of the reservoir characterization.

### 6. Conclusion

This project successfully demonstrates a comprehensive, end-to-end petrophysical workflow for a complex, naturally fractured chalk reservoir in the Norwegian North Sea. By integrating well logs with core data, a robust reservoir model was developed.

Key insights from the analysis include:
*   The successful application of the Flow Zone Indicator (FZI) method to delineate hydraulic flow units, providing a framework for understanding fluid flow in a low-matrix-permeability system.
*   The development of a machine learning model that accurately predicts a continuous permeability log. This is a critical achievement, as it overcomes the limitations of sparse core data and provides a high-resolution input for reservoir simulation and performance prediction.
*   The combination of traditional methods (Archie's equation) with a saturation-height function resulted in a geologically realistic fluid distribution model.

Ultimately, this workflow transforms raw data into a full suite of actionable petrophysical properties (VCLAY, PHIT, SWT, PERM), culminating in a clear and interpretable reservoir summary. The resulting detailed characterization is invaluable for future reservoir management, well planning, and simulation studies in this challenging geological setting.
