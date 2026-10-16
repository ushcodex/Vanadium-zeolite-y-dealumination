# 4.0 RESULTS AND DISCUSSION

## 4.1 Model and Adsorption Geometries

The DFT optimisations produced a set of reference and adsorption minima for the local Zeolite Y model. Table 4.1 summarises the accepted structures and their frequency checks. Figure 4.1 compares the two pre-reaction complexes, and Table 4.2 reports selected aluminium–oxygen distances from the optimised geometries.

[TBL: Table 4.1: Accepted DFT reference and adsorption minima | State;Optimisation result;Vibrational assessment | Cluster reference;Converged;One flat reference mode at −4.64 cm⁻¹ | H₃VO₄;Converged;Minimum, zero imaginary modes | H₂O;Converged;Minimum, zero imaginary modes | V-PRC;Converged;Minimum, zero imaginary modes | V-I1;Converged;Minimum, zero imaginary modes | W-PRC;Converged;Minimum, zero imaginary modes | W-P;Converged;Minimum, zero imaginary modes]

Figure 4.1 shows a close vanadic-acid oxygen contact with aluminium in V-PRC and a more distant water position in W-PRC. The two complexes therefore present distinct starting geometries for the adsorption-energy comparison in Section 4.2. Their orientations are consistent with the adsorbate–aluminium distances reported in Table 4.2.

[FIG: fig4_1_complexes.png | Figure 4.1: Optimised adsorption complexes at B3LYP-D3(BJ)/def2-TZVP. Left, vanadic acid (V-PRC); right, water (W-PRC) | Source: author, rendered from the optimised Cartesian coordinates]

In V-PRC, a vanadic-acid oxygen contacted aluminium while the acid-site Al–O bond lengthened relative to the isolated cluster. W-PRC retained water outside the aluminium coordination sphere. In W-P, a water-derived oxygen approached aluminium as one framework Al–O distance lengthened. These distances show the different local geometries sampled along the two routes.

[TBL: Table 4.2: Selected aluminium–oxygen distances in converged DFT structures (Å) | Structure;Nearest Al···O distance to adsorbate;Longest framework Al–O distance;Structural interpretation | Cluster reference;—;1.919;Protonated framework reference | V-PRC;1.947;2.042;Vanadic oxygen approached Al and the acid-site Al–O bond lengthened | V-I1;3.529;1.791;Framework Al–O bonds remained short in the chemisorbed intermediate | W-PRC;3.337;1.885;Water remained outside the Al coordination sphere | W-P;1.718;3.129;Water-derived oxygen approached Al with an elongated framework Al–O bond]

## 4.2 Electronic Adsorption Energies

Table 4.3 compares electronic adsorption energies at GFN2-xTB, B3LYP-D3(BJ)/def2-TZVP, and PBE0-D3(BJ)/def2-TZVP. Negative values show electronic stabilisation of each complex relative to its separated cluster and adsorbate. The difference ΔΔE uses the sign convention in Eq. (3.2); negative values favour vanadic acid. Appendix B.2 shows the substitutions for the DFT values.

[TBL: Table 4.3: Electronic adsorption energies of vanadic acid and water (kJ mol⁻¹) | Level of theory;H₃VO₄;H₂O;ΔΔE = ΔE(H₃VO₄) − ΔE(H₂O) | GFN2-xTB;−196.9;−69.6;−127.3 | B3LYP-D3(BJ)/def2-TZVP;−93.01;−78.32;−14.69 | PBE0-D3(BJ)/def2-TZVP, single point;−93.07;−78.62;−14.44]

Both DFT levels predict a more negative electronic adsorption energy for vanadic acid. Their relative preferences differ by only 0.24 kJ mol⁻¹, providing a consistent comparison across the two hybrid functionals. GFN2-xTB predicts a substantially larger vanadic-acid preference and serves as the structure-screening level for these adsorbates. The DFT energies are direct values; Appendix A.2 records the counterpoise fragment-job status.

Table 4.4 reports relative electronic energies for the converged post-adsorption minima. Each route uses its own separated cluster-and-adsorbate reference, so the values describe stabilisation within that route. The three levels of theory place V-I1 and W-P below their respective separated references.

[TBL: Table 4.4: Relative electronic energies of converged post-adsorption minima (kJ mol⁻¹) | State;GFN2-xTB;B3LYP-D3(BJ)/def2-TZVP;PBE0-D3(BJ)/def2-TZVP single point | V-I1;−385.1;−115.38;−120.13 | W-P;−65.9;−24.02;−22.88]

## 4.3 Transition-State Assessment

The vanadic-acid pathway yielded a GFN2-xTB candidate for the first framework Al–O cleavage step. Table 4.5 gives its candidate barrier and mode alongside the water-hydrolysis control. Appendix A.1 and A.3 record the DFT frequency assessment and the two-sided displacement outcomes used to classify both pathways; Appendix B.6 shows the candidate-barrier substitutions.

[TBL: Table 4.5: Tier 1 pathway candidates for framework Al–O cleavage and water hydrolysis | Route and step;Candidate imaginary mode;Candidate barrier relative to starting minimum;Assessment record | V-I1 to V-I2;−78.21 cm⁻¹;160.70 kJ mol⁻¹;V-TS2 passed the Tier 1 transition-state criteria | W-PRC to W-P;−226.10 cm⁻¹;29.29 kJ mol⁻¹;W-TS displacement assessment is in Appendix A.3]

The accepted GFN2-xTB candidate provides a screening-level energy for the first vanadic-acid cleavage step. The DFT and water-path outcomes in Appendix A show the distinction between a screening candidate and a validated reaction-path barrier. The reported barrier therefore describes the GFN2-xTB model and its accepted candidate geometry.

## 4.4 Harmonic Gibbs Energies

Table 4.6 compares harmonic Gibbs energies at 298.15 K and 1003.15 K, using the separated cluster and adsorbate as the reference. Water has the more favourable adsorption Gibbs energy at both temperatures. The difference increases from 11.82 kJ mol⁻¹ at 298.15 K to 66.36 kJ mol⁻¹ at 1003.15 K. Appendix B.4 shows the thermal-correction substitutions.

[TBL: Table 4.6: Harmonic Gibbs free energies relative to the separated cluster and adsorbate (kJ mol⁻¹) | State;ΔG at 298.15 K;ΔG at 1003.15 K | V-PRC;−17.0;+133.4 | V-I1;−35.8;+108.3 | W-PRC;−28.9;+67.0 | W-P;+30.8;+132.7]

At 1003.15 K, both pre-reaction complexes have positive standard adsorption Gibbs energies, while W-PRC is lower by 66.36 kJ mol⁻¹. These harmonic values establish the temperature-dependent ordering used in the conditional site-occupation calculation in Section 4.5. The larger separation at 1003.15 K reflects the differing thermal corrections for V-PRC and W-PRC in Table B.1.

## 4.5 Conditional Competitive Site-Occupation Estimate

The 1003.15 K Gibbs energies for V-PRC and W-PRC were combined with the regenerator partial pressures to calculate a competitive-site scenario. Table 4.7 gives the dimensionless equilibrium constants and fractions from Eqs. (3.4) and (3.5). Appendix B.1 and B.5 show the pressure and site-fraction substitutions.

[TBL: Table 4.7: Formal single-site occupation estimate at 1003.15 K | Species or ratio;K° at 1003.15 K;Partial pressure p/p°;Calculated site fraction or ratio | H₃VO₄;1.13 × 10⁻⁷;2 × 10⁻⁶ to 2 × 10⁻⁵;2.27 × 10⁻¹³ to 2.27 × 10⁻¹² | H₂O;3.23 × 10⁻⁴;0.4;1.29 × 10⁻⁴ | θ(H₂O)/θ(H₃VO₄);—;—;5.7 × 10⁷ to 5.7 × 10⁸]

For the stated pressure range, the formal estimate assigns the larger site fraction to water. Its single-site result uses ideal-gas standard states, one equivalent site, and independent adsorbates; Appendix B.5 presents the full arithmetic. The result characterises the specified gas-phase model for comparison with pore-aware calculations.

## 4.6 Relation to Proposed Mechanisms

The DFT energies favour electronic binding of vanadic acid, while the high-temperature Gibbs energies and steam-rich gas favour water in the conditional site-occupation scenario. Table 2.1 and Figure 2.3 place these results alongside the vanadic-acid, steam-dominated, and sodium-mediated mechanisms discussed by Wormsbecher et al. (1986), Trujillo et al. (1997), Pine (1990), and Xu et al. (2002). The adsorption comparison describes acid-site association; the pathway assessment in Appendix A supplies the corresponding transition-state evidence. Together, the results identify electronic binding, thermal competition, and pathway energy as separate quantities for evaluating Zeolite Y dealumination.
