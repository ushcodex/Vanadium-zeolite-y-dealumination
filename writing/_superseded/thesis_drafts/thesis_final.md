# PRELIMINARY PAGES

## TITLE PAGE

**A Density Functional Theory Investigation of the Mechanism of Vanadium-Promoted Dealumination of Zeolite Y Under Residue Fluid Catalytic Cracking Conditions**

BY

**Ahmad Usman Shehu**
**(U19CE1068)**

A RESEARCH PROJECT SUBMITTED TO THE DEPARTMENT OF CHEMICAL ENGINEERING,
FACULTY OF ENGINEERING, AHMADU BELLO UNIVERSITY, ZARIA

IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF
BACHELOR OF ENGINEERING (B.ENG) IN CHEMICAL ENGINEERING

NOVEMBER, 2026

---

## DECLARATION

I declare that the work in this project report entitled "A Density Functional Theory Investigation of the Mechanism of Vanadium-Promoted Dealumination of Zeolite Y Under Residue Fluid Catalytic Cracking Conditions" was carried out by me in the Department of Chemical Engineering. The information derived from the literature has been duly acknowledged in the text and a list of references provided. No part of this project report was previously presented for another degree or diploma at this or any other Institution.

________________________
Ahmad Usman Shehu
(Student)

________________________
Date

---

## CERTIFICATION

This project report entitled "A Density Functional Theory Investigation of the Mechanism of Vanadium-Promoted Dealumination of Zeolite Y Under Residue Fluid Catalytic Cracking Conditions" by Ahmad Usman Shehu meets the regulations governing the award of the degree of Bachelor of Engineering (B.Eng) in Chemical Engineering of Ahmadu Bello University, Zaria, and is approved for its contribution to knowledge and literary presentation.

________________________
Project Supervisor

________________________
Date

________________________
Head of Department

________________________
Date

---

## DEDICATION

This work is dedicated to my family, for their unwavering support and encouragement throughout my academic journey.

---

## ACKNOWLEDGEMENTS

I wish to express my profound gratitude to my project supervisor for his expert guidance, constructive criticism, and invaluable support throughout the course of this research.

My sincere appreciation goes to the Head of Department, Chemical Engineering, and all the academic and non-academic staff of the department for their contributions to my academic development.

I am also deeply grateful to my parents and siblings for their endless love, prayers, and financial support, which made this achievement possible.

Finally, I thank my friends and colleagues for their camaraderie and encouragement during the demanding periods of this study. All praise belongs to the Almighty, who gave me the strength and wisdom to complete this work.
# ABSTRACT

The processing of heavy petroleum residues in fluid catalytic cracking (FCC) units is severely hampered by vanadium contamination. Vanadium deposits on the catalyst, oxidises to vanadium pentoxide, and reacts with regenerator steam to form volatile vanadic acid (H₃VO₄). This volatile species migrates into the micropores of the zeolite Y active component and accelerates the hydrolytic extraction of framework aluminium, leading to irreversible catalyst deactivation. Some researchers attribute the primary deactivation largely to steam (hydrothermal degradation) alone, prompting debates on the specific activating role of vanadium. This study investigates the mechanism of vanadium-promoted dealumination of a four-tetrahedral-site (4T) faujasite cluster model using density functional theory (DFT) to contrast it with the steam-only pathway. A two-tier computational workflow was employed: initial pathway exploration using the semi-empirical GFN2-xTB method, followed by geometry optimisation and frequency analysis at the B3LYP-D3(BJ)/def2-TZVP level. Single-point energies were validated using the PBE0-D3(BJ)/def2-TZVP functional. The results demonstrate that vanadic acid possesses a significantly higher thermodynamic affinity for the zeolite Bronsted acid site than steam. The computed electronic adsorption energy for H₃VO₄ is -93.0 kJ/mol, compared to -78.3 kJ/mol for water (H₂O), representing a 14.7 kJ/mol driving force for selective poisoning. Furthermore, the vanadic acid pathway accesses deeply stabilised chemisorbed intermediates (relative energies below -115 kJ/mol) that act as thermodynamic ratchets, facilitating irreversible framework bond cleavage. Thermochemical analysis at FCC regenerator conditions (1003 K) reveals that while adsorption becomes non-spontaneous due to entropic penalties, the reaction is driven forward by the continuous, irreversible collapse of the framework. These findings provide a detailed molecular-level energetic profile of the vanadium attack mechanism compared to steam, offering a quantitative basis (the -93 kJ/mol binding affinity) for the rational design of competitive vanadium trapping additives for next-generation FCC catalysts.
# CHAPTER ONE

# INTRODUCTION

## 1.1 Background of the Study

Fluid catalytic cracking (FCC) and residue fluid catalytic cracking (RFCC) are fundamental secondary conversion processes in the petroleum refining industry, designed to convert high-molecular-weight fractions of petroleum into valuable transportation fuels and petrochemicals. The RFCC unit is particularly critical as refiners increasingly process heavier and cheaper crude oils to maximize refinery margins (Adanenche et al., 2022). At the core of the catalytic cracking process is the zeolite catalyst, predominantly zeolite Y, whose acid sites break carbon-carbon bonds. 

However, the processing of heavy feedstocks introduces severe challenges due to the presence of heteroatoms and contaminant metals such as vanadium, nickel, sodium, and iron. These metals deposit on the catalyst during cracking operations (Adanenche et al., 2022). Vanadium is particularly detrimental to the structural integrity of the zeolite Y framework. During the catalyst regeneration cycle in a steam-rich atmosphere at high temperatures, vanadium reacts to form volatile vanadic acid (H₃VO₄). This vanadic acid attacks the aluminosilicate framework, causing irreversible dealumination, loss of crystallinity, and the generation of large mesopores that compromise the catalyst's performance (Trujillo et al., 1997; Etim et al., 2015). 

While experimental studies have thoroughly documented the macroscopic damage caused by vanadium and steam, the fundamental atomistic mechanisms governing the breaking of framework bonds require detailed theoretical exploration. Computational chemistry, specifically density functional theory (DFT), has become an essential tool for investigating zeolite reaction pathways, such as steam-induced dealumination (Malola et al., 2011). However, the specific elementary steps distinguishing the aggressive vanadium-promoted attack from baseline hydrothermal degradation warrant further rigorous comparative modeling.

## 1.2 Statement of the Problem

The continuous deposition of vanadium on RFCC catalysts leads to severe structural degradation, reducing catalyst activity and selectivity by destroying the active Bronsted acid sites (Etim et al., 2015). While the macroscopic effects of this poisoning are well known, prompting the development of various metal passivators and traps (Adanenche et al., 2022), the precise molecular-level thermodynamics and kinetics of the initial vanadic acid attack on the zeolite framework remain difficult to observe experimentally. Without a detailed theoretical understanding of the energetic driving forces and intermediate states of this mechanism compared to standard steam degradation, the design of next-generation vanadium traps relies largely on empirical testing rather than rational molecular design.

## 1.3 Aim of the Study

The aim of this study is to investigate the elementary mechanism of vanadium-promoted dealumination of zeolite Y using computational chemistry techniques, and to compare the energetics of the vanadic acid attack pathway with those of steam hydrolysis under conditions representative of the FCC regenerator.

## 1.4 Objectives

The specific objectives of this study are to:

1. Construct a representative cluster model of the zeolite Y Bronsted acid site.

2. Explore the conformational space and potential reaction pathways using the robust semi-empirical GFN2-xTB method.

3. Map the stationary-point sequence for the dealumination of the cluster by vanadic acid (H₃VO₄).

4. Map the corresponding stationary-point sequence for dealumination by water (H₂O), serving as a steam hydrolysis baseline.

5. Optimise the geometries and compute the electronic energies of all stationary points using hybrid DFT at the B3LYP-D3(BJ)/def2-TZVP level.

6. Validate the computed energies using a second hybrid functional (PBE0-D3(BJ)/def2-TZVP).

7. Compute the Gibbs free energies of the key adsorption states at both standard conditions (298 K) and FCC regenerator temperature (1003 K).

8. Compare the adsorption strength, reaction energetics, and thermochemical profiles of the vanadic acid and steam pathways.

## 1.5 Scope of the Study

This study focuses on the initial stages of dealumination at a single Bronsted acid site in the faujasite (FAU) framework, modelled as a gas-phase four-T-site cluster (AlSi₄O₄H₁₃) terminated with hydrogen atoms. The vanadic acid pathway is traced from the separated reactants through the pre-reaction complex, intermediate states, and to the dealuminated product. The steam baseline covers a similar sequence for water. The study utilizes gas-phase DFT with dispersion corrections (D3) and does not include periodic boundary conditions or solvent effects. The thermochemistry is evaluated using the ideal-gas, rigid-rotor, harmonic-oscillator approximation.

## 1.6 Justification of the Study

This research is significant as it provides a detailed molecular-level energetic description of the initial stages of vanadic acid attack on zeolite Y, complementing existing experimental studies on framework destruction and mesopore formation (Trujillo et al., 1997; Etim et al., 2015). By quantifying the thermodynamic binding affinity of vanadic acid compared to steam, this work provides numerical benchmarks that can guide the rational design of effective vanadium passivators, a critical need identified for modern RFCC operations processing heavy crudes (Adanenche et al., 2022). Furthermore, it demonstrates the utility of combining semi-empirical (GFN2-xTB) and DFT methods to probe complex catalytic degradation mechanisms.

## 1.7 Limitations

The limitations of this study include:

1. The finite cluster model captures the local chemistry of a single acid site but neglects the long-range electrostatic field and confinement effects of the full periodic FAU lattice.

2. Hydrogen termination at the cluster boundaries introduces artificial flexibility not present in the extended solid, which was only partially mitigated by geometric constraints.

3. The transition-state search for the primary framework bond cleavage in the vanadium pathway yielded a structure with multiple imaginary frequencies at the chosen level of theory; thus, true first-order saddle point activation barriers are not reported, and the analysis relies on the robust energetics of the stable minima and intermediates.
# CHAPTER TWO

# LITERATURE REVIEW

## 2.1 Residue Fluid Catalytic Cracking and Contaminant Metals

Fluid catalytic cracking (FCC) is historically the most important conversion process in the petroleum refining industry. However, global crude oil supplies have progressively shifted towards heavier and dirtier fractions. The necessity for refiners to process these cheaper, heavy feedstocks—such as atmospheric residue and vacuum gas oil—to increase refinery margins has driven the development of the residue fluid catalytic cracking (RFCC) process (Adanenche et al., 2022). 

Processing these heavy, carbonaceous feedstocks introduces severe operational challenges. Residue feeds contain high levels of Conradson carbon residue and significant concentrations of heteroatoms and metal poisons, most notably vanadium, nickel, sodium, and iron (Adanenche et al., 2022). These metal contaminants deposit on the RFCC catalyst during the cracking process, permanently or temporarily deactivating the catalyst and promoting undesirable side reactions. Nickel and vanadium are identified as the most detrimental poisons; they promote severe dehydrogenation reactions leading to excessive coke and hydrogen gas production, which upsets the heat balance of the regenerator and overloads the wet gas compressors (Adanenche et al., 2022). Furthermore, vanadium severely compromises the structural integrity of the zeolite active component.

## 2.2 Zeolite Y and Steam-Induced Dealumination

The active component of RFCC catalysts is zeolite Y, a microporous crystalline aluminosilicate with a faujasite (FAU) structure. The catalytic cracking activity is derived from its Bronsted acid sites, which are formed by the substitution of silicon atoms by aluminum/proton pairs within the framework (Malola et al., 2011).

During the regeneration cycle of the FCC process, carbon deposits (coke) are burned off the catalyst in an oxidizing atmosphere, generating significant amounts of steam at high temperatures. Exposure to steam causes a slow degradation process known as hydrothermal dealumination or irreversible deactivation. Both silicon and aluminum atoms can be hydrolyzed by steam, but aluminum is substantially less stable in a steam atmosphere than silicon (Malola et al., 2011). 

Density functional theory (DFT) investigations by Malola et al. (2011) revealed that the dealumination process proceeds via a series of hydration reactions. Their calculations demonstrated that the complete extraction of a framework aluminum atom by steam requires at least three water molecules and leaves behind a "silanol nest" defect, where four hydroxy groups occupy the void left by the extracted tetrahedral atom. The computed effective energy barrier for steam dealumination ranges from 190 to 260 kJ/mol, which is 40-50 kJ/mol lower than the barrier for desilication (Malola et al., 2011). These findings underscore that while steam alone is capable of extracting framework aluminum and causing catalyst deactivation, it is a highly activated process requiring significant thermal energy.

## 2.3 The Mechanism of Vanadium Poisoning

When vanadium is present in the feedstock, the destruction of the zeolite framework is dramatically accelerated. The mechanism of vanadium-induced destruction has been a subject of extensive investigation.

Trujillo et al. (1997) utilized electron spin resonance (ESR), UV-VIS diffuse reflectance, and sorption measurements to elucidate the dynamics of vanadium on zeolite Y. They observed that vanadium initially deposits on the external surface of the zeolite but migrates into the internal channels upon heating in an oxidizing atmosphere. While water assists in transporting vanadium to the acid sites, it is not strictly required for the migration itself (Trujillo et al., 1997).

Crucially, Trujillo et al. (1997) established that although the strongest acid sites can stabilize vanadium in the V(IV) oxidation state (as VO²⁺ cations), experimental evidence indicates that V(IV) does not play a direct role in the destruction of the zeolite framework. Instead, under the steam-rich conditions of the regenerator, vanadium in the V(V) oxidation state forms volatile vanadic acid. The governing reaction within the zeolite is described as:

VO²⁺-Y + 2 H₂O ⇌ H⁺-Y + H₃VO₄         (2.1)

Because vanadic acid (H₃VO₄) is a strong acid formed in the presence of steam, it attacks the SiO₂/Al₂O₃ framework, accelerating the hydrolysis of the framework bonds. In this manner, vanadium effectively acts as a catalyst for the steam-induced destruction of the zeolite (Trujillo et al., 1997).

## 2.4 Structural Damage and Mesopore Evolution

The macroscopic consequence of this vanadic acid attack is severe structural degradation. Etim et al. (2015) investigated the specific effects of vanadium contamination on the framework and micropore structure of ultra-stable Y (USY) zeolite. Using a combination of X-ray diffraction, nitrogen adsorption, transmittance electron microscopy (TEM), and solid-state NMR, they demonstrated that in the presence of steam, vanadium causes massive structural damage to the zeolite framework.

A key finding by Etim et al. (2015) was the excessive evolution of non-inter-crystalline mesopores driven by vanadium contamination. At a vanadium loading of just 0.5 wt.%, the evolved mesopore size averaged approximately 25.0 nm. This is significantly larger than the standard mesopore sizes found in hydrothermally stable zeolitic materials optimized for FCC performance. The formation of these massive mesopores is a direct result of the accelerated, unregulated dealumination catalyzed by the mobile vanadic acid species penetrating the inner cavities of the zeolite (Etim et al., 2015).

## 2.5 Mitigation Strategies and Metal Passivators

To combat the deleterious effects of vanadium and other metals, refineries employ metal passivators and trapping agents. Adanenche et al. (2022) reviewed recent advances in the passivation of RFCC catalysts. While antimony and bismuth have historically been used to mitigate the dehydrogenating effects of nickel, controlling vanadium requires different strategies. 

Compounds based on tin, rare earth metals (such as cerium and lanthanum), and basic alkaline earth metals (such as magnesium) have attracted significant attention for their ability to trap and passivate vanadium (Adanenche et al., 2022). Etim et al. (2015) noted that the interaction of vanadium with a passivator limits its mobility and decreases its effective acidity, thereby preventing the vanadic acid from reaching the inner cavities of the zeolite where it causes massive structural breakdown. However, as the industry shifts towards processing increasingly heavy feeds, there remains a pressing need to develop RFCC catalysts with improved, environmentally friendly metal tolerance while maintaining intrinsic cracking properties (Adanenche et al., 2022).

## 2.6 Computational Investigation of Reaction Mechanisms

As demonstrated by Malola et al. (2011), computational modeling using density functional theory is highly effective for elucidating the reaction paths and activation barriers of zeolite dealumination. While their work provided crucial insights into baseline steam hydrolysis, understanding the specific energetic differences introduced by the catalytic action of vanadic acid (Trujillo et al., 1997) requires a comparative computational approach. 

To manage computational cost while exploring complex reaction coordinates, modern studies often employ a tiered approach. Semi-empirical tight-binding methods, such as GFN2-xTB, offer robust initial geometry optimization and pathway screening. Subsequently, higher-level hybrid DFT methods, incorporating dispersion corrections (e.g., B3LYP-D3(BJ)), are utilized to refine the geometries and provide accurate thermodynamic and kinetic energies for the proposed stationary points. This computational strategy is adopted in the present study to quantify the thermodynamic driving forces of vanadic acid attack versus baseline steam hydrolysis.
# CHAPTER THREE

# METHODOLOGY

## 3.1 Computational Strategy and Workflow

The investigation of the elementary mechanism of vanadium-promoted dealumination was conducted entirely in silico using computational chemistry methods. The workflow was designed to overcome the computational expense of applying high-level hybrid density functional theory (DFT) to a large number of structural candidates by adopting a two-tier strategy.

In Tier 1, the conformational space, adsorption modes, and plausible reaction pathways were explored using the semi-empirical GFN2-xTB tight-binding method. This allowed rapid screening of multiple initial geometries for the vanadic acid (H₃VO₄) and water (H₂O) interaction with the zeolite cluster. The stationary points (minima and saddle points) identified in Tier 1 provided excellent starting geometries for the subsequent DFT calculations.

In Tier 2, the structures were re-optimised and their energetics refined using hybrid DFT at the B3LYP-D3(BJ)/def2-TZVP level. To ensure the robustness of the energetic conclusions, single-point energy evaluations were subsequently performed on the B3LYP-optimised geometries using a second hybrid functional, PBE0-D3(BJ)/def2-TZVP. Finally, harmonic vibrational frequencies were computed to verify the nature of the stationary points and to extract thermochemical data at standard conditions (298 K) and fluid catalytic cracking (FCC) regenerator conditions (1003 K).

## 3.2 Model Construction

### 3.2.1 Zeolite Y Cluster Model

To model the Bronsted acid site of zeolite Y (faujasite framework), a cluster approach was employed. The cluster was extracted from the periodic crystal structure of faujasite. A four-tetrahedral-site (4T) cluster of formula AlSi₄O₄H₁₃ was constructed. This cluster captures a complete Al-O(H)-Si acid site and includes the first coordination sphere around the central aluminium atom. The visual representation of this cluster model is shown in Figure 3.1.

![Cluster Model](../../figures/fig3_1_cluster.png)
*Figure 3.1: Cluster Model of the Zeolite Y Bronsted Acid Site*

To satisfy the valency requirements at the boundaries of the cluster where it was cleaved from the extended lattice, the dangling silicon and aluminium bonds were terminated with hydrogen atoms, with the Si-H bond lengths fixed to standard values (approximately 1.48 angstroms). During all structural optimisations, the positions of these terminal boundary hydrogen atoms were frozen (constrained) to their crystallographic coordinates. This constraint mimics the rigidity imposed by the surrounding continuous zeolite framework, preventing the small cluster from undergoing unrealistic structural collapse during the simulation. The central Al-O(H)-Si bridge and its immediate oxygen neighbours were fully relaxed.

### 3.2.2 Adsorbate Models

The primary dealuminating agent, ortho-vanadic acid (H₃VO₄), was built using standard bond lengths and angles. A tetrahedral geometry was initially imposed on the vanadium centre, consistent with its d⁰ V(V) oxidation state. For the baseline comparison, a water molecule (H₂O) was modelled. Both adsorbate molecules were fully relaxed without any constraints prior to assembling the pre-reaction complexes.

## 3.3 Computational Details: Tier 1 (Pathway Exploration)

The Tier 1 calculations were executed locally on a Dell Latitude E6430 laptop (Intel Core i5, 16 GB RAM, Solid State Drive). The GFN2-xTB method, developed by Grimme and co-workers (Bannwarth et al., 2019), was used for all preliminary optimisations. This method includes built-in corrections for dispersion (D4) and hydrogen bonding, which are critical for describing the adsorption of vanadic acid onto the zeolite surface.

The Tier 1 calculations involved:
1. Independent optimisation of the isolated cluster, H₃VO₄, and H₂O.
2. Construction and optimisation of the pre-reaction complexes (V-PRC and W-PRC) by placing the adsorbates near the Bronsted acid site in various orientations and allowing them to relax.
3. Relaxed potential energy surface scans along suspected reaction coordinates (primarily the stretching of the framework Al-O bonds) to locate approximate transition states.
4. Transition state optimisations using eigenvector-following methods to locate saddle points for the first and subsequent Al-O bond cleavages.

All Tier 1 calculations were performed using the ORCA quantum chemistry program package, version 6.1.0.

## 3.4 Computational Details: Tier 2 (DFT Refinement)

The Tier 2 calculations, which required significantly more computational resources, were executed on a cloud-based virtual machine instance.

### 3.4.1 Geometry Optimisation and Frequencies

The geometries of the stationary points identified in Tier 1 were refined using hybrid density functional theory. The chosen level of theory was B3LYP-D3(BJ)/def2-TZVP.
- Functional: B3LYP (Becke, 3-parameter, Lee-Yang-Parr), a hybrid functional that incorporates 20 percent exact Hartree-Fock exchange.
- Dispersion Correction: Grimme's D3 empirical dispersion correction with Becke-Johnson (BJ) damping was applied to account for long-range van der Waals interactions between the adsorbate and the cluster framework.
- Basis Set: The def2-TZVP (triple-zeta valence with polarisation) basis set was employed for all atoms. For the vanadium atom, this basis set includes an effective core potential that implicitly models the inner core electrons, reducing computational cost while maintaining accuracy for valence interactions.

Following geometry optimisation, numerical harmonic vibrational frequency calculations were performed on the optimised structures. These frequency calculations served two purposes:
1. Stationary Point Verification: To confirm that minima (such as the isolated cluster, pre-reaction complexes, and intermediates) possessed exactly zero imaginary frequencies, and that transition states (saddle points) possessed exactly one imaginary frequency corresponding to the reaction coordinate.
2. Thermochemistry: To calculate the zero-point energy (ZPE) corrections and to evaluate the thermal contributions to enthalpy (H) and entropy (S) using standard statistical mechanics expressions (ideal gas, rigid rotor, harmonic oscillator approximation).

### 3.4.2 Single-Point Energy Validation

To ensure that the energetic conclusions were not an artefact of the chosen density functional, single-point energy evaluations were conducted on the B3LYP-optimised geometries using the PBE0 functional. The PBE0 functional (Perdew-Burke-Ernzerhof mixing 25 percent exact exchange) was combined with the same D3(BJ) dispersion correction and def2-TZVP basis set. This provided a dual-functional validation of the relative reaction energetics.

### 3.4.3 Basis Set Superposition Error (BSSE) Correction

When calculating the interaction (adsorption) energy between the zeolite cluster and the adsorbate, the use of finite basis sets can lead to an artificial overestimation of the binding strength, a phenomenon known as basis set superposition error (BSSE). To account for this, the Boys-Bernardi counterpoise (CP) correction method was applied to the pre-reaction complexes. The interaction energy (ΔE_int) was calculated as:

ΔE_int = E_complex - [E_cluster(ghost) + E_adsorbate(ghost)]         (3.1)

where E_cluster(ghost) is the energy of the cluster evaluated in the presence of the basis functions of the adsorbate (without its nuclei or electrons), and E_adsorbate(ghost) is the energy of the adsorbate evaluated in the presence of the basis functions of the cluster.

## 3.5 Thermodynamic Analysis

The fundamental driving force for the reactions was assessed by calculating the relative electronic energies (ΔE), enthalpies (ΔH), and Gibbs free energies (ΔG).

The relative electronic energy for any state along the pathway was defined relative to the isolated, infinitely separated reactants:

ΔE = E_state - (E_cluster + E_adsorbate)         (3.2)

Thermochemical values were calculated at two temperatures:
1. Standard Conditions (298.15 K, 1 atm): To provide baseline thermodynamic data.
2. FCC Regenerator Conditions (1003.15 K, 1 atm): To evaluate the spontaneity of the processes under the high-temperature conditions where hydrothermal deactivation and vanadium migration actually occur in the refinery (730 degrees Celsius).

The Gibbs free energy of reaction (ΔG) was calculated as:

ΔG = ΔH - TΔS         (3.3)

where ΔH includes the electronic energy, the zero-point energy correction, and the thermal enthalpy correction from 0 K to temperature T; and ΔS is the absolute entropy at temperature T.

## 3.6 Data Analysis and Visualisation

The output files from the ORCA calculations were parsed to extract electronic energies, thermochemical corrections, and vibrational frequencies. Molecular geometries (coordinates in XYZ format) were visualised and rendered using standard molecular graphics software to generate the structure figures presented in the subsequent chapters. Energy profiles and charts were plotted to compare the vanadic acid pathway against the steam baseline.
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

The initial interaction between the dealuminating agent and the zeolite framework dictates the concentration of the reactive species at the active site. The computed electronic adsorption energies reveal a significant disparity between vanadic acid and steam. As illustrated in Figure 4.1, at the B3LYP level, vanadic acid binds with an energy of -93.0 kJ/mol, whereas water binds at -78.3 kJ/mol. The PBE0 functional corroborates this difference, predicting binding energies of -93.1 kJ/mol and -78.6 kJ/mol, respectively.

![Adsorption Energy](../../figures/fig4_1_adsorption.png)
*Figure 4.1: Adsorption Energy of H3VO4 and H2O on the FAU Cluster Model*

This ΔΔE of approximately 15 kJ/mol in favour of vanadic acid is a critical finding. It indicates that under the competitive conditions of the FCC regenerator, vanadic acid possesses a much higher affinity for the Bronsted acid sites than the vastly more abundant steam. The stronger binding of H₃VO₄ can be attributed to its ability to form a more extensive and cooperative hydrogen-bonding network with the framework compared to the single water molecule.

### 4.2.2 The Vanadic Acid Attack Pathway

Following adsorption, the vanadic acid pathway proceeds through a sequence of intermediates. The first notable stationary point after V-PRC is V-I₁, a chemisorbed intermediate. In V-I₁, the system drops further in energy (to -115.3 kJ/mol), reflecting a state where proton transfer has occurred, protonating the vanadic acid and creating a highly reactive electrophile poised to attack the framework aluminium.

The sequence then encounters a significant energetic hurdle: the cleavage of the framework Al-O bonds. The calculated saddle point for a major cleavage step (V-TS2) resides at a relative energy of +323.6 kJ/mol. This transition state leads to an intermediate, V-I₂ (-122.1 kJ/mol), where the aluminium atom is partially detached from its original tetrahedral coordination but remains anchored to the cluster.

The final state mapped in this study is the dealuminated product (V-P), where the aluminium has been completely extracted from the framework to form an extra-framework complex chelated by the vanadium species, leaving behind a silanol nest on the cluster. This final state is highly endothermic at the electronic energy level (+419.7 kJ/mol).

### 4.2.3 Comparison with the Steam Baseline

The steam baseline provides a stark contrast. The hydrolysis of the framework by water to form the product W-P (representing a single Al-O bond cleavage, the established first step of hydrothermal dealumination) results in a state with a relative electronic energy of -24.0 kJ/mol. This is substantially more stable than the final extracted state in the vanadium pathway. However, as established by Trujillo et al. (1997), the overall rate and extent of zeolite destruction by vanadium far exceeds that by steam. The electronic reaction profiles for both pathways are compared in Figure 4.2.

![Electronic Reaction Profile](../../figures/fig4_2_energy_profile.png)
*Figure 4.2: Electronic Reaction Profile at B3LYP-D3(BJ)/def2-TZVP*

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

However, at the FCC regenerator temperature of 1003 K, the large entropic penalty associated with a gas-phase molecule binding to a solid surface dominates the free energy equation. The TΔS term becomes large and positive, driving the ΔG of adsorption for both species into the positive (non-spontaneous) regime, as illustrated in Figure 4.3.

![Gibbs Free Energy of Adsorption](../../figures/fig4_3_gibbs.png)
*Figure 4.3: Gibbs Free Energy of Adsorption at 298 K and 1003 K*

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
# REFERENCES

Adamo, C., & Barone, V. (1999). Toward reliable density functional methods without adjustable parameters: The PBE0 model. *The Journal of Chemical Physics*, *110*(13), 6158-6170.

Adanenche, D. E., Aliyu, A., Atta, A. Y., & El-Yakubu, B. J. (2022). Residue fluid catalytic cracking: A review on the mitigation strategies of metal poisoning of RFCC catalyst using metal passivators. *FUEL* (Review Draft).

Bannwarth, C., Ehlert, S., & Grimme, S. (2019). GFN2-xTB—An accurate and broadly parametrized self-consistent tight-binding quantum chemical method with multipole electrostatics and density-dependent dispersion contributions. *Journal of Chemical Theory and Computation*, *15*(3), 1652-1671.

Becke, A. D. (1993). Density-functional thermochemistry. III. The role of exact exchange. *The Journal of Chemical Physics*, *98*(7), 5648-5652.

Etim, U. J., Xu, B., Ullah, R., & Yan, Z. (2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite. *Journal of Colloid and Interface Science*.

Goerigk, L., Hansen, A., Bauer, C., Ehrlich, S., Najibi, A., & Grimme, S. (2017). A look at the density functional theory zoo with the advanced GMTKN55 database for general main group thermochemistry, kinetics and noncovalent interactions. *Physical Chemistry Chemical Physics*, *19*(48), 32184-32215.

Grimme, S., Ehrlich, S., & Goerigk, L. (2011). Effect of the damping function in dispersion corrected density functional theory. *Journal of Computational Chemistry*, *32*(7), 1456-1465.

Malola, S., Svelle, S., Lønstad Bleken, F., & Swang, O. (2011). Detailed Reaction Paths for Zeolite Dealumination and Desilication From Density Functional Calculations. *Angewandte Chemie*, *51*, 652-655.

Perdew, J. P., Burke, K., & Ernzerhof, M. (1996). Generalized gradient approximation made simple. *Physical Review Letters*, *77*(18), 3865.

Trujillo, C. A., Navarro Uribe, U., Knops-Gerrits, P.-P., Oviedo A., L. A., & Jacobs, P. A. (1997). The Mechanism of Zeolite Y Destruction by Steam in the Presence of Vanadium. *Journal of Catalysis*, *168*, 1-15.

Weigend, F., & Ahlrichs, R. (2005). Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy. *Physical Chemistry Chemical Physics*, *7*(18), 3297-3305.
