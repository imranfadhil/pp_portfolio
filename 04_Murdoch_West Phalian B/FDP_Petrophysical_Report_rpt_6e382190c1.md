---
title: "Field Development Plan (FDP) Petrophysical Evaluation Report"
project: "Murdoch"
date: "2026-11-25 08:26"
author: "Petrophysics Team"
report_type: "FDP_FULL"
platform: "Prepared with quick_pp — Quantitative Petrophysics & Reservoir Evaluation Suite"
version: "1.0"
---

# 1. Executive Summary

This Field Development Plan (FDP) Petrophysical Evaluation integrates wireline log conditioning, Gamma Ray Shale Volume Index (Vsh,GR) Model lithology evaluation, Routine Core Analysis (RCA), Hydraulic Flow Unit ($FZI$) rock typing, and Leverett-$J$ Saturation Height Modeling ($SHF$) across **4 evaluated well(s)** (`44-22-1, 44-22-6Z, 44-22-3, 44-22-4`) in **Murdoch**, focusing on the target reservoir succession (`West Phalian B`). Across the evaluated target zones, net-thickness-weighted mean effective porosity ($\phi_e$) is **$0.102\text{ v/v}$** with a pore-volume weighted water saturation ($S_w$) of **$0.286\text{ v/v}$** and cumulative zonal mean Hydrocarbon Pore Thickness ($HCPT$) of **$1.54\text{ m}$**. The primary pay container is **West Phalian B**, delivering a field-mean Net Pay of **$21.1\text{ m}$** ($NTG_{pay} = 0.09\text{ v/v}$, Mean Net Reservoir $= 28.5\text{ m}$, $\phi_e = 0.102\text{ v/v}$, $S_w = 0.286\text{ v/v}$, $HCPT = 1.54\text{ m}$).


### Table 1.1: Field-Wide Zonal Net Reservoir & Net Pay Summary (Thickness & Pore-Volume Weighted)

| Zone | Wells | Mean Gross (m) | Mean Net Res (m) | $NTG_{res}$ | $\bar{V}_{sh,res}$ | $\bar{\phi}_{e,res}$ | $K_{geom,res}$ (mD) | Mean Net Pay (m) | $NTG_{pay}$ | $\bar{\phi}_{e,pay}$ | $\bar{S}_{w,pay}$ | Mean $HCPT$ (m) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **West Phalian B** | 4 | 236.3 | 28.5 | 0.12 | 0.120 | 0.100 | 8.4 | 21.1 | 0.09 | 0.102 | 0.286 | **1.54** |

<div class="page-break"></div>

# 2. Well Inventory & Data Availability

A total of **4** well(s) were evaluated in this Field Development Study (`Murdoch`), comprising **13487.6 m** of logged borehole section across **31** stratigraphic zone(s) (Target Reservoir Zones: `West Phalian B`). Across the field dataset, **1081** total Routine Core Analysis (RCA) plugs are loaded in the database, of which **791** valid depth-matched plugs reside within the target reservoir zones and have non-null overlapping log porosity.

The petrophysical database for **Murdoch** comprises **4 wells** totaling **13487.6 m** of logged borehole section across **31 mapped geological formations**, with volumetric and CPI reporting filtered to the **1 target reservoir zone(s)** (`West Phalian B`). A total of **1081 Routine Core Analysis (RCA) plug measurements** are loaded in the project inventory (Table 2.1), of which **791 valid plugs** overlap log-evaluated target reservoir intervals for active porosity calibration.


### 2.1 Multi-Well Wireline, Deviation Survey, Core & Pressure Inventory

| Well Name | UWI | KB (m) | TVD Survey | Top–Bottom (m MD) | Logged (m) | Raw Curves Available | Core (RCA/SCAL) | Pressure Data | Tops |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **44-22-1** | GB_044_22_01 | 33.2 | ✓ | `0.0–4262.2` | 4262.2 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (541 pts) | Yes (16 pts) | 34 |
| **44-22-6Z** | GB_044_22_06Z | 35.7 | ✓ | `2383.4–3938.6` | 1555.2 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (121 pts) | Yes (9 pts) | 15 |
| **44-22-3** | GB_044_22_03 | 33.8 | ✓ | `0.0–3884.7` | 3884.7 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (181 pts) | Yes (20 pts) | 37 |
| **44-22-4** | GB_044_22_04 | 34.1 | ✓ | `62.3–3847.8` | 3785.5 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (238 pts) | Yes (9 pts) | 32 |


![Figure 2.1: Multi-Well Data Inventory Matrix](/static/reports/rpt_6e382190c1/fig_2_1_inventory_heatmap.png)

<div class="page-break"></div>

# 3. Data Quality Control (QA/QC) & Conditioning

Rigorous borehole environmental conditioning and multi-well normalization were executed prior to quantitative interpretation. Across the 4 evaluated well(s), maximum washout/bad-hole flagging is **2.9%** (using caliper washout $> 2.0$ in (inches) and $\Delta\rho > 0.15$ g/cc criteria). All evaluated reservoir intervals exhibit good borehole stability (<15% washout flagging), requiring minimal synthetic curve reconstruction.


### 3.1 Borehole Environment, Bad-Hole Flagging & Normalization Criteria

* **Bad-Hole Criteria Applied:** Caliper washout $> 2.0$ in (inches) above bit size (`8.5 in`), Density correction $\Delta\rho > 0.15$ g/cc, or density washout $\rho_b < 1.95$ g/cc.
* **Bad-Hole Mitigation Mode:** `vsh_gr (GR Shale Fallback)` (shale/porosity fallback in rugose washouts to prevent optimistic density porosity spikes).
* **Hydrocarbon Light-Fluid Correction:** Gaymard-Poupon crossplot rotation applied where $\rho_{hc} = 0.8$ g/cc and $HI_{hc} = 0.9$.
* **Normalization Method:** Stratigraphic Zonal P10–P90 Quantile Alignment across target reservoir zones.

### 3.2 Well-by-Well QA/QC & Conditioning Summary

| Well Name | Evaluated Samples | Bad-Hole Samples | Bad-Hole (%) | HC-Corrected (%) | Tight / Coal Flags | GR P50 (gAPI) | RHOB P50 (g/cc) | QC Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **44-22-1** | 1378 | 0 | 0.0% | 58.4% | 0 / 110 | 89.9 | 2.592 | **PASS** |
| **44-22-6Z** | 2026 | 1 | 0.1% | 0.0% | 0 / 148 | 94.5 | 2.712 | **PASS** |
| **44-22-3** | 1161 | 14 | 1.2% | 33.9% | 0 / 105 | 99.4 | 2.684 | **PASS** |
| **44-22-4** | 1751 | 51 | 2.9% | 12.6% | 0 / 130 | 88.5 | 2.606 | **PASS** |


![Figure 3.1: Curve Distribution Pre- and Post-Normalization & Bad-Hole Audit](/static/reports/rpt_6e382190c1/fig_3_1_qaqc_norm_plot.png)

<div class="page-break"></div>

# 4. Lithology, Mineralogy & Porosity Evaluation

### 4.1 Methodology, Core-to-Log Alignment & Petrophysical Equations

* **Lithology Model:** `Gamma Ray Shale Volume Index (Vsh,GR) Model`
* **Porosity Model:** `Clay-Corrected Matrix Density Total & Effective Porosity` with clay-bound water ($CBW$) partitioning.
* **Core-to-Log Calibration Scope:** Total RCA core plugs loaded $= 1081$; valid target-zone plugs (`West Phalian B`) with overlapping depth-matched log porosity used in regression $= 791$.

$$I_{GR} = \frac{GR - GR_{clean}}{GR_{shale} - GR_{clean}}, \quad \phi_D = \frac{\rho_{ma} - \rho_b}{\rho_{ma} - \rho_{fl}}, \quad \phi_e = \phi_t - V_{sh} \cdot \phi_{sh}$$

| Parameter | Symbol | Value | Unit | Basis / Reference |
| :--- | :---: | :---: | :---: | :--- |
| Clean Matrix Density | $\rho_{ma}$ | 2.65 | $\text{g/cc}$ | Matrix Grain Density (2.65 g/cc Matrix (Measured RCA mean = 2.65 g/cc)) |
| Filtrate / Fluid Density | $\rho_{fl}$ | 1.0 | $\text{g/cc}$ | Mud Filtrate / Invasion Zone |
| Dry Clay Density | $\rho_{clay}$ | 2.73 | $\text{g/cc}$ | Clay Mineralogy Endpoint |
| Dry Clay Neutron | $NPHI_{clay}$ | 0.35 | $\text{v/v}$ | Neutron-Density Crossplot Clay Point |
| Clean GR Endpoint | $GR_{clean}$ | 10.0 | $\text{gAPI}$ | P5 Clean Reservoir Baseline |
| Shale GR Endpoint | $GR_{shale}$ | 125.5 | $\text{gAPI}$ | P95 Intra-Reservoir Shale Baseline |
| Gamma source | $\gamma$ | derived_cgr | — | Calibrate for the selected response |
| Derived CGR inputs | — | THOR / POTA | ppm / % | Th / K |
| CGR coefficients | $a_{Th}$ / $a_K$ | 4 / 16 | gAPI/ppm / gAPI/% | Verify tool calibration |
| Clean / shale gamma endpoints | — | 6.5 / 88.5 | gAPI | Selected gamma response |
| Total Core Plugs Loaded | $N_{core,total}$ | 1081 | plugs | Full-Wellbore RCA Inventory (Table 2.1) |
| Target-Zone Calibration Plugs | $N_{core,target}$ | 791 | plugs | Valid Overlapping Plugs (`West Phalian B`) |
| Core-to-Log Depth Matching | $\Delta d_{core}$ / $s_{core}$ | +0.00 m / 1.000$\times$ | $\text{m}$ | Piecewise Tie-Point Table (3 ties) ($d_{ref} = 3721.3\text{ m}$) (`RAW_DEPTH` $\to$ `DEPTH`) |
| Core Overburden Stress | $\sigma_{eff}$ (NCS) | 3500 | $\text{psi}$ | Well-Consolidated Sandstone Compaction ($c_\phi = 4.5e-06\text{ psi}^{-1}$, $c_k = 3.0e-05\text{ psi}^{-1}$) |
| Klinkenberg Slippage Pressure | $P_m$ | 45.0 | $\text{psi}$ | Jones Correlation (`CPERM_AIR` / `CPERM_ORI` $\to$ `CPERM`) |
| Core-to-Log Calibration | $R^2$ / $\text{RMSE}$ | 0.00 / 0.037 | $\text{v/v}$ | Mean Bias ($\phi_{log} - \phi_{core}$) $= -0.019\text{ v/v}$ |

> **Core-to-Log Depth Matching Lineage:** Driller's core plug depths were depth-matched to wireline logs using **Piecewise Tie-Point Table (3 ties)** ($\Delta d = +0.00\text{ m}$, stretch factor $s = 1.0000\times$, anchor pivot $d_{ref} = 3721.3\text{ m}$, mean plug shift $= +5.58\text{ m}$). Original unshifted driller's depths (`RAW_DEPTH`) and per-plug shifts (`SHIFT_M`) are preserved on every RCA sample, while unshifted log-grid curves are retained as `CPORE_UNSHIFTED` and `CPERM_UNSHIFTED`.
> **Core Overburden & Klinkenberg Lineage:** Ambient laboratory core porosity and gas permeability were corrected to reservoir stress ($\sigma_{eff} = 3500\text{ psi}$, $P_m = 45.0\text{ psi}$, `Well-Consolidated Sandstone` compaction). Uncorrected baseline curves are preserved as `CPORE_AMB` / `CPORE_ORI` and `CPERM_AIR` / `CPERM_ORI`, while active evaluation curves `CPORE` and `CPERM` store reservoir-corrected values ($\bar{\phi}_{amb} = 0.087 \to \bar{\phi}_{res} = 0.086\text{ v/v}$, $\bar{K}_{air} = 1.4 \to \bar{K}_{liq} = 1.0\text{ mD}$).

Shale volume ($V_{sh}$) and mineral fractions were resolved using the **Gamma Ray Shale Volume Index (Vsh,GR) Model** constrained by clean sand ($GR_{clean} = 10.0\text{ gAPI}$, $\rho_{ma} = 2.65\text{ g/cc}$) and intra-reservoir shale endpoints ($GR_{shale} = 125.5\text{ gAPI}$, $\rho_{clay} = 2.73\text{ g/cc}$). Log-derived total porosity ($\phi_t$) compared against overburden-corrected core plug porosity exhibits **poor statistical correlation, indicating unresolved core depth-shifts, non-overlapping depth intervals, or variable matrix grain density that must be rectified prior to static model handover** ($R^2 = 0.00$, $\text{RMSE} = 0.037\text{ v/v}$ across **791 valid target-zone calibration plugs** out of **1081 total core plugs loaded** across the field).



![Figure 4.1: Neutron-Density Crossplot, Core-to-Log Porosity Calibration & Matrix Grain Density QC](/static/reports/rpt_6e382190c1/fig_4_1_nd_crossplot.png)

<div class="page-break"></div>

# 5. Rock Typing & Permeability Modeling

### 5.1 Hydraulic Flow Units (FZI / DRT) & Permeability Transforms

Rock typing and continuous permeability ($K$) prediction were established using **Core Plugs (n=777)** via the Reservoir Quality Index ($RQI$), Normalized Porosity ($\phi_z$), Flow Zone Indicator ($FZI$), and Discrete Rock Typing ($DRT$) formulation:

$$RQI = 0.0314 \sqrt{\frac{K}{\phi_e}}, \quad \phi_z = \frac{\phi_e}{1 - \phi_e}, \quad FZI = \frac{RQI}{\phi_z}, \quad DRT = \text{round}(2 \ln(FZI) + 10.6)$$

| Rock Type | $DRT$ / Class | FZI Range ($\mu\text{m}$) | Samples ($n$) | Sample Share (%) | Semi-Log Porosity-Permeability Transform | Regression $R^2$ |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **RT1 — Nano/Micro-Porous Argillaceous** | DRT 1 (FZI < 0.50) | < 0.50 | 137 | 17.6% | $\log_{10}(K) = 12.98 \cdot \phi_e + (-2.07)$ | 0.73 |
| **RT2 — Meso/Macro-Porous Shoreface** | DRT 2 (0.50–1.50) | 0.50 – 1.50 | 474 | 61.0% | $\log_{10}(K) = 15.53 \cdot \phi_e + (-1.66)$ | 0.72 |
| **RT3 — Meso/Macro-Porous Shoreface** | DRT 3 (1.50–3.00) | 1.50 – 3.00 | 126 | 16.2% | $\log_{10}(K) = 17.63 \cdot \phi_e + (-1.24)$ | 0.94 |
| **RT4 — Mega-Porous Clean Channel Sand** | DRT 4 (FZI ≥ 3.00) | ≥ 3.00 | 40 | 5.1% | $\log_{10}(K) = 20.56 \cdot \phi_e + (-0.86)$ | 0.93 |

### 5.2 Core Permeability Calibration (`PERM` $\times$ `CPERM`) & Data Lineage

| Calibration / Lineage Parameter | Symbol | Value | Unit | Basis / Reference |
| :--- | :---: | :---: | :---: | :--- |
| Overlapping Core Perm Plugs | $N_{perm,cal}$ | 692 | plugs | Target-Zone `PERM` $\times$ `CPERM` Parity |
| Log-Core Permeability Parity | $R^2$ / $\text{RMSE}_{\log_{10}}$ | 0.00 / 1.009 | $\text{dec}$ | Multiplicative Factor Error $= 10.21\times$ |
| Core-to-Log Depth Shift | $\Delta d_{core}$ / $s_{core}$ | +0.00 m / 1.000$\times$ | $\text{m}$ | Piecewise Tie-Point Table (3 ties) (`RAW_DEPTH` $\to$ `DEPTH`, `CPERM_UNSHIFTED` $\to$ `CPERM`) |
| Overburden & Klinkenberg $K$ | $\sigma_{eff}$ / $P_m$ | 3500 / 45.0 | $\text{psi}$ | `CPERM_AIR` $\to$ `CPERM` ($c_k = 3.0e-05\text{ psi}^{-1}$, Jones) |

Hydraulic Flow Unit partitioning on **Core Plugs (n=777)** classified the reservoir into four Discrete Rock Types (`RT1` through `RT4`) using Flow Zone Indicator cut-offs of $0.5, 1.5,\text{ and }3.0\text{ }\mu\text{m}$. Dominant flow capacity is controlled by **RT3 (Macro-Porous Upper Shoreface)** and **RT4 (Mega-Porous Channel Sand)**, which represent **21.4%** of reservoir samples while contributing **89.8%** of cumulative permeability-thickness ($\sum K\cdot h$) on the Stratigraphic Modified Lorenz Plot ($SMLP$).



![Figure 5.1: Core/Log Porosity-Permeability Crossplot by Rock Type & Stratigraphic Modified Lorenz Plot](/static/reports/rpt_6e382190c1/fig_5_1_perm_crossplot.png)

<div class="page-break"></div>

# 6. Fluid Contacts & Water Saturation ($S_w$)

### 6.1 Electrical Properties, Formation Water Resistivity & Saturation Equation

* **Saturation Model:** `Waxman-Smits Shaly-Sand Cation Exchange ($Q_v$) Model`
* **Free Water Level ($FWL$):** $3726.6\text{ m TVDss}$
* **Formation Water Salinity & Resistivity:** $150000\text{ ppm NaCl equivalent}$, $R_w = 0.017\text{ }\Omega\cdot\text{m} \text{ @ } 75.0^\circ\text{C}$ (Arps temperature scaling).
* **Electrical Tortuosity, Cementation & Saturation Exponents:** $a = 1.0$, $m = 1.84$, $n = 2.0$

$$S_w^n + R_w \cdot B \cdot Q_v \cdot S_w^{n-1} = \frac{a \cdot R_w}{\phi_t^m \cdot R_t} \quad \text{(Waxman-Smits Shaly-Sand)} \qquad S_w = \left(\frac{a \cdot R_w}{\phi_t^m \cdot R_t}\right)^{1/n} \quad \text{(Archie)}$$

| Parameter | Symbol | Value | Unit | Basis / Calibration |
| :--- | :---: | :---: | :---: | :--- |
| Tortuosity Factor | $a$ | 1.0 | unitless | Electrical Tortuosity / Pickett Plot |
| Cementation Exponent | $m$ | 1.84 | unitless | Formation Factor ($F = a / \phi^m$) |
| Saturation Exponent | $n$ | 2.0 | unitless | Resistivity Index ($RI = S_w^{-n}$) |
| Formation Water Resistivity | $R_w$ | 0.017 | $\Omega\cdot\text{m}$ | Water Zone Pickett $S_w = 100\%$ Ro Trend |
| Free Water Level | $FWL$ | 3726.6 | $\text{m TVDss}$ | Resistivity-Porosity Fluid Contact Interpretation |

Water saturation ($S_w$) was evaluated using the **Waxman-Smits Shaly-Sand Cation Exchange ($Q_v$) Model** to account for clay-bound counter-ion conductivity ($B \cdot Q_v$) in shaly-sand and heterolithic intervals, where Archie saturation would otherwise overestimate $S_w$. Formation water resistivity was anchored at $R_w = 0.017\text{ }\Omega\cdot\text{m}$ at $75.0^\circ\text{C}$ ($150,000\text{ ppm NaCl}$) with electrical exponents $a=1.0, m=1.84, n=2.0$ and a target-reservoir Free Water Level at $FWL = 3726.6\text{ m TVDss}$.



![Figure 6.1: Pickett Plot & Water Saturation Profile vs. Free Water Level](/static/reports/rpt_6e382190c1/fig_6_1_pickett_shf_plot.png)

### 6.2 Multi-Well & Zonal Fluid Contacts, Proved Column & Uncertainty Brackets

Accurate delineation of fluid contacts is fundamental to volumetric in-place estimation and dynamic reservoir simulation. The proved hydrocarbon column is bounded by the shallowest and deepest proved fluid limits, while discrete contacts (OWC, GOC, GWC) and Free Water Levels (FWL) define the hydrostatic equilibrium boundaries.

| Well Name | Zone | Fault Block | Contact / Limit Type | Depth (m TVDss) | Determination Method / Source | Geological Notes / Remarks |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| 44-22-3 | West Phalian B | - | **GUT** | 3421.6 | Log Evaluation (Gas column top) | Proved Gas Up To at 3421.6 m TVDss in West Phalian B |
| 44-22-1 | West Phalian B | - | **GUT** | 3423.1 | Log Evaluation (Gas column top) | Proved Gas Up To at 3423.1 m TVDss in West Phalian B |
| 44-22-4 | All Zones | - | **GUT** | 3551.2 | Petrophysical Log Evaluation | - |
| 44-22-3 | West Phalian B | - | **GDT** | 3584.3 | Log Evaluation (Lowest proved gas pay) | Proved Gas Down To at 3584.3 m TVDss in West Phalian B |
| 44-22-1 | West Phalian B | - | **GDT** | 3625.3 | Log Evaluation (Lowest proved gas pay) | Proved Gas Down To at 3625.3 m TVDss in West Phalian B |
| 44-22-4 | All Zones | - | **GDT** | 3695.4 | Petrophysical Log Evaluation | - |
| 44-22-1 | West Phalian B | - | **FWL** | 3697.0 | FWL Optimizer (Capillary Pc = 0 datum) | Optimized Free Water Level (Pc = 0 datum) for West Phalian B |
| 44-22-3 | West Phalian B | - | **FWL** | 3697.0 | FWL Optimizer (Capillary Pc = 0 datum) | Optimized Free Water Level (Pc = 0 datum) for West Phalian B |
| 44-22-4 | All Zones | - | **FWL** | 3697.0 | Petrophysical Log Evaluation | - |

#### Hydrocarbon Column & Uncertainty Bracket Summary by Zone

* **Zone: `West Phalian B`**:
  - **Proved Gas Column:** $3421.6\text{ m}$ (GUT) to $3625.3\text{ m TVDss}$ (GDT) [Proved Gross Gas Column: $203.7\text{ m}$].
  - **Free Water Level (FWL):** $3697.0\text{ m TVDss}$ (Capillary $P_c = 0$ Datum).
* **Zone: `All Zones`**:
  - **Proved Gas Column:** $3551.2\text{ m}$ (GUT) to $3695.4\text{ m TVDss}$ (GDT) [Proved Gross Gas Column: $144.2\text{ m}$].
  - **Free Water Level (FWL):** $3697.0\text{ m TVDss}$ (Capillary $P_c = 0$ Datum).

<div class="page-break"></div>

# 7. Capillary Pressure, Saturation Height Modeling (SHF) & SCAL

### 7.1 Leverett $J$-Function, Lab-to-Reservoir $P_c$ Scaling & Core Stress Lineage

To initialize continuous 3D water saturation in the static geological cellular model above the Free Water Level ($FWL = 3726.6\text{ m TVDss}$, Basis: `Inferred from Hydrocarbon-Water Transition Zone (TVDss)`), log-derived $S_w$ was reconciled with capillary pressure ($P_c$) curves via the Leverett $J$-Function and Lab-to-Reservoir interfacial tension scaling:

$$P_{c,res} = P_{c,lab} \cdot \frac{(\sigma \cos\theta)_{res}}{(\sigma \cos\theta)_{lab}}, \quad h = TVD_{ss}(FWL) - TVD_{ss}, \quad J(S_w) = \frac{0.2166 \cdot P_{c,res}}{\sigma_{res} \cos\theta_{res}} \sqrt{\frac{K}{\phi}}$$

* **Reservoir Interfacial Tension & Wettability:** $(\sigma \cos\theta)_{res} = 26.0\text{ dynes/cm}$ ($\sigma_{res} = 30.0\text{ dynes/cm}$, $\theta_{res} = 30.0^\circ$).
* **Laboratory Fluid System & $P_c$ Scaling:** $(\sigma \cos\theta)_{lab} = 367.7\text{ dynes/cm}$ ($\sigma_{lab} = 480.0\text{ dynes/cm}$, $\theta_{lab} = 140.0^\circ$; Multiplier $= 0.0707\times$; Reference $25.0\text{ psi Lab} \to 1.766\text{ psi Reservoir}$; Lineage: `PC_LAB` $\to$ `PC`).
* **Core Overburden & Klinkenberg Stress Lineage:** $\sigma_{eff} = 3500\text{ psi}$ (Well-Consolidated Sandstone, $c_\phi = 4.5e-06\text{ psi}^{-1}$, $c_k = 3.0e-05\text{ psi}^{-1}$), $P_m = 45.0\text{ psi}$ (Jones); baseline preserved in `CPORE_AMB` / `CPORE_ORI` and `CPERM_AIR` / `CPERM_ORI`, active curves updated in `CPORE` and `CPERM`.
* **Fluid Density Gradient:** $\rho_w = 1.05\text{ g/cc}$, $\rho_{hc} = 0.8\text{ g/cc}$ ($\Delta\rho = 0.25\text{ g/cc}$).
* **Log $S_w$ vs. $SHF$ Reconciliation:** Mean RMSE $= 0.200\text{ v/v}$, Mean Bias ($S_w - SHF$) $= -0.026\text{ v/v}$.

### 7.2 Dynamic Simulation Relative Permeability ($K_{rw}, K_{ro}$) — Calibrated LET SCAL & Core Parameterization


$$S_e = \frac{S_w - S_{wc}}{1 - S_{wc} - S_{or}}, \quad K_{rw}(S_w) = K_{rw}^0 \cdot (S_e)^{N_w}, \quad K_{ro}(S_w) = K_{ro}^0 \cdot (1 - S_e)^{N_o}$$

| Parameter | Symbol | Value | Unit | Provenance / Dynamic Simulation Role |
| :--- | :---: | :---: | :---: | :--- |
| Relative Permeability Model | $\text{Model}$ | LET | — | Active Single-Well / Simulation SCAL Model |
| Connate Water Saturation | $S_{wc}$ | 0.15 | $\text{v/v}$ | Immobile Water Endpoint (Calibrated LET SCAL & Core Parameterization) |
| Residual Oil Saturation | $S_{or}$ | 0.20 | $\text{v/v}$ | Waterflood Residual Hydrocarbon (Calibrated LET SCAL & Core Parameterization) |
| Max Water RelPerm | $K_{rw}^0$ | 0.45 | $\text{frac}$ | Endpoint @ $S_w = 1 - S_{or}$ (Calibrated LET SCAL & Core Parameterization) |
| Max Oil RelPerm | $K_{ro}^0$ | 0.90 | $\text{frac}$ | Endpoint @ $S_w = S_{wc}$ (Calibrated LET SCAL & Core Parameterization) |
| LET Water Parameters | $L_w / E_w / T_w$ | 2.0 / 1.5 / 2.0 | unitless | Lomeland-Ebeltoft-Thomas Water Curve |
| LET Oil Parameters | $L_o / E_o / T_o$ | 2.0 / 1.5 / 2.0 | unitless | Lomeland-Ebeltoft-Thomas Oil Curve |
| SWOF Entry / Max $P_{cow}$ | $P_{ce}$ / $P_{c,\max}$ | 1.50 / 50.0 | $\text{psi}$ | Reservoir Capillary Pressure Table Bounds |

3D static model water saturation initialization via the Leverett $J$-Function ($\sigma\cos\theta = 26.0\text{ dynes/cm}$) reconciles with wireline log $S_w$ ($\text{RMSE} = 0.200\text{ v/v}$, mean bias $-0.026\text{ v/v}$). Dynamic simulation relative permeability tables (`SWOF`, **Calibrated LET SCAL & Core Parameterization**) were parameterized using Corey exponents $N_w = 2.5, N_o = 2.5$ with $S_{wc} = 0.15\text{ v/v}$ and $S_{or} = 0.20\text{ v/v}$.



![Figure 7.1: Capillary Pressure Leverett J-Function by Rock Type & Relative Permeability Curves](/static/reports/rpt_6e382190c1/fig_7_1_shf_scal_plot.png)

<div class="page-break"></div>

# 8. Cut-offs, Sums & Averages (Reservoir Summary) & Uncertainty

### 8.1 Applied Net Rock, Net Reservoir & Net Pay Cut-offs

* **Shale Volume Cut-off ($V_{sh,cutoff}$):** $\le 0.40\text{ v/v}$ (Defines **Net Rock** flag)
* **Effective Porosity Cut-off ($\phi_{e,cutoff}$):** $\ge 0.08\text{ v/v}$ (Defines **Net Reservoir** flag where $V_{sh} \le V_{sh,cutoff}$)
* **Water Saturation Cut-off ($S_{w,cutoff}$):** $\le 0.65\text{ v/v}$ (Defines **Net Pay** flag where Net Reservoir $= 1$)

$$\text{NTG} = \frac{\sum h_{net}}{\sum h_{gross}}, \quad \bar{\phi}_e = \frac{\sum h_i \cdot \phi_{e,i}}{\sum h_i}, \quad \bar{S}_w = \frac{\sum h_i \cdot \phi_{e,i} \cdot S_{w,i}}{\sum h_i \cdot \phi_{e,i}}, \quad HCPT = \sum h_i \cdot \phi_{e,i} \cdot (1 - S_{w,i})$$

### 8.2 Well-by-Well Zonal Net Reservoir & Net Pay Summary

| Well | Zone | Interval (m MD) | Interval (m TVDss) | Gross (m) | Net Res (m) | $NTG_{res}$ | $\bar{V}_{sh,res}$ | $\bar{\phi}_{e,res}$ | $K_{geom,res}$ (mD) | Net Pay (m) | $NTG_{pay}$ | $\bar{\phi}_{e,pay}$ | $\bar{S}_{w,pay}$ | $HCPT$ (m) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **44-22-1** | West Phalian B | `3453.1–3661.9` | `3419.8–3628.5` | 208.8 | 36.6 | 0.17 | 0.134 | 0.091 | 4.2 | 36.6 | 0.17 | 0.091 | 0.293 | **2.35** |
| **44-22-6Z** | West Phalian B | `3630.0–3928.0` | `3570.4–3830.3` | 297.9 | 23.3 | 0.08 | 0.060 | 0.096 | 2.9 | 0.0 | 0.00 | — | — | **0.00** |
| **44-22-3** | West Phalian B | `3446.1–3622.9` | `3411.7–3587.9` | 176.8 | 28.6 | 0.16 | 0.174 | 0.112 | 14.1 | 28.6 | 0.16 | 0.112 | 0.235 | **2.45** |
| **44-22-4** | West Phalian B | `3581.1–3842.8` | `3546.7–3808.0` | 261.7 | 25.3 | 0.10 | 0.096 | 0.103 | 32.6 | 19.2 | 0.07 | 0.108 | 0.353 | **1.34** |

### 8.3 Probabilistic Petrophysical Uncertainty Ranges (P90 / P50 / P10 — $N = 1000$ Realizations)

Probabilistic petrophysical uncertainty ranges were quantified across $N = 1000$ Monte Carlo realizations perturbing matrix density ($\sigma_{\rho_{ma}} = \pm 0.015\text{ g/cc}$), clean/shale Gamma Ray endpoints ($\sigma_{GR} = \pm 5\text{ gAPI}$), Archie tortuosity/cementation/saturation parameters ($\sigma_m = \pm 0.08, \sigma_n = \pm 0.10, \sigma_{R_w} = \pm 10\%$), and Net Pay cut-offs ($\Delta V_{sh} = \pm 0.05, \Delta\phi_e = \pm 0.015, \Delta S_w = \pm 0.05$).

| Zone | Metric | P90 (Conservative / Low) | P50 (Base Case) | P10 (Optimistic / High) | Uncertainty Spread (P10/P90) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **West Phalian B** | HCPT (m) / Φe (v/v) / Sw (v/v) | 0.57 m (Φ=0.099, Sw=0.329) | **1.52 m (Φ=0.102, Sw=0.282)** | 2.42 m (Φ=0.115, Sw=0.232) | 4.25× |


Zonal summation decouples **Net Reservoir** ($V_{sh} \le 0.40\text{ v/v}$, $\phi_e \ge 0.08\text{ v/v}$) from **Net Pay** ($S_w \le 0.65\text{ v/v}$) so static geomodelers can populate 3D aquifer porosity and permeability in water-bearing penetrations. Monte Carlo / Latin Hypercube ($N = 1000$ realizations) uncertainty propagation across the pay-bearing target zones indicates a median P10/P90 $HCPT$ ratio of **4.25×**, driven by matrix density ($\rho_{ma}$), cementation exponent ($m$), and $R_w$ uncertainty.



![Figure 8.1: Cut-off Sensitivity & Probabilistic HCPT Distribution](/static/reports/rpt_6e382190c1/fig_8_1_uncertainty_plot.png)

<div class="page-break"></div>

# 9. Upscaling, Log Blocking & Deliverables Handover

### 9.1 Static Geomodel Cellular Blocking & Cardwell-Parsons Averaging

Fine-scale evaluated CPI logs ($0.1524\text{ m}$ sampling) were upscaled onto cellular grid blocks ($h_{cell} = 2.0\text{ m}$, zone-constrained) using PRMS/SEC and static geomodeling best practices:

* **Shale Volume ($V_{sh}$) & Porosity ($\phi_t, \phi_e$) & $NTG$:** Thickness-weighted arithmetic average: $\bar{\phi}_{cell} = \frac{\sum h_i \phi_i}{\sum h_i}$.
* **Water Saturation ($S_w$):** Pore-volume weighted average: $\bar{S}_{w,cell} = \frac{\sum h_i \phi_i S_{w,i}}{\sum h_i \phi_i}$.
* **Horizontal Permeability Proxy ($K_h$):** Arithmetic mean: $K_{arith} = \frac{\sum h_i K_i}{\sum h_i}$.
* **Effective Heterogeneous Permeability ($K_{eff}$):** Geometric mean ($\omega \to 0$): $K_{geom} = \exp\left(\frac{\sum h_i \ln K_i}{\sum h_i}\right)$.
* **Vertical Permeability Proxy ($K_v$):** Harmonic mean ($\omega = -1$): $K_{harm} = \frac{\sum h_i}{\sum (h_i / K_i)}$, yielding vertical anisotropy ratio $K_v / K_h = K_{harm} / K_{arith}$.

| Well Name | Fine-Scale Samples | Blocked Grid Cells (2.0m) | Mean $\phi_{blocked}$ (v/v) | Mean $S_{w,blocked}$ (v/v) | $K_{arith}$ ($K_h$, mD) | $K_{geom}$ ($K_{eff}$, mD) | $K_{harm}$ ($K_v$, mD) | Mean $K_v / K_h$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **44-22-1** | 1371 | 105 | 0.028 | 0.584 | 1.2 | 1.0 | 0.81 | 0.680 |
| **44-22-6Z** | 1956 | 149 | 0.016 | 1.000 | 0.4 | 0.3 | 0.23 | 0.647 |
| **44-22-3** | 1161 | 89 | 0.025 | 0.768 | 3.6 | 2.7 | 2.12 | 0.584 |
| **44-22-4** | 1718 | 131 | 0.022 | 0.884 | 6.0 | 4.6 | 3.59 | 0.596 |

Fine-scale evaluated CPI logs within the target reservoir succession were blocked to $2.0\text{ m}$ cellular resolution honoring geological zone boundaries. Cardwell-Parsons directional permeability bounds yield a field-mean vertical-to-horizontal anisotropy ratio ($K_v / K_h = K_{harm} / K_{arith}$) across the evaluated wells, preserving thin-bed vertical baffles for Eclipse/Intersect dynamic simulation.



![Figure 9.1: Fine-Scale CPI vs. Upscaled Blocked Logs Comparison Track](/static/reports/rpt_6e382190c1/fig_9_1_upscaling_plot.png)

### 9.2 FDP Subsurface Deliverables Handover Manifest

| Deliverable Artifact | Format | Target Consumer | QA/QC Verification Status |
| :--- | :---: | :--- | :---: |
| **Evaluated CPI Composite Well Logs** | `.las` / `.csv` | Petrel / RMS Static Modeling | ✓ Verified (4 Wells) |
| **Zonal Sums & Averages Master Table** | `.csv` / `.md` | Reserves Audit & Volumetric STOIIP | ✓ Verified (31 Zones) |
| **Upscaled Cellular Blocked Logs** | `.csv` | 3D Property Population (`K_h`, `K_v`, `PHIE`, `SW`) | ✓ Verified (2.0m Grid) |
| **SCAL & Saturation Height Function Deck** | `SWOF` / `.inc` | Eclipse / Intersect Dynamic Simulation | ✓ Verified (Leverett-J & Corey/LET) |
| **FDP Petrophysical Evaluation Report** | `.md` / `.pdf` | Subsurface Peer Review & Gate Approval | ✓ Complete |

<div class="page-break"></div>

# Appendix A: Composite Petrophysical Evaluation Logs (CPI)


### Well: `44-22-6Z`

![CPI Log - 44-22-6Z](/static/reports/rpt_6e382190c1/cpi_44-22-6Z.png)

<div class="page-break"></div>

### Well: `44-22-4`

![CPI Log - 44-22-4](/static/reports/rpt_6e382190c1/cpi_44-22-4.png)

<div class="page-break"></div>

### Well: `44-22-1`

![CPI Log - 44-22-1](/static/reports/rpt_6e382190c1/cpi_44-22-1.png)

<div class="page-break"></div>

### Well: `44-22-3`

![CPI Log - 44-22-3](/static/reports/rpt_6e382190c1/cpi_44-22-3.png)