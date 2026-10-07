# Verified result tables

Built by `simulation/analysis/build_tables.py` from `orca_register.csv`, which is
produced by `simulation/analysis/parse_orca.py` straight from the ORCA logs.
1 Eh = 2625.499639 kJ/mol (CODATA 2018).

## Tier 1, GFN2-xTB (ORCA 6.1.0, Dell Latitude E6430)

| state | log file | E / Eh | rel. to separated reactants / kJ/mol | imaginary modes |
|---|---|---|---|---|
| cluster | `01_models/cluster/cluster-T1-V02.out` | -31.34551236 | reference | 0 |
| H2O | `01_models/h2o/h2o-T1-V01.out` | -5.07054445 | reference | 0 |
| H3VO4 | `01_models/h3vo4/h3vo4-T1-V01.out` | -19.77512769 | reference | 0 |
| V-PRC | `02_tier1/V-R/V-R-T1-V02.out` | -51.19563631 | -196.90 | 0 |
| V-I1 | `02_tier1/V-I1/V-I1-T1-V01.out` | -51.26731716 | -385.10 | 0 |
| V-TS2 | `02_tier1/V-TS2/optts3_bandB_ci.out` | -51.20610884 | -224.40 | 1 |
| V-I2 | `02_tier1/V-I2/V-I2-T1-V04_pos.out` | -51.25104052 | -342.37 | 0 |
| V-P | `02_tier1/V-TS3/V-TS3-T1-V02.out` | -51.15221675 | -82.90 | 0 |
| W-PRC | `02_tier1/W-PRC/W-PRC-T1-V02.out` | -36.44256091 | -69.59 | 0 |
| W-TS | `02_tier1/W-TS/optts2_bandD_ci.out` | -36.43140308 | -40.29 | 1 |
| W-P | `02_tier1/W-P/W-P-T1-V01.out` | -36.44113826 | -65.85 | 0 |

Tier 1 reference zero, vanadium route: -51.12064005 Eh.
Tier 1 reference zero, steam route: -36.41605681 Eh.

## Tier 2, B3LYP-D3(BJ)/def2-TZVP (ORCA 6.1.1, cloud)

### Converged and frequency verified

| state | log file | cycles | E / Eh | ZPE / Eh | H(298) corr / Eh | G(298) corr / Eh | G(1003) corr / Eh | imaginary |
|---|---|---|---|---|---|---|---|---|
| cluster | `03_tier2_completion/results/s1_03_cluster_optfreq.out` | 1 | -1709.39409388 | 0.13065186 | 0.00094421 | 0.08466275 | -0.10976592 | -4.64 |
| H2O | `03_tier2_completion/results/s1_01_h2o_optfreq.out` | 4 | -76.42662980 | 0.02114986 | 0.00094421 | 0.00350503 | -0.05398928 | 0 |
| H3VO4 | `03_tier2_completion/results/s1_02_h3vo4_optfreq.out` | 14 | -1246.82501396 | 0.04368951 | 0.00094421 | 0.01335237 | -0.10253549 | 0 |
| V-PRC | `03_tier2_completion/results/s1_04_vprc_optfreq.out` | 40 | -2956.25453185 | 0.17863014 | 0.00094421 | 0.12694676 | -0.12607009 | 0 |
| W-PRC | `03_tier2_completion/results/s1_05_wprc_optfreq.out` | 63 | -1785.85055438 | 0.15613750 | 0.00094421 | 0.10700319 | -0.10839383 | 0 |
| V-I1 | `03_tier2_completion/results/s4_01_vi1_optfreq.out` | 27 | -2956.26305203 | 0.18123679 | 0.00094421 | 0.12833343 | -0.12709898 | 0 |
| W-P | `03_tier2_completion/results/s4_04_wp_optfreq.out` | 75 | -1785.82987393 | 0.15597141 | 0.00094421 | 0.10904705 | -0.10407863 | 0 |

### Started but not converged (reported, not used for the conclusions)

| state | log file | status | best E / Eh |
|---|---|---|---|
| V-I2 | `03_tier2_completion/results/first_pass/s4_02_vi2_optfreq.out` | 90 opt cycles, terminated normally, not converged | -2956.26562215 |
| V-I2 | `03_tier2_completion/results/s4_02_vi2_optfreq.out` | 60 opt cycles, not converged | -2956.26639173 |
| V-P | `03_tier2_completion/results/first_pass/s4_03_vp_optfreq.out` | 90 opt cycles, terminated normally, not converged | -2956.05925722 |
| V-P | `03_tier2_completion/results/s4_03_vp_optfreq.out` | 25 opt cycles, job did not terminate normally | -2956.05930432 |
| V-TS2 | `03_tier2_completion/results/s4_05_vts2_optts.out` | OptTS stopped at 200 cycles with 14 imaginary modes | -2956.09584386 |

Tier 2 reference zero, vanadium route: -2956.21910784 Eh.
Tier 2 reference zero, steam route: -1785.82072368 Eh.

### Adsorption thermodynamics at the Brønsted site

| quantity | vanadic acid, H3VO4 | steam, H2O | vanadic acid minus steam |
|---|---|---|---|
| electronic dE | -93.01 | -78.32 | -14.69 |
| dE with ZPE | -81.75 | -66.94 | -14.81 |
| dH at 298.15 K | -95.48 | -80.80 | -14.69 |
| dG at 298.15 K | -17.05 | -28.87 | 11.82 |
| dG at 1003.15 K | 133.39 | 67.03 | 66.36 |

Thermal corrections are the G-E(el) and H-E(el) terms printed by ORCA in the
frequency run of each job. The reference is the separated cluster plus the free
molecule, each at its own optimised geometry.

### PBE0-D3(BJ)/def2-TZVP single points on the Tier 2 geometries

| state | log file | E / Eh |
|---|---|---|
| cluster | `03_tier2_completion/results/pbe0_cluster.out` | -1708.73603847 |
| H2O | `03_tier2_completion/results/pbe0_h2o.out` | -76.37772540 |
| H3VO4 | `03_tier2_completion/results/pbe0_h3vo4.out` | -1246.47959790 |
| V-PRC | `03_tier2_completion/results/pbe0_v-prc.out` | -2955.25108328 |
| W-PRC | `03_tier2_completion/results/pbe0_w-prc.out` | -1785.14371013 |
| V-I1 | `03_tier2_completion/results/pbe0_v-i1.out` | -2955.26139255 |
| V-I2 | `03_tier2_completion/results/pbe0_v-i2.out` | -2955.26152473 |
| V-P | `03_tier2_completion/results/pbe0_v-p.out` | -2955.05828171 |
| W-P | `03_tier2_completion/results/pbe0_w-p.out` | -1785.12248001 |
| V-TS2(candidate) | `03_tier2_completion/results/pbe0_v-ts2.out` | -2955.08636153 |

PBE0 electronic adsorption energy, vanadic acid: -93.07 kJ/mol.
PBE0 electronic adsorption energy, steam: -78.62 kJ/mol.
PBE0 margin, vanadic acid over steam: -14.44 kJ/mol.

### Tier 2 stationary-point ladder (electronic energies only)

| state | relative to separated cluster + H3VO4 / kJ/mol | note |
|---|---|---|
| V-PRC | -93.01 | converged, 0 imaginary |
| V-I1 | -115.38 | converged, 0 imaginary |
| V-I2 | -122.12 | not converged; bracket only |
| V-P | 419.69 | not converged; bracket only |
| V-TS2 | 323.63 | rejected: 14 imaginary modes |

| state | relative to separated cluster + H2O / kJ/mol | note |
|---|---|---|
| W-PRC | -78.32 | converged, 0 imaginary |
| W-P | -24.02 | converged, 0 imaginary |

### Tier 1 barrier summary (GFN2-xTB)

| step | barrier / kJ/mol | imaginary mode / cm-1 |
|---|---|---|
| V-PRC -> V-TS2 (first Al-O cleavage via V-I1) | 160.70 (from V-I1) | -78.21 |
| W-PRC -> W-TS (steam hydrolysis) | 29.29 (from W-PRC) | -226.10 |

V-I1 lies -188.20 kJ/mol below V-PRC at Tier 1.
V-I2 lies 42.73 kJ/mol above V-I1 at Tier 1.

### Cluster reference check

| run | E / Eh | cycles | converged | imaginary |
|---|---|---|---|---|
| `03_tier2_completion/results/first_pass/s1_03_cluster_optfreq.out` | -1709.39409330 | 66 | no | 0 |
| `03_tier2_completion/results/s1_03_cluster_optfreq.out` | -1709.39409388 | 1 | yes | -4.64 |

Spread between the two cluster runs: 0.0015 kJ/mol.

