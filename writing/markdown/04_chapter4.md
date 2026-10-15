# 4.0 RESULTS AND DISCUSSION

## 4.1 Model Structures and Geometry Checks

The cluster and adsorbates were optimised before the adsorption energies were compared. Figure 4.1 shows the converged vanadic-acid and water complexes at the model Brønsted acid site. Both complexes remained bound to the site after DFT refinement, but the geometries alone did not establish which adsorbate had the lower energy.

[FIG: fig4_1_complexes.png | Figure 4.1: Optimised adsorption complexes at B3LYP-D3(BJ)/def2-TZVP. Left, vanadic acid (V-PRC); right, water (W-PRC) | Source: author, rendered from the optimised Cartesian coordinates]

Table 4.1 summarises the termination, convergence, and vibrational checks for the structures used in the analysis. The cluster reference had a low-magnitude imaginary mode that was treated as numerical noise under the criterion in Section 3.5. This qualification was retained because the cluster energy was used as the reference for the absolute adsorption energies.

[TBL: Table 4.1: Convergence and vibrational checks for structures calculated at B3LYP-D3(BJ)/def2-TZVP | State;Optimisation status;Imaginary frequencies;Assessment | Cluster reference;Converged;1 (−4.64 cm⁻¹);Accepted as a flat reference minimum | H₃VO₄;Converged;0;Accepted minimum | H₂O;Converged;0;Accepted minimum | V-PRC;Converged;0;Accepted minimum | V-I1;Converged;0;Accepted minimum | V-TS2;Not converged;14;Rejected, not a first-order saddle point | V-I2;Not converged;0;Rejected, cycle limit reached | V-P;Did not terminate;Not calculated;Rejected, job stopped before completion | W-PRC;Converged;0;Accepted minimum | W-P;Converged;0;Accepted minimum]

The candidate structure V-TS2 failed the convergence and vibrational checks. A first-order transition state should have one chemically meaningful imaginary frequency, so V-TS2 was not used as a transition state. The other unsuccessful vanadic-acid structures also failed the convergence or completion checks. Their energies were not treated as validated stationary-point energies.

## 4.2 Adsorption Energies

Table 4.2 compares the electronic adsorption energies of vanadic acid and water at three calculation levels. The negative values indicate that both adsorbates formed lower-energy complexes than the separated cluster and molecule. The difference, ΔΔE, was defined as the vanadic-acid adsorption energy minus the water adsorption energy; a negative value therefore favoured vanadic acid.

[TBL: Table 4.2: Electronic adsorption energies and their difference for vanadic acid and water | Level of theory;H₃VO₄ (kJ mol⁻¹);H₂O (kJ mol⁻¹);ΔΔE = ΔE(H₃VO₄) − ΔE(H₂O) (kJ mol⁻¹) | GFN2-xTB;−196.9;−69.6;−127.3 | B3LYP-D3(BJ)/def2-TZVP;−93.01;−78.32;−14.69 | PBE0-D3(BJ)/def2-TZVP, single point;−93.07;−78.62;−14.44]

Both DFT calculations predicted a more negative electronic adsorption energy for vanadic acid than for water. Their close agreement showed that this ordering was stable to the change of functional, although agreement between two methods did not establish the absolute accuracy of either value. The calculations therefore supported a relative electronic binding preference, not a general conclusion about catalyst performance.

GFN2-xTB predicted a much larger preference for vanadic acid than either DFT calculation. It was therefore suitable for initial geometry screening but not for measuring the adsorption-energy difference in this system. The DFT values were not counterpoise-corrected because the fragment calculations did not produce a complete, converged correction. The absolute adsorption energies may therefore include basis-set-superposition error, and no numerical correction was assumed.

The electronic-energy difference does not by itself establish an adsorption equilibrium or a dealumination rate. It shows that, within this cluster model and at these electronic-structure levels, vanadic acid formed the more strongly bound electronic complex. Entropy, gas composition, pore confinement, and the later bond-cleavage steps also affect the behaviour of adsorbates in a regenerator.

## 4.3 Thermochemical Assessment

Table 4.3 gives the B3LYP harmonic Gibbs free energies of the accepted minima relative to the separated cluster and adsorbate. At 298.15 K, the gas-phase harmonic model favoured water adsorption over vanadic-acid adsorption. This result differed from the electronic-energy comparison and showed that the predicted ordering depended on whether thermal corrections were included.

[TBL: Table 4.3: Harmonic Gibbs free energies relative to the separated cluster and adsorbate at B3LYP-D3(BJ)/def2-TZVP | State;ΔG at 298.15 K (kJ mol⁻¹);ΔG at 1003.15 K (kJ mol⁻¹) | V-PRC;−17.0;+133.4 | V-I1;−35.8;+108.3 | W-PRC;−28.9;+67.0 | W-P;+30.8;+132.7]

At 1003.15 K, the calculated Gibbs free energies for both pre-reaction complexes were positive. The model therefore predicted that gas-phase adsorption was unfavourable at this temperature and that water was less unfavourable than vanadic acid. This ordering differed from the electronic adsorption energies because the harmonic thermal corrections were substantial.

The 1003.15 K values were based on an ideal-gas, rigid-rotor, harmonic-oscillator treatment. That treatment did not represent pore confinement or the local gas environment inside a working catalyst. The electronic adsorption-energy comparison was not a Gibbs free-energy difference and could not be used directly as an equilibrium constant. For these reasons, no quantitative Langmuir site-occupancy estimate was made from the present calculations.

## 4.4 Evaluation of the Dealumination Pathway

The pathway assessment was limited by the convergence and vibrational failures summarised in Table 4.1. V-I1 was a converged minimum, but the candidate V-TS2 structure did not pass the tests required for a first-order saddle point. The subsequent vanadic-acid structures did not yield a validated pathway. Although W-P was a converged minimum, no density-functional transition state for the corresponding water-hydrolysis step was established in this calculation set. The results therefore did not establish a density-functional activation barrier for either route.

The adsorption-energy comparison alone cannot determine whether vanadic acid accelerates dealumination. The calculation did not include sodium, a periodic pore, or a validated transition state, and it did not model reaction rates. It therefore did not test Trujillo et al.’s (1997) local-concentration proposal or Xu et al.’s (2002) sodium-mediated mechanism. The results provided no direct confirmation of the vanadic-acid mechanism proposed by Wormsbecher et al. (1986), but they did not refute it either.
