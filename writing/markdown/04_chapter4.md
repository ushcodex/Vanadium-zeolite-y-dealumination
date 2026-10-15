# 4.0 RESULTS AND DISCUSSION

## 4.1 Model and Adsorption Geometries

The 22-atom cluster retained the local structure needed for the adsorption comparison. Table 4.1 summarises convergence and vibrational checks, while Table 4.2 lists selected aluminium–oxygen distances. The cluster reference had a small imaginary frequency, which was treated as numerical noise under the criterion in Section 3.6. The two pre-reaction adsorption complexes converged as minima, allowing their energies to be compared with the same cluster reference.

[TBL: Table 4.1: Convergence and vibrational checks for the DFT structures | State;Optimisation status;Imaginary frequencies;Assessment | Cluster reference;Converged;1 (−4.64 cm⁻¹);Retained as a flat reference minimum | H₃VO₄;Converged;0;Accepted minimum | H₂O;Converged;0;Accepted minimum | V-PRC;Converged;0;Accepted minimum | V-I1;Converged;0;Accepted minimum | V-TS2;Not converged;14;Rejected as a transition state | V-I2;Not converged;Not calculated;Not accepted, cycle limit reached | V-P;Did not terminate;Not calculated;Not accepted, job stopped before completion | W-PRC;Converged;0;Accepted minimum | W-P;Converged;0;Accepted minimum]

Figure 4.1 compares the optimised pre-reaction complexes. The vanadic-acid oxygen approached aluminium closely, while water remained farther from the aluminium centre. The structural difference is consistent with the electronic-energy comparison in Section 4.2, but geometry alone does not establish either the equilibrium population or the rate of framework hydrolysis.

[FIG: fig4_1_complexes.png | Figure 4.1: Optimised adsorption complexes at B3LYP-D3(BJ)/def2-TZVP. Left, vanadic acid (V-PRC); right, water (W-PRC) | Source: author, rendered from the optimised Cartesian coordinates]

Table 4.2 gives selected aluminium–oxygen distances from the converged structures. In V-PRC, vanadic acid formed a close contact with aluminium and the acid-site aluminium–oxygen bond lengthened relative to the isolated cluster. In W-PRC, water remained outside the aluminium coordination sphere. The converged water product showed a longer framework aluminium–oxygen distance and a new short contact to an oxygen from water, consistent with one hydrolysis step in the model.

[TBL: Table 4.2: Selected aluminium–oxygen distances in converged DFT structures (Å) | Structure;Nearest Al···O distance to adsorbate;Longest framework Al–O distance;Structural interpretation | Cluster reference;Not applicable;1.919;Protonated framework reference | V-PRC;1.947;2.042;Vanadic oxygen approached Al and the acid-site Al–O bond lengthened | V-I1;3.529;1.791;Framework Al–O bonds remained short after the first intermediate formed | W-PRC;3.337;1.885;Water remained outside the Al coordination sphere | W-P;1.718;3.129;Water-derived oxygen approached Al as one framework Al–O bond lengthened]

The distances indicate that vanadic acid and water followed different local geometries at the model site. The short V-PRC contact was consistent with direct interaction between a vanadic-acid oxygen and aluminium. The W-P geometry showed that water could also reach a structure with an elongated framework bond, so the geometry comparison did not uniquely identify the operative catalyst mechanism.

## 4.2 Electronic Adsorption Energies

Table 4.3 compares the adsorption energies obtained at the GFN2-xTB, B3LYP-D3(BJ)/def2-TZVP, and PBE0-D3(BJ)/def2-TZVP levels. The negative values indicate that both molecules formed lower-electronic-energy complexes than the separated cluster and adsorbate. The difference, ΔΔE, was defined as the vanadic-acid adsorption energy minus the water adsorption energy; a negative value therefore favoured vanadic acid.

[TBL: Table 4.3: Electronic adsorption energies of vanadic acid and water (kJ mol⁻¹) | Level of theory;H₃VO₄;H₂O;ΔΔE = ΔE(H₃VO₄) − ΔE(H₂O) | GFN2-xTB;−196.9;−69.6;−127.3 | B3LYP-D3(BJ)/def2-TZVP;−93.01;−78.32;−14.69 | PBE0-D3(BJ)/def2-TZVP, single point;−93.07;−78.62;−14.44]

Both DFT methods predicted more negative electronic adsorption energy for vanadic acid than for water. Their close agreement showed that the relative ordering was stable to the functional change, although it did not establish the absolute accuracy of either method. The DFT comparison therefore supported a modest electronic binding preference for vanadic acid at this cluster site.

GFN2-xTB predicted a much larger vanadic-acid preference than either DFT calculation. It was useful for generating starting geometries and screening candidate structures, but its adsorption-energy difference was not suitable as the final quantitative result. The DFT adsorption energies were not counterpoise-corrected because the fragment calculations did not produce a complete correction; the values in Table 4.3 are therefore uncorrected electronic energies.

Table 4.4 shows the relative electronic energies of the two converged post-adsorption minima. V-I1 and W-P lay below their respective separated cluster-and-adsorbate references at all three levels. The two pathways use separate reference energies, so the values should not be compared as a direct reaction barrier. The larger GFN2-xTB stabilization of V-I1 than the DFT estimates also shows why the semi-empirical values were used for screening rather than quantitative pathway energetics.

[TBL: Table 4.4: Relative electronic energies of converged post-adsorption minima (kJ mol⁻¹) | State;GFN2-xTB;B3LYP-D3(BJ)/def2-TZVP;PBE0-D3(BJ)/def2-TZVP single point | V-I1;−385.1;−115.38;−120.13 | W-P;−65.9;−24.02;−22.88]

## 4.3 Transition-State Assessment

The pathway searches produced one accepted GFN2-xTB saddle-point candidate for the first Al–O cleavage step in the vanadic-acid route. Table 4.5 summarises this result alongside the water-hydrolysis candidate. The vanadic-acid candidate passed the Tier 1 frequency and two-sided displacement checks, so it provided a screening-level barrier for the model. The water candidate did not pass the displacement test because both displaced structures returned to the pre-reaction complex.

[TBL: Table 4.5: Transition-state search results for the first framework Al–O cleavage steps | Route and step;GFN2-xTB result;DFT assessment | V-I1 to V-I2;Accepted Tier 1 candidate, one imaginary mode at −78.21 cm⁻¹ and barrier of 160.70 kJ mol⁻¹ above V-I1;DFT refinement did not retain first-order saddle-point character, as summarised in Table 4.1 | W-PRC to W-P;Candidate with one imaginary mode at −226.10 cm⁻¹ and barrier of 29.29 kJ mol⁻¹ above W-PRC;Two-sided displacement returned to W-PRC, so the candidate was not accepted and was not refined at DFT]

The Tier 1 result showed that the GFN2-xTB search could locate a saddle-point candidate for the vanadic-acid cleavage step. Its DFT refinement did not retain first-order saddle-point character, so the GFN2-xTB barrier could not be treated as a DFT activation barrier. No validated DFT barrier was obtained for the water step. The calculations therefore established a useful screening result, but not a DFT comparison of reaction rates.

## 4.4 Harmonic Gibbs Energies

Table 4.6 gives the harmonic Gibbs free energies of the accepted minima relative to the separated cluster and adsorbate. At both temperatures, the free-energy ordering differed from the electronic adsorption-energy ordering: the model favoured water adsorption after thermal corrections were included. The separation between the two pre-reaction complexes was larger at the regenerator temperature than at room temperature. At 1003.15 K, both pre-reaction complexes lay above their separated gas-phase references, so the model predicted unfavourable gas-phase adsorption at that temperature.

[TBL: Table 4.6: Harmonic Gibbs free energies relative to the separated cluster and adsorbate (kJ mol⁻¹) | State;ΔG at 298.15 K;ΔG at 1003.15 K | V-PRC;−17.0;+133.4 | V-I1;−35.8;+108.3 | W-PRC;−28.9;+67.0 | W-P;+30.8;+132.7]

These results show why an electronic adsorption energy should not be substituted for a Gibbs free energy in a high-temperature site-occupation calculation. The harmonic thermochemistry incorporated temperature-dependent contributions that changed the relative preference. The calculation nevertheless treated the adsorbed complex as an ideal-gas species and did not include pore confinement, so its Gibbs energies were not a definitive description of a working RFCC catalyst.

## 4.5 Conditional Competitive Site-Occupation Estimate

The Gibbs energies of V-PRC and W-PRC were combined with the reported gas partial pressures to calculate a formal competitive-site estimate at 1003.15 K. Table 4.7 gives the resulting equilibrium constants and site fractions under the single-site Langmuir expression described in Section 3.5. Under these assumptions, water had the larger adsorption term because its harmonic Gibbs energy was more favourable and its partial pressure was much higher. The calculation therefore predicted a very small vanadic-acid fraction for the assumed gas composition.

[TBL: Table 4.7: Formal single-site occupation estimate at 1003.15 K | Species or ratio;K° at 1003.15 K;Partial pressure p/p°;Calculated site fraction or ratio | H₃VO₄;1.13 × 10⁻⁷;2 × 10⁻⁶ to 2 × 10⁻⁵;2.27 × 10⁻¹³ to 2.27 × 10⁻¹² | H₂O;3.23 × 10⁻⁴;0.4;1.29 × 10⁻⁴ | θ(H₂O)/θ(H₃VO₄);Not applicable;Not applicable;5.7 × 10⁷ to 5.7 × 10⁸]

The formal estimate quantified the effect of the specified partial pressures and harmonic free energies; it did not establish the actual site population in an operating catalyst. The calculation assumed an ideal-gas standard state, one equivalent site, and no interactions between adsorbed molecules. The local cluster and harmonic treatment did not include pore confinement, local enrichment of vanadic acid, or anharmonic effects. The calculated ratio should therefore be interpreted as a conditional comparison of thermal and pressure terms, not as a measured or definitive equilibrium prediction.

## 4.6 Implications for the Proposed Mechanisms

The model's electronic-energy preference for vanadic acid was consistent with a direct interaction at the acid site, but it did not demonstrate that H₃VO₄ drove framework dealumination. Under the stated pressure range, the conditional high-temperature estimate favoured water occupation, showing that thermal corrections and gas composition changed the comparison. These results neither verified nor excluded the vanadic-acid route discussed by Wormsbecher et al. (1986) and Trujillo et al. (1997). They also did not rule out Pine's (1990) steam-driven explanation or Xu et al.'s (2002) sodium-mediated pathway.

The GFN2-xTB saddle-point candidate provided a starting point for further work, while the DFT frequency analysis showed that the same candidate was not a validated DFT transition state. Adsorption and conditional site occupation do not determine a reaction rate without a reliable activation barrier. The calculations therefore clarified the model's relative binding and thermochemical predictions but did not establish which mechanism controlled catalyst dealumination.
