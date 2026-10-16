# 4.0 RESULTS AND DISCUSSION

## 4.1 Local Cluster and Adsorption Structures

GFN2-xTB screening selected starting orientations for vanadic acid and water at the local Zeolite Y acid site. Subsequent B3LYP-D3(BJ)/def2-TZVP optimisations produced the accepted reference, pre-reaction, and post-adsorption minima listed in Table 4.1. The protonated framework Al–O bond in the cluster reference was 1.919 Å, compared with 1.695–1.716 Å for the other three Al–O bonds, identifying the model acid-site distortion.

[TBL: Table 4.1: Accepted DFT reference and adsorption minima | State;Optimisation result;Vibrational assessment | Cluster reference;Converged;One flat reference mode at −4.64 cm⁻¹ | H₃VO₄;Converged;Minimum, zero imaginary modes | H₂O;Converged;Minimum, zero imaginary modes | V-PRC;Converged;Minimum, zero imaginary modes | V-I1;Converged;Minimum, zero imaginary modes | W-PRC;Converged;Minimum, zero imaginary modes | W-P;Converged;Minimum, zero imaginary modes]

The cluster's −4.64 cm⁻¹ mode was a flat reference motion; the other accepted DFT minima had zero imaginary modes. Figure 4.1 shows the distinct pre-reaction orientations: vanadic acid approached framework aluminium in V-PRC, whereas water remained farther from aluminium in W-PRC. The selected aluminium–oxygen distances in Table 4.2 quantify these differences and the rearrangements in the post-adsorption structures.

[FIG: fig4_1_complexes.png | Figure 4.1: Optimised adsorption complexes at B3LYP-D3(BJ)/def2-TZVP. Left, vanadic acid (V-PRC); right, water (W-PRC) | Source: author, rendered from the optimised Cartesian coordinates]

[TBL: Table 4.2: Selected aluminium–oxygen distances in converged DFT structures (Å) | Structure;Nearest Al···O distance to adsorbate;Longest framework Al–O distance;Structural interpretation | Cluster reference;—;1.919;Protonated framework reference | V-PRC;1.947;2.042;Vanadic oxygen approached Al and the acid-site Al–O bond lengthened | V-I1;3.529;1.791;Framework Al–O bonds remained short in the chemisorbed intermediate | W-PRC;3.337;1.885;Water remained outside the Al coordination sphere | W-P;1.718;3.129;Water-derived oxygen approached Al with an elongated framework Al–O bond]

The V-PRC geometry also placed vanadium 2.274 Å from a framework oxygen. In W-PRC, the acid proton lay 1.587 Å from the water oxygen, while a water hydrogen lay 1.825 Å from a framework oxygen; these contacts are consistent with two hydrogen bonds. The direct acid-site association is consistent with the vanadic-acid route proposed by Wormsbecher et al. (1986), and the water contacts accord with the water-assisted interactions studied by Malola et al. (2012); the optimised geometries alone do not establish framework cleavage.

## 4.2 Electronic Adsorption Energies

Table 4.3 shows that both DFT levels favour electronic adsorption of vanadic acid over water. The relative difference, ΔΔE_{ads} = ΔE_{ads}(H₃VO₄) − ΔE_{ads}(H₂O), is negative at each level, as defined in Eq. (3.2). Appendix B.2 gives the numerical substitutions for comparison with the temperature-dependent Gibbs energies in Section 4.4.

[TBL: Table 4.3: Electronic adsorption energies of vanadic acid and water (kJ mol⁻¹) | Level of theory;H₃VO₄;H₂O;ΔΔE_{ads} = ΔE_{ads}(H₃VO₄) − ΔE_{ads}(H₂O) | GFN2-xTB;−196.9;−69.6;−127.3 | B3LYP-D3(BJ)/def2-TZVP;−93.01;−78.32;−14.69 | PBE0-D3(BJ)/def2-TZVP, single point;−93.07;−78.62;−14.44]

B3LYP and PBE0 give similar relative preferences, differing by 0.25 kJ mol⁻¹, so the electronic ranking is consistent across the two hybrid functionals. GFN2-xTB predicts a much larger preference of 127.3 kJ mol⁻¹, about 8.7 times the DFT difference; it therefore provides a screening result rather than a quantitative substitute for the DFT energies. The sign of the DFT preference is consistent with the direct vanadic-acid route proposed by Wormsbecher et al. (1986), although the cited studies do not provide a matched numerical comparison of H₃VO₄ and H₂O at this cluster site, and electronic adsorption energies do not establish a reaction mechanism.

## 4.3 Pathway Energetics

The post-adsorption minima were lower in electronic energy than their respective separated cluster-and-adsorbate references at all three levels of theory (Table 4.4). V-I1 was more stabilised than the water-path minimum W-P at each level, but the size of this difference depended on the method. GFN2-xTB predicted substantially greater stabilisation of V-I1 relative to W-P than either DFT level.

[TBL: Table 4.4: Relative electronic energies of converged post-adsorption minima (kJ mol⁻¹) | State;GFN2-xTB;B3LYP-D3(BJ)/def2-TZVP;PBE0-D3(BJ)/def2-TZVP single point | V-I1;−385.1;−115.38;−120.13 | W-P;−65.9;−24.02;−22.88]

The GFN2-xTB search produced a candidate for the first framework Al–O cleavage step in the vanadic-acid route. Table 4.5 reports its energy and imaginary mode alongside the water-path candidate. Appendix A.3 records the two-sided displacement checks, and Appendix B.6 gives the energy substitutions.

[TBL: Table 4.5: Tier 1 pathway candidates for framework Al–O cleavage and water hydrolysis | Route and step;Imaginary frequency (cm⁻¹);Candidate energy above starting minimum (kJ mol⁻¹);Assessment | V-I1 to V-I2;−78.21;160.70;V-TS2 passed the GFN2-xTB Tier 1 and two-sided displacement criteria | W-PRC to W-P;−226.10;29.29;W-TS was rejected because both displacements returned to W-PRC]

The V-I1-to-V-I2 candidate lies 160.70 kJ mol⁻¹ above V-I1 and passed the GFN2-xTB displacement criteria, but it is not a validated DFT barrier. The water-path candidate lies 29.29 kJ mol⁻¹ above W-PRC, yet both displacements returned to W-PRC, so its energy is not an accepted activation barrier. The separate DFT V-TS2 optimisation did not converge and had 14 imaginary modes (Appendix A.1); Malola et al. (2012) reported a water-assisted DFT pathway whose effective barrier depended on the water reference state, but no direct barrier comparison is justified here.

## 4.4 Harmonic Gibbs Energies

At 298.15 K, the harmonic adsorption Gibbs energies favoured water over vanadic acid by 11.82 kJ mol⁻¹. At 1003.15 K, the preference increased to 66.36 kJ mol⁻¹, with both pre-reaction complexes having positive standard adsorption Gibbs energies (Table 4.6). The post-adsorption minima also became less favourable as temperature increased: V-I1 shifted from −35.77 to +108.32 kJ mol⁻¹, and W-P shifted from +30.79 to +132.66 kJ mol⁻¹.

[TBL: Table 4.6: Harmonic standard Gibbs energies of adsorption relative to the separated cluster and adsorbate (kJ mol⁻¹) | State;ΔG^{°}_{ads} at 298.15 K;ΔG^{°}_{ads} at 1003.15 K | V-PRC;−17.05;+133.39 | V-I1;−35.77;+108.32 | W-PRC;−28.87;+67.03 | W-P;+30.79;+132.66]

The Gibbs-energy ranking reverses the electronic adsorption preference reported in Section 4.2, and the water advantage widens with temperature because the thermal corrections differ between V-PRC and W-PRC (Appendix B.4). This sensitivity to thermochemical reference states is consistent with Malola et al.'s (2012) finding that the water reference affects calculated dealumination energetics, although their periodic pathway is not directly comparable with this cluster adsorption model. The 1003.15 K values use ideal-gas, rigid-rotor, harmonic-oscillator thermochemistry and do not include pore confinement or coverage-dependent interactions.

## 4.5 Conditional Competitive Site-Occupation Estimate

Using the 1003.15 K Gibbs energies and regenerator partial pressures, the conditional single-site model gives a water fraction of 1.29 × 10⁻⁴ and a vanadic-acid fraction of 2.27 × 10⁻¹³ to 2.27 × 10⁻¹² (Table 4.7). The resulting water-to-vanadic-acid occupation ratio is 5.7 × 10⁷ to 5.7 × 10⁸; the standard equilibrium constants and substitutions are given in Appendix B.5. At the 3.37 × 10⁻⁶ atm H₃VO₄ partial pressure reported by Trujillo et al. (1997), the calculated ratio is approximately 3.39 × 10⁸.

[TBL: Table 4.7: Formal single-site occupation estimate at 1003.15 K | Species or ratio;K^{°} at 1003.15 K;Partial pressure p/p^{°};Calculated site fraction or ratio | H₃VO₄;1.13 × 10⁻⁷;2 × 10⁻⁶ to 2 × 10⁻⁵;2.27 × 10⁻¹³ to 2.27 × 10⁻¹² | H₂O;3.23 × 10⁻⁴;0.4;1.29 × 10⁻⁴ | θ(H₂O)/θ(H₃VO₄);—;—;5.7 × 10⁷ to 5.7 × 10⁸]

The model predicts a much greater conditional occupation by water under the stated steam-rich gas composition, in line with the steam-dominated interpretation discussed by Pine (1990). The predicted fractions are small despite their large ratio, so they represent relative competition in the specified equilibrium model rather than measured coverage or reaction rate. The result does not exclude the vanadic-acid route proposed by Wormsbecher et al. (1986): Trujillo et al. (1997) discussed local vanadium enrichment, whereas the present estimate uses bulk gas partial pressures and does not model pore confinement or competing reaction barriers.

---