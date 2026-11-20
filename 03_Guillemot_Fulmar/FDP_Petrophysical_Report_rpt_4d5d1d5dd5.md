---
title: "Field Development Plan (FDP) Petrophysical Evaluation Report"
project: "Guillemot"
date: "2026-11-19 23:49"
author: "Petrophysics Team"
report_type: "FDP_FULL"
platform: "Prepared with quick_pp — Quantitative Petrophysics & Reservoir Evaluation Suite"
version: "1.0"
---

# 1. Executive Summary

This Field Development Plan (FDP) Petrophysical Evaluation integrates wireline log conditioning, Modified Kuttan Sand-Silt-Clay (SSC) Ternary Model lithology evaluation, Routine Core Analysis (RCA), Hydraulic Flow Unit ($FZI$) rock typing, and Leverett-$J$ Saturation Height Modeling ($SHF$) across **10 evaluated well(s)** (`21-29a-10, 21-25-2, 21-30-8, 21-29a-10Z, 21-25-3, 21-24-2, 21-30-5, 21-29a-8, 21-29b-7, 21-29a-6`) in **Guillemot**, focusing on the target reservoir succession (`Fulmar`). Across the evaluated target zones, net-thickness-weighted mean effective porosity ($\phi_e$) is **$0.218\text{ v/v}$** with a pore-volume weighted water saturation ($S_w$) of **$0.389\text{ v/v}$** and cumulative zonal mean Hydrocarbon Pore Thickness ($HCPT$) of **$4.21\text{ m}$**. The primary pay container is **Fulmar**, delivering a field-mean Net Pay of **$31.6\text{ m}$** ($NTG_{pay} = 0.31\text{ v/v}$, Mean Net Reservoir $= 80.7\text{ m}$, $\phi_e = 0.218\text{ v/v}$, $S_w = 0.389\text{ v/v}$, $HCPT = 4.21\text{ m}$).


### Table 1.1: Field-Wide Zonal Net Reservoir & Net Pay Summary (Thickness & Pore-Volume Weighted)

| Zone | Wells | Mean Gross (m) | Mean Net Res (m) | $NTG_{res}$ | $\bar{V}_{sh,res}$ | $\bar{\phi}_{e,res}$ | $K_{geom,res}$ (mD) | Mean Net Pay (m) | $NTG_{pay}$ | $\bar{\phi}_{e,pay}$ | $\bar{S}_{w,pay}$ | Mean $HCPT$ (m) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Fulmar** | 4 | 101.3 | 80.7 | 0.80 | 0.231 | 0.192 | 19.0 | 31.6 | 0.31 | 0.218 | 0.389 | **4.21** |

<div class="page-break"></div>

# 2. Well Inventory & Data Availability

A total of **10** well(s) were evaluated in this Field Development Study (`Guillemot`), comprising **25592.5 m** of logged borehole section across **24** stratigraphic zone(s) (Target Reservoir Zones: `Fulmar`). Across the field dataset, **1242** total Routine Core Analysis (RCA) plugs are loaded in the database, of which **416** valid depth-matched plugs reside within the target reservoir zones and have non-null overlapping log porosity.

The petrophysical database for **Guillemot** comprises **10 wells** totaling **25592.5 m** of logged borehole section across **24 mapped geological formations**, with volumetric and CPI reporting filtered to the **1 target reservoir zone(s)** (`Fulmar`). A total of **1242 Routine Core Analysis (RCA) plug measurements** are loaded in the project inventory (Table 2.1), of which **416 valid plugs** overlap log-evaluated target reservoir intervals for active porosity calibration.


### 2.1 Multi-Well Wireline, Deviation Survey, Core & Pressure Inventory

| Well Name | UWI | KB (m) | TVD Survey | Top–Bottom (m MD) | Logged (m) | Raw Curves Available | Core (RCA/SCAL) | Pressure Data | Tops |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **21-29a-10** | 21-29a-10 | 25.3 | ✓ | `0.0–2143.7` | 2143.7 | `TVD, TVDSS, GR, NPHI, RHOB, CALI, DTC, RES_DEEP, RES_MED` | No | No | 0 |
| **21-25-2** | 1069 | 25.9 | ✓ | `0.0–2703.0` | 2703.0 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (127 pts) | Yes (36 pts) | 20 |
| **21-30-8** | 7068 | 25.0 | ✓ | `0.0–2657.2` | 2657.2 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (437 pts) | Yes (26 pts) | 23 |
| **21-29a-10Z** | 21-29a-10Z | 25.3 | ✓ | `0.0–2284.5` | 2284.5 | `TVD, TVDSS, GR, NPHI, RHOB, CALI, DTC, RES_DEEP, RES_MED` | No | No | 0 |
| **21-25-3** | 4189 | 27.4 | ✓ | `0.0–3381.4` | 3381.4 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (223 pts) | No | 21 |
| **21-24-2** | 1067 | 25.3 | ✓ | `169.9–2561.5` | 2391.6 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, AVG_ERROR, B, BADHOLE` | Yes (108 pts) | No | 21 |
| **21-30-5** | 4262 | 25.6 | ✓ | `0.0–2971.8` | 2971.8 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, ROCK_FLAG, PERM_TRANS, SHF` | Yes (9 pts) | Yes (4 pts) | 21 |
| **21-29a-8** | 4193 | 25.6 | ✓ | `160.0–2262.1` | 2102.1 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, B, BADHOLE, BS` | Yes (129 pts) | No | 20 |
| **21-29b-7** | 1074 | 25.0 | ✓ | `0.0–2840.4` | 2840.4 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, B, BADHOLE, BVW` | Yes (77 pts) | No | 21 |
| **21-29a-6** | 1076 | 24.7 | ✓ | `0.0–2116.8` | 2116.8 | `TVD, TVDSS, GR, RT, NPHI, RHOB, VCLAY, PHIT, PERM, SWT, B, BADHOLE, BVW` | Yes (132 pts) | Yes (29 pts) | 13 |


![Figure 2.1: Multi-Well Data Inventory Matrix](/static/reports/rpt_4d5d1d5dd5/fig_2_1_inventory_heatmap.png)

<div class="page-break"></div>

# 3. Data Quality Control (QA/QC) & Conditioning

Rigorous borehole environmental conditioning and multi-well normalization were executed prior to quantitative interpretation. Across the 4 evaluated well(s), maximum washout/bad-hole flagging is **0.0%** (using caliper washout $> 2.0$ in (inches) and $\Delta\rho > 0.15$ g/cc criteria). All evaluated reservoir intervals exhibit good borehole stability (<15% washout flagging), requiring minimal synthetic curve reconstruction.


### 3.1 Borehole Environment, Bad-Hole Flagging & Normalization Criteria

* **Bad-Hole Criteria Applied:** Caliper washout $> 2.0$ in (inches) above bit size (`8.5 in`), Density correction $\Delta\rho > 0.15$ g/cc, or density washout $\rho_b < 1.95$ g/cc.
* **Bad-Hole Mitigation Mode:** `vsh_gr (GR Shale Fallback)` (shale/porosity fallback in rugose washouts to prevent optimistic density porosity spikes).
* **Hydrocarbon Light-Fluid Correction:** Gaymard-Poupon crossplot rotation applied where $\rho_{hc} = 0.8$ g/cc and $HI_{hc} = 0.9$.
* **Normalization Method:** Stratigraphic Zonal P10–P90 Quantile Alignment across target reservoir zones.

### 3.2 Well-by-Well QA/QC & Conditioning Summary

| Well Name | Evaluated Samples | Bad-Hole Samples | Bad-Hole (%) | HC-Corrected (%) | Tight / Coal Flags | GR P50 (gAPI) | RHOB P50 (g/cc) | QC Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **21-25-2** | 393 | 0 | 0.0% | 12.5% | 0 / 0 | 62.2 | 2.292 | **PASS** |
| **21-30-8** | 375 | 0 | 0.0% | 4.8% | 0 / 0 | 47.5 | 2.344 | **PASS** |
| **21-25-3** | 1496 | 0 | 0.0% | 2.8% | 0 / 0 | 69.6 | 2.385 | **PASS** |
| **21-30-5** | 401 | 0 | 0.0% | 30.4% | 0 / 0 | 45.1 | 2.353 | **PASS** |


![Figure 3.1: Curve Distribution Pre- and Post-Normalization & Bad-Hole Audit](/static/reports/rpt_4d5d1d5dd5/fig_3_1_qaqc_norm_plot.png)

<div class="page-break"></div>

# 4. Lithology, Mineralogy & Porosity Evaluation

### 4.1 Methodology, Core-to-Log Alignment & Petrophysical Equations

* **Lithology Model:** `Modified Kuttan Sand-Silt-Clay (SSC) Ternary Model`
* **Porosity Model:** `Clay-Corrected Matrix Density Total & Effective Porosity` with clay-bound water ($CBW$) partitioning.
* **Core-to-Log Calibration Scope:** Total RCA core plugs loaded $= 1242$; valid target-zone plugs (`Fulmar`) with overlapping depth-matched log porosity used in regression $= 416$.

$$V_{sand} + V_{silt} + V_{clay} = 1, \quad \phi_D = \frac{\rho_{ma} - \rho_b}{\rho_{ma} - \rho_{fl}}, \quad \phi_e = \phi_t - V_{clay,bulk} \cdot \phi_{sh}$$

| Parameter | Symbol | Value | Unit | Basis / Reference |
| :--- | :---: | :---: | :---: | :--- |
| Clean Matrix Density | $\rho_{ma}$ | 2.65 | $\text{g/cc}$ | Matrix Grain Density (2.65 g/cc Matrix (Measured RCA mean = 2.65 g/cc)) |
| Filtrate / Fluid Density | $\rho_{fl}$ | 1.0 | $\text{g/cc}$ | Mud Filtrate / Invasion Zone |
| Dry Clay Density | $\rho_{clay}$ | 2.7 | $\text{g/cc}$ | Clay Mineralogy Endpoint |
| Dry Clay Neutron | $NPHI_{clay}$ | 0.33 | $\text{v/v}$ | Neutron-Density Crossplot Clay Point |
| Clean GR Endpoint | $GR_{clean}$ | 15.0 | $\text{gAPI}$ | P5 Clean Reservoir Baseline |
| Shale GR Endpoint | $GR_{shale}$ | 115.0 | $\text{gAPI}$ | P95 Intra-Reservoir Shale Baseline |
| Total Core Plugs Loaded | $N_{core,total}$ | 1242 | plugs | Full-Wellbore RCA Inventory (Table 2.1) |
| Target-Zone Calibration Plugs | $N_{core,target}$ | 416 | plugs | Valid Overlapping Plugs (`Fulmar`) |
| Core-to-Log Depth Matching | $\Delta d_{core}$ / $s_{core}$ | +0.00 m / 1.000$\times$ | $\text{m}$ | Affine Shift & Stretch ($d_{ref} = 1763.0\text{ m}$) (`RAW_DEPTH` $\to$ `DEPTH`) |
| Core Overburden Stress | $\sigma_{eff}$ (NCS) | 3500 | $\text{psi}$ | Well-Consolidated Sandstone Compaction ($c_\phi = 4.5e-06\text{ psi}^{-1}$, $c_k = 3.0e-05\text{ psi}^{-1}$) |
| Klinkenberg Slippage Pressure | $P_m$ | 45.0 | $\text{psi}$ | Jones Correlation (`CPERM_AIR` / `CPERM_ORI` $\to$ `CPERM`) |
| Core-to-Log Calibration | $R^2$ / $\text{RMSE}$ | 0.03 / 0.046 | $\text{v/v}$ | Mean Bias ($\phi_{log} - \phi_{core}$) $= -0.010\text{ v/v}$ |

> **Core-to-Log Depth Matching Lineage:** Driller's core plug depths were depth-matched to wireline logs using **Affine Shift & Stretch** ($\Delta d = +0.00\text{ m}$, stretch factor $s = 1.0000\times$, anchor pivot $d_{ref} = 1763.0\text{ m}$, mean plug shift $= +0.00\text{ m}$). Original unshifted driller's depths (`RAW_DEPTH`) and per-plug shifts (`SHIFT_M`) are preserved on every RCA sample, while unshifted log-grid curves are retained as `CPORE_UNSHIFTED` and `CPERM_UNSHIFTED`.
> **Core Overburden & Klinkenberg Lineage:** Ambient laboratory core porosity and gas permeability were corrected to reservoir stress ($\sigma_{eff} = 3500\text{ psi}$, $P_m = 45.0\text{ psi}$, `Well-Consolidated Sandstone` compaction). Uncorrected baseline curves are preserved as `CPORE_AMB` / `CPORE_ORI` and `CPERM_AIR` / `CPERM_ORI`, while active evaluation curves `CPORE` and `CPERM` store reservoir-corrected values.

Shale volume ($V_{sh}$) and mineral fractions were resolved using the **Modified Kuttan Sand-Silt-Clay (SSC) Ternary Model** constrained by clean sand ($GR_{clean} = 15.0\text{ gAPI}$, $\rho_{ma} = 2.65\text{ g/cc}$) and intra-reservoir shale endpoints ($GR_{shale} = 115.0\text{ gAPI}$, $\rho_{clay} = 2.7\text{ g/cc}$). Log-derived total porosity ($\phi_t$) compared against overburden-corrected core plug porosity exhibits **poor statistical correlation, indicating unresolved core depth-shifts, non-overlapping depth intervals, or variable matrix grain density that must be rectified prior to static model handover** ($R^2 = 0.03$, $\text{RMSE} = 0.046\text{ v/v}$ across **416 valid target-zone calibration plugs** out of **1242 total core plugs loaded** across the field).



![Figure 4.1: Neutron-Density Crossplot, Core-to-Log Porosity Calibration & Matrix Grain Density QC](/static/reports/rpt_4d5d1d5dd5/fig_4_1_nd_crossplot.png)

<div class="page-break"></div>

# 5. Rock Typing & Permeability Modeling

### 5.1 Hydraulic Flow Units (FZI / DRT) & Permeability Transforms

Rock typing and continuous permeability ($K$) prediction were established using **Core Plugs (n=404)** via the Reservoir Quality Index ($RQI$), Normalized Porosity ($\phi_z$), Flow Zone Indicator ($FZI$), and Discrete Rock Typing ($DRT$) formulation:

$$RQI = 0.0314 \sqrt{\frac{K}{\phi_e}}, \quad \phi_z = \frac{\phi_e}{1 - \phi_e}, \quad FZI = \frac{RQI}{\phi_z}, \quad DRT = \text{round}(2 \ln(FZI) + 10.6)$$

| Rock Type | $DRT$ / Class | FZI Range ($\mu\text{m}$) | Samples ($n$) | Sample Share (%) | Semi-Log Porosity-Permeability Transform | Regression $R^2$ |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **RT1 — Nano/Micro-Porous Argillaceous** | DRT 1 (FZI < 0.17) | < 0.17 | 6 | 1.5% | $\log_{10}(K) = 13.1 \cdot \phi_e + (-3.21)$ | 0.98 |
| **RT2 — Meso/Macro-Porous Shoreface** | DRT 2 (0.17–1.13) | 0.17 – 1.13 | 263 | 65.1% | $\log_{10}(K) = 10.75 \cdot \phi_e + (-1.68)$ | 0.56 |
| **RT3 — Mega-Porous Clean Channel Sand** | DRT 3 (FZI ≥ 1.13) | ≥ 1.13 | 135 | 33.4% | $\log_{10}(K) = 8.33 \cdot \phi_e + (0.06)$ | 0.51 |

### 5.2 Core Permeability Calibration (`PERM` $\times$ `CPERM`) & Data Lineage

| Calibration / Lineage Parameter | Symbol | Value | Unit | Basis / Reference |
| :--- | :---: | :---: | :---: | :--- |
| Overlapping Core Perm Plugs | $N_{perm,cal}$ | 404 | plugs | Target-Zone `PERM` $\times$ `CPERM` Parity |
| Log-Core Permeability Parity | $R^2$ / $\text{RMSE}_{\log_{10}}$ | 0.00 / 1.315 | $\text{dec}$ | Multiplicative Factor Error $= 20.65\times$ |
| Core-to-Log Depth Shift | $\Delta d_{core}$ / $s_{core}$ | +0.00 m / 1.000$\times$ | $\text{m}$ | Affine Shift & Stretch (`RAW_DEPTH` $\to$ `DEPTH`, `CPERM_UNSHIFTED` $\to$ `CPERM`) |
| Overburden & Klinkenberg $K$ | $\sigma_{eff}$ / $P_m$ | 3500 / 45.0 | $\text{psi}$ | `CPERM_AIR` $\to$ `CPERM` ($c_k = 3.0e-05\text{ psi}^{-1}$, Jones) |

Hydraulic Flow Unit partitioning on **Core Plugs (n=404)** classified the reservoir into four Discrete Rock Types (`RT1` through `RT4`) using Flow Zone Indicator cut-offs of $0.5, 1.5,\text{ and }3.0\text{ }\mu\text{m}$. Dominant flow capacity is controlled by **RT3 (Macro-Porous Upper Shoreface)** and **RT4 (Mega-Porous Channel Sand)**, which represent **33.4%** of reservoir samples while contributing **94.6%** of cumulative permeability-thickness ($\sum K\cdot h$) on the Stratigraphic Modified Lorenz Plot ($SMLP$).



![Figure 5.1: Core/Log Porosity-Permeability Crossplot by Rock Type & Stratigraphic Modified Lorenz Plot](/static/reports/rpt_4d5d1d5dd5/fig_5_1_perm_crossplot.png)

<div class="page-break"></div>

# 6. Fluid Contacts & Water Saturation ($S_w$)

### 6.1 Electrical Properties, Formation Water Resistivity & Saturation Equation

* **Saturation Model:** `Archie Clean-Sand Water Saturation Model`
* **Free Water Level ($FWL$):** $2418.6\text{ m TVDss}$
* **Formation Water Salinity & Resistivity:** $35000\text{ ppm NaCl equivalent}$, $R_w = 0.080\text{ }\Omega\cdot\text{m} \text{ @ } 75.0^\circ\text{C}$ (Arps temperature scaling).
* **Electrical Tortuosity, Cementation & Saturation Exponents:** $a = 1.0$, $m = 2.0$, $n = 2.0$

$$S_w^n + R_w \cdot B \cdot Q_v \cdot S_w^{n-1} = \frac{a \cdot R_w}{\phi_t^m \cdot R_t} \quad \text{(Waxman-Smits Shaly-Sand)} \qquad S_w = \left(\frac{a \cdot R_w}{\phi_t^m \cdot R_t}\right)^{1/n} \quad \text{(Archie)}$$

| Parameter | Symbol | Value | Unit | Basis / Calibration |
| :--- | :---: | :---: | :---: | :--- |
| Tortuosity Factor | $a$ | 1.0 | unitless | Electrical Tortuosity / Pickett Plot |
| Cementation Exponent | $m$ | 2.0 | unitless | Formation Factor ($F = a / \phi^m$) |
| Saturation Exponent | $n$ | 2.0 | unitless | Resistivity Index ($RI = S_w^{-n}$) |
| Formation Water Resistivity | $R_w$ | 0.080 | $\Omega\cdot\text{m}$ | Water Zone Pickett $S_w = 100\%$ Ro Trend |
| Free Water Level | $FWL$ | 2418.6 | $\text{m TVDss}$ | Resistivity-Porosity Fluid Contact Interpretation |

Water saturation ($S_w$) was evaluated using the **Archie Clean-Sand Water Saturation Model** to account for clay-bound counter-ion conductivity ($B \cdot Q_v$) in shaly-sand and heterolithic intervals, where Archie saturation would otherwise overestimate $S_w$. Formation water resistivity was anchored at $R_w = 0.080\text{ }\Omega\cdot\text{m}$ at $75.0^\circ\text{C}$ ($35,000\text{ ppm NaCl}$) with electrical exponents $a=1.0, m=2.0, n=2.0$ and a target-reservoir Free Water Level at $FWL = 2418.6\text{ m TVDss}$.



![Figure 6.1: Pickett Plot & Water Saturation Profile vs. Free Water Level](/static/reports/rpt_4d5d1d5dd5/fig_6_1_pickett_shf_plot.png)

### 6.2 Multi-Well & Zonal Fluid Contacts, Proved Column & Uncertainty Brackets

Accurate delineation of fluid contacts is fundamental to volumetric in-place estimation and dynamic reservoir simulation. The proved hydrocarbon column is bounded by the shallowest and deepest proved fluid limits, while discrete contacts (OWC, GOC, GWC) and Free Water Levels (FWL) define the hydrostatic equilibrium boundaries.

> [!NOTE]
> Discrete single-well fluid contact markers (GUT/GDT/OUT/ODT/WUT/OWC/GOC/FWL) have not yet been extracted or committed to ancillary data for this project. Global saturation model uses $FWL = 2418.6\text{ m TVDss}$.

<div class="page-break"></div>

# 7. Capillary Pressure, Saturation Height Modeling (SHF) & SCAL

### 7.1 Leverett $J$-Function, Lab-to-Reservoir $P_c$ Scaling & Core Stress Lineage

To initialize continuous 3D water saturation in the static geological cellular model above the Free Water Level ($FWL = 2418.6\text{ m TVDss}$, Basis: `Overridden to Target-Zone Transition Zone (TVDss)`), log-derived $S_w$ was reconciled with capillary pressure ($P_c$) curves via the Leverett $J$-Function and Lab-to-Reservoir interfacial tension scaling:

$$P_{c,res} = P_{c,lab} \cdot \frac{(\sigma \cos\theta)_{res}}{(\sigma \cos\theta)_{lab}}, \quad h = TVD_{ss}(FWL) - TVD_{ss}, \quad J(S_w) = \frac{0.2166 \cdot P_{c,res}}{\sigma_{res} \cos\theta_{res}} \sqrt{\frac{K}{\phi}}$$

* **Reservoir Interfacial Tension & Wettability:** $(\sigma \cos\theta)_{res} = 26.0\text{ dynes/cm}$ ($\sigma_{res} = 30.0\text{ dynes/cm}$, $\theta_{res} = 30.0^\circ$).
* **Laboratory Fluid System & $P_c$ Scaling:** $(\sigma \cos\theta)_{lab} = 367.7\text{ dynes/cm}$ ($\sigma_{lab} = 480.0\text{ dynes/cm}$, $\theta_{lab} = 140.0^\circ$; Multiplier $= 0.0707\times$; Reference $25.0\text{ psi Lab} \to 1.766\text{ psi Reservoir}$; Lineage: `PC_LAB` $\to$ `PC`).
* **Core Overburden & Klinkenberg Stress Lineage:** $\sigma_{eff} = 3500\text{ psi}$ (Well-Consolidated Sandstone, $c_\phi = 4.5e-06\text{ psi}^{-1}$, $c_k = 3.0e-05\text{ psi}^{-1}$), $P_m = 45.0\text{ psi}$ (Jones); baseline preserved in `CPORE_AMB` / `CPORE_ORI` and `CPERM_AIR` / `CPERM_ORI`, active curves updated in `CPORE` and `CPERM`.
* **Fluid Density Gradient:** $\rho_w = 1.05\text{ g/cc}$, $\rho_{hc} = 0.8\text{ g/cc}$ ($\Delta\rho = 0.25\text{ g/cc}$).
* **Log $S_w$ vs. $SHF$ Reconciliation:** Mean RMSE $= 0.250\text{ v/v}$, Mean Bias ($S_w - SHF$) $= -0.164\text{ v/v}$.

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

3D static model water saturation initialization via the Leverett $J$-Function ($\sigma\cos\theta = 26.0\text{ dynes/cm}$) reconciles with wireline log $S_w$ ($\text{RMSE} = 0.250\text{ v/v}$, mean bias $-0.164\text{ v/v}$). Dynamic simulation relative permeability tables (`SWOF`, **Calibrated LET SCAL & Core Parameterization**) were parameterized using Corey exponents $N_w = 2.5, N_o = 2.5$ with $S_{wc} = 0.15\text{ v/v}$ and $S_{or} = 0.20\text{ v/v}$.



![Figure 7.1: Capillary Pressure Leverett J-Function by Rock Type & Relative Permeability Curves](/static/reports/rpt_4d5d1d5dd5/fig_7_1_shf_scal_plot.png)

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
| **21-25-2** | Fulmar | `2489.1–2548.9` | — (No TVD) | 59.7 | 53.5 | 0.90 | 0.190 | 0.222 | 54.9 | 52.7 | 0.88 | 0.223 | 0.341 | **7.75** |
| **21-30-8** | Fulmar | `2435.0–2491.9` | `2412.6–2443.0` | 56.8 | 34.0 | 0.60 | 0.232 | 0.221 | 27.1 | 34.0 | 0.60 | 0.221 | 0.316 | **5.14** |
| **21-25-3** | Fulmar | `3098.1–3326.0` | `2571.3–2646.2` | 227.8 | 177.1 | 0.78 | 0.263 | 0.181 | 9.8 | 39.6 | 0.17 | 0.210 | 0.524 | **3.96** |
| **21-30-5** | Fulmar | `2681.0–2742.0` | — (No TVD) | 61.0 | 58.2 | 0.95 | 0.168 | 0.182 | 42.5 | 0.0 | 0.00 | — | — | **0.00** |

### 8.3 Probabilistic Petrophysical Uncertainty Ranges (P90 / P50 / P10 — $N = 1000$ Realizations)

Probabilistic petrophysical uncertainty ranges were quantified across $N = 1000$ Monte Carlo realizations perturbing matrix density ($\sigma_{\rho_{ma}} = \pm 0.015\text{ g/cc}$), clean/shale Gamma Ray endpoints ($\sigma_{GR} = \pm 5\text{ gAPI}$), Archie tortuosity/cementation/saturation parameters ($\sigma_m = \pm 0.08, \sigma_n = \pm 0.10, \sigma_{R_w} = \pm 10\%$), and Net Pay cut-offs ($\Delta V_{sh} = \pm 0.05, \Delta\phi_e = \pm 0.015, \Delta S_w = \pm 0.05$).

| Zone | Metric | P90 (Conservative / Low) | P50 (Base Case) | P10 (Optimistic / High) | Uncertainty Spread (P10/P90) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Fulmar** | HCPT (m) / Φe (v/v) / Sw (v/v) | 3.20 m (Φ=0.191, Sw=0.431) | **4.17 m (Φ=0.216, Sw=0.389)** | 6.04 m (Φ=0.242, Sw=0.371) | 1.89× |


Zonal summation decouples **Net Reservoir** ($V_{sh} \le 0.40\text{ v/v}$, $\phi_e \ge 0.08\text{ v/v}$) from **Net Pay** ($S_w \le 0.65\text{ v/v}$) so static geomodelers can populate 3D aquifer porosity and permeability in water-bearing penetrations. Monte Carlo / Latin Hypercube ($N = 1000$ realizations) uncertainty propagation across the pay-bearing target zones indicates a median P10/P90 $HCPT$ ratio of **1.89×**, driven by matrix density ($\rho_{ma}$), cementation exponent ($m$), and $R_w$ uncertainty.



![Figure 8.1: Cut-off Sensitivity & Probabilistic HCPT Distribution](/static/reports/rpt_4d5d1d5dd5/fig_8_1_uncertainty_plot.png)

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
| **21-25-2** | 393 | 30 | 0.216 | 0.376 | 221.4 | 109.0 | 53.87 | 0.243 |
| **21-30-8** | 374 | 29 | 0.194 | 0.375 | 90.4 | 21.5 | 6.86 | 0.076 |
| **21-25-3** | 1496 | 114 | 0.173 | 0.687 | 39.1 | 19.7 | 10.88 | 0.278 |
| **21-30-5** | 401 | 31 | 0.178 | 0.999 | 115.5 | 70.7 | 45.12 | 0.391 |

Fine-scale evaluated CPI logs within the target reservoir succession were blocked to $2.0\text{ m}$ cellular resolution honoring geological zone boundaries. Cardwell-Parsons directional permeability bounds yield a field-mean vertical-to-horizontal anisotropy ratio ($K_v / K_h = K_{harm} / K_{arith}$) across the evaluated wells, preserving thin-bed vertical baffles for Eclipse/Intersect dynamic simulation.



![Figure 9.1: Fine-Scale CPI vs. Upscaled Blocked Logs Comparison Track](/static/reports/rpt_4d5d1d5dd5/fig_9_1_upscaling_plot.png)

### 9.2 FDP Subsurface Deliverables Handover Manifest

| Deliverable Artifact | Format | Target Consumer | QA/QC Verification Status |
| :--- | :---: | :--- | :---: |
| **Evaluated CPI Composite Well Logs** | `.las` / `.csv` | Petrel / RMS Static Modeling | ✓ Verified (10 Wells) |
| **Zonal Sums & Averages Master Table** | `.csv` / `.md` | Reserves Audit & Volumetric STOIIP | ✓ Verified (24 Zones) |
| **Upscaled Cellular Blocked Logs** | `.csv` | 3D Property Population (`K_h`, `K_v`, `PHIE`, `SW`) | ✓ Verified (2.0m Grid) |
| **SCAL & Saturation Height Function Deck** | `SWOF` / `.inc` | Eclipse / Intersect Dynamic Simulation | ✓ Verified (Leverett-J & Corey/LET) |
| **FDP Petrophysical Evaluation Report** | `.md` / `.pdf` | Subsurface Peer Review & Gate Approval | ✓ Complete |

<div class="page-break"></div>

# Appendix A: Composite Petrophysical Evaluation Logs (CPI)


### Well: `21-25-3`

![CPI Log - 21-25-3](/static/reports/rpt_4d5d1d5dd5/cpi_21-25-3.png)

<div class="page-break"></div>

### Well: `21-30-5`

![CPI Log - 21-30-5](/static/reports/rpt_4d5d1d5dd5/cpi_21-30-5.png)

<div class="page-break"></div>

### Well: `21-25-2`

![CPI Log - 21-25-2](/static/reports/rpt_4d5d1d5dd5/cpi_21-25-2.png)

<div class="page-break"></div>

### Well: `21-30-8`

![CPI Log - 21-30-8](/static/reports/rpt_4d5d1d5dd5/cpi_21-30-8.png)