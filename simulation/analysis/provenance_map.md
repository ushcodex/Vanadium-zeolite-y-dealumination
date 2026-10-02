# Tier 1 Computation Provenance Map

Every energy value admitted to the thesis is traced to exactly one input file, output log, XYZ structure file, and calculation register row ID.

---

## Provenance Map Table

| Register Row ID | State | Input File | Output Log File | Final Geometry XYZ | Electronic Energy (Eh) | Status / Role |
|---|---|---|---|---|---|---|
| `cluster-T1-V02` | `cluster` | `01_models/cluster/cluster-T1-V02.inp` | `01_models/cluster/cluster-T1-V02.out` | `01_models/cluster/cluster-T1-V02.xyz` | $-31.34551236$ | Accepted isolated cluster minimum |
| `h3vo4-T1-V01` | `H3VO4` | `01_models/h3vo4/h3vo4-T1-V01.inp` | `01_models/h3vo4/h3vo4-T1-V01.out` | `01_models/h3vo4/h3vo4-T1-V01.xyz` | $-19.77512769$ | Accepted isolated vanadic acid minimum |
| `h2o-T1-V01` | `H2O` | `01_models/h2o/h2o-T1-V01.inp` | `01_models/h2o/h2o-T1-V01.out` | `01_models/h2o/h2o-T1-V01.xyz` | $-5.07054445$ | Accepted isolated water minimum |
| `V-R-T1-V02` | `V-R` | `02_tier1/V-R/V-R-T1-V02.inp` | `02_tier1/V-R/V-R-T1-V02.out` | `02_tier1/V-R/V-R-T1-V02.xyz` | $-51.19563631$ | Accepted (Collapsed into PRC basin, 0.1925 nm contact) |
| `V-PRC-T1-V01` | `V-PRC` | `02_tier1/V-PRC/V-PRC-T1-V01.inp` | `02_tier1/V-PRC/V-PRC-T1-V01.out` | `02_tier1/V-PRC/V-PRC_canonical.xyz` | $-51.19461241$ | Superseded (Unconverged first pass restored) |
| `V-PRC_canonical` | `V-PRC` | `02_tier1/V-PRC/V-PRC_canonical.xyz` | `02_tier1/V-R/V-R-T1-V02.out` | `02_tier1/V-PRC/V-PRC_canonical.xyz` | $-51.19563631$ | Accepted canonical H-bonded complex |
| `V-TS1-T1-V01` | `V-TS1` | `02_tier1/V-TS1/neb_V-TS1-T1-V01.inp` | `02_tier1/V-TS1/freq_V-TS1-T1-V01.out` | `02_tier1/V-TS1/V-TS1_peak.xyz` | $-50.88659123$ | Artifact, excluded (source: `freq_V-TS1-T1-V01.out`) |
| `V-TS1-T1-V02` | `V-TS1` | `02_tier1/V-TS1/neb_ts_bandA.inp` | `02_tier1/V-TS1/freq_bandA_ci.out` | `02_tier1/V-TS1/neb_ts_bandA_NEB-CI_converged.xyz` | $-51.05820550$ | Candidate, under refinement (CI image estimate $+360.82 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS1-T1-V03` | `V-TS1` | `02_tier1/V-TS1/optts_bandA_ci.inp` | `02_tier1/V-TS1/optts_bandA_ci.out` | `02_tier1/V-TS1/optts_bandA_ci.xyz` | $-51.08132900$ | Candidate, under refinement (OptTS Pass 1 $+300.12 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS1-T1-V04` | `V-TS1` | `02_tier1/V-TS1/optts2_bandA_ci.inp` | `02_tier1/V-TS1/optts2_bandA_ci.out` | `02_tier1/V-TS1/optts2_bandA_ci.xyz` | $-51.08133370$ | Slid to minimum (OptTS continuation 1 converged to 0 imag basin) |
| `V-TS1-T1-V05` | `V-TS1` | `02_tier1/V-TS1/V-TS1_ci_pos_disp.inp` | `02_tier1/V-TS1/V-TS1_ci_pos_disp.out` | `02_tier1/V-TS1/V-TS1_ci_pos_disp.xyz` | $-51.08139865$ | Diagnostic run (CI +0.01nm displacement converged to +300 kJ/mol basin) |
| `V-TS1-T1-V06` | `V-TS1` | `02_tier1/V-TS1/V-TS1_ci_neg_disp.inp` | `02_tier1/V-TS1/V-TS1_ci_neg_disp.out` | `02_tier1/V-TS1/V-TS1_ci_neg_disp.xyz` | $-51.08138390$ | Diagnostic run (CI -0.01nm displacement converged to +300 kJ/mol basin) |
| `V-I1-T1-V01` | `V-I1` | `02_tier1/V-TS1/V-TS1-T1-V02.inp` | `02_tier1/V-TS1/V-TS1-T1-V02.out` | `02_tier1/V-I1/V-I1_canonical.xyz` | $-51.26731716$ | Accepted chemisorbed intermediate minimum |
| `V-TS2-T1-V01` | `V-TS2` | `02_tier1/V-TS2/neb_V-TS2-T1-V01.inp` | `02_tier1/V-TS2/freq_V-TS2-T1-V01.out` | `02_tier1/V-TS2/V-TS2_peak.xyz` | $-50.84621402$ | Artifact, excluded (source: `freq_V-TS2-T1-V01.out`) |
| `V-TS2-T1-V02` | `V-TS2` | `02_tier1/V-TS2/neb_ts_bandB.inp` | `02_tier1/V-TS2/freq_bandB_ci.out` | `02_tier1/V-TS2/neb_ts_bandB_NEB-CI_converged.xyz` | $-51.10991869$ | Candidate, under refinement (CI image estimate $+413.25 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS2-T1-V03` | `V-TS2` | `02_tier1/V-TS2/optts_bandB_ci.inp` | `02_tier1/V-TS2/optts_bandB_ci.out` | `02_tier1/V-TS2/optts_bandB_ci.xyz` | $-51.19071400$ | Candidate, under refinement (OptTS Pass 1 $+201.12 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS2-T1-V04` | `V-TS2` | `02_tier1/V-TS2/optts2_bandB_ci.inp` | `02_tier1/V-TS2/optts2_bandB_ci.out` | `02_tier1/V-TS2/optts2_bandB_ci.xyz` | $-51.20596103$ | Candidate, under refinement (OptTS continuation 1 $+161.09 \text{ kJ/mol}$; Step 0 freqs: 1 imag) |
| `V-TS2-T1-V05` | `V-TS2` | `02_tier1/V-TS2/optts3_bandB_ci.inp` | `02_tier1/V-TS2/optts3_bandB_ci.out` | `02_tier1/V-TS2/optts3_bandB_ci.xyz` | $-51.20610884$ | Accepted (OptTS continuation 2 CONVERGED, barrier $+160.70 \text{ kJ/mol}$ vs $V\text{-}I_1$; 1 imag: $-78.21 \text{ cm}^{-1}$; A1-A5 passed) |
| `V-TS2-T1-V06` | `V-TS2` | `02_tier1/V-TS2/V-TS2_ts_pos_disp.inp` | `02_tier1/V-TS2/V-TS2_ts_pos_disp.out` | `02_tier1/V-TS2/V-TS2_ts_pos_disp.xyz` | $-51.24508512$ | Diagnostic run (A4) (Mode 6 +0.01nm displacement converged to V-I2 well, +15.64 kJ/mol vs V-I2, 0 imag) |
| `V-TS2-T1-V07` | `V-TS2` | `02_tier1/V-TS2/V-TS2_ts_neg_disp.inp` | `02_tier1/V-TS2/V-TS2_ts_neg_disp.out` | `02_tier1/V-TS2/V-TS2_ts_neg_disp.xyz` | $-51.22653425$ | Diagnostic run (A4) (Mode 6 -0.01nm displacement converged to V-I1 well, +107.08 kJ/mol vs V-I1, 0 imag) |
| `V-I2-T1-V03` | `V-I2` | `02_tier1/V-TS2/V-TS2-T1-V03.inp` | `02_tier1/V-TS2/V-TS2-T1-V03.out` | `02_tier1/V-TS2/V-TS2-T1-V03.xyz` | $-51.25102836$ | Superseded (imag mode $-118.68 \text{ cm}^{-1}$ restored) |
| `V-I2-T1-V04` | `V-I2` | `02_tier1/V-I2/V-I2-T1-V04_pos.inp` | `02_tier1/V-I2/V-I2-T1-V04_pos.out` | `02_tier1/V-I2/V-I2_canonical.xyz` | $-51.25104052$ | Accepted hydrolysed intermediate minimum (mode-displaced) |
| `V-TS3-T1-V01` | `V-TS3` | `02_tier1/V-TS3/neb_V-TS3-T1-V01.inp` | `02_tier1/V-TS3/freq_V-TS3-T1-V01.out` | `02_tier1/V-TS3/V-TS3_peak.xyz` | $-50.60576010$ | Artifact, excluded (source: `freq_V-TS3-T1-V01.out`) |
| `V-TS3-T1-V02` | `V-TS3` | `02_tier1/V-TS3/neb_ts_bandC.inp` | `02_tier1/V-TS3/freq_bandC_ci.out` | `02_tier1/V-TS3/neb_ts_bandC_NEB-CI_converged.xyz` | $-51.05369850$ | Candidate, under refinement (CI image estimate $+518.12 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS3-T1-V03` | `V-TS3` | `02_tier1/V-TS3/optts_bandC_ci.inp` | `02_tier1/V-TS3/optts_bandC_ci.out` | `02_tier1/V-TS3/optts_bandC_ci.xyz` | $-51.06621100$ | Candidate, under refinement (OptTS Pass 1 $+485.27 \text{ kJ/mol}$; Step 0 freqs) |
| `V-TS3-T1-V04` | `V-TS3` | `02_tier1/V-TS3/optts2_bandC_ci.inp` | `02_tier1/V-TS3/optts2_bandC_ci.out` | `02_tier1/V-TS3/optts2_bandC_ci.xyz` | $-51.06676972$ | Candidate, under refinement (OptTS continuation 1 $+483.80 \text{ kJ/mol}$; Step 0 freqs: 3 imag) |
| `V-TS3-T1-V05` | `V-TS3` | `02_tier1/V-TS3/optts3_bandC_ci.inp` | `02_tier1/V-TS3/optts3_bandC_ci.out` | `02_tier1/V-TS3/optts3_bandC_ci.xyz` | $-51.06496560$ | Candidate, under refinement (OptTS continuation 2 $+488.54 \text{ kJ/mol}$; Step 0 freqs: 1 imag $-40.33 \text{ cm}^{-1}$) |
| `V-P-T1-V01` | `V-P` | `02_tier1/V-TS3/V-TS3-T1-V02.inp` | `02_tier1/V-TS3/V-TS3-T1-V02.out` | `02_tier1/V-P/V-P_canonical.xyz` | $-51.15221675$ | Accepted product minimum |
| `W-PRC-T1-V02` | `W-PRC` | `02_tier1/W-PRC/W-PRC-T1-V02.inp` | `02_tier1/W-PRC/W-PRC-T1-V02.out` | `02_tier1/W-PRC/W-PRC-T1-V02.xyz` | $-36.44256091$ | Accepted water complex minimum |
| `W-TS-T1-V01` | `W-TS` | `02_tier1/W-TS/neb_W-TS-T1-V01.inp` | `02_tier1/W-TS/neb_W-TS-T1-V01.out` | `02_tier1/W-TS/neb_W-TS-T1-V01_NEB-CI_converged.xyz` | $-36.40334386$ | Superseded (Old CI-NEB run restored for audit trail) |
| `W-TS-T1-V02` | `W-TS` | `02_tier1/W-TS/neb_ts_bandD.inp` | `02_tier1/W-TS/freq_bandD_ci.out` | `02_tier1/W-TS/neb_ts_bandD_NEB-CI_converged.xyz` | $-36.41774965$ | Candidate, under refinement (CI image estimate $+65.14 \text{ kJ/mol}$; Step 0 freqs) |
| `W-TS-T1-V03` | `W-TS` | `02_tier1/W-TS/optts_bandD_ci.inp` | `02_tier1/W-TS/optts_bandD_ci.out` | `02_tier1/W-TS/optts_bandD_ci.xyz` | $-36.43115234$ | Candidate, under refinement (OptTS Pass 1 $+29.95 \text{ kJ/mol}$; Step 0 freqs) |
| `W-TS-T1-V04` | `W-TS` | `02_tier1/W-TS/optts2_bandD_ci.inp` | `02_tier1/W-TS/optts2_bandD_ci.out` | `02_tier1/W-TS/optts2_bandD_ci.xyz` | $-36.43140308$ | Candidate (pending A4) (OptTS continuation 1 CONVERGED; 1 imag: $-226.10 \text{ cm}^{-1}$) |
| `W-TS-T1-V05` | `W-TS` | `02_tier1/W-TS/optts_bandD_frozencaps.inp` | `02_tier1/W-TS/optts_bandD_frozencaps.out` | `02_tier1/W-TS/optts_bandD_frozencaps.xyz` | $-36.41883009$ | Diagnostic run (Step E2 frozen caps; 5 imag modes) |
| `W-TS-T1-V06` | `W-TS` | `02_tier1/W-TS/W-TS_pos_disp.inp` | `02_tier1/W-TS/W-TS_pos_disp.out` | `02_tier1/W-TS/W-TS_pos_disp.xyz` | $-36.44204682$ | Diagnostic run (Mode 6 +0.01nm displacement converged to W-PRC well, +1.35 kJ/mol vs W-PRC) |
| `W-TS-T1-V07` | `W-TS` | `02_tier1/W-TS/W-TS_neg_disp.inp` | `02_tier1/W-TS/W-TS_neg_disp.out` | `02_tier1/W-TS/W-TS_neg_disp.xyz` | $-36.44204971$ | Diagnostic run (Mode 6 -0.01nm displacement converged to W-PRC well, +1.34 kJ/mol vs W-PRC) |
| `W-P-T1-V01` | `W-P` | `02_tier1/W-P/W-P-T1-V01.inp` | `02_tier1/W-P/W-P-T1-V01.out` | `02_tier1/W-P/W-P-T1-V01.xyz` | $-36.44113826$ | Accepted water product minimum |
