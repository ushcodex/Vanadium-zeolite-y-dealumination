# APPENDICES

## Appendix A. Calculation Register

This register records the accepted DFT minima, incomplete DFT jobs, counterpoise fragment calculations, and transition-state checks used in the thesis. Job identifiers and log files are retained under `simulation/03_tier2_completion/results/` and `simulation/02_tier1/`.

### A.1 DFT structure and pathway jobs

Table A.1 identifies the structures used in Chapter Four and the main incomplete pathway jobs. The register distinguishes converged minima from jobs whose final geometries or frequencies were unavailable.

[TBL: Table A.1: DFT reference, adsorption, and pathway calculation register | Method and state;ORCA output;Status and frequency result;Use in thesis | B3LYP cluster reference;s1_03_cluster_optfreq.out;Converged, one flat reference mode at −4.64 cm⁻¹;Energy and Gibbs reference | B3LYP H₃VO₄;s1_02_h3vo4_optfreq.out;Converged minimum, zero imaginary modes;Isolated vanadic-acid reference | B3LYP H₂O;s1_01_h2o_optfreq.out;Converged minimum, zero imaginary modes;Isolated water reference | B3LYP V-PRC;s1_04_vprc_optfreq.out;Converged minimum, zero imaginary modes;Vanadic-acid adsorption energy and geometry | B3LYP W-PRC;s1_05_wprc_optfreq.out;Converged minimum, zero imaginary modes;Water adsorption energy and geometry | B3LYP V-I1;s4_01_vi1_optfreq.out;Converged minimum, zero imaginary modes;Post-adsorption minimum | B3LYP W-P;s4_04_wp_optfreq.out;Converged minimum, zero imaginary modes;Water-path post-adsorption minimum | PBE0 adsorption and post-adsorption single points;pbe0_cluster.out, pbe0_h2o.out, pbe0_h3vo4.out, pbe0_v-prc.out, pbe0_w-prc.out, pbe0_v-i1.out, pbe0_w-p.out;Completed;Electronic-energy comparison in Tables 4.3 and 4.4 | B3LYP V-TS2;s4_05_vts2_optts.out;200 cycles reached, optimisation unconverged, 14 imaginary modes;DFT transition-state assessment in Appendix A | B3LYP V-I2;first_pass/s4_02_vi2_optfreq.out and s4_02_vi2_optfreq.out;90- and 60-cycle runs, both unconverged, frequency data unavailable;Excluded from final DFT minima | B3LYP V-P;first_pass/s4_03_vp_optfreq.out and s4_03_vp_optfreq.out;90-cycle run unconverged, 25-cycle run ended before normal completion;Excluded from final DFT minima]

### A.2 Counterpoise fragment calculations

Four manual ghost-fragment jobs were run for the PBE0 counterpoise estimate. Table A.2 records their outcomes. Three jobs completed normally and the V-PRC cluster-fragment job terminated in the LEANSCF step, leaving the fragment set incomplete; the Chapter Four adsorption energies therefore use the direct electronic values.

[TBL: Table A.2: PBE0 counterpoise ghost-fragment calculation register | Complex and fragment;Output file;Final status;Final energy / Eh | V-PRC cluster ghost;v-prc_cp_ghost-cluster.out;LEANSCF error termination;Unavailable | V-PRC H₃VO₄ ghost;v-prc_cp_ghost-h3vo4.out;Normal termination;−1708.714841090478 | W-PRC cluster ghost;w-prc_cp_ghost-cluster.out;Normal termination;−76.378622223824 | W-PRC H₂O ghost;w-prc_cp_ghost-h2o.out;Normal termination;−1708.730926698051]

### A.3 Tier 1 transition-state and displacement register

Table A.3 summarises the GFN2-xTB candidate structures and the paired mode-displacement results. The vanadic-acid candidate passed the recorded acceptance checks; both water-path displacements returned to W-PRC.

[TBL: Table A.3: Tier 1 pathway candidate and two-sided displacement register | Candidate output;Imaginary mode and status;Positive displacement;Negative displacement;Classification | V-TS2, optts3_bandB_ci.out;−78.21 cm⁻¹;V-TS2_ts_pos_disp.out → V-I2 well (+15.64 kJ mol⁻¹ vs V-I2);V-TS2_ts_neg_disp.out → V-I1 well (+107.08 kJ mol⁻¹ vs V-I1);Accepted GFN2-xTB saddle-point candidate, A1–A5 passed | W-TS, optts2_bandD_ci.out;−226.10 cm⁻¹;W-TS_pos_disp.out → W-PRC well (+1.35 kJ mol⁻¹ vs W-PRC);W-TS_neg_disp.out → W-PRC well (+1.34 kJ mol⁻¹ vs W-PRC);Candidate rejected by the two-sided displacement criterion]

## Appendix B. Worked Calculations

Appendix B gives the numerical substitutions behind Tables 4.3–4.7. Energies were converted using 1 Eh = 2625.499638 kJ mol⁻¹. Values are shown to sufficient precision to reproduce the rounded results in Chapter Four.

### B.1 Regenerator partial-pressure conversions

Equation (2.1) describes the proposed formation of gas-phase vanadic acid. At 20% steam and a total pressure of 2 atm, the water partial pressure used in Eq. (3.5) was calculated as shown in Eq. (B.1):

p(H₂O) = 0.20 × 2 atm = 0.40 atm
(B.1)

A range of 1–10 ppm H₃VO₄ at 2 atm gives the partial pressures in Eq. (B.2):

p(H₃VO₄) = (1–10) × 10⁻⁶ × 2 atm = 2 × 10⁻⁶ to 2 × 10⁻⁵ atm
(B.2)

The 3.37 × 10⁻⁶ atm estimate by Trujillo et al. (1997) corresponds to the concentration calculated in Eq. (B.3):

x(H₃VO₄) = [3.37 × 10⁻⁶ atm / 2 atm] × 10⁶ = 1.685 ppm
(B.3)

Equations (B.1)–(B.3) provide the gas composition used in the conditional occupation calculation.

### B.2 Electronic adsorption energies

Using Eq. (3.1), the B3LYP adsorption energy for vanadic acid was calculated from the cluster and isolated-molecule energies. Equation (B.4) gives the reference sum, and Eq. (B.5) subtracts that reference from the V-PRC energy:

E(reference, H₃VO₄) = −1709.394093884 − 1246.825013959 = −2956.219107843 Eh
(B.4)

ΔEₐdₛ(H₃VO₄, B3LYP) = −2956.254531846 − (−2956.219107843) = −0.035424003 Eh
(B.5)

Conversion of Eq. (B.5) to kJ mol⁻¹ is shown in Eq. (B.6):

ΔEₐdₛ = −0.035424003 × 2625.499638 = −93.0057 kJ mol⁻¹
(B.6)

The water reference sum and W-PRC difference are shown in Eqs. (B.7) and (B.8); Eq. (B.9) gives the converted energy:

E(reference, H₂O) = −1709.394093884 − 76.426629796 = −1785.820723680 Eh
(B.7)

ΔEₐdₛ(H₂O, B3LYP) = −1785.850554383 − (−1785.820723680) = −0.029830703 Eh
(B.8)

ΔEₐdₛ = −0.029830703 × 2625.499638 = −78.3205 kJ mol⁻¹
(B.9)

The B3LYP relative preference from Eq. (3.2) is calculated in Eq. (B.10):

ΔΔE(B3LYP) = −93.0057 − (−78.3205) = −14.6852 kJ mol⁻¹
(B.10)

The same Eq. (3.1) was applied to the PBE0 single-point values using their own cluster and isolated-molecule references. Equations (B.11)–(B.13) show the vanadic-acid calculation, and Eqs. (B.14)–(B.16) show the water calculation:

E(reference, H₃VO₄, PBE0) = −1708.736038466 − 1246.479597897 = −2955.215636364 Eh
(B.11)

ΔEₐdₛ(H₃VO₄, PBE0) = −2955.251083282 − (−2955.215636364) = −0.035446919 Eh
(B.12)

ΔEₐdₛ = −0.035446919 × 2625.499638 = −93.0659 kJ mol⁻¹
(B.13)

E(reference, H₂O, PBE0) = −1708.736038466 − 76.377725398 = −1785.113763864 Eh
(B.14)

ΔEₐdₛ(H₂O, PBE0) = −1785.143710125 − (−1785.113763864) = −0.029946261 Eh
(B.15)

ΔEₐdₛ = −0.029946261 × 2625.499638 = −78.6239 kJ mol⁻¹
(B.16)

Equation (B.17) gives the PBE0 preference using Eq. (3.2):

ΔΔE(PBE0) = −93.0659 − (−78.6239) = −14.4420 kJ mol⁻¹
(B.17)

The substitutions in Eqs. (B.4)–(B.17) produce the DFT entries in Table 4.3. For GFN2-xTB, the separated references are E(reference, H₃VO₄) = −31.34551236 − 19.77512769 = −51.12064005 Eh and E(reference, H₂O) = −31.34551236 − 5.07054445 = −36.41605681 Eh. Applying Eq. (3.1) gives ΔEₐdₛ(V-PRC) = [−51.19563631 − (−51.12064005)] × 2625.499638 = −196.90 kJ mol⁻¹ and ΔEₐdₛ(W-PRC) = [−36.44256091 − (−36.41605681)] × 2625.499638 = −69.59 kJ mol⁻¹. Their difference from Eq. (3.2) is −196.90 − (−69.59) = −127.31 kJ mol⁻¹.

### B.3 Relative energies of post-adsorption minima

The post-adsorption energies in Table 4.4 use the separated cluster-and-adsorbate reference for the corresponding route. Equations (B.18) and (B.19) show the Tier 1 values for V-I1 and W-P:

ΔE(V-I1, xTB) = [−51.26731716 − (−51.12064005)] × 2625.499638 = −385.10 kJ mol⁻¹
(B.18)

ΔE(W-P, xTB) = [−36.44113826 − (−36.41605681)] × 2625.499638 = −65.85 kJ mol⁻¹
(B.19)

The corresponding B3LYP calculations appear in Eqs. (B.20) and (B.21), and the PBE0 single-point calculations appear in Eqs. (B.22) and (B.23):

ΔE(V-I1, B3LYP) = [−2956.263052029 − (−2956.219107843)] × 2625.499638 = −115.3754 kJ mol⁻¹
(B.20)

ΔE(W-P, B3LYP) = [−1785.829873928 − (−1785.820723680)] × 2625.499638 = −24.0240 kJ mol⁻¹
(B.21)

ΔE(V-I1, PBE0) = [−2955.261392549 − (−2955.215636364)] × 2625.499638 = −120.1328 kJ mol⁻¹
(B.22)

ΔE(W-P, PBE0) = [−1785.122480008 − (−1785.113763864)] × 2625.499638 = −22.8842 kJ mol⁻¹
(B.23)

### B.4 Harmonic Gibbs-energy substitutions

For each state, the adsorption Gibbs energy was calculated from Eq. (3.3). The harmonic thermal correction is the difference between ΔGₐdₛ and the corresponding electronic ΔEₐdₛ. Table B.1 lists the B3LYP electronic energies, thermal corrections, and Gibbs energies for the four states in Table 4.6:

[TBL: Table B.1: Electronic and harmonic Gibbs-energy terms for accepted DFT states (kJ mol⁻¹) | State;Electronic ΔEₐdₛ;Thermal correction at 298.15 K;ΔGₐdₛ at 298.15 K;Thermal correction at 1003.15 K;ΔGₐdₛ at 1003.15 K | V-PRC;−93.0057;+75.9600;−17.0457;+226.4003;+133.3946 | V-I1;−115.3754;+79.6007;−35.7747;+223.6989;+108.3235 | W-PRC;−78.3205;+49.4524;−28.8681;+145.3513;+67.0308 | W-P;−24.0240;+54.8185;+30.7945;+156.6808;+132.6568]

The temperature-dependent values in Table B.1 follow the substitutions in Eqs. (B.24) and (B.25):

ΔGₐdₛ(V-PRC, 298.15 K) = −93.0057 + 75.9600 = −17.0457 kJ mol⁻¹
(B.24)

ΔGₐdₛ(V-PRC, 1003.15 K) = −93.0057 + 226.4003 = +133.3946 kJ mol⁻¹
(B.25)

ΔGₐdₛ(W-PRC, 298.15 K) = −78.3205 + 49.4524 = −28.8681 kJ mol⁻¹
(B.26)

ΔGₐdₛ(W-PRC, 1003.15 K) = −78.3205 + 145.3513 = +67.0308 kJ mol⁻¹
(B.27)

Applying Eq. (3.3) to the two post-adsorption minima gives ΔGₐdₛ(V-I1, 298.15 K) = −115.3754 + 79.6007 = −35.7747 kJ mol⁻¹ and ΔGₐdₛ(V-I1, 1003.15 K) = −115.3754 + 223.6989 = +108.3235 kJ mol⁻¹. For W-P, the corresponding substitutions are ΔGₐdₛ(W-P, 298.15 K) = −24.0240 + 54.8185 = +30.7945 kJ mol⁻¹ and ΔGₐdₛ(W-P, 1003.15 K) = −24.0240 + 156.6808 = +132.6568 kJ mol⁻¹, as listed in Table B.1.

The water-favouring differences at 298.15 K and 1003.15 K are calculated in Eqs. (B.28) and (B.29):

ΔG(V-PRC) − ΔG(W-PRC), 298.15 K = −17.0457 − (−28.8681) = +11.8224 kJ mol⁻¹
(B.28)

ΔG(V-PRC) − ΔG(W-PRC), 1003.15 K = 133.3946 − 67.0308 = +66.3638 kJ mol⁻¹
(B.29)

### B.5 Competitive-site equilibrium constants and fractions

Equation (3.4) was evaluated with R = 0.008314462618 kJ mol⁻¹ K⁻¹ and T = 1003.15 K. The substitutions in Eqs. (B.30) and (B.31) give the standard equilibrium constants:

K°(H₃VO₄) = exp[−133.3945918 / (0.008314462618 × 1003.15)] = 1.1329138 × 10⁻⁷
(B.30)

K°(H₂O) = exp[−67.0307562 / (0.008314462618 × 1003.15)] = 3.2339647 × 10⁻⁴
(B.31)

The pressure-weighted terms qᵢ = K°ᵢ(pᵢ/p°) used in Eq. (3.5) are calculated in Eqs. (B.32)–(B.34):

q(H₂O) = 3.2339647 × 10⁻⁴ × (0.4/1.0) = 1.2935859 × 10⁻⁴
(B.32)

q(H₃VO₄, 1 ppm) = 1.1329138 × 10⁻⁷ × (2 × 10⁻⁶/1.0) = 2.2658275 × 10⁻¹³
(B.33)

q(H₃VO₄, 10 ppm) = 1.1329138 × 10⁻⁷ × (2 × 10⁻⁵/1.0) = 2.2658275 × 10⁻¹²
(B.34)

For 1 ppm H₃VO₄, Eq. (3.5) gives the denominator and fractions in Eqs. (B.35) and (B.36):

D = 1 + 2.2658275 × 10⁻¹³ + 1.2935859 × 10⁻⁴ = 1.0001293586
(B.35)

θ(H₃VO₄) = 2.2658275 × 10⁻¹³/D = 2.2655344 × 10⁻¹³; θ(H₂O) = 1.2935859 × 10⁻⁴/D = 1.2934186 × 10⁻⁴
(B.36)

θ(H₂O)/θ(H₃VO₄), 1 ppm = 1.2934186 × 10⁻⁴ / 2.2655344 × 10⁻¹³ = 5.7091102 × 10⁸
(B.37)

For 10 ppm H₃VO₄, the corresponding substitutions appear in Eqs. (B.38) and (B.39):

D = 1 + 2.2658275 × 10⁻¹² + 1.2935859 × 10⁻⁴ = 1.0001293586
(B.38)

θ(H₃VO₄) = 2.2658275 × 10⁻¹²/D = 2.2655344 × 10⁻¹²; θ(H₂O) = 1.2935859 × 10⁻⁴/D = 1.2934186 × 10⁻⁴
(B.39)

θ(H₂O)/θ(H₃VO₄), 10 ppm = 1.2934186 × 10⁻⁴ / 2.2655344 × 10⁻¹² = 5.7091102 × 10⁷
(B.40)

Equations (B.30)–(B.40) reproduce the ranges in Table 4.7 under the standard-pressure, single-site, ideal-gas harmonic assumptions stated in Section 3.5.

### B.6 Tier 1 candidate barrier substitutions

The GFN2-xTB candidate barrier was calculated from the candidate and starting-minimum energies in the Tier 1 register. Equation (B.41) shows the accepted V-TS2 result; Eq. (B.42) shows the water-path candidate energy difference recorded in Table 4.5.

ΔE‡(V-I1 → V-I2) = [−51.20610884 − (−51.26731716)] × 2625.499638 = 160.7024 kJ mol⁻¹
(B.41)

ΔE‡(W-PRC → W-TS candidate) = [−36.43140308 − (−36.44256091)] × 2625.499638 = 29.2949 kJ mol⁻¹
(B.42)

The W-TS energy difference in Eq. (B.42) is a candidate value; its displacement record and classification are given in Table A.3.
