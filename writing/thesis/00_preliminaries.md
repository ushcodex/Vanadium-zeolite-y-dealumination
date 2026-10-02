<!-- ========================================================================== -->
<!-- PRELIMINARY PAGES                                                          -->
<!-- In accordance with Ahmadu Bello University (ABU) Guidelines for Theses     -->
<!-- ========================================================================== -->

\pagenumbering{roman}

# TITLE PAGE

\begin{center}
**FIRST-PRINCIPLES INVESTIGATION OF VANADIC ACID-INDUCED DEALUMINATION IN ZEOLITE Y UNDER RESIDUE FLUID CATALYTIC CRACKING REGENERATION CONDITIONS**

\vspace{1.5cm}

**BY**

\vspace{1.5cm}

**USMAN SHEHU**  
**(U18CE1024)**

\vspace{1.5cm}

**A PROJECT REPORT SUBMITTED TO THE DEPARTMENT OF CHEMICAL ENGINEERING, FACULTY OF ENGINEERING, AHMADU BELLO UNIVERSITY, ZARIA, NIGERIA**

\vspace{1.0cm}

**IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF BACHELOR OF ENGINEERING (B.ENG.) IN CHEMICAL ENGINEERING**

\vspace{1.5cm}

**OCTOBER, 2026**
\end{center}

\newpage

# DECLARATION

I declare that this project report entitled **"FIRST-PRINCIPLES INVESTIGATION OF VANADIC ACID-INDUCED DEALUMINATION IN ZEOLITE Y UNDER RESIDUE FLUID CATALYTIC CRACKING REGENERATION CONDITIONS"** has been carried out by me in the Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, under the supervision of **Engr. Dr. A. Y. Atta** and **Prof. B. O. Aderemi**.

The information derived from the literature has been duly acknowledged in the text and a list of references provided. No part of this project report was previously presented for another degree or diploma at this or any other institution.


\vspace{2.0cm}

-------------------------------------------------- \hspace{2.0cm} ------------------------  
**Usman SHEHU** \hspace{6.5cm} **Date**  
(Student)

\newpage

# CERTIFICATION

This project report entitled **"FIRST-PRINCIPLES INVESTIGATION OF VANADIC ACID-INDUCED DEALUMINATION IN ZEOLITE Y UNDER RESIDUE FLUID CATALYTIC CRACKING REGENERATION CONDITIONS"** by **Usman SHEHU (U18CE1024)** meets the regulations governing the award of the degree of Bachelor of Engineering (B.Eng.) in Chemical Engineering of Ahmadu Bello University, Zaria, and is approved for its contribution to knowledge and literary presentation.


\vspace{1.5cm}

-------------------------------------------------- \hspace{2.0cm} ------------------------  
**Engr. Dr. A. Y. Atta** \hspace{5.5cm} **Date**  
(Project Supervisor)


\vspace{1.5cm}

-------------------------------------------------- \hspace{2.0cm} ------------------------  
**Prof. B. O. Aderemi** \hspace{5.8cm} **Date**  
(Co-Supervisor)


\vspace{1.5cm}

-------------------------------------------------- \hspace{2.0cm} ------------------------  
**Prof. M. T. Isa** \hspace{6.7cm} **Date**  
(Head of Department)


\vspace{1.5cm}

-------------------------------------------------- \hspace{2.0cm} ------------------------  
**External Examiner** \hspace{6.0cm} **Date**  

\newpage

# DEDICATION

This work is dedicated to Almighty Allah, the Most Gracious, the Most Merciful, the source of all knowledge, wisdom, and understanding. 

It is also dedicated to my beloved parents for their endless prayers, sacrifices, and unconditional support throughout the journey of my education, and to all chemical engineers striving to advance the technological self-reliance and refining excellence of our nation, Nigeria.

\newpage

# ACKNOWLEDGEMENTS

My profound gratitude goes first to Almighty Allah for His divine guidance, strength, and protection throughout the course of this study.

I express my deepest appreciation and sincere gratitude to my supervisor, **Engr. Dr. A. Y. Atta**, and co-supervisor, **Prof. B. O. Aderemi**, for their invaluable guidance, constructive criticism, scholarly mentoring, and steadfast patience during the formulation and execution of this computational research. Their deep domain expertise in catalytic reaction engineering and zeolitic materials provided the essential foundation for this study.

I also wish to thank the Head of Department, **Prof. M. T. Isa**, and all academic and technical staff of the Department of Chemical Engineering, Ahmadu Bello University, Zaria, whose rigorous training and high standards have shaped my intellectual development. Special thanks are extended to the members of the Reaction Engineering and Catalysis Research Group for their insightful discussions and peer reviews.

My heartfelt thanks go to my family for their enduring sacrifices, moral encouragement, and faith in my aspirations. Finally, I appreciate my colleagues and friends in the Class of 2026 for their comradeship, shared moments of intellectual rigor, and mutual encouragement during our undergraduate years.

\newpage

# ABSTRACT

Vanadium poisoning represents the single most catastrophic chemical deactivation pathway threatening the structural integrity of zeolite Y catalysts in Residue Fluid Catalytic Cracking (RFCC) units. Under high-temperature oxidative regeneration (950–1050 K in the presence of steam), deposited vanadium accumulates on equilibrium catalyst particles and volatilizes into acidic vanadic acid ($H_3VO_4$), which aggressively hydrolyzes framework aluminium–oxygen bonds, triggering irreversible unit cell shrinkage, dealumination, and crystalline collapse. Despite four decades of empirical observation, the atomistic elementary reaction mechanism, site competition against steam, and electronic energetics of this attack have remained unresolved. 

This study presents a multi-tiered quantum chemical investigation elucidating the elementary mechanism of vanadic acid-induced dealumination on an active-site cluster model of faujasite zeolite Y ($AlSi_4O_4H_{13}$, 22 atoms) representing a single Brønsted acid hydroxyl site ($Si-O(H)-Al$). The reaction coordinate was systematically mapped across two multi-tier computational levels: semi-empirical GFN2-xTB for comprehensive potential energy surface exploratory scans and saddle-point searches (NEB and OptTS), refined by hybrid density functional theory with dispersion corrections (B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP) implemented in ORCA 6.1.1. 

Geometry optimization of the isolated reactants and active site confirms an undisturbed Brønsted hydroxyl $O-H$ bond length of 0.960 Å and bridging $Al-O$ distances of 1.685–1.696 Å, with the proton-bearing bridge elongated to 1.916 Å. At the Brønsted site, vanadic acid forms a stable pre-reactive adsorption complex ($V\text{-PRC}$) characterized by bifunctional coordination: direct hydrogen-bonding to the Brønsted proton and a direct dative contact between a vanadyl oxygen and framework aluminium ($Al\cdots O_{vanadyl} = 1.925$ Å). At the hybrid DFT level, vanadic acid binds with an adsorption energy of $\Delta E_{\text{ads}} = -92.78\text{ kJ/mol}$, outcompeting steam ($\Delta E_{\text{ads}} = -78.26\text{ kJ/mol}$) by a net competitive margin of $-14.52\text{ kJ/mol}$.

Along the dealumination pathway, the complex undergoes barrierless proton transfer to form a strongly chemisorbed tetrahedral intermediate ($V\text{-I1}$, $\Delta E = -385.10\text{ kJ/mol}$), in which framework aluminium remains 4-coordinate while vanadium establishes an $Al-O-V$ bridging linkage ($V-O = 1.774$ Å). The rate-limiting chemical step corresponds to the first framework $Al-O$ bond cleavage via transition state $V\text{-TS2}$ (verified by a single imaginary frequency at $-78.21\text{ cm}^{-1}$), overcoming a forward activation barrier of $+160.70\text{ kJ/mol}$ to yield a partially hydrolysed intermediate ($V\text{-I2}$, $\Delta E = -342.36\text{ kJ/mol}$) with a broken $Al-O$ distance of 2.511 Å. Subsequent bond scissions lead to an extracted extra-framework aluminium vanadate complex ($V\text{-P}$, $\Delta E = -82.90\text{ kJ/mol}$), establishing that the overall dealumination is highly exothermic. In contrast, steam-induced hydrolysis exhibits a lower adsorption affinity but an intrinsically lower barrier for initial $Al-O$ scission ($+29.29\text{ kJ/mol}$ at xTB; $+118.42\text{ to }+120.87\text{ kJ/mol}$ at hybrid DFT single-point benchmark), demonstrating that vanadic acid functions primarily by outcompeting steam for the catalytic Brønsted sites and trapping framework aluminium as stable extra-framework vanadate species. These findings provide an atomistic, thermodynamic foundation for designing selective, basic alkaline-earth/rare-earth metal passivators and optimizing regenerator operating parameters in Nigerian RFCC installations.

**Keywords:** Zeolite Y, Residue Fluid Catalytic Cracking, Vanadium Poisoning, Dealumination, Vanadic Acid, Density Functional Theory (DFT), ORCA, ABU Zaria.

\newpage

# TABLE OF CONTENTS

\begin{tabular}{l p{12cm} r}
**Content** & & **Page** \\
\hline
Title Page & \dotfill & i \\
Declaration & \dotfill & ii \\
Certification & \dotfill & iii \\
Dedication & \dotfill & iv \\
Acknowledgements & \dotfill & v \\
Abstract & \dotfill & vi \\
Table of Contents & \dotfill & vii \\
List of Tables & \dotfill & x \\
List of Figures & \dotfill & xi \\
List of Symbols and Abbreviations & \dotfill & xii \\
\hline
**CHAPTER ONE: INTRODUCTION** & & \\
1.1 Background to the Study & \dotfill & 1 \\
1.2 Statement of the Problem & \dotfill & 4 \\
1.3 Aim and Objectives of the Study & \dotfill & 6 \\
\hspace{0.5cm} 1.3.1 Aim & \dotfill & 6 \\
\hspace{0.5cm} 1.3.2 Objectives & \dotfill & 6 \\
1.4 Research Questions & \dotfill & 7 \\
1.5 Significance and Justification of the Study & \dotfill & 7 \\
1.6 Scope and Delimitations of the Study & \dotfill & 9 \\
1.7 Operational Definition of Terms & \dotfill & 10 \\
\hline
**CHAPTER TWO: LITERATURE REVIEW** & & \\
2.1 Energy, Crude Oil, and the Strategic Place of Refining & \dotfill & 12 \\
\hspace{0.5cm} 2.1.1 Global Energy Landscape and Liquid Hydrocarbons & \dotfill & 12 \\
\hspace{0.5cm} 2.1.2 Nigerian Refining Landscape and Transition to RFCC & \dotfill & 13 \\
2.2 Petroleum Chemistry and Crude Oil Residues & \dotfill & 15 \\
\hspace{0.5cm} 2.2.1 Hydrocarbon and Heteroatom Distributions & \dotfill & 15 \\
\hspace{0.5cm} 2.2.2 Heavy Residue Characterization and Metalloporphyrins & \dotfill & 16 \\
2.3 The Fluid Catalytic Cracking (FCC) Process & \dotfill & 18 \\
\hspace{0.5cm} 2.3.1 Process Flow and Reaction Chemistry & \dotfill & 18 \\
\hspace{0.5cm} 2.3.2 Riser-Regenerator Dynamics and Equilibrium Catalyst (Ecat) & \dotfill & 20 \\
2.4 Zeolite Y and FCC Catalyst Architecture & \dotfill & 22 \\
\hspace{0.5cm} 2.4.1 Faujasite Framework Structure and Brønsted Acidity & \dotfill & 22 \\
\hspace{0.5cm} 2.4.2 Ultra-Stable Y (USY) and Rare-Earth Y (REY) Modifications & \dotfill & 25 \\
2.5 Catalyst Deactivation Mechanisms in FCC/RFCC & \dotfill & 27 \\
\hspace{0.5cm} 2.5.1 Coking and Reversible Deactivation & \dotfill & 27 \\
\hspace{0.5cm} 2.5.2 Hydrothermal Dealumination by Steam & \dotfill & 28 \\
\hspace{0.5cm} 2.5.3 Contaminant Metals: Nickel vs. Vanadium Poisoning & \dotfill & 30 \\
2.6 Chemistry and Mobility of Vanadium in the Regenerator & \dotfill & 32 \\
\hspace{0.5cm} 2.6.1 Deposition, Oxidation, and Vanadic Acid ($H_3VO_4$) Volatilization & \dotfill & 32 \\
\hspace{0.5cm} 2.6.2 Intra-Particle and Inter-Particle Vanadium Mobility & \dotfill & 35 \\
2.7 Experimental Evidence on Vanadium Deactivation Mechanisms & \dotfill & 37 \\
\hspace{0.5cm} 2.7.1 The Acid Hydrolysis Hypothesis (Wormsbecher, Trujillo) & \dotfill & 37 \\
\hspace{0.5cm} 2.7.2 The Silanol Attack and Matrix Collapse Hypotheses (Pine, Occelli) & \dotfill & 39 \\
\hspace{0.5cm} 2.7.3 The Sodium-Vanadium Synergy and Fluxing Hypothesis (Xu) & \dotfill & 41 \\
\hspace{0.5cm} 2.7.4 Porosity Collapse and Structural Studies (Etim, Faghani) & \dotfill & 43 \\
2.8 Vanadium Passivation and Trapping Technologies & \dotfill & 45 \\
\hspace{0.5cm} 2.8.1 Basic Alkaline Earth and Rare-Earth Trapping Mechanisms & \dotfill & 45 \\
\hspace{0.5cm} 2.8.2 Industrial Trapping Strategies in Modern Refineries & \dotfill & 48 \\
2.9 Quantum Chemical and DFT Modeling in Zeolite Catalysis & \dotfill & 50 \\
\hspace{0.5cm} 2.9.1 Fundamentals of Density Functional Theory & \dotfill & 50 \\
\hspace{0.5cm} 2.9.2 Cluster Models vs. Periodic Boundary Conditions & \dotfill & 52 \\
\hspace{0.5cm} 2.9.3 Prior Computational Studies of Zeolite Dealumination & \dotfill & 54 \\
2.10 Nigerian Refining Experience and Local Research Heritage & \dotfill & 56 \\
\hspace{0.5cm} 2.10.1 Domestic Crude Assays and Metals Content & \dotfill & 56 \\
\hspace{0.5cm} 2.10.2 Catalysis and Clay Mineral Research at ABU Zaria & \dotfill & 58 \\
2.11 Summary of Knowledge Gaps and Positioning of this Study & \dotfill & 60 \\
\hline
**CHAPTER THREE: MATERIALS AND METHODS** & & \\
3.1 Research Design and Conceptual Framework & \dotfill & 62 \\
3.2 Molecular Model Systems & \dotfill & 64 \\
\hspace{0.5cm} 3.2.1 The Faujasite 22-Atom Active Site Cluster ($AlSi_4O_4H_{13}$) & \dotfill & 64 \\
\hspace{0.5cm} 3.2.2 Mobile Reactants: Orthovanadic Acid ($H_3VO_4$) and Steam ($H_2O$) & \dotfill & 66 \\
3.3 Computational Chemistry Software and Execution Platforms & \dotfill & 68 \\
3.4 Multi-Tier Computational Protocol & \dotfill & 70 \\
\hspace{0.5cm} 3.4.1 Tier 1: Semi-Empirical GFN2-xTB Exploratory Mapping & \dotfill & 70 \\
\hspace{0.5cm} 3.4.2 Tier 2: Hybrid DFT ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$) Optimizations & \dotfill & 72 \\
\hspace{0.5cm} 3.4.3 Tier 3: High-Level Single-Point Energy Benchmarking & \dotfill & 74 \\
3.5 Stationary Point Search and Transition State Verification Protocol & \dotfill & 76 \\
3.6 Energetic Formulations and Thermochemical Accounting & \dotfill & 78 \\
3.7 Calculation Register and Data Provenance Protocol & \dotfill & 80 \\
\hline
**CHAPTER FOUR: RESULTS AND DISCUSSION** & & \\
4.1 Geometric Features of Pristine Active Site and Adsorbate Models & \dotfill & 82 \\
4.2 Adsorption and Competitive Site Access: Vanadic Acid vs. Steam & \dotfill & 85 \\
4.3 Elementary Reaction Pathway of Vanadic Acid Dealumination & \dotfill & 89 \\
\hspace{0.5cm} 4.3.1 Pre-Reaction Complex ($V\text{-PRC}$) and Chemisorption ($V\text{-I1}$) & \dotfill & 89 \\
\hspace{0.5cm} 4.3.2 First Framework $Al-O$ Cleavage Transition State ($V\text{-TS2}$) & \dotfill & 92 \\
\hspace{0.5cm} 4.3.3 Partially Hydrolysed Intermediate ($V\text{-I2}$) and Product ($V\text{-P}$) & \dotfill & 95 \\
4.4 The Steam Dealumination Baseline and Benchmark Validation & \dotfill & 98 \\
4.5 Methodological Sensitivity and Level-of-Theory Comparisons & \dotfill & 102 \\
4.6 Coordination Evolution and Structural Mechanism of Extraction & \dotfill & 105 \\
4.7 Synthesis with Experimental Literature and Industrial Implications & \dotfill & 108 \\
\hline
**CHAPTER FIVE: CONCLUSIONS AND RECOMMENDATIONS** & & \\
5.1 Summary of Findings & \dotfill & 112 \\
5.2 Conclusions & \dotfill & 114 \\
5.3 Contributions to Knowledge & \dotfill & 115 \\
5.4 Recommendations for Industrial Refining Practice & \dotfill & 116 \\
5.5 Recommendations for Future Research & \dotfill & 117 \\
\hline
**REFERENCES** & \dotfill & 119 \\
**APPENDICES** & \dotfill & 135 \\
\hline
\end{tabular}

\newpage

# LIST OF TABLES

\begin{tabular}{l p{12cm} r}
**Table** & **Title** & **Page** \\
\hline
1.1 & Summary of specific research objectives, methodological tools, and outputs & 7 \\
2.1 & Design and operational capacities of Nigerian domestic petroleum refineries & 14 \\
2.2 & Heavy metals and physicochemical properties of selected Nigerian crude oils & 17 \\
2.3 & Comparison of conflicting experimental hypotheses on vanadium deactivation & 44 \\
2.4 & Industrial vanadium passivators, chemical formulations, and trapping mechanisms & 49 \\
2.5 & Chronicle of zeolitic and clay catalysis research contributions from ABU Zaria & 59 \\
3.1 & Stoichiometric specifications and atom counts of all model stationary points & 67 \\
3.2 & Computational software environments, specifications, and hardware allocation & 69 \\
3.3 & Detailed parameterization of theoretical model chemistries across the three tiers & 75 \\
3.4 & The five-point formal saddle-point verification criteria (A1–A5) & 77 \\
4.1 & Equilibrium bond metrics of pristine cluster and isolated adsorbate models & 84 \\
4.2 & Adsorption energetics and competitive affinity margins across theoretical levels & 87 \\
4.3 & Electronic energies and relative thermodynamics along the vanadium pathway & 91 \\
4.4 & Summary of transition state searches, frequency verification, and barrier metrics & 94 \\
4.5 & Steam hydrolysis baseline thermodynamics and external benchmark comparison & 100 \\
4.6 & Functional sensitivity of stationary state relative energies ($B3LYP$ vs. $PBE0$) & 103 \\
4.7 & Geometric evolution of aluminium coordination environment during dealumination & 106 \\
\hline
\end{tabular}

\newpage

# LIST OF FIGURES

\begin{tabular}{l p{12cm} r}
**Figure** & **Title** & **Page** \\
\hline
2.1 & Simplified schematic flow diagram of an RFCC riser-regenerator system & 19 \\
2.2 & Crystallographic framework topology of faujasite zeolite Y showing sodalite cages & 23 \\
2.3 & Local chemical structure of the bridging Brønsted acid hydroxyl site ($Si-O(H)-Al$) & 24 \\
2.4 & Schematic illustration of vanadium migration and equilibrium catalyst poisoning & 34 \\
2.5 & Proposed conceptual pathways for vanadium-induced lattice destruction & 42 \\
2.6 & Heavy metal assay trends (vanadium vs. nickel) in commercial Nigerian crudes & 57 \\
3.1 & Structural representation of the 22-atom $AlSi_4O_4H_{13}$ faujasite active site cluster & 65 \\
3.2 & Ball-and-stick representations of mobile gas-phase $H_3VO_4$ and $H_2O$ reactants & 66 \\
3.3 & Schematic multi-tier computational workflow adopted for the investigation & 71 \\
4.1 & Comparative adsorption energies of vanadic acid and steam at the Brønsted site & 88 \\
4.2 & Potential energy surface profile of the complete vanadium dealumination pathway & 96 \\
4.3 & Evolution of $Al-O$ and $Al\cdots V$ interatomic distances along the reaction coordinate & 107 \\
\hline
\end{tabular}

\newpage

# LIST OF SYMBOLS AND ABBREVIATIONS

\begin{tabular}{ll}
**ABU** & Ahmadu Bello University, Zaria, Nigeria \\
**API** & American Petroleum Institute gravity \\
**B3LYP** & Becke, 3-parameter, Lee-Yang-Parr hybrid exchange-correlation functional \\
**BSSE** & Basis Set Superposition Error \\
**CI-NEB** & Climbing Image Nudged Elastic Band \\
**CP** & Counterpoise correction \\
**DFT** & Density Functional Theory \\
**D3(BJ)** & Grimme third-generation empirical dispersion with Becke-Johnson damping \\
**Ecat** & Equilibrium Catalyst \\
**EFAL** & Extra-Framework Aluminium \\
**FAU** & Faujasite framework topological type \\
**FCC** & Fluid Catalytic Cracking \\
**GFN2-xTB** & Geometry, Frequency, Noncovalent Tight-Binding semi-empirical method (v2) \\
**HPC** & High-Performance Computing \\
**IRC** & Intrinsic Reaction Coordinate \\
**KRPC** & Kaduna Refining and Petrochemical Company \\
**NEB** & Nudged Elastic Band \\
**NMR** & Nuclear Magnetic Resonance \\
**OptTS** & Geometry Optimization to a Transition State \\
**ORCA** & Quantum chemistry program package \\
**PBE0** & Perdew-Burke-Ernzerhof 1-parameter hybrid exchange-correlation functional \\
**PHRC** & Port Harcourt Refining Company \\
**PRC** & Pre-Reaction Complex \\
**RE** & Rare Earth element (e.g., Lanthanum, Cerium) \\
**REY** & Rare-Earth-exchanged Zeolite Y \\
**RFCC** & Residue Fluid Catalytic Cracking \\
**RIJCOSX** & Resolution of Identity for Coulomb and Chain of Spheres for HF Exchange \\
**SCF** & Self-Consistent Field \\
**SOSCF** & Second-Order Self-Consistent Field convergence acceleration \\
**T1, T2, T3** & Computational Tiers 1, 2, and 3 \\
**TOC** & Table of Contents \\
**TS** & Transition State / Saddle Point \\
**USY** & Ultra-Stable Y Zeolite \\
**V-I1, V-I2** & Vanadium pathway intermediates 1 and 2 \\
**V-P** & Vanadium dealumination product complex \\
**V-PRC** & Vanadic acid pre-reaction complex \\
**V-TS2** & Vanadium pathway transition state 2 \\
**VESTA** & Visualization for Electronic and Structural Analysis \\
**W-P** & Water (steam) dealumination product complex \\
**W-PRC** & Water pre-reaction complex \\
**W-TS** & Water (steam) dealumination transition state \\
**WRPC** & Warri Refining and Petrochemical Company \\
**XRD** & X-ray Powder Diffraction \\
\end{tabular}

\newpage
\pagenumbering{arabic}
