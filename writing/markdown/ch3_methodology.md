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
