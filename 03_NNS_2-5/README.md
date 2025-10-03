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
4.  **`04_saturation.ipynb`**: Estimation of water saturation using the Archie equation and saturation height functions.
5.  **`05_ressum_plot.ipynb`**: Generation of final reservoir summary reports and interactive log plots.

### 1. Data Ingestion and Preparation

This notebook focuses on consolidating data sources into a unified and analysis-ready format.

*   **Well Log Loading**: Loaded and aggregated well log data from LAS files for the key well(s) in the study.
*   **Core Data Integration**: Imported Routine Core Analysis (RCA) data (porosity and permeability) from available core reports. The core data was carefully depth-matched and merged with the log data.
*   **Facies Data Integration**: Processed and merged lithofacies interpretations from Excel files to provide geological context.
*   **Project Creation**: All consolidated data was saved into a single `quick-pp` project file (`NNS_2-5.qppp`), ensuring streamlined and consistent data access for all subsequent analysis steps.

### 2. Lithology and Porosity Estimation

