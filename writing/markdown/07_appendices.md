# APPENDICES

## Appendix A. Calculation Register

### A.1 Numerical input register

The numerical inputs are listed before the calculation-status register. Electronic energies are final single-point energies in hartree (Eh); the thermal entries are the ORCA absolute harmonic Gibbs corrections, G − Eₑₗ, at each temperature. Source paths are relative to the repository root. The worked calculations in Appendix B cite these tables and use 1 Eh = 2625.4996394799 kJ mol⁻¹.

[TBL: Table A.1: B3LYP-D3(BJ)/def2-TZVP electronic-energy inputs | State;Electronic energy (Eh);Source output log | Zeolite Y cluster;−1709.394093884281;simulation/03_tier2_completion/results/s1_03_cluster_optfreq.out | H₂O;−76.426629795556;simulation/03_tier2_completion/results/s1_01_h2o_optfreq.out | H₃VO₄;−1246.825013958827;simulation/03_tier2_completion/results/s1_02_h3vo4_optfreq.out | V-PRC;−2956.254531846348;simulation/03_tier2_completion/results/s1_04_vprc_optfreq.out | W-PRC;−1785.850554383119;simulation/03_tier2_completion/results/s1_05_wprc_optfreq.out | V-I1;−2956.263052028540;simulation/03_tier2_completion/results/s4_01_vi1_optfreq.out | W-P;−1785.829873927753;simulation/03_tier2_completion/results/s4_04_wp_optfreq.out]

[TBL: Table A.2: PBE0-D3(BJ)/def2-TZVP single-point electronic-energy inputs | State;Electronic energy (Eh);Source output log | Zeolite Y cluster;−1708.736038466437;simulation/03_tier2_completion/results/pbe0_cluster.out | H₂O;−76.377725397537;simulation/03_tier2_completion/results/pbe0_h2o.out | H₃VO₄;−1246.479597897213;simulation/03_tier2_completion/results/pbe0_h3vo4.out | V-PRC;−2955.251083282212;simulation/03_tier2_completion/results/pbe0_v-prc.out | W-PRC;−1785.143710125366;simulation/03_tier2_completion/results/pbe0_w-prc.out | V-I1;−2955.261392548875;simulation/03_tier2_completion/results/pbe0_v-i1.out | W-P;−1785.122480008438;simulation/03_tier2_completion/results/pbe0_w-p.out]

[TBL: Table A.3: GFN2-xTB electronic-energy inputs for adsorption and pathway comparisons | State;Electronic energy (Eh);Source output log | Zeolite Y cluster;−31.34551236;simulation/01_models/cluster/cluster-T1-V02.out | H₂O;−5.07054445;simulation/01_models/h2o/h2o-T1-V01.out | H₃VO₄;−19.77512769;simulation/01_models/h3vo4/h3vo4-T1-V01.out | V-PRC;−51.19563631;simulation/02_tier1/V-R/V-R-T1-V02.out | V-I1;−51.26731716;simulation/02_tier1/V-I1/V-I1-T1-V01.out | V-TS2;−51.20610884;simulation/02_tier1/V-TS2/optts3_bandB_ci.out | V-I2;−51.25104052;simulation/02_tier1/V-I2/V-I2-T1-V04_pos.out | V-P;−51.15221675;simulation/02_tier1/V-TS3/V-TS3-T1-V02.out | W-PRC;−36.44256091;simulation/02_tier1/W-PRC/W-PRC-T1-V02.out | W-TS;−36.43140308;simulation/02_tier1/W-TS/optts2_bandD_ci.out | W-P;−36.44113826;simulation/02_tier1/W-P/W-P-T1-V01.out]

[TBL: Table A.4: B3LYP absolute harmonic Gibbs corrections, G − Eₑₗ (Eh) | State;G − Eₑₗ at 298.15 K / 1003.15 K;Source frequency output log | Zeolite Y cluster;0.08466275 / −0.10976592;simulation/03_tier2_completion/results/s1_03_cluster_optfreq.out | H₂O;0.00350503 / −0.05398928;simulation/03_tier2_completion/results/s1_01_h2o_optfreq.out | H₃VO₄;0.01335237 / −0.10253549;simulation/03_tier2_completion/results/s1_02_h3vo4_optfreq.out | V-PRC;0.12694676 / −0.12607009;simulation/03_tier2_completion/results/s1_04_vprc_optfreq.out | W-PRC;0.10700319 / −0.10839383;simulation/03_tier2_completion/results/s1_05_wprc_optfreq.out | V-I1;0.12833343 / −0.12709898;simulation/03_tier2_completion/results/s4_01_vi1_optfreq.out | W-P;0.10904705 / −0.10407863;simulation/03_tier2_completion/results/s4_04_wp_optfreq.out]

[TBL: Table A.5: Thermochemical constants and regenerator conditions | Input;Value and unit;Source or basis | Hartree conversion, C;2625.4996394799 kJ mol⁻¹ Eh⁻¹;simulation/analysis/build_tables.py, CODATA 2018 | Gas constant, R;0.00831446261815324 kJ mol⁻¹ K⁻¹;simulation/analysis/build_tables.py and writing/markdown/_results.json | Lower temperature;298.15 K;ORCA harmonic thermochemistry | Regenerator temperature;1003.15 K;730 °C converted to kelvin, Wormsbecher et al. (1986) | Standard pressure, p°;1 atm;ORCA ideal-gas thermochemistry standard state | Total regenerator pressure;2 atm;Wormsbecher et al. (1986) | Steam mole fraction, y(H₂O);0.20;Wormsbecher et al. (1986) | Water partial pressure, p(H₂O);0.4 atm;derived as 0.20 × 2 atm | H₃VO₄ concentration range;1–10 ppm;Wormsbecher et al. (1986) | H₃VO₄ partial-pressure range;2 × 10⁻⁶–2 × 10⁻⁵ atm;derived from 1–10 ppm at 2 atm | Trujillo H₃VO₄ partial pressure;3.37 × 10⁻⁶ atm;Trujillo et al. (1997)]

### A.2 Calculation-status register

This register preserves completed, incomplete, and rejected calculation evidence. Chapter Four uses the accepted DFT minima and the stated PBE0 single-point comparisons. Tier 1 candidates retain their method and validation level in the pathway evidence.

[TBL: Table A.6: DFT optimisation, frequency, and single-point status evidence | Calculation;Source output log(s);Recorded status and use | B3LYP cluster reference;simulation/03_tier2_completion/results/s1_03_cluster_optfreq.out;Converged reference with one flat mode at −4.64 cm⁻¹, used for electronic and Gibbs references | B3LYP H₂O;simulation/03_tier2_completion/results/s1_01_h2o_optfreq.out;Converged minimum with zero imaginary modes, isolated water reference | B3LYP H₃VO₄;simulation/03_tier2_completion/results/s1_02_h3vo4_optfreq.out;Converged minimum with zero imaginary modes, isolated vanadic-acid reference | B3LYP V-PRC;simulation/03_tier2_completion/results/s1_04_vprc_optfreq.out;Converged minimum with zero imaginary modes, adsorption energy and geometry | B3LYP W-PRC;simulation/03_tier2_completion/results/s1_05_wprc_optfreq.out;Converged minimum with zero imaginary modes, adsorption energy and geometry | B3LYP V-I1;simulation/03_tier2_completion/results/s4_01_vi1_optfreq.out;Converged minimum with zero imaginary modes, post-adsorption energy and geometry | B3LYP W-P;simulation/03_tier2_completion/results/s4_04_wp_optfreq.out;Converged minimum with zero imaginary modes, post-adsorption energy and geometry | PBE0 comparison single points;Source logs listed individually in Table A.2;Completed on the listed B3LYP geometries, electronic-energy comparison | B3LYP V-I2;simulation/03_tier2_completion/results/first_pass/s4_02_vi2_optfreq.out and simulation/03_tier2_completion/results/s4_02_vi2_optfreq.out;90-cycle first pass unconverged at −2956.26562215 Eh and 60-cycle rerun unconverged at −2956.26639173 Eh, frequency data unavailable, excluded from accepted DFT minima | B3LYP V-P;simulation/03_tier2_completion/results/first_pass/s4_03_vp_optfreq.out and simulation/03_tier2_completion/results/s4_03_vp_optfreq.out;90-cycle first pass unconverged at −2956.05925722 Eh and the 25-cycle rerun ended before normal completion at −2956.05930432 Eh, excluded from accepted DFT minima | B3LYP V-TS2;simulation/03_tier2_completion/results/s4_05_vts2_optts.out;OptTS reached 200 cycles at −2956.09584386 Eh and retained 14 imaginary modes, no validated DFT barrier]

[TBL: Table A.7: PBE0 counterpoise ghost-fragment status evidence | Complex and fragment;Source output log and termination status;Final electronic energy (Eh) | V-PRC cluster ghost;simulation/03_tier2_completion/results/v-prc_cp_ghost-cluster.out, LEANSCF error termination;Unavailable | V-PRC H₃VO₄ ghost;simulation/03_tier2_completion/results/v-prc_cp_ghost-h3vo4.out, normal termination;−1708.714841090478 | W-PRC cluster ghost;simulation/03_tier2_completion/results/w-prc_cp_ghost-cluster.out, normal termination;−76.378622223824 | W-PRC H₂O ghost;simulation/03_tier2_completion/results/w-prc_cp_ghost-h2o.out, normal termination;−1708.730926698051]

[TBL: Table A.8: Tier 1 transition-state candidate and displacement evidence | Candidate or displacement;Output log and numerical evidence;Register assessment or destination | V-TS2, V-I1 → V-I2;simulation/02_tier1/V-TS2/optts3_bandB_ci.out, one imaginary mode at −78.21 cm⁻¹, E = −51.20610884 Eh;V-TS2-T1-V05 accepted, A1–A5 passed | V-TS2 positive displacement;simulation/02_tier1/V-TS2/V-TS2_ts_pos_disp.out;Relaxed to V-I2 well, +15.64 kJ mol⁻¹ relative to V-I2 | V-TS2 negative displacement;simulation/02_tier1/V-TS2/V-TS2_ts_neg_disp.out;Relaxed to V-I1 well, +107.08 kJ mol⁻¹ relative to V-I1 | W-TS, W-PRC → W-P;simulation/02_tier1/W-TS/optts2_bandD_ci.out, one imaginary mode at −226.10 cm⁻¹, E = −36.43140308 Eh;W-TS-T1-V04 candidate, +29.29 kJ mol⁻¹ relative to W-PRC | W-TS positive displacement;simulation/02_tier1/W-TS/W-TS_pos_disp.out;Relaxed to W-PRC well, +1.35 kJ mol⁻¹ relative to W-PRC | W-TS negative displacement;simulation/02_tier1/W-TS/W-TS_neg_disp.out;Relaxed to W-PRC well, +1.34 kJ mol⁻¹ relative to W-PRC, candidate rejected as saddle point]

## Appendix B. Numerical Working

All electronic energies in the substitutions below are taken from Tables A.1–A.3, the harmonic corrections from Table A.4, and the constants and conditions from Table A.5. Values are shown to the precision needed to reproduce the reported results; the full source energies remain in the input register.

The gas composition and partial pressures were converted as follows:

p_{i} = y_{i} P_{total};    x_{i} (ppm) = 10^{6} p_{i} / P_{total}

(B.1)

[TBL: Table B.1: Regenerator gas-composition substitutions | Quantity;Substitution and result | Water partial pressure;0.20 × 2 atm = 0.400 atm | H₃VO₄ partial pressure at 1 ppm;1 × 10⁻⁶ × 2 atm = 2 × 10⁻⁶ atm | H₃VO₄ partial pressure at 10 ppm;10 × 10⁻⁶ × 2 atm = 2 × 10⁻⁵ atm | Trujillo concentration equivalent;3.37 × 10⁻⁶ atm ÷ 2 atm × 10⁶ = 1.685 ppm]

The same adsorption-energy expression was applied to pre-reaction complexes and post-adsorption minima, using the corresponding isolated cluster and molecule as the reference:

ΔE_{rel} = [E_{state} − E_{cluster} − E_{molecule}] × C

(B.2)

[TBL: Table B.2: Electronic adsorption and post-adsorption relative-energy substitutions | Method and state;Numerical substitution in Eh multiplied by C;Result (kJ mol⁻¹) | B3LYP V-PRC;[−2956.254531846348 − (−1709.394093884281) − (−1246.825013958827)] × 2625.4996394799;−93.0057 | B3LYP W-PRC;[−1785.850554383119 − (−1709.394093884281) − (−76.426629795556)] × 2625.4996394799;−78.3205 | PBE0 V-PRC;[−2955.251083282212 − (−1708.736038466437) − (−1246.479597897213)] × 2625.4996394799;−93.0659 | PBE0 W-PRC;[−1785.143710125366 − (−1708.736038466437) − (−76.377725397537)] × 2625.4996394799;−78.6239 | GFN2-xTB V-PRC;[−51.19563631 − (−31.34551236) − (−19.77512769)] × 2625.4996394799;−196.9027 | GFN2-xTB W-PRC;[−36.44256091 − (−31.34551236) − (−5.07054445)] × 2625.4996394799;−69.5865 | B3LYP V-I1;[−2956.263052028540 − (−1709.394093884281) − (−1246.825013958827)] × 2625.4996394799;−115.3754 | B3LYP W-P;[−1785.829873927753 − (−1709.394093884281) − (−76.426629795556)] × 2625.4996394799;−24.0240 | PBE0 V-I1;[−2955.261392548875 − (−1708.736038466437) − (−1246.479597897213)] × 2625.4996394799;−120.1328 | PBE0 W-P;[−1785.122480008438 − (−1708.736038466437) − (−76.377725397537)] × 2625.4996394799;−22.8842 | GFN2-xTB V-I1;[−51.26731716 − (−31.34551236) − (−19.77512769)] × 2625.4996394799;−385.1007 | GFN2-xTB W-P;[−36.44113826 − (−31.34551236) − (−5.07054445)] × 2625.4996394799;−65.8513]

The relative electronic preference is the difference between the two pre-reaction adsorption energies:

ΔΔE_{ads} = ΔE_{ads}(H₃VO₄) − ΔE_{ads}(H₂O)

(B.3)

[TBL: Table B.3: Electronic adsorption-preference substitutions | Method;Substitution in kJ mol⁻¹;Vanadic-acid minus water result (kJ mol⁻¹) | B3LYP-D3(BJ)/def2-TZVP;−93.0057 − (−78.3205);−14.6852 | PBE0-D3(BJ)/def2-TZVP single point;−93.0659 − (−78.6239);−14.4420 | GFN2-xTB;−196.9027 − (−69.5865);−127.3161]

The adsorption Gibbs energy combines the electronic adsorption energy with the difference between the complex and separated-fragment harmonic corrections:

ΔG^{°}_{ads}(T) = ΔE_{ads} + C{[G − Eₑₗ]_{complex} − [G − Eₑₗ]_{cluster} − [G − Eₑₗ]_{molecule}}

(B.4)

[TBL: Table B.4: Harmonic adsorption-Gibbs substitutions at 298.15 K | State;Substitution and result (kJ mol⁻¹) | V-PRC;−93.0057 + [0.12694676 − 0.08466275 − 0.01335237] × 2625.4996394799 = −17.0457 | V-I1;−115.3754 + [0.12833343 − 0.08466275 − 0.01335237] × 2625.4996394799 = −35.7747 | W-PRC;−78.3205 + [0.10700319 − 0.08466275 − 0.00350503] × 2625.4996394799 = −28.8681 | W-P;−24.0240 + [0.10904705 − 0.08466275 − 0.00350503] × 2625.4996394799 = +30.7945]

[TBL: Table B.5: Harmonic adsorption-Gibbs substitutions at 1003.15 K | State;Substitution and result (kJ mol⁻¹) | V-PRC;−93.0057 + [−0.12607009 − (−0.10976592) − (−0.10253549)] × 2625.4996394799 = +133.3946 | V-I1;−115.3754 + [−0.12709898 − (−0.10976592) − (−0.10253549)] × 2625.4996394799 = +108.3235 | W-PRC;−78.3205 + [−0.10839383 − (−0.10976592) − (−0.05398928)] × 2625.4996394799 = +67.0308 | W-P;−24.0240 + [−0.10407863 − (−0.10976592) − (−0.05398928)] × 2625.4996394799 = +132.6568]

The Gibbs-energy preference uses the same sign convention as the electronic comparison:

ΔΔG^{°}_{ads} = ΔG^{°}_{ads}(H₃VO₄) − ΔG^{°}_{ads}(H₂O)

(B.5)

[TBL: Table B.6: Temperature-dependent Gibbs-energy preference | Temperature;Substitution in kJ mol⁻¹;Vanadic-acid minus water result (kJ mol⁻¹) | 298.15 K;−17.0457 − (−28.8681);+11.8224 | 1003.15 K;+133.3946 − (+67.0308);+66.3638]

The standard equilibrium constant follows from the adsorption Gibbs energy at 1003.15 K:

K^{°}_{i} = exp[−ΔG^{°}_{ads,i} / (R T)]

(B.6)

[TBL: Table B.7: Standard equilibrium-constant substitutions at 1003.15 K | Species;Substitution and result | H₂O;exp[−67.0307562 ÷ (0.00831446261815324 × 1003.15)] = 3.23396471 × 10⁻⁴ | H₃VO₄;exp[−133.3945918 ÷ (0.00831446261815324 × 1003.15)] = 1.13291375 × 10⁻⁷]

The dimensionless adsorption weight for each gas species is:

q_{i} = K^{°}_{i} (p_{i} / p^{°})

(B.7)

[TBL: Table B.8: Unnormalised competitive-site weights | Species or condition;Substitution and result | H₂O at 0.4 atm;3.23396471 × 10⁻⁴ × (0.4 / 1) = 1.29358589 × 10⁻⁴ | H₃VO₄ at 1 ppm;1.13291375 × 10⁻⁷ × (2 × 10⁻⁶ / 1) = 2.26582750 × 10⁻¹³ | H₃VO₄ at 10 ppm;1.13291375 × 10⁻⁷ × (2 × 10⁻⁵ / 1) = 2.26582750 × 10⁻¹² | H₃VO₄ at Trujillo pressure;1.13291375 × 10⁻⁷ × (3.37 × 10⁻⁶ / 1) = 3.81791934 × 10⁻¹³]

For one equivalent site, the occupied fractions are normalised by the vacant-site weight, which is one:

θ_{i} = q_{i} / (1 + q_{H₂O} + q_{H₃VO₄})

(B.8)

[TBL: Table B.9: Competitive-site fraction substitutions | H₃VO₄ pressure case;Substitution and result | 1 ppm, p = 2 × 10⁻⁶ atm;θ(H₂O) = 1.29358589 × 10⁻⁴ ÷ (1 + 1.29358589 × 10⁻⁴ + 2.26582750 × 10⁻¹³) = 1.29341857 × 10⁻⁴, and θ(H₃VO₄) = 2.26582750 × 10⁻¹³ ÷ (1 + 1.29358589 × 10⁻⁴ + 2.26582750 × 10⁻¹³) = 2.26553443 × 10⁻¹³ | 10 ppm, p = 2 × 10⁻⁵ atm;θ(H₂O) = 1.29358589 × 10⁻⁴ ÷ (1 + 1.29358589 × 10⁻⁴ + 2.26582750 × 10⁻¹²) = 1.29341857 × 10⁻⁴, and θ(H₃VO₄) = 2.26582750 × 10⁻¹² ÷ (1 + 1.29358589 × 10⁻⁴ + 2.26582750 × 10⁻¹²) = 2.26553443 × 10⁻¹² | Trujillo pressure, p = 3.37 × 10⁻⁶ atm;θ(H₂O) = 1.29358589 × 10⁻⁴ ÷ (1 + 1.29358589 × 10⁻⁴ + 3.81791934 × 10⁻¹³) = 1.29341857 × 10⁻⁴, and θ(H₃VO₄) = 3.81791934 × 10⁻¹³ ÷ (1 + 1.29358589 × 10⁻⁴ + 3.81791934 × 10⁻¹³) = 3.81742552 × 10⁻¹³]

Because both occupied fractions share the same normalising denominator, their ratio simplifies to:

θ_{H₂O} / θ_{H₃VO₄} = q_{H₂O} / q_{H₃VO₄} = K^{°}_{H₂O} p_{H₂O} / (K^{°}_{H₃VO₄} p_{H₃VO₄})

(B.9)

[TBL: Table B.10: Water-to-vanadic-acid occupation-ratio substitutions | H₃VO₄ pressure case;Substitution and result | 1 ppm, p = 2 × 10⁻⁶ atm;1.29358589 × 10⁻⁴ ÷ 2.26582750 × 10⁻¹³ = 5.7091 × 10⁸ | 10 ppm, p = 2 × 10⁻⁵ atm;1.29358589 × 10⁻⁴ ÷ 2.26582750 × 10⁻¹² = 5.7091 × 10⁷ | Trujillo pressure, p = 3.37 × 10⁻⁶ atm;1.29358589 × 10⁻⁴ ÷ 3.81791934 × 10⁻¹³ = 3.3882 × 10⁸]

The Tier 1 candidate energy difference was evaluated from each candidate and its corresponding starting minimum:

ΔE^{‡}_{candidate} = [E_{candidate} − E_{start}] × C

(B.10)

[TBL: Table B.11: Tier 1 candidate-barrier substitutions | Candidate step;Substitution and result | V-I1 → V-I2, GFN2-xTB;[−51.20610884 − (−51.26731716)] × 2625.4996394799 = 160.70 kJ mol⁻¹ | W-TS candidate above W-PRC, GFN2-xTB;[−36.43140308 − (−36.44256091)] × 2625.4996394799 = 29.29 kJ mol⁻¹]

The V-I1-to-V-I2 value is a GFN2-xTB candidate barrier supported by the frequency and two-sided displacement evidence in Table A.8. The W-TS energy difference is a candidate value; both displaced structures returned to W-PRC. The separate DFT V-TS2 optimisation reached 200 cycles and retained 14 imaginary modes, as recorded in Table A.6, so it does not establish a validated DFT barrier.
