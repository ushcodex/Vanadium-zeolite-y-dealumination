# CHAPTER FIVE

# CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Summary of Findings

This study employed a two-tier computational workflow, combining semi-empirical (GFN2-xTB) pathway exploration with hybrid density functional theory (B3LYP-D3(BJ) and PBE0-D3(BJ)), to investigate the elementary mechanism of zeolite Y dealumination by vanadic acid (H₃VO₄) and steam (H₂O). A four-tetrahedral-site (4T) cluster model was used to represent the catalytically active Bronsted acid site of the faujasite framework.

The principal findings are as follows:

1. Adsorption Energetics: Vanadic acid binds to the zeolite Bronsted acid site significantly more strongly than steam. The electronic adsorption energy (ΔE) for vanadic acid is -93.0 kJ/mol, compared with -78.3 kJ/mol for water, representing a ΔΔE of approximately 15 kJ/mol in favour of the metal poison. This finding was consistent across both the B3LYP and PBE0 density functionals.

2. Chemisorbed Intermediates: Following initial hydrogen-bonded adsorption, the vanadic acid pathway accesses deeply stabilised chemisorbed intermediates (V-I₁ and V-I₂), which exhibit relative electronic energies below -115 kJ/mol. These states involve proton transfer to the vanadic acid, preparing the framework for subsequent aluminium-oxygen bond cleavage.

3. Thermochemistry at FCC Conditions: At the high temperatures typical of fluid catalytic cracking regenerators (1003 K), the Gibbs free energy of adsorption for both vanadic acid and steam becomes positive due to the large entropic penalty of binding gas-phase molecules. The reaction must therefore be driven forward by high steam partial pressures and the irreversible nature of framework collapse.

4. Saddle Point Complexity: The transition state for the major framework bond cleavage (V-TS2) resides in a flat, complex region of the potential energy surface. Within the constraints of the finite cluster model, a true first-order saddle point could not be definitively isolated, highlighting the challenges of modelling concerted bond-breaking events in truncated zeolite models.

## 5.2 Conclusions

Based on the computational findings, the following conclusions are drawn:

1. The molecular basis for the severe and rapid deactivation of FCC catalysts by vanadium lies, initially, in thermodynamics. Vanadic acid, once formed in the regenerator gas phase, is a potent electrophile that outcompetes steam for adsorption at the critical Bronsted acid sites, selectively targeting the active centres responsible for cracking.

2. The vanadic acid attack pathway is characterised by the existence of highly stable, chemisorbed intermediate states. These intermediates likely function as thermodynamic traps that prevent the reversal of early bond-breaking events, thereby accelerating the irreversible extraction of aluminium from the framework in a ratchet-like mechanism.

3. Hybrid density functional theory, augmented with empirical dispersion corrections (D3(BJ)), provides a robust and internally consistent framework for studying these complex heterogeneous catalytic degradation processes, as evidenced by the excellent agreement between the B3LYP and PBE0 functionals for the stable stationary points.

## 5.3 Recommendations

To mitigate the effects of vanadium poisoning in industrial FCC operations, particularly in Nigerian refineries processing high-metal residues, the following recommendations are proposed:

1. Design of Vanadium Traps: The computed adsorption energies provide a quantitative benchmark for the design of new vanadium trapping additives. To effectively protect the zeolite, a trapping material (such as a basic metal oxide) must possess a binding affinity for vanadic acid that significantly exceeds the -93 kJ/mol affinity of the zeolite acid site, ensuring that the poison is captured before it can access the micropores.

2. Catalyst Formulation: Given that vanadic acid targets the Bronsted proton, catalyst formulations that optimise the acid site density and strength (such as precisely dealuminated ultra-stable Y zeolites) may exhibit altered susceptibility to vanadium attack. Further development of these tailored matrices is recommended.

## 5.4 Suggestions for Future Work

The computational study of catalyst deactivation is a complex undertaking, and several avenues for further research remain open:

1. Periodic Boundary Conditions: Future studies should employ periodic DFT calculations on the full faujasite unit cell. This would eliminate the boundary constraints inherent in the cluster model, capture long-range electrostatic effects, and potentially resolve the transition states for the Al-O bond cleavages with greater accuracy.

2. The Role of Sodium: Industrial observations confirm that trace sodium dramatically accelerates vanadium poisoning through the formation of sodium vanadate species. Subsequent computational investigations should model the ternary interaction between the zeolite framework, vanadic acid, and sodium cations.

3. Alternative Attack Pathways: The mechanism mapped in this study assumes an initial attack on the Al-O(H)-Si bridge. Exploring parallel pathways, such as attack on non-protonated Al-O-Si bridges or interaction with extra-framework aluminium species, would provide a more comprehensive picture of the deactivation network.
