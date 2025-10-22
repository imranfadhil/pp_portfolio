# ~Work in Progress~

# Petrophysical Analysis of UK North Sea Block 22/30

*Contains information provided by the North Sea Transition Authority and/or other third parties.*

### Geological Background
Block 22/30 is situated in the Central Graben of the UK Central North Sea, an area renowned for its High-Pressure/High-Temperature (HPHT) fields and long history as a hydrocarbon province. The primary reservoirs were deposited in diverse marine environments: the Upper Jurassic Fulmar Formation formed in shallow marine shoreface settings, heavily reworked by storms and tides, while the Paleocene Forties Sandstone Member represents a deep-water submarine fan system, characterized by thinner, more distal sheet-like lobes in this specific block.

The key producing reservoirs include the Upper Jurassic Fulmar Formation, a primary gas condensate reservoir (e.g., Shearwater Field), and the Middle Jurassic Pentland Formation. Although a major producer elsewhere, the Paleocene Forties Sandstone Member is considered a secondary, poorer-quality reservoir in Block 22/30 due to its distal nature. The main source rock for these hydrocarbons is the Upper Jurassic Kimmeridge Clay Formation.

Exploration and production in Block 22/30 face several significant challenges. These include extreme HPHT conditions requiring specialized equipment and techniques, complex reservoir quality and architecture (especially the distal Forties Sandstone), and issues inherent to a mature basin such as declining production, aging infrastructure, and rising operational costs. Additionally, economic and environmental pressures, including volatile oil prices, increasing regulations, and a global shift towards cleaner energy, further impact the viability of developments in the region.

### 1. Data Ingestion and Preparation

This notebook focuses on consolidating data sources into a unified and analysis-ready format.

*   **Well Log Loading**: Loaded and aggregated well log data from LAS files for the key well(s) in the study.
*   **Core Data Integration**: Imported Routine Core Analysis (RCA) data (porosity and permeability) from available core reports. The core data was depth-matched and merged with the log data.
*   **Tops Data Integration**
*   **Project Creation**: All consolidated data was saved into a single `quick-pp` project file (`22-30.qppp`), ensuring streamlined and consistent data access for all subsequent analysis steps.

* **Wells** being analysed:
    1. **22/30b-11** (Jan 1994)
    2. **22/30c-8** (Feb 1991)
    3. **22/30c-10** (Mac 1993)
    4. **22/30c-13** (Sep 1994)
