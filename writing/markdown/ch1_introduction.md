# CHAPTER ONE

# INTRODUCTION

## 1.1 Background of the Study

Every day, fluid catalytic cracking (FCC) units in petroleum refineries around the world convert millions of barrels of heavy gas oil into the gasoline, diesel, and petrochemical feedstocks that sustain modern economies. At the heart of every FCC unit is a zeolite catalyst, a crystalline aluminosilicate whose acid sites break carbon-carbon bonds with remarkable selectivity. Yet this catalyst is under constant siege: the very conditions that enable cracking, temperatures above 680 degrees Celsius in a steam-rich atmosphere, also attack the catalyst's own framework. 

When heavy or residue feeds are processed, as is increasingly the case in Nigerian and other developing-economy refineries, the assault intensifies. Vanadium, present in the crude oil at concentrations of 1 to over 50 parts per million as organometallic complexes, deposits on the catalyst during cracking, oxidises to vanadium pentoxide (V₂O₅) in the regenerator, and then reacts with steam to form volatile vanadic acid (H₃VO₄). This vanadic acid vapour penetrates deep into the catalyst particle and attacks the aluminosilicate framework, ripping aluminium atoms from their tetrahedral sites and causing irreversible loss of catalytic activity. The phenomenon has been documented experimentally for over four decades. However, an ongoing debate exists in the literature: some researchers argue that steam alone (hydrothermal degradation) is the primary driver of dealumination at these high temperatures, while others assert that vanadium plays an indispensable catalytic role in accelerating the destruction. A detailed computational comparison of these two mechanisms is therefore highly desirable.

## 1.2 Statement of the Problem

Vanadium contamination of FCC catalysts is one of the most costly operational problems in petroleum refining, responsible for accelerated catalyst replacement, reduced product yields, and increased coke and gas make. Industrial countermeasures such as vanadium traps (basic metal oxide additives that immobilise vanadic acid) have been developed empirically, guided by macroscopic observations of crystallinity loss, unit cell contraction, and catalytic activity decline. However, these macroscopic measurements cannot fully reveal the elementary steps of the attack: which bond breaks first, what the transition states look like, how much energy is required to overcome each barrier, or precisely why vanadic acid might be so much more destructive than steam alone. Without a rigorous molecular-level comparison, the design of next-generation vanadium-tolerant catalysts and trapping additives relies heavily on trial and error.

Density functional theory (DFT), a quantum mechanical computational method, coupled with semi-empirical exploratory techniques like GFN2-xTB, can provide exactly this information by computing the energies and geometries of reactants, intermediates, transition states, and products along a proposed reaction pathway. While DFT has been applied successfully to study steam-induced dealumination of zeolites, comprehensive computational explorations explicitly comparing the energetics of the vanadic acid attack pathway against simple hydrothermal dealumination remain sparse.

## 1.3 Aim of the Study

The aim of this study is to investigate the elementary mechanism of vanadium-promoted dealumination of zeolite Y using computational chemistry techniques, and to compare the energetics of the vanadic acid attack pathway with those of steam hydrolysis under conditions representative of the FCC regenerator.

## 1.4 Objectives

The specific objectives of this study are to:

1. Construct a cluster model of the zeolite Y Bronsted acid site suitable for semi-empirical and DFT calculations.

2. Explore the conformational space and potential reaction pathways using the robust GFN2-xTB tight-binding method.

3. Map the stationary-point sequence (pre-reaction complex, intermediates, and product) for the dealumination of the cluster by vanadic acid (H₃VO₄).

4. Map the corresponding stationary-point sequence for dealumination by water (H₂O), as a steam hydrolysis baseline.

5. Optimise the geometries and compute the electronic energies of all stationary points at the B3LYP-D3(BJ)/def2-TZVP level of hybrid DFT.

6. Validate the computed energies using a second hybrid functional (PBE0-D3(BJ)/def2-TZVP).

7. Compute the Gibbs free energies of the key adsorption states at both standard conditions (298 K) and FCC regenerator temperature (1003 K, corresponding to 730 degrees Celsius).

8. Compare the adsorption strength, reaction energetics, and thermochemical profiles of the vanadic acid and steam pathways to draw mechanistic conclusions relevant to FCC catalyst deactivation.

## 1.5 Scope of the Study

This study focuses on the initial stages of dealumination at a single Bronsted acid site in the faujasite (FAU) framework, modelled as a four-T-site cluster (AlSi₄O₄H₁₃) terminated with hydrogen atoms. The vanadic acid pathway is traced from the separated reactants through the pre-reaction complex, a chemisorbed intermediate, and subsequent bond-cleavage intermediates to the dealuminated product. The steam baseline covers the same sequence for water.

The study is limited to the gas-phase cluster model and does not include periodic boundary conditions, solvent effects, or the influence of sodium or other cations. The reaction is studied at zero pressure; the thermochemistry is evaluated at the ideal-gas, rigid-rotor, harmonic-oscillator level at two temperatures (298 K and 1003 K). Transition-state barriers are reported where the saddle-point search converged to a stationary point with the correct mode character; where convergence was not achieved, the barrier is identified as a limitation and discussed accordingly.

## 1.6 Justification of the Study

This research is significant for three main reasons:

First, it contributes a detailed molecular-level description of the vanadic acid attack on zeolite Y, enhancing the computational catalysis literature alongside established experimental works such as those by Mitchell (1980), Pine (1990), Etim et al. (2015), and local Nigerian researchers like Adenenche et al. (2022) who have highlighted the challenges of heavy crude processing.

Second, it quantifies the thermodynamic advantage that vanadic acid holds over steam as a dealumination agent, providing a numerical target (the binding energy margin) that vanadium traps must overcome to protect the catalyst. This information can guide the rational design of trapping additives.

Third, it demonstrates the feasibility of applying modern, multi-tier computational workflows (GFN2-xTB followed by hybrid DFT) to industrially relevant catalyst deactivation problems. This highlights that significant mechanistic insights are accessible using a combination of local workstations and cloud resources.

## 1.7 Limitations

The following limitations apply to this study:

1. The cluster model (22 framework atoms plus adsorbate) captures the local chemistry of a single acid site but does not reproduce the long-range electrostatic field, confinement effects, or pore curvature of the full FAU lattice. Adsorption energies may differ from periodic values by 10 to 20 kJ/mol.

2. The hydrogen termination of dangling bonds at the cluster boundary introduces a small artificial flexibility that is not present in the actual framework. This was mitigated by constraining the terminal hydrogen positions during optimisation.

3. Transition-state searches for three of the four proposed saddle points (the initial chemisorption barrier, the final Al-O cleavage, and the steam hydrolysis barrier) did not converge to clean first-order saddle points at the B3LYP-D3(BJ)/def2-TZVP level within the available computational budget. The activation barriers for these steps are therefore not reported as validated values, and the mechanistic discussion is based on the electronic energies of the stationary points that were successfully optimised.

4. The thermochemistry uses the ideal-gas, rigid-rotor, harmonic-oscillator approximation, which may overestimate the entropy of adsorption for large adsorbates on solid surfaces.
