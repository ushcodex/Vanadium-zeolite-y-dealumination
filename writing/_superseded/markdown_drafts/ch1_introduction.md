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
