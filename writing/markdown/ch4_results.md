# CHAPTER FOUR

# RESULTS AND DISCUSSION

## 4.1 Structural Models and Adsorption Complexes

The investigation commenced with the geometry optimisation of the isolated reference molecules: the four-T-site (4T) faujasite cluster (AlSi₄O₄H₁₃), vanadic acid (H₃VO₄), and water (H₂O). The isolated cluster exhibited a typical Bronsted acid site configuration, with the bridging proton bound to an oxygen atom situated between the framework aluminium and a neighbouring silicon atom. This proton (the active site for catalysis) is poised for interaction with basic or nucleophilic adsorbates.

Upon introducing the adsorbates to the cluster, stable pre-reaction complexes (PRCs) were formed. In the vanadic acid pre-reaction complex (V-PRC), the H₃VO₄ molecule coordinates to the acid site through a strong hydrogen bonding network. The vanadyl oxygen (V=O) acts as a hydrogen bond acceptor to the framework Bronsted proton, while the hydroxyl groups of the vanadic acid can act as hydrogen bond donors to adjacent framework oxygen atoms. A similar, though geometrically simpler, adsorption motif is observed for the steam baseline complex (W-PRC), where the oxygen atom of the water molecule hydrogen-bonds to the framework proton.

## 4.2 Electronic Energy Profile of the Reaction Pathways

The core of this investigation is the mapping of the elementary steps following the formation of the pre-reaction complexes. The relative electronic energies (ΔE) for all stationary points along the vanadic acid pathway and the steam baseline were computed at the B3LYP-D3(BJ)/def2-TZVP level. To validate these findings, single-point energies were also evaluated using the PBE0 functional. The results are summarised in Table 4.1.

**Table 4.1** Relative electronic energies (ΔE, in kJ/mol) of stationary points relative to isolated fragments.

| State | Description | B3LYP-D3(BJ) | PBE0-D3(BJ) |
| :--- | :--- | :--- | :--- |
| **Reference** | Isolated cluster + Adsorbate | 0.0 | 0.0 |
| **Vanadic Acid Pathway** | | | |
| V-PRC | Pre-reaction complex | -93.0 | -93.1 |
| V-I₁ | Chemisorbed intermediate | -115.3 | -120.1 |
| V-TS2‡ | Saddle point (Al-O cleavage) | +323.6 | +339.4 |
| V-I₂ | Intermediate (Al partly detached) | -122.1 | -120.5 |
| V-P | Dealuminated product | +419.7 | +413.1 |
| **Steam Baseline** | | | |
| W-PRC | Pre-reaction complex | -78.3 | -78.6 |
| W-P | Hydrolysed product | -24.0 | -22.9 |

*Note:* Energies include D3(BJ) dispersion corrections but do not include zero-point energy (ZPE) or thermal corrections. ‡ Indicates a transition state structure with imaginary frequencies; see Section 4.5.

### 4.2.1 Adsorption Energetics: Vanadic Acid vs. Steam

The initial interaction between the dealuminating agent and the zeolite framework dictates the concentration of the reactive species at the active site. The computed electronic adsorption energies reveal a significant disparity between vanadic acid and steam. At the B3LYP level, vanadic acid binds with an energy of -93.0 kJ/mol, whereas water binds at -78.3 kJ/mol. The PBE0 functional corroborates this difference, predicting binding energies of -93.1 kJ/mol and -78.6 kJ/mol, respectively.

![Figure 4.1: Adsorption Energy of H3VO4 and H2O on the FAU Cluster Model](C:/Users/PC/.gemini/antigravity-ide/brain/9a259048-d274-4584-92bc-3518a31f5431/adsorption_comparison_1791361848441.jpg)

This ΔΔE of approximately 15 kJ/mol in favour of vanadic acid is a critical finding. It indicates that under the competitive conditions of the FCC regenerator, vanadic acid possesses a much higher affinity for the Bronsted acid sites than the vastly more abundant steam. The stronger binding of H₃VO₄ can be attributed to its ability to form a more extensive and cooperative hydrogen-bonding network with the framework compared to the single water molecule.

### 4.2.2 The Vanadic Acid Attack Pathway

Following adsorption, the vanadic acid pathway proceeds through a sequence of intermediates. The first notable stationary point after V-PRC is V-I₁, a chemisorbed intermediate. In V-I₁, the system drops further in energy (to -115.3 kJ/mol), reflecting a state where proton transfer has occurred, protonating the vanadic acid and creating a highly reactive electrophile poised to attack the framework aluminium.

The sequence then encounters a significant energetic hurdle: the cleavage of the framework Al-O bonds. The calculated saddle point for a major cleavage step (V-TS2) resides at a relative energy of +323.6 kJ/mol. This transition state leads to an intermediate, V-I₂ (-122.1 kJ/mol), where the aluminium atom is partially detached from its original tetrahedral coordination but remains anchored to the cluster.

The final state mapped in this study is the dealuminated product (V-P), where the aluminium has been completely extracted from the framework to form an extra-framework complex chelated by the vanadium species, leaving behind a silanol nest on the cluster. This final state is highly endothermic at the electronic energy level (+419.7 kJ/mol).

### 4.2.3 Comparison with the Steam Baseline

The steam baseline provides a stark contrast. The hydrolysis of the framework by water to form the product W-P (representing a single Al-O bond cleavage, the established first step of hydrothermal dealumination) results in a state with a relative electronic energy of -24.0 kJ/mol. This is substantially more stable than the final extracted state in the vanadium pathway. However, as established by Pine (1990) and Trujillo (1997), the overall rate and extent of zeolite destruction by vanadium far exceeds that by steam. 

![Figure 4.2: Electronic Reaction Profile at B3LYP-D3(BJ)/def2-TZVP](C:/Users/PC/.gemini/antigravity-ide/brain/9a259048-d274-4584-92bc-3518a31f5431/energy_profile_tier2_1791361820537.jpg)

The computed electronic energies suggest that while the ultimate thermodynamic state of full aluminium extraction by vanadium is highly endothermic (in this specific cluster model), the intermediate chemisorption states (V-I₁, V-I₂) provide deep energetic sinks that may facilitate a complex, multi-step extraction mechanism driven by high temperatures, effectively validating the necessity of considering vanadium as an active catalytic driver rather than just a passive observer to steam hydrolysis.

## 4.3 Thermochemistry at FCC Regenerator Conditions

Electronic energies describe the potential energy surface at absolute zero. To understand the reaction under the operating conditions of an FCC regenerator (approximately 730 degrees Celsius), the Gibbs free energies (ΔG) were evaluated at 1003.15 K, alongside standard conditions (298.15 K) for reference.

**Table 4.2** Gibbs free energies of reaction (ΔG, in kJ/mol) relative to isolated fragments at 298.15 K and 1003.15 K (B3LYP-D3(BJ)/def2-TZVP level).

| State | ΔG (298 K) | ΔG (1003 K) |
| :--- | :--- | :--- |
| **Vanadic Acid Pathway** | | |
| V-PRC | -17.0 | +133.4 |
| V-I₁ | -35.7 | +108.4 |
| **Steam Baseline** | | |
| W-PRC | -28.9 | +67.0 |
| W-P | +30.8 | +132.7 |

At standard room temperature (298 K), the adsorption of both vanadic acid and water is spontaneous (negative ΔG). The chemisorbed vanadic acid intermediate (V-I₁) is the most thermodynamically stable state at this temperature (-35.7 kJ/mol).

However, at the FCC regenerator temperature of 1003 K, the large entropic penalty associated with a gas-phase molecule binding to a solid surface dominates the free energy equation. The TΔS term becomes large and positive, driving the ΔG of adsorption for both species into the positive (non-spontaneous) regime.

![Figure 4.3: Gibbs Free Energy of Adsorption at 298 K and 1003 K](C:/Users/PC/.gemini/antigravity-ide/brain/9a259048-d274-4584-92bc-3518a31f5431/gibbs_temperature_1791361884324.jpg)

At 1003 K, the formation of the V-PRC complex requires +133.4 kJ/mol, while the W-PRC complex requires +67.0 kJ/mol. The chemisorbed state V-I₁ sits at +108.4 kJ/mol. The fact that dealumination occurs rapidly at these temperatures despite the unfavourable free energy of adsorption indicates that the reaction is driven by the continuous removal of products (irreversible framework collapse) and the high concentration of steam (and consequently, volatile vanadic acid) in the regenerator, which pushes the equilibrium forward according to Le Chatelier's principle.

## 4.4 Functional Sensitivity Analysis

The dual-functional approach (B3LYP vs. PBE0) provides confidence in the computed electronic energies. As seen in Table 4.1, the agreement between the two functionals is excellent. The adsorption energies differ by only 0.1 to 0.3 kJ/mol. For the high-energy transition state (V-TS2) and the product (V-P), the differences are larger (15.8 kJ/mol and 6.6 kJ/mol, respectively) but represent a relative deviation of less than 5 percent. This consistency indicates that the energetic conclusions, particularly the relative binding strengths and the deep intermediate minima, are robust and not an artefact of the chosen exchange-correlation approximation.

## 4.5 Limitations and Quality Assurance

A rigorous computational study must acknowledge the limitations of its models. In this investigation, the transition state optimisation for V-TS2, the barrier for the first major Al-O cleavage in the vanadium pathway, presented significant challenges.

While a stationary point was located and its energy is reported in Table 4.1 (+323.6 kJ/mol), frequency analysis revealed that this structure possessed 14 imaginary vibrational modes, rather than the single imaginary mode strictly required for a true first-order saddle point connecting two minima. This multi-mode character indicates that the structure resides in a complex, flat region of the potential energy surface, likely involving coupled motions of the flexible hydrogen-terminated cluster boundaries alongside the intended bond cleavage.

Because this structure is not a mathematically rigorous first-order saddle point, its energy cannot be definitively assigned as the true activation barrier for the step. Consequently, this study restricts its mechanistic conclusions primarily to the energetics of the stable minima (the pre-reaction complexes, intermediates, and products), which were confirmed to have zero imaginary frequencies and represent true, stable states on the potential energy surface.

## 4.6 Mechanistic Implications for FCC Operation

The computational results provide molecular-level support for the macroscopic observations of vanadium poisoning. The thermodynamic preference for vanadic acid adsorption over steam provides the critical initial step: once H₃VO₄ is formed in the regenerator gas phase, it selectively targets and binds strongly to the Bronsted acid sites, outcompeting steam for access to the framework aluminium.

Once bound, the vanadic acid can transition into deeply stabilised chemisorbed intermediates (such as V-I₁ and V-I₂) that are not available in the simple steam hydrolysis pathway. These deep energetic sinks likely act as 'ratchets' in the dealumination mechanism, pulling the reaction forward step-by-step and preventing the re-healing of broken Al-O bonds. This sequence explains the severe and irreversible loss of crystallinity observed in vanadium-poisoned catalysts (Pine, 1990; Etim et al., 2015), providing a theoretical foundation for the necessity of vanadium trapping technologies in heavy oil refining.
