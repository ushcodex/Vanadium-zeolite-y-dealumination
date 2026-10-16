# 4.0 RESULTS AND DISCUSSION

## 4.1 Local Cluster and Adsorption Structures

GFN2-xTB screening selected starting orientations for vanadic acid and water at the local Zeolite Y acid site. Subsequent B3LYP-D3(BJ)/def2-TZVP optimisations produced the accepted reference, pre-reaction, and post-adsorption minima listed in Table 4.1. In the cluster reference, the protonated framework Al–O bond measured 1.919 Å, compared with 1.695–1.716 Å for the other three Al–O bonds, identifying the local acid-site distortion represented by the model.

[TBL: Table 4.1: Accepted DFT reference and adsorption minima | State;Optimisation result;Vibrational assessment | Cluster reference;Converged;One flat reference mode at −4.64 cm⁻¹ | H₃VO₄;Converged;Minimum, zero imaginary modes | H₂O;Converged;Minimum, zero imaginary modes | V-PRC;Converged;Minimum, zero imaginary modes | V-I1;Converged;Minimum, zero imaginary modes | W-PRC;Converged;Minimum, zero imaginary modes | W-P;Converged;Minimum, zero imaginary modes]

The cluster's −4.64 cm⁻¹ mode was a flat reference motion; the other accepted DFT minima had zero imaginary modes. Figure 4.1 shows the distinct pre-reaction orientations: vanadic acid approached framework aluminium in V-PRC, whereas water remained farther from aluminium in W-PRC. The aluminium–oxygen distances in Table 4.2 quantify these differences and the rearrangements in the post-adsorption structures.

[FIG: fig4_1_complexes.png | Figure 4.1: Optimised adsorption complexes at B3LYP-D3(BJ)/def2-TZVP. Left, vanadic acid (V-PRC); right, water (W-PRC) | Source: author, rendered from the optimised Cartesian coordinates]

[TBL: Table 4.2: Selected aluminium–oxygen distances in converged DFT structures (Å) | Structure;Nearest Al···O distance to adsorbate;Longest framework Al–O distance;Structural interpretation | Cluster reference;—;1.919;Protonated framework reference | V-PRC;1.947;2.042;Vanadic oxygen approached Al and the acid-site Al–O bond lengthened | V-I1;3.529;1.791;Framework Al–O bonds remained short in the chemisorbed intermediate | W-PRC;3.337;1.885;Water remained outside the Al coordination sphere | W-P;1.718;3.129;Water-derived oxygen approached Al with an elongated framework Al–O bond]

The V-PRC geometry also placed vanadium 2.274 Å from a framework oxygen. In W-PRC, the acid proton lay 1.587 Å from the water oxygen, while a water hydrogen lay 1.825 Å from a framework oxygen; these contacts are consistent with two hydrogen bonds. The direct acid-site association agrees with the vanadic-acid route discussed by Wormsbecher et al. (1986), and the water contacts accord with the water-assisted interactions studied by Malola et al. (2012). These optimised structures describe adsorption geometries; evidence for framework cleavage comes from the pathway calculations.

## 4.2 Electronic Adsorption Energies

Table 4.3 shows that both DFT levels favour electronic adsorption of vanadic acid over water. The vanadic-acid-minus-water energy difference, ΔΔE_{ads} = ΔE_{ads}(H₃VO₄) − ΔE_{ads}(H₂O), is −14.69 kJ mol⁻¹ at B3LYP and −14.44 kJ mol⁻¹ at PBE0, following the sign convention in Eq. (3.2). Tables B.2 and B.3 give the source-traceable substitutions and method comparison before the temperature-dependent Gibbs results in Section 4.4.

[TBL: Table 4.3: Electronic adsorption energies of vanadic acid and water (kJ mol⁻¹) | Level of theory;H₃VO₄;H₂O;ΔΔE_{ads} = ΔE_{ads}(H₃VO₄) − ΔE_{ads}(H₂O) | GFN2-xTB;−196.9;−69.6;−127.3 | B3LYP-D3(BJ)/def2-TZVP;−93.01;−78.32;−14.69 | PBE0-D3(BJ)/def2-TZVP, single point;−93.07;−78.62;−14.44]

B3LYP and PBE0 give similar relative preferences, differing by 0.25 kJ mol⁻¹, so the electronic ranking is consistent across the two hybrid functionals. GFN2-xTB predicts a much larger preference of 127.3 kJ mol⁻¹, about 8.7 times the DFT difference; this value serves as a screening estimate, while the DFT calculations provide the quantitative comparison. The DFT sign agrees with the direct vanadic-acid route proposed by Wormsbecher et al. (1986). These energies quantify relative binding; the pathway calculations provide the separate evidence about framework cleavage.

## 4.3 Pathway Energetics

The post-adsorption minima lie below their respective separated cluster-and-adsorbate references at all three levels of theory (Table 4.4). V-I1 is more stabilised than the water-path minimum W-P at each level, although the size of this difference depends on the method. GFN2-xTB predicts substantially greater relative stabilisation of V-I1 than either DFT level, so the method-dependent spread warrants caution in interpreting the screening energies.

[TBL: Table 4.4: Relative electronic energies of converged post-adsorption minima (kJ mol⁻¹) | State;GFN2-xTB;B3LYP-D3(BJ)/def2-TZVP;PBE0-D3(BJ)/def2-TZVP single point | V-I1;−385.1;−115.38;−120.13 | W-P;−65.9;−24.02;−22.88]

The GFN2-xTB search produced a candidate for the first framework Al–O cleavage step in the vanadic-acid route. Table 4.5 compares its energy and imaginary mode with the water-path candidate; Table A.8 records the two-sided displacement destinations, and Table B.11 shows the numerical energy substitutions.

[TBL: Table 4.5: Tier 1 pathway candidates for framework Al–O cleavage and water hydrolysis | Route and step;Imaginary frequency (cm⁻¹);Candidate energy above starting minimum (kJ mol⁻¹);Assessment | V-I1 to V-I2;−78.21;160.70;V-TS2 passed the GFN2-xTB Tier 1 frequency and two-sided displacement criteria | W-PRC to W-P;−226.10;29.29;Both W-TS displacements relaxed to W-PRC]

The V-I1-to-V-I2 candidate lies 160.70 kJ mol⁻¹ above V-I1 and passed the GFN2-xTB displacement criteria; it supports a screening-level barrier estimate, while a validated DFT barrier remains to be established. Both displaced W-TS structures relaxed to W-PRC, so the 29.29 kJ mol⁻¹ difference is a candidate energy separation, not an activation barrier. The B3LYP V-TS2 optimisation reached 200 cycles and retained 14 imaginary modes (Table A.6). Malola et al. (2012) reported a water-assisted DFT pathway whose effective barrier depended on the water reference state; their periodic pathway and the present cluster candidates use different structural and reaction references, so the comparison remains qualitative.

## 4.4 Harmonic Gibbs Energies

Figure 4.2 shows that all four B3LYP standard adsorption Gibbs energies shift upward between 298.15 and 1003.15 K. The Gibbs preference for water over vanadic acid increases from 11.82 to 66.36 kJ mol⁻¹, and both pre-reaction complexes move from negative values at 298.15 K to positive values at 1003.15 K. The post-adsorption minima also become less favourable with increasing temperature, as shown by their upward trends in the same figure.

[FIG: fig4_2_gibbs_temperature.png | Figure 4.2: B3LYP-D3(BJ)/def2-TZVP standard Gibbs energies of adsorption at 298.15 and 1003.15 K for pre-reaction complexes V-PRC and W-PRC and post-adsorption minima V-I1 and W-P. Point labels give the calculated values; the dotted line marks zero | Source: author, generated from the ORCA thermochemistry register using tools/make_chapter4_plots.py]

The Gibbs-energy preference for water contrasts with the electronic adsorption preference for vanadic acid in Section 4.2; the temperature-dependent harmonic corrections widen the difference between V-PRC and W-PRC (Tables B.4–B.6). This sensitivity to thermochemical reference states is consistent with Malola et al.'s (2012) finding that the water reference affects calculated dealumination energetics. Their periodic pathway uses a different structural and reaction reference, so comparison with the present cluster adsorption model remains qualitative. The values use ideal-gas, rigid-rotor, harmonic-oscillator thermochemistry at a 1 atm standard state and omit pore confinement and coverage-dependent interactions.

## 4.5 Conditional Competitive Site-Occupation Estimate

Figure 4.3 shows the conditional single-site fractions at 1003.15 K as the H₃VO₄ pressure increases from 2 × 10⁻⁶ to 2 × 10⁻⁵ atm. At the displayed precision, the water fraction remains 1.29 × 10⁻⁴, while the vanadic-acid fraction increases from 2.27 × 10⁻¹³ to 2.27 × 10⁻¹². The corresponding water-to-vanadic-acid occupation ratio falls from 5.71 × 10⁸ to 5.71 × 10⁷; at the 3.37 × 10⁻⁶ atm pressure reported by Trujillo et al. (1997), the model gives 3.39 × 10⁸ (Tables B.7–B.10).

[FIG: fig4_3_site_occupation.png | Figure 4.3: Conditional water and vanadic-acid site fractions at 1003.15 K and 2 atm total pressure, with p(H₂O) = 0.4 atm and p(H₃VO₄) spanning 1–10 ppm. The logarithmic vertical axis displays the small site fractions across their full range | Source: author, generated using tools/make_chapter4_plots.py and the equilibrium inputs in Table A.5]

The model predicts a much greater conditional occupation by water under the stated steam-rich gas composition, consistent with the steam-dominated interpretation discussed by Pine (1990). The small calculated fractions and their large ratio describe relative competition in the specified equilibrium model; empirical coverage and reaction rates require independent measurements. Trujillo et al. (1997) discussed local vanadium enrichment; the present estimate uses bulk gas partial pressures and leaves pore-scale enrichment, interactions, and competing reaction barriers outside its scope.

---