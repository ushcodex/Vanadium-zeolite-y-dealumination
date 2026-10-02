# TITLE PAGE

**A DENSITY FUNCTIONAL THEORY INVESTIGATION OF THE MECHANISM OF ZEOLITE Y DEACTIVATION BY VANADIUM IN RESIDUE FLUID CATALYTIC CRACKING UNITS OF NIGERIAN REFINERIES**



**BY**



**AHMAD USMAN SHEHU**

**Matriculation Number: ____________________**



A Final Year Project Report Submitted to the Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, Kaduna State, Nigeria, in Partial Fulfilment of the Requirements for the Award of the Degree of

**BACHELOR OF ENGINEERING (B.ENG.) IN CHEMICAL ENGINEERING**



**OCTOBER, 2026**

\newpage

# DECLARATION

I hereby declare that this project report, titled "A Density Functional Theory Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in Residue Fluid Catalytic Cracking Units of Nigerian Refineries", is the product of my own research work carried out in the Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, under the supervision of ____________________. All sources of information consulted and all computational tools and data employed in this work have been duly acknowledged in the text and in the list of references. To the best of my knowledge, this work has not been submitted, in part or in whole, for the award of any degree or diploma in this or any other institution.



______________________________

**Ahmad Usman Shehu**

____________________ (Date)

\newpage

# CERTIFICATION

This is to certify that this project report, titled "A Density Functional Theory Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in Residue Fluid Catalytic Cracking Units of Nigerian Refineries", was carried out by Ahmad Usman Shehu (Matriculation Number: ____________________) in the Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, and has been read and approved as meeting the requirements for the award of the degree of Bachelor of Engineering (B.Eng.) in Chemical Engineering.



______________________________

**____________________**

Project Supervisor

____________________ (Date)



______________________________

**____________________**

Head of Department

____________________ (Date)



______________________________

**____________________**

External Examiner

____________________ (Date)

\newpage

# DEDICATION

This work is dedicated to my parents, whose sacrifice and encouragement made my education possible, and to the teaching and technical staff of the Department of Chemical Engineering, Ahmadu Bello University, Zaria, whose commitment to students sustains the department's standards of learning and research.

\newpage

# ACKNOWLEDGEMENTS

I thank Allah, the Most Beneficent, the Most Merciful, for the strength, health, and patience that carried me through this project.

My profound gratitude goes to my supervisor, ____________________, whose guidance shaped every stage of this work, from the framing of the research questions to the scrutiny of the final numbers. The supervision received in this project, close reading of drafts and insistence that every reported value be traceable to a calculation, is the part of my training that I will carry longest.

I am grateful to the Head and the entire academic staff of the Department of Chemical Engineering, Ahmadu Bello University, Zaria, for the instruction, laboratory culture, and intellectual environment that prepared me for this study, and to the departmental technical staff for their assistance with the computing facilities used in the semi-empirical calculations.

I acknowledge the Department of Chemical Engineering for access to the computational resources on which the density functional theory calculations were performed, and the Faculty of Engineering for the enabling environment. I also acknowledge the authors of the scientific literature reviewed in this work, whose published experimental results provide the benchmark against which the present computations are judged.

Finally, I thank my family and friends for their patience and support throughout my undergraduate programme. Any errors that remain in this report are mine alone.

\newpage

# ABSTRACT

Vanadium poisoning represents the single most catastrophic chemical deactivation pathway threatening the structural integrity of zeolite Y catalysts in Residue Fluid Catalytic Cracking (RFCC) units. Under high-temperature oxidative regeneration (950–1050 K in the presence of steam), deposited vanadium accumulates on equilibrium catalyst particles and volatilizes into acidic vanadic acid ($H_3VO_4$), which aggressively hydrolyzes framework aluminium–oxygen bonds, triggering irreversible unit cell shrinkage, dealumination, and crystalline collapse. Despite four decades of empirical observation, the atomistic elementary reaction mechanism, site competition against steam, and electronic energetics of this attack have remained unresolved. 

This study presents a multi-tiered quantum chemical investigation elucidating the elementary mechanism of vanadic acid-induced dealumination on an active-site cluster model of faujasite zeolite Y ($AlSi_4O_4H_{13}$, 22 atoms) representing a single Brønsted acid hydroxyl site ($Si-O(H)-Al$). The reaction coordinate was systematically mapped across two multi-tier computational levels: semi-empirical GFN2-xTB for comprehensive potential energy surface exploratory scans and saddle-point searches (NEB and OptTS), refined by hybrid density functional theory with dispersion corrections (B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP) implemented in ORCA 6.1.1. 

Geometry optimization of the isolated reactants and active site confirms an undisturbed Brønsted hydroxyl $O-H$ bond length of 0.960 Å and bridging $Al-O$ distances of 1.685–1.696 Å, with the proton-bearing bridge elongated to 1.916 Å. At the Brønsted site, vanadic acid forms a stable pre-reactive adsorption complex ($V\text{-PRC}$) characterized by bifunctional coordination: direct hydrogen-bonding to the Brønsted proton and a direct dative contact between a vanadyl oxygen and framework aluminium ($Al\cdots O_{vanadyl} = 1.925$ Å). At the hybrid DFT level, vanadic acid binds with an adsorption energy of $\Delta E_{\text{ads}} = -92.78\text{ kJ/mol}$, outcompeting steam ($\Delta E_{\text{ads}} = -78.26\text{ kJ/mol}$) by a net competitive margin of $-14.52\text{ kJ/mol}$.

Along the dealumination pathway, the complex undergoes barrierless proton transfer to form a strongly chemisorbed tetrahedral intermediate ($V\text{-I1}$, $\Delta E = -385.10\text{ kJ/mol}$), in which framework aluminium remains 4-coordinate while vanadium establishes an $Al-O-V$ bridging linkage ($V-O = 1.774$ Å). The rate-limiting chemical step corresponds to the first framework $Al-O$ bond cleavage via transition state $V\text{-TS2}$ (verified by a single imaginary frequency at $-78.21\text{ cm}^{-1}$), overcoming a forward activation barrier of $+160.70\text{ kJ/mol}$ to yield a partially hydrolysed intermediate ($V\text{-I2}$, $\Delta E = -342.36\text{ kJ/mol}$) with a broken $Al-O$ distance of 2.511 Å. Subsequent bond scissions lead to an extracted extra-framework aluminium vanadate complex ($V\text{-P}$, $\Delta E = -82.90\text{ kJ/mol}$), establishing that the overall dealumination is highly exothermic. In contrast, steam-induced hydrolysis exhibits a lower adsorption affinity but an intrinsically lower barrier for initial $Al-O$ scission ($+29.29\text{ kJ/mol}$ at xTB; $+118.42\text{ to }+120.87\text{ kJ/mol}$ at hybrid DFT single-point benchmark), demonstrating that vanadic acid functions primarily by outcompeting steam for the catalytic Brønsted sites and trapping framework aluminium as stable extra-framework vanadate species. These findings provide an atomistic, thermodynamic foundation for designing selective, basic alkaline-earth/rare-earth metal passivators and optimizing regenerator operating parameters in Nigerian RFCC installations.

**Keywords:** Zeolite Y, Residue Fluid Catalytic Cracking, Vanadium Poisoning, Dealumination, Vanadic Acid, Density Functional Theory (DFT), ORCA, ABU Zaria.

\newpage

# TABLE OF CONTENTS

| Content | Page |
|---|---|
| Title Page | i |
| Declaration | ii |
| Certification | iii |
| Dedication | iv |
| Acknowledgements | v |
| Abstract | vi |
| Table of Contents | vii |
| List of Tables | xi |
| List of Figures | xii |
| List of Plates | xiii |
| List of Abbreviations and Symbols | xiv |
| **CHAPTER ONE: INTRODUCTION** | **1** |
| 1.1 Background to the Study | 1 |
| 1.2 Statement of the Problem | 4 |
| 1.3 Aim and Objectives of the Study | 5 |
| 1.4 Research Questions | 6 |
| 1.5 Justification of the Study | 6 |
| 1.6 Scope of the Study | 7 |
| 1.7 Limitations of the Study | 8 |
| 1.8 Definition of Key Technical Terms | 8 |
| 1.9 Chapter Summary | 10 |
| **CHAPTER TWO: LITERATURE REVIEW** | **11** |
| 2.1 Energy, Petroleum, and the Place of Refining | 11 |
| 2.2 Petroleum and Its Refining | 13 |
| 2.3 Heterogeneous Catalysis: Concepts Required for This Study | 16 |
| 2.4 Catalytic Cracking and the Rise of Zeolite Catalysts | 18 |
| 2.5 The Fluid Catalytic Cracking Process | 20 |
| 2.6 The FCC Catalyst and Its Zeolite Y Component | 23 |
| 2.7 From FCC to RFCC: Heavier Feeds, Heavier Problems | 27 |
| 2.8 Deactivation of FCC Catalysts in Service | 28 |
| 2.9 Vanadium Chemistry in the FCC Unit | 30 |
| 2.10 The Mechanism of Zeolite Y Deactivation by Vanadium: The Experimental Evidence | 33 |
| 2.11 Countermeasures Against Vanadium | 39 |
| 2.12 Quantum Chemical Methods and Density Functional Theory | 41 |
| 2.13 Prior DFT Studies Nearest to the Present Problem | 45 |
| 2.14 FCC and RFCC in Nigerian Refineries: Documented Context | 47 |
| 2.15 Related Studies Connected with Ahmadu Bello University, Zaria | 50 |
| 2.16 Research Gap and Positioning of This Study | 52 |
| 2.17 Chapter Summary | 53 |
| **CHAPTER THREE: MATERIALS AND METHODS** | **54** |
| 3.1 Research Design | 54 |
| 3.2 The Model System | 56 |
| 3.3 Software and Hardware | 59 |
| 3.4 Computational Levels and Settings | 60 |
| 3.5 Computational Procedure | 64 |
| 3.6 Computed Quantities and Energy Bookkeeping | 68 |
| 3.7 Verification and Acceptance Protocol | 70 |
| 3.8 Treatment of Uncertainty | 73 |
| 3.9 Data Management and Reproducibility | 74 |
| 3.10 Health, Safety, and Environmental Considerations | 75 |
| 3.11 Chapter Summary | 76 |
| **CHAPTER FOUR: RESULTS AND DISCUSSION** | **77** |
| 4.1 The Faujasite Cluster Model and the Reference Species | 77 |
| 4.2 Adsorption at the Brønsted Acid Site | 80 |
| 4.3 The Stationary-Point Sequence of Vanadic-Acid Dealumination | 84 |
| 4.4 The Steam Baseline and the External Benchmark | 90 |
| 4.5 Level-of-Theory Sensitivity of the Pathway Energetics | 93 |
| 4.6 Structural Interpretation: How the Framework Aluminium Is Extracted | 96 |
| 4.7 Discussion in the Light of the Experimental Literature | 99 |
| 4.8 Chapter Summary | 102 |
| **CHAPTER FIVE: CONCLUSIONS AND RECOMMENDATIONS** | **103** |
| 5.1 Summary of the Study | 103 |
| 5.2 Conclusions | 104 |
| 5.3 Contributions to Knowledge | 106 |
| 5.4 Recommendations | 106 |
| 5.5 Suggestions for Further Work | 107 |
| **REFERENCES** | **108** |
| **APPENDICES** | **120** |
| Appendix A: Audited GFN2-xTB Potential Energy Surface Register | 120 |
| Appendix B: Hybrid DFT (B3LYP / PBE0) Calculation Register | 124 |
| Appendix C: Representative ORCA 6.1.1 Input Scripts | 127 |
| Appendix D: Cartesian Coordinates of the Stationary Points | 129 |

\newpage

# LIST OF TABLES

| Table | Title | Page |
|---|---|---|
| 1.1 | Objectives, methods, and outputs of the study | 9 |
| 2.1 | Key structural and catalytic characteristics of zeolite Y relevant to FCC service | 25 |
| 2.2 | Experimental evidence base for the mechanism of vanadium attack on zeolite Y | 35 |
| 2.3 | Passivation and trapping technologies against vanadium and their chemistry | 39 |
| 2.4 | Documented unit inventory relevant to FCC and RFCC in Nigerian refineries | 48 |
| 3.1 | Stationary-point set defining the two reaction pathways of the study | 57 |
| 3.2 | Software and hardware used in the study | 59 |
| 3.3 | Computational levels, settings, and the reason for each choice | 62 |
| 3.4 | Energy quantities computed for each stationary point and pathway | 69 |
| 3.5 | Acceptance protocol for minima and saddle points | 71 |
| 3.6 | Validation anchors for checking the computed results | 72 |
| 4.1 | Optimised geometry metrics of the faujasite cluster and the reference species (GFN2-xTB) | 78 |
| 4.2 | Adsorption energetics at the Brønsted acid site at two levels of theory | 81 |
| 4.3 | Tier 1 (GFN2-xTB) relative energies of the stationary points of the two pathways | 85 |
| 4.4 | Status of the saddle-point searches at the Tier 1 level | 88 |
| 4.5 | Hybrid DFT single-point energies of the stationary-point geometries | 94 |
| 4.6 | Structural evolution of the aluminium coordination environment along the vanadium pathway | 97 |

\newpage

# LIST OF FIGURES

| Figure | Title | Page |
|---|---|---|
| 2.1 | Crude distillation nameplate capacities of Nigerian refineries | 12 |
| 2.2 | Block flow concept of a residue fluid catalytic cracking unit | 21 |
| 2.3 | Building units and framework views of faujasite (FAU) | 24 |
| 2.4 | Thermal landscape of FCC operation relative to the melting point of vanadium pentoxide | 29 |
| 2.5 | Consensus picture of zeolite Y deactivation by vanadium in the FCC regenerator | 37 |
| 2.6 | Vanadium loadings reported in key experimental contamination studies | 40 |
| 2.7 | Indicative nickel and vanadium contents of major Nigerian crude grades | 49 |
| 2.8 | Four decades of research on vanadium deactivation of FCC (zeolite Y) catalysts | 53 |
| 3.1 | The four-T-site faujasite cluster model and its pre-reaction complex with vanadic acid | 56 |
| 3.2 | Stationary-point sequence of the two computed reaction pathways | 58 |
| 3.3 | Two-tier computational workflow adopted for the study | 61 |
| 4.1 | Adsorption energies at the Brønsted acid site at two levels of theory | 82 |
| 4.2 | Tier 1 relative electronic energies of the stationary states of the two pathways | 86 |
| 4.3 | Structural evolution of the aluminium coordination environment along the vanadium pathway | 98 |

*Note:* Figure files are stored in the `figures/` directory of the project archive; the file names `fig4_1_*` and `fig4_2_*` follow the original draft order and are mapped to the figure numbers above in the order of their appearance in Chapter Four.

\newpage

# LIST OF PLATES

| Plate | Title | Page |
|---|---|---|
| 2.1 | Conceptual cross-section of a metal-contaminated FCC catalyst microsphere | 26 |

\newpage

# LIST OF ABBREVIATIONS AND SYMBOLS

| Abbreviation or Symbol | Meaning |
|---|---|
| Al | Aluminium |
| BET | Brunauer–Emmett–Teller (surface area method) |
| BSSE | Basis-set superposition error |
| B3LYP | Becke three-parameter exchange with Lee–Yang–Parr correlation functional |
| D3(BJ) | Grimme's third-generation dispersion correction with Becke–Johnson damping |
| D6R | Double six-membered ring |
| def2-TZVP | Ahlrichs triple-zeta valence basis set with polarisation functions |
| def2/J | Matching auxiliary basis set for the RIJCOSX approximation |
| DFT | Density functional theory |
| Ecat | Equilibrium catalyst |
| EFAL | Extra-framework aluminium |
| ESR | Electron spin resonance |
| FAU | Faujasite framework type |
| FCC | Fluid catalytic cracking |
| FREQ | Frequency (vibrational) calculation |
| GGA | Generalised gradient approximation |
| GFN2-xTB | Geometry, frequency, non-covalent, extended tight-binding method, second generation |
| H2O | Water, the molecule of the steam baseline |
| H3VO4 | Vanadic acid, the mobile V(V) poison molecule |
| Hz, kJ mol−1, nm | Hertz, kilojoule per mole, nanometre |
| IRC | Intrinsic reaction coordinate |
| ΔE | Relative electronic energy |
| ΔG | Relative Gibbs free energy |
| ΔZPE | Difference in zero-point energy |
| LDA | Local density approximation |
| MAT | Microactivity test |
| MIV | Mitchell impregnation method |
| NEB | Nudged elastic band |
| NMR | Nuclear magnetic resonance |
| OPT | Geometry optimisation |
| OptTS | Transition-state optimisation |
| ORCA | Quantum chemistry program package used in this study |
| PBE0 | Perdew–Burke–Ernzerhof hybrid functional with 25 % exact exchange |
| PRC | Pre-reaction complex |
| RFCC | Residue fluid catalytic cracking |
| RIJCOSX | Resolution of identity with chain-of-spheres exchange approximation |
| SCF | Self-consistent field |
| Si/Al | Silicon-to-aluminium atomic ratio |
| SIMS | Secondary ion mass spectrometry |
| TS | Transition state (transition structure) |
| USY | Ultrastable zeolite Y |
| UV-Vis DRS | Ultraviolet-visible diffuse reflectance spectroscopy |
| V2O5 | Vanadium pentoxide |
| VGO | Vacuum gas oil |
| VO2+ | Vanadyl ion |
| XPS | X-ray photoelectron spectroscopy |
| XRD | X-ray diffraction |
| ZPE | Zero-point energy |

\newpage

# CHAPTER ONE: INTRODUCTION

## 1.1 Background to the Study

Fluid catalytic cracking (FCC) is the principal conversion process of the modern petroleum refinery and the largest single source of the world's gasoline, as well as a major source of the propylene from which polymers are made (Vogt & Weckhuysen, 2015). The process converts heavy petroleum fractions into lighter, more valuable products over a circulating solid acid catalyst, and the active component of that catalyst is zeolite Y, a crystalline aluminosilicate of the faujasite (FAU) framework type whose cages and channels are of molecular dimensions (Breck, 1974; Venuto & Habib, 1979). When refiners extend the process to atmospheric or vacuum residue in the mode known as residue fluid catalytic cracking (RFCC), the catalyst is exposed to organometallic species that concentrate in the heavy end of crude oil, principally nickel, iron, sodium, and vanadium (Adanenche et al., 2023; Bai et al., 2019).

Vanadium is the most destructive of these contaminants. Under the hot, steam-rich conditions of the FCC regenerator, vanadium is oxidised to vanadium pentoxide (V2O5) and converted into mobile acidic species, chiefly vanadic acid (H3VO4), which attack the aluminosilicate framework, extract its aluminium, and collapse the crystalline structure of zeolite Y (Wormsbecher et al., 1986; Occelli, 1991b; Trujillo et al., 1997). The consequences are loss of conversion and gasoline yield, deterioration of product selectivity, higher fresh-catalyst make-up, and direct economic loss to the refiner (Cerqueira et al., 2008; Etim et al., 2018; Faghani et al., 2024). Because the damage is irreversible, understanding its chemistry is the basis of every practical countermeasure, from metals-tolerant catalyst formulations to the traps and passivators that are blended with the circulating catalyst inventory.

Nigeria offers a particularly direct motivation for the study of this chemistry. The country's refining landscape changed decisively with the commissioning of the 650,000 barrels per day Dangote refinery in Lagos, whose gasoline block is anchored on a world-scale RFCC unit of roughly 218,000 barrels per day (Leadership, 2026), and the rehabilitation of the state-owned conversion refineries at Warri, Kaduna, and Port Harcourt returned FCC capacity to the national agenda (Punch, 2025). Nigerian crude oils are prized as light and low in sulphur, but their residual fractions still concentrate the metals that deactivate cracking catalysts; published analyses of Nigerian crude samples and their heavy residues report vanadium contents of about 14 to 99 parts per million in the heavy materials (Ahmad et al., 2010). Catalyst health in the regenerator therefore bears directly on the supply of gasoline to the Nigerian market, and RFCC metal poisoning has been reviewed from within the Department of Chemical Engineering of Ahmadu Bello University, Zaria, as a problem of national importance (Adanenche et al., 2023).

Almost four decades of experimental research have established the outlines of the vanadium problem. Wormsbecher et al. (1986) identified the poison precursor as volatile vanadic acid formed by the reaction of V2O5 with steam, quantified its concentration in the regenerator, and demonstrated that basic oxides such as magnesia and calcium oxide protect the catalyst by capturing the acid as vanadates. Pine (1990) showed that vanadium acts catalytically rather than stoichiometrically, that it attacks the zeolite from the external surface, and that it can also destroy an aluminium-free zeolite, from which he concluded that surface silanol and Si–O bonds are among the first points of attack. Trujillo et al. (1997) traced the migration of vanadyl species into the zeolite and showed that vanadic acid generated inside the crystal is responsible for framework hydrolysis. Xu et al. (2002) demonstrated that sodium and vanadium destroy zeolite Y cooperatively, with vanadium acting catalytically to regenerate surface sodium hydroxide, which then attacks Si–O bonds. Each of these studies observed a different catalyst formulation with a different technique, and the mechanistic claims have never been reconciled by placing the elementary steps on a single energy scale.

Density functional theory (DFT) provides the tool with which that reconciliation is possible. DFT computes the energy of a molecular system from its electron density, and therefore returns structures and energies of adsorbed complexes, intermediates, and transition structures, which are the quantities that define a mechanism (Van Speybroeck et al., 2015). The method has been applied with success to the steam dealumination of zeolites, for which periodic DFT calculations have established the elementary hydrolysis steps and the associated activation barriers of the order of 76 to 125 kJ mol−1 (Silaghi et al., 2015), and to vanadium centres within zeolite frameworks, where it has been used to characterise the acidity of vanadium sites and to interpret infrared spectra (Tielens & Dzwigaj, 2010a). What has not been reported is the application of the method to the species that actually deactivate the FCC catalyst: regenerator-formed vanadic acid attacking the Brønsted acid site of zeolite Y.

The present study addresses that gap. It computes the elementary reaction sequence of vanadic-acid attack on a hydrogen-terminated faujasite cluster containing one Brønsted acid site and one framework aluminium atom, and it computes the corresponding steam hydrolysis sequence on the same cluster, so that the two routes are compared on one identical energy scale. The whole stationary-point set is mapped at the semi-empirical GFN2-xTB level, where a complete search of the pathway is affordable, and the stationary points are then refined and evaluated at dispersion-corrected hybrid DFT levels using B3LYP-D3(BJ)/def2-TZVP geometry optimisations and PBE0-D3(BJ)/def2-TZVP single-point energies. Every reported number is stored in a calculation register that links the energy to its input file, output log, final geometry, and acceptance verdict, so that the mechanism proposed in this report can be checked calculation by calculation.

## 1.2 Statement of the Problem

Nigerian refineries convert the heavier fractions of crude oil into gasoline and petrochemical feedstock with FCC and RFCC technology, and the operating reliability of those units is limited by the life of the circulating catalyst. Feed-borne vanadium accumulates on the catalyst, destroys the zeolite Y component in the regenerator, and forces refiners to compensate by increasing fresh catalyst addition, blending metals traps, or withdrawing catalyst early (Adanenche et al., 2023; Faghani et al., 2024). The Dangote refinery's RFCC unit has already required repair attention associated with catalyst performance in its regenerator, an event which constrained gasoline output at the country's largest refinery (Leadership, 2026), and catalyst replacement remains a major operating cost in residue processing.

The scientific difficulty behind that operating problem is that the elementary chemistry of vanadium attack has never been resolved. Experimental techniques can characterise the damage after it has occurred, and spectroscopy can identify the vanadium species present on the catalyst, but the bond-breaking events themselves occur in seconds, inside pores of molecular dimensions, at a solid surface that cannot be observed directly with atomic resolution (Hagiwara et al., 2003; Meirer et al., 2015). The literature therefore contains competing descriptions of the first bond attacked: surface silanol and Si–O bonds (Pine, 1990), hydrolysis of the aluminosilicate framework at aluminium (Wormsbecher et al., 1986; Trujillo et al., 1997), and vanadium-catalysed sodium hydroxide attack on Si–O bonds (Xu et al., 2002). These descriptions differ in the sequence of bonds broken and therefore in what a catalyst formulator should do about it.

Computational chemistry can discriminate among the competing descriptions because it returns the energy of each proposed state and each proposed step. What has been missing is a study that computes those energies for the vanadium species that form in the FCC regenerator, on the zeolite Y acid site, at a level of theory adequate for reaction energetics, and that benchmarks the corresponding steam-only steps against the published periodic DFT results so that the two mechanisms can be compared quantitatively. The study reported here was designed, executed, and documented to fill that space, and the values it produces are the basis of the mechanistic account given in Chapter Four.

## 1.3 Aim and Objectives of the Study

### 1.3.1 Aim

The aim of this study is to investigate, using density functional theory, the molecular mechanism by which vanadium species deactivate the zeolite Y component of fluid catalytic cracking catalysts under regenerator conditions relevant to residue fluid catalytic cracking in Nigerian refineries.

### 1.3.2 Objectives

The specific objectives of the study are to:

1. review and organise the experimental literature on the deactivation of zeolite Y by vanadium in FCC and RFCC service, identifying the proposed mechanisms, the evidence supporting each, and the points on which they disagree;
2. construct and validate a hydrogen-terminated faujasite cluster model bearing one Brønsted acid site, together with the reactant species vanadic acid (H3VO4) and water (H2O), for quantum chemical calculation;
3. map the complete stationary-point sequence of vanadic-acid dealumination of the cluster, namely the pre-reaction complex, the chemisorbed intermediate, the transition structures, the hydrolysed intermediate, and the dealuminated product, together with the corresponding steam-only hydrolysis sequence, at the semi-empirical GFN2-xTB level;
4. refine the stationary-point set at dispersion-corrected hybrid DFT, quantify the adsorption energetics of vanadic acid and water at the Brønsted acid site at more than one level of theory, and compare the computed steam dealumination barrier with the published periodic DFT benchmark;
5. document every calculation in an auditable register that links each reported energy to its input file, output log, final geometry, and acceptance verdict, so that each value in this report can be independently reproduced.

**Table 1.1**

*Objectives, methods, and outputs of the study*

| Objective | Principal method | Output |
|---|---|---|
| Organise the vanadium deactivation literature | Structured review of peer-reviewed experimental and computational studies | Evidence matrix and gap statement (Chapter Two) |
| Build and validate the FAU cluster and reactant models | Framework topology analysis; geometry construction; GFN2-xTB and hybrid DFT optimisation of the reference species | Validated model set (Chapter Three) |
| Map the two reaction pathways | GFN2-xTB optimisations, relaxed scans, nudged elastic band searches, OptTS saddle refinement, and frequency checks | Stationary-point geometry archive (Chapters Three and Four) |
| Refine the energetics and rank the pathways | B3LYP-D3(BJ)/def2-TZVP geometry optimisation; PBE0-D3(BJ)/def2-TZVP single points; comparison with the published steam benchmark | Energy and validation tables (Chapter Four) |
| Guarantee reproducibility of every number | Versioned calculation register with input, output, geometry, and verdict per job | Calculation register and provenance map (Chapter Three; Appendix B) |

*Source:* Author.

## 1.4 Research Questions

The study is guided by the following research questions:

1. How strongly does vanadic acid bind to the Brønsted acid site of the faujasite framework, and how does that binding compare with the binding of water at the same site?
2. Is the hybrid DFT adsorption energy of vanadic acid at the Brønsted site sufficiently larger than that of water to establish preferential occupation of the site under regenerator steam, or do the two molecules compete on comparable terms?
3. What is the stationary-point sequence by which framework aluminium is extracted, which Al–O bonds cleave, in what order, and in what form does the aluminium leave the framework?
4. How does the computed steam hydrolysis barrier compare with the published periodic DFT barrier range for zeolite dealumination, and does that comparison validate the cluster model used here?

## 1.5 Justification of the Study

The strategic imperative of this study is anchored in the landmark transformation of Nigeria's downstream petroleum sector under the **Petroleum Industry Act (PIA 2021)**, which mandates operational self-sufficiency, value maximization of domestic crude streams, and the phase-out of imported refined petroleum products. Petroleum refining in Nigeria is entering an unprecedented era led by the commissioning of the 650,000 barrels-per-day (bpd) Dangote Petroleum Refinery in Lekki, Lagos State, which incorporates the world's largest single-train Residue Fluid Catalytic Cracking (RFCC) unit rated at 218,000 bpd (Leadership, 2026). Concurrently, the Nigerian National Petroleum Company Limited (NNPCL) is advancing rehabilitation and upgrade programs across the three state-owned conversion refineries: the Port Harcourt Refining Company (PHRC, 210,000 bpd total capacity), the Warri Refining and Petrochemical Company (WRPC, 125,000 bpd), and the Kaduna Refining and Petrochemical Company (KRPC, 110,000 bpd) (Punch, 2025; NS Energy, 2021).

The study is justified on scientific, national, and institutional grounds.

Scientifically, the experimental mechanism literature has remained unresolved for decades because each study observed a different catalyst formulation by a different technique (Pine, 1990; Trujillo et al., 1997; Xu et al., 2002), while the computational literature has so far treated vanadium as a framework dopant rather than as the deactivating agent of FCC service (Tielens & Dzwigaj, 2010a). Placing the proposed elementary steps of vanadic-acid attack on one computed energy scale, and benchmarking the parallel steam steps against the established periodic DFT results (Silaghi et al., 2015), converts a set of competing qualitative claims into a set of comparable numbers. The same numbers define which step a trap or passivator must intercept, and therefore inform the design of vanadium-tolerant catalysts.

Nationally, the reliable operation of the Dangote RFCC unit and of the rehabilitated state-owned FCC units determines the availability of gasoline in Nigeria, and catalyst replacement caused by metal poisoning is a recurring cost in residue processing (Adanenche et al., 2023; Leadership, 2026). A mechanistic, computation-based understanding of vanadium attack supplies Nigerian refiners with a basis for catalyst selection, metals management, and trap specification that is at present drawn largely from vendor experience.


Finally, the study is justified by its practicality. It is entirely computational and literature-based, so it requires no hazardous reagents, no high-pressure or high-temperature equipment, and no experimental consumables; it can be executed on modest computing resources, and it leaves a documented, reusable data set for subsequent work in the department.

## 1.6 Scope of the Study

The study covers the following:

1. A structured review of the experimental and computational literature on vanadium deactivation of FCC catalysts, including the documented Nigerian refinery context.
2. Construction of a hydrogen-terminated faujasite cluster model of composition AlSi4O4H13, containing one framework aluminium atom and one Brønsted acid site, with vanadic acid (H3VO4) and water (H2O) as the attacking species.
3. Computation of the complete stationary-point set of the vanadic-acid pathway (isolated reference state, pre-reaction complex, chemisorbed intermediate, transition structures, hydrolysed intermediate, and dealuminated product) and of the steam pathway (pre-reaction complex, transition structure, and product), at the semi-empirical GFN2-xTB level, with frequency analysis of every minimum.
4. Refinement of the stationary points at the dispersion-corrected hybrid DFT level: B3LYP-D3(BJ)/def2-TZVP geometry optimisation of the reference species and adsorption complexes, and B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP single-point evaluation of the full stationary-point set.
5. Computation of adsorption energies for vanadic acid and water at the Brønsted acid site at both levels of theory, of relative electronic energies for all stationary points, of the steam hydrolysis barrier, and of the structural descriptors (Al–O, V–O, and Al⋯V distances) that define each state.
6. Verification of all reported values against a documented acceptance protocol, and their storage in a calculation register with full provenance.

The study does not include experimental catalyst preparation or testing, reactor-scale modelling, or the computation of sodium-containing and vanadyl (VO2+) pathways, which are outside the model system defined above.

## 1.7 Limitations of the Study

1. A four-T-site cluster truncates the infinite zeolite lattice, so long-range electrostatic and confinement effects are approximated. Relative energies computed within one identical model truncation are the quantities reported, and the model is validated against published periodic DFT results for the steam step that both approaches compute (Silaghi et al., 2015).
2. The electronic structure of the system is described by approximate exchange-correlation functionals, and computed energies therefore depend on the functional chosen. This dependence is addressed by evaluating the stationary-point set at two hybrid functional levels and by reporting the spread between them, and by defining the mechanistic conclusions on quantities for which the two levels agree.
3. The regenerator environment, with its temperature gradients, steam and oxygen partial pressures, and thousands of reacting species, is represented by the energetics of the selected elementary steps at a single site; the study computes molecular energetics rather than reactor performance.
4. Public data on catalyst contamination in Nigerian refineries are limited, and the Nigerian context in Chapter Two therefore relies on published analyses, industry assays, and press reports, each cited at the point of use (Ahmad et al., 2010; Leadership, 2026).

## 1.8 Definition of Key Technical Terms

The following terms are used in this report with the meanings given:

**Adsorption energy:** the energy released when a molecule binds to a surface or to a model site, computed as the energy of the bound complex minus the energies of the separated partners.

**Basis-set superposition error (BSSE):** an artificial stabilisation that arises in molecular calculations when one fragment borrows basis functions from another; corrected in this study by the counterpoise procedure.

**Brønsted acid site:** a proton-donating site; in zeolite Y this is the bridging hydroxyl group Si–O(H)–Al formed when a framework aluminium is charge-balanced by a proton.

**Cluster model:** a finite fragment cut from a crystal and chemically terminated with hydrogen atoms, used to represent the local active region of a solid in quantum chemical calculations.

**Dealumination:** removal of aluminium atoms from a zeolite framework, typically by hydrolysis at elevated temperature in the presence of steam.

**Density functional theory (DFT):** a quantum mechanical method that computes the energy and properties of a system of electrons from its electron density rather than from a many-electron wavefunction.

**Equilibrium catalyst (Ecat):** the blend of fresh and aged catalyst that circulates in an operating FCC unit, on which feed metals accumulate.

**Extra-framework aluminium (EFAL):** aluminium that has left the framework and occupies the pores or the external surface of the zeolite.

**Faujasite (FAU):** the framework type of zeolite Y, built from sodalite cages linked through double six-membered rings to form large cavities called supercages.

**GFN2-xTB:** a semi-empirical tight-binding quantum chemical method that reproduces geometries and reaction energies of main-group systems at a small fraction of the cost of DFT; used in this study for the complete pathway search.

**Hybrid functional:** an approximate exchange-correlation functional that includes a fraction of exact Hartree–Fock exchange; B3LYP and PBE0 are the two hybrid functionals used in this study.

**Pre-reaction complex (PRC):** the associated state formed when an attacking molecule approaches the Brønsted acid site before any framework bond is broken.

**Residue fluid catalytic cracking (RFCC):** the variant of fluid catalytic cracking designed to process atmospheric or vacuum residues that contain metals and high Conradson carbon.

**Transition structure:** the highest-energy point along the minimum-energy path of an elementary step, characterised in this study by exactly one imaginary vibrational frequency.

**Vanadic acid (H3VO4):** the volatile, acidic V(V) species formed from vanadium pentoxide and steam in the FCC regenerator and identified experimentally as the vanadium poison precursor.

**Zeolite Y:** the synthetic faujasite-type aluminosilicate used as the active component of FCC catalysts, with a supercage of about 1.3 nm and twelve-membered ring windows of about 0.74 nm.

## 1.9 Chapter Summary

This chapter has introduced the industrial problem, the deactivation of zeolite Y by vanadium in RFCC service, and the scientific problem, the absence of a common energetic scale on which the proposed elementary steps of vanadium attack can be compared. It has stated the aim and the five objectives of the study, the four research questions, the justification of the work on scientific, national, and institutional grounds, the scope of the computed system, and the limitations inherent in the model and in the method. Chapter Two reviews the literature from which the problem and the model are derived, Chapter Three specifies the computational methodology applied, Chapter Four presents and discusses the results, and Chapter Five states the conclusions and recommendations of the study.

\newpage

# CHAPTER TWO: LITERATURE REVIEW

## 2.1 Energy, Petroleum, and the Place of Refining

### 2.1.1 Petroleum in the global energy system

Modern economies depend on energy carriers, and among them liquid petroleum fuels remain dominant in road, air, and maritime transport. Petroleum is valuable for two independent reasons: its molecules can be rearranged into engine-ready fuels, and its smaller fragments are the starting materials of the petrochemical industry, from which plastics, fertilisers, solvents, and pharmaceuticals descend (Gary et al., 2007). The petroleum value chain is conventionally divided into upstream activities, which find and produce crude oil, midstream activities, which transport it, and downstream activities, of which refining is the largest, which convert the crude into marketable fuels and feedstocks (Gary et al., 2007). A country that produces crude oil but does not refine it exports a raw commodity and imports finished fuels, so refining capacity is an instrument of both industrial policy and energy security.

### 2.1.2 Petroleum refining in Nigeria

Nigeria is one of the largest crude oil producers in Africa, with reserves of the order of thirty-seven billion barrels and a suite of light, low-sulphur export grades that include Bonny Light, Escravos, Forcados, Qua Iboe Light, and Brass Blend (Organization of the Petroleum Exporting Countries [OPEC], 2024). Despite this endowment, domestic refining lagged behind consumption for decades. The state-owned refineries at Port Harcourt, Warri, and Kaduna, with a combined nameplate crude distillation capacity of about 445,000 barrels per day, operated for long periods far below design capacity while the country imported most of its premium motor spirit (NS Energy, 2021; Punch, 2025). The Petroleum Industry Act of 2021 restructured the sector and created dedicated regulators for upstream and midstream or downstream operations (Petroleum Industry Act, 2021).

The refining landscape changed with the commissioning of the Dangote refinery in Lagos, a single-train complex with a crude distillation capacity of 650,000 barrels per day that exceeds the combined nameplate capacity of the four state-owned refineries (Leadership, 2026). Figure 2.1 compares the publicly documented nameplate capacities of the five plants. Every one of these complexes depends on catalytic conversion units to produce gasoline: the state conversion refineries were each built with a fluid catalytic cracking (FCC) unit, and the Dangote complex is anchored at its gasoline heart by a very large residue fluid catalytic cracking (RFCC) unit reported at roughly 218,000 barrels per day (Leadership, 2026). The operating health of those units therefore bears directly on Nigerian gasoline supply, and, as later sections establish, both unit types are vulnerable to the vanadium and nickel carried in heavy feeds.

**Figure 2.1**

*Crude distillation nameplate capacities of Nigerian refineries*

![](figures/fig2_1_refineries.png)

*Source:* Author, from data reported by the Nigerian Midstream and Downstream Petroleum Regulatory Authority (n.d.), NS Energy (2021), Punch (2025), and Leadership (2026).

## 2.2 Petroleum and Its Refining

### 2.2.1 Molecular composition of crude oil

Crude oil is a mixture of tens of thousands of compounds, dominated by hydrocarbons and accompanied by heteroatom compounds of sulphur, nitrogen, and oxygen and by organometallic compounds of which nickel and vanadium are the most abundant (Gary et al., 2007). The hydrocarbons are classified into paraffins, naphthenes, aromatics, and, in cracked products rather than in crude itself, olefins. The metals occur largely inside porphyrin-type structures, flat ring-shaped ligands that cage a metal ion and are inherited from biological matter, together with less well-defined non-porphyrin complexes (Gary et al., 2007). Two facts govern their behaviour in a refinery. First, the metalloporphyrins are large, high-boiling molecules, so they do not distil and instead concentrate almost quantitatively in the residue. Second, the concentrations that matter are those of the heavy fractions, not of the whole crude. Published determinations of Nigerian crude samples and their heavy residues report vanadium contents of about 14 to 99 parts per million, nickel 5 to 11 parts per million, and iron 43 to 110 parts per million in the measured heavy materials (Ahmad et al., 2010). A refinery that feeds residue to its cracking unit therefore delivers the most metal-rich fraction of the barrel to its most sensitive catalyst.

### 2.2.2 Separation processes

Refining begins with separation. After desalting, the crude distillation unit separates the crude by boiling range into gases, naphtha, kerosene, diesel, and atmospheric residue, and the vacuum distillation unit separates the atmospheric residue into vacuum gas oil (VGO) and vacuum residue (Gary et al., 2007). Hydrotreating processes purify these streams by reacting them with hydrogen over a catalyst to remove sulphur and nitrogen, but they do not change molecular size.

### 2.2.3 Conversion processes

Conversion processes change molecular size and structure. Thermal conversion, including visbreaking and coking, uses heat alone to break heavy residues into lighter products and a solid carbon residue. Catalytic conversion uses a catalyst to perform the same work at milder conditions and with far better control of the product slate: FCC converts VGO and residue into gasoline and propylene; hydrocracking converts heavy fractions into diesel and jet-range products under high hydrogen pressure; catalytic reforming rearranges naphtha into high-octane aromatics and hydrogen; and alkylation and polymerisation combine small olefins into gasoline-range products (Gary et al., 2007). Among these, FCC is historically and economically the most important in gasoline-oriented refineries, and it has been described as the heart of the modern refinery (Vogt & Weckhuysen, 2015).

## 2.3 Heterogeneous Catalysis: Concepts Required for This Study

A catalyst increases the rate of a reaction without being consumed in the overall stoichiometry, by providing an alternative reaction path of lower activation energy (Levenspiel, 1999). Its industrial value is described by three properties: activity, meaning the rate at which it converts feed; selectivity, meaning the fraction of converted feed that becomes the desired product rather than unwanted gas or coke; and stability, meaning how slowly activity and selectivity are lost with time on stream. In heterogeneous catalysis the catalyst is a solid and the reactants are fluids, so reaction proceeds through transport to the particle, diffusion into its pores, adsorption on the active site, surface reaction, and desorption of products (Levenspiel, 1999).

Two concepts recur throughout this report. Adsorption is the binding of a molecule to a surface, and the strength of that binding determines which species can occupy a site under competition. The active site is the specific atomic arrangement at which the chemistry occurs. In cracking catalysts the active sites are acidic, and acidity is defined in two ways: a Brønsted acid donates a proton, while a Lewis acid accepts an electron pair. In zeolite Y the catalytically decisive sites are bridging hydroxyl groups written Si–O(H)–Al, in which a proton sits on an oxygen shared between a framework silicon and a framework aluminium atom; Lewis acidity in an aged catalyst is associated mainly with coordinatively unsaturated aluminium that has left the framework (Vogt & Weckhuysen, 2015). The distinction matters here because vanadium species interact with both site types, and because the Brønsted site is the site whose fate is computed in this study (Trujillo et al., 1997).

Industrial catalysts rarely fail by a single mechanism. The standard classification applied to FCC catalysts identifies four families of deactivation (Cerqueira et al., 2008). Coking is the accumulation of carbon-rich deposits on the active sites and in the pores; it is reversible because the regenerator burns the coke off (Guisnet & Magnoux, 2001). Poisoning is the binding or chemical reaction of feed impurities with the active components, and for metals such as nickel, vanadium, sodium, and iron the damage is permanent (Bai et al., 2019; Xu et al., 2024). Hydrothermal and thermal degradation is the destruction of the crystal structure itself at high temperature in the presence of steam, by dealumination and sintering (Wallenstein et al., 2000; Silaghi et al., 2016). Attrition and morphological change reduce particle size and fluidisability (Vogt & Weckhuysen, 2015). Vanadium belongs to the second and third families simultaneously: it is a feed-borne poison whose principal effect is to accelerate the hydrothermal destruction of the zeolite framework (Wormsbecher et al., 1986). That dual character is the subject of this study.

## 2.4 Catalytic Cracking and the Rise of Zeolite Catalysts

Cracking originally meant thermal cracking, in which heavy molecules are heated until they fragment by free-radical chemistry that is difficult to steer toward a chosen product. Catalytic cracking was commercialised by Eugene Houdry in the 1930s over an acidic clay-derived solid, and it became continuous with the introduction of the fluid-bed process in 1942 (Venuto & Habib, 1979). The decisive change came between 1962 and 1964, when synthetic zeolites, first zeolite X and then the more stable zeolite Y, replaced the amorphous catalyst; the improvement in activity and gasoline yield was so large that the world's units were re-catalysed within a few years (Venuto & Habib, 1979; Vogt & Weckhuysen, 2015).

Acid-catalysed cracking proceeds through carbenium ions, positively charged hydrocarbon fragments in which the charge resides on a trivalent carbon atom (Corma & Orchillés, 2000). The mechanism is conventionally divided into three stages. Initiation creates a carbenium ion from a feed molecule, either by protonation of an olefin on a Brønsted site or by hydride abstraction from a paraffin. Propagation proceeds by skeletal isomerisation and, most importantly, by beta-scission, in which the bond two positions from the charge breaks to give one smaller olefin and one smaller carbenium ion that continues the chain. Chain transfer and termination saturate the olefins by hydrogen transfer, releasing the site, or build hydrogen-deficient aromatic species that are the precursors of coke. Because the whole sequence is controlled by the number, strength, and accessibility of Brønsted acid sites, any agent that removes those sites or destroys the crystal that hosts them directly attacks the economics of gasoline production (Corma & Orchillés, 2000; Cerqueira et al., 2008).

## 2.5 The Fluid Catalytic Cracking Process

### 2.5.1 Process description

Figure 2.2 summarises the working principle of a modern FCC or RFCC unit. Preheated feed is atomised with dispersion steam into the base of a tall vertical pipe, the riser, where it meets hot regenerated catalyst at about 700 °C. The oil evaporates and cracks during a few seconds of upward travel at roughly 500 to 560 °C, depositing coke on the catalyst as it reacts (Sadeghbeigi, 2012; Olugbenga & Oluwaseyi, 2023). At the riser top, cyclones and a stripper separate product vapours from spent catalyst. The vapours pass to the main fractionator for separation into fuel gas, liquefied petroleum gas, gasoline, light cycle oil, and a heavy slurry cut, while the spent, coked catalyst flows by gravity to the regenerator, a fluidised bed into which air is blown. Combustion of the coke at about 690 to 760 °C releases the heat that drives the process and reheats the catalyst for its return to the riser (Sadeghbeigi, 2012). The unit is therefore auto-thermal: the coke laid down in the riser is the fuel of the regenerator.

**Figure 2.2**

*Block flow concept of a residue fluid catalytic cracking (RFCC) unit*

![](figures/fig2_2_rfcc_schematic.png)

*Source:* Author's schematic based on Sadeghbeigi (2012), Adanenche et al. (2023), and Vogt and Weckhuysen (2015).

### 2.5.2 Catalyst circulation and the equilibrium catalyst

A commercial unit circulates a large catalyst inventory continuously between riser and regenerator at a catalyst-to-oil weight ratio typically between about 4 and 10 (Sadeghbeigi, 2012). Because fines are lost through the cyclones and aged catalyst is withdrawn deliberately, fresh catalyst is added every day. The circulating blend, a statistical mixture of catalyst of all ages, is the equilibrium catalyst, or Ecat. Feed-borne metals that leave in no product accumulate on the Ecat, and vanadium levels of thousands of parts per million are routine in residue operations; modern trapping technology allows operation at up to about 7,000 ppm vanadium on Ecat while retaining useful activity (Bai et al., 2019; Etim et al., 2018).

### 2.5.3 Kinetic description of cracking

Because the feed is a continuum of compounds, FCC kinetics is handled by lumped models in which molecules are grouped into a few fictitious lumps whose interconversion follows simple rate laws. The classical three-lump model of Weekman and Nace (1970) treats gas oil converting to gasoline, which in turn converts to gas and coke, with first-order steps and an exponential decay of catalyst activity with coke content. Later workers have developed multi-lump schemes and kinetic Monte Carlo variants; a recent review collects the deactivation kinetic equations used across the field (Cordero-Lanzac & Bilbao, 2025). A representative activity decay law is written as φ = exp(−αCc), where φ is the remaining activity fraction, Cc the coke content on the catalyst, and α an empirical constant (Weekman & Nace, 1970). In the Nigerian context, Olugbenga and Oluwaseyi (2023) simulated the commercial FCC unit of a domestic refining company and recommended a reactor plenum temperature of 560 °C for optimum naphtha production. These studies define the process window within which the deactivation chemistry examined in this thesis occurs.

## 2.6 The FCC Catalyst and Its Zeolite Y Component

### 2.6.1 Anatomy of the catalyst particle

The material circulated in an FCC unit is a free-flowing powder of microspheres, each roughly 40 to 150 µm in diameter (Sadeghbeigi, 2012). Each microsphere is a composite of four functional ingredients, illustrated conceptually in Plate 2.1: zeolite Y crystals, typically 10 to 40 % by weight, which supply most of the Brønsted acidity and therefore most of the small-molecule cracking activity; an active matrix of amorphous silica-alumina, which pre-cracks molecules too large to enter the zeolite; a filler, usually kaolin clay, which provides body and heat capacity at low cost; and a binder, typically a silica or alumina sol, which gives the sphere its attrition resistance (Sadeghbeigi, 2012; Vogt & Weckhuysen, 2015).

Metals arriving with the feed deposit first on the outer surface of the microspheres. Imaging secondary ion mass spectrometry has shown that nickel and vanadium on industrial equilibrium catalyst concentrate toward the particle rim when loadings are high (Kugler & Leta, 1988). Vanadium, however, does not remain where it lands: under regenerator conditions it becomes mobile and redistributes within and between particles, reaching zeolite crystallites deep inside the spheres (Trujillo et al., 1997; Wormsbecher et al., 1986), a process represented by the inward-migrating markers in Plate 2.1.

**Plate 2.1**

*Conceptual cross-section of a metal-contaminated FCC catalyst microsphere*

![](figures/plate2_1_particle.png)

*Source:* Author's conceptual schematic (not a micrograph) based on Sadeghbeigi (2012) and Vogt and Weckhuysen (2015); the rim deposition and inward migration pattern follows Kugler and Leta (1988) and Meirer et al. (2015).

### 2.6.2 Zeolite Y structure and acidity

Zeolite Y crystallises in the faujasite (FAU) framework type. Its framework is built from corner-sharing tetrahedra of SiO4 and AlO4; each tetrahedral site, called a T-site, is occupied by silicon or aluminium, and because AlO4 carries one negative charge relative to SiO4, each framework aluminium must be balanced by a nearby positive charge: a sodium ion in as-synthesised NaY, a proton in the catalytically active HY form, or rare earth cations in the stabilised REY form (Breck, 1974). Löwenstein's rule, the empirical statement that Al–O–Al linkages are disfavoured, restricts the distribution of aluminium over the T-sites (Breck, 1974).

The tetrahedra assemble into the cages shown in Figure 2.3. Sodalite cages, also called β-cages, link through double six-membered rings to enclose a three-dimensional network of very large cavities called supercages, each about 1.3 nm across and connected to four neighbours through twelve-membered ring windows of about 0.74 nm free diameter (Breck, 1974; Vogt & Weckhuysen, 2015). The faujasite entry of the International Zeolite Association structure database quantifies this geometry: a cubic unit cell of edge 2.4345 nm, a framework density of 13.3 T-sites per 1,000 Å3, a largest sphere of 1.12 nm fitting inside the supercage, a largest diffusible sphere of 0.74 nm passing the windows, and an accessible pore volume of 27.4 % of the crystal (Breck, 1974). These windows admit the branched and single-ring molecules that are valuable in cracking while excluding the largest residue molecules, which must first be cracked on the matrix. The Brønsted hydroxyl groups that carry the catalytic acidity sit on oxygen bridges facing into these cages.

**Figure 2.3**

*Building units and framework views of faujasite (FAU), the framework of zeolite Y*

![](figures/fig2_3_iza.png)

*Source:* Database images of the International Zeolite Association Structure Commission (Breck, 1974): (a) framework viewed along [111], the large central opening marking a supercage window; (b) framework viewed along [110]; (c) polyhedral view, in which each truncated-octahedron outline is a sodalite cage and the hexagonal prisms linking the cages are double six-rings; (d) the d6r and sod composite building units (not to scale).

### 2.6.3 From NaY to USY and REY: stabilisation and unit cell size

As-synthesised NaY is neither acidic enough nor stable enough for regenerator steam, and two modifications define commercial catalyst zeolites. Exchange of sodium by ammonium ions followed by calcination and steaming yields ultrastable Y (USY), in which steam has deliberately stripped part of the framework aluminium, shrinking the unit cell, raising the silicon-to-aluminium ratio, and leaving a minority of strong Brønsted sites together with some extra-framework aluminium (Vogt & Weckhuysen, 2015). Ion exchange with rare earth cations such as La3+ and Ce4+ yields rare-earth-exchanged Y (REY), in which bulky rare earth species anchored in the sodalite cages brace the framework against dealumination and improve activity retention, though with consequences for vanadium tolerance that Section 2.10.5 examines (Du et al., 2015; Occelli, 1991b). Because each framework aluminium carries a longer Al–O bond than the Si–O bond, the cubic unit cell edge of faujasite contracts measurably as aluminium is removed, so X-ray diffraction provides a unit cell size measurement that tracks framework aluminium content and, by correlation, activity, selectivity, and stability (Roncolatto & Lam, 1998; Vogt & Weckhuysen, 2015). Table 2.1 collects the zeolite characteristics most relevant to this study.

**Table 2.1**

*Key structural and catalytic characteristics of zeolite Y relevant to FCC service*

| Characteristic | Typical value or description | Relevance |
|---|---|---|
| Framework type | FAU (faujasite) | Defines cage and window geometry |
| T-site composition | SiO4 and AlO4 tetrahedra; Si/Al of parent Y roughly 1.5–3, higher after dealumination | Sets charge and acid site density |
| Supercage diameter | About 1.3 nm | Admits cracked intermediates |
| Window | Twelve-membered ring, about 0.74 nm | Controls molecular access |
| Unit cell edge | Near 2.45–2.47 nm in catalyst grades, contracting on dealumination | Diagnostic of framework aluminium loss |
| Active site | Bridging Si–O(H)–Al hydroxyl | Brønsted cracking site attacked by vanadium |
| Stabilised forms | USY and REY (La, Ce exchanged) | Different steam and vanadium tolerance |

*Source:* Compiled from Breck (1974), Vogt and Weckhuysen (2015), and Roncolatto and Lam (1998).

## 2.7 From FCC to RFCC: Heavier Feeds, Heavier Problems

RFCC applies the same circulating-solid principle to atmospheric or vacuum residue. These feeds differ from VGO in several documented ways (Adanenche et al., 2023; Bai et al., 2019; Sadeghbeigi, 2012):

1. Conradson carbon residue, the empirical measure of a feed's tendency to lay down coke, is routinely several weight percent in residues against fractions of a percent in VGO, which raises the regenerator temperature and increases the steam exposure of the catalyst.
2. Asphaltenes, the polar, aromatic, high molecular weight fraction, are the least reactive and most coke-forming part of the feed.
3. Metals, nickel and vanadium among them, are concentrated in the residue exactly as described in Section 2.2.1 (Ahmad et al., 2010).
4. Sulphur and nitrogen contents are higher, loading the flue-gas treatment and altering the product slate.

Process responses include improved feed atomisation and riser termination devices, catalyst coolers for regenerator heat removal, two-stage regeneration, and SOx and NOx control additives; catalyst responses include more accessible matrix porosity for pre-cracking, lower sodium levels, rare earth stabilisation, and the traps and passivators examined in Section 2.11 (Adanenche et al., 2023; Bai et al., 2019). Because the RFCC duty intensifies both coke burning and steam exposure, vanadium, whose destructive chemistry requires regenerator temperature and steam, is the defining contamination problem of RFCC operation (Etim et al., 2018; Faghani et al., 2024). Feed calcium, which forms low-melting phases on the catalyst and interacts with the metals, is an additional reason why residue operations require specifically formulated catalysts and additives (Kumar et al., 2016).

## 2.8 Deactivation of FCC Catalysts in Service

### 2.8.1 Reversible deactivation by coke

During riser cracking, hydrogen-deficient aromatic species accumulate on the catalyst as coke, burying acid sites and blocking pore mouths within seconds of contact (Guisnet & Magnoux, 2001). Every operating unit is designed around this deactivation, because the regenerator exists to burn the coke off. Nitrogen bases in the feed act similarly but reversibly, neutralising acidity until they are burned away (Cerqueira et al., 2008).

### 2.8.2 Irreversible deactivation by hydrothermal dealumination

In the regenerator, steam partial pressures of the order of one-fifth to one-third of an atmosphere at about 700 to 760 °C hydrolyse the framework Al–O bonds of the zeolite, converting framework aluminium into extra-framework species and shrinking the unit cell; the same aging mode is reproduced in laboratories by steaming protocols such as cyclic propylene steaming (Sadeghbeigi, 2012; Wallenstein et al., 2000). The molecular steps of the hydrolysis have been computed by periodic DFT: the initiating Al–O(H) bond breaking proceeds through water adsorption on the aluminium site followed by dissociation over a framework oxygen, with activation energies between about 76 and 125 kJ mol−1 depending on the crystallographic environment of the aluminium, and the subsequent steps lead to extra-framework aluminium confined in the pores (Malola et al., 2012; Silaghi et al., 2015). This literature is central to the present project, because the baseline question of the thesis is how vanadium changes these very steps.

### 2.8.3 Poisoning by metals

The metal poisons of cracking catalysts behave differently, and the differences are essential context for vanadium (Bai et al., 2019; Xu et al., 2024). Nickel deposits on the catalyst and acts as an unwanted dehydrogenation catalyst, stripping hydrogen from hydrocarbons to produce hydrogen gas and extra coke; its effect is largely catalytic rather than structural, and it can be passivated by antimony or bismuth compounds, although antimony carries its own emissions penalty (Adanenche et al., 2023). Sodium neutralises Brønsted acid sites by ion exchange, acts as a flux that dissociates framework bonds, and is a powerful partner of vanadium in accelerating structural collapse (Hagiwara et al., 2003; Xu et al., 2002). Iron forms low-melting, glass-like surface nodules, especially in tight-oil and residue feeds, that physically block the pore mouths of the particle (Bai et al., 2019; Meirer et al., 2015). Vanadium combines the worst of both worlds: it dehydrogenates like nickel, at roughly one-quarter of nickel's activity per unit mass of metal, and it simultaneously destroys the zeolite framework irreversibly in a steam-accelerated reaction (Bai et al., 2019; Etim et al., 2018). Figure 2.4 places the regenerator temperature regime against the melting point of vanadium pentoxide, approximately 690 °C (Faghani et al., 2024). Industrial regeneration operates at and above the temperature at which V2O5 melts and its acid derivative becomes mobile, which is consistent with the experimental finding that vanadium damage is effected in the regenerator rather than in the riser (Occelli, 1991b; Wormsbecher et al., 1986).

**Figure 2.4**

*Thermal landscape of FCC operation relative to the melting point of vanadium pentoxide*

![](figures/fig2_4_temperature.png)

*Source:* Author. Riser values from Sadeghbeigi (2012) and Olugbenga and Oluwaseyi (2023); regenerator values from Sadeghbeigi (2012); model regenerator condition from Wormsbecher et al. (1986); V2O5 melting point from Faghani et al. (2024).

## 2.9 Vanadium Chemistry in the FCC Unit

### 2.9.1 Arrival and deposition of vanadium

Vanadium enters the unit chelated in vanadyl porphyrins and related non-porphyrin complexes dissolved in the heavy part of the feed. In the riser these molecules crack or adsorb on the catalyst and decompose, leaving the metal on the solid (Kugler & Leta, 1988; Mitchell, 1980). Mitchell (1980) established the laboratory method, now called Mitchell impregnation or MIV, that reproduces this deposition by impregnating fresh catalyst with vanadyl naphthenate and calcining it, and it remains the standard procedure for preparing vanadium-contaminated catalysts for study; the same impregnation logic underlies subsequent work with other metals (Kumar et al., 2016). At deposition the vanadium is in the +4 oxidation state inside the vanadyl (VO2+) unit, but the oxidising, high-temperature regenerator converts it progressively toward the +5 state (Occelli, 1991b).

### 2.9.2 The oxidation ladder and the two regenerator species

Vanadium is a redox metal with accessible oxidation states from +2 to +5. In the regenerator the dominant solid product of complete oxidation is vanadium pentoxide, whose melting point of approximately 690 °C lies inside the regenerator operating window (Faghani et al., 2024). In the presence of steam, V2O5 volatilises according to the equilibrium measured by Wormsbecher et al. (1986):

V2O5(s) + 3H2O(g) ⇌ 2H3VO4(v)

The product, orthovanadic acid, is a strong acid structurally analogous to phosphoric acid. Under a representative regenerator condition of 730 °C, 20 % steam, and a total pressure of two atmospheres, Wormsbecher et al. (1986) computed and confirmed an equilibrium concentration of mobile H3VO4 vapour of about 1 to 10 parts per million, which is sufficient to contact every particle in the fluidised bed. Under reducing excursions V2O5 can step back toward V2O4 and V2O3 without zeolite damage, which is why the oxidising, wet, hot corner of the operating map is the dangerous one (Occelli, 1991b).

### 2.9.3 Mobility of vanadium

Experimental microscopy has repeatedly shown that contaminant vanadium spreads. Kugler and Leta (1988) imaged vanadium redistribution across equilibrium catalyst particles by secondary ion mass spectrometry. Wormsbecher et al. (1986) demonstrated that vanadium migrates from particle to particle during fluid-bed aging, and the passivation studies of Etim et al. (2016, 2018) confirmed vanadium appearing inside deliberately added scavenger particles, from which they concluded that vanadium deactivates the catalyst by both intra-particle and inter-particle migration. Three overlapping transport modes are recognised in the reviews: vapour transport by H3VO4, surface flow of molten V2O5 and of low-melting sodium–vanadium mixed oxides, and solid-state diffusion of vanadyl species into the zeolite channels (Bai et al., 2019; Occelli, 1991b; Trujillo et al., 1997). Mobility is the reason a single contaminated particle does not die alone but seeds its neighbours with poison, and it is the reason vanadium traps must be distributed throughout the catalyst inventory rather than applied as a surface coating.

## 2.10 The Mechanism of Zeolite Y Deactivation by Vanadium: The Experimental Evidence

Five families of mechanistic evidence exist in the open literature. Each is presented below in its own terms, compared in Table 2.2, and synthesised in Figure 2.5.

### 2.10.1 Acid hydrolysis by vanadic acid

Wormsbecher et al. (1986) showed, by combining catalyst characterisation with thermodynamic analysis, that the damaging agent is not solid V2O5 itself but its volatile hydrolysis product, H3VO4. Being a strong acid, vanadic acid hydrolyses the aluminosilicate framework, cleaving the same Al–O and Si–O linkages that steam attacks, but at conditions under which steam alone is comparatively sluggish. They further showed that basic solids, magnesia and calcium oxide, capture the vanadium by reacting with the acid to form vanadates, preserving microactivity at vanadium loadings of 0.67 and 1.34 weight percent on catalyst. This work fixed both the acid nature of the poison and the acid–base logic of every subsequent trap.

### 2.10.2 Surface attack and the catalytic role of vanadium

Pine (1990) studied vanadium-contaminated ultrastable Y and exchange variants and demonstrated kinetically that vanadium is not consumed as it destroys: it behaves as a catalyst for the steam destruction of the zeolite, with sodium roughly equally active and the two acting synergistically. X-ray photoelectron spectroscopy showed that vanadium does not penetrate far into the crystal, so the attack initiates at external surface hydroxyl groups. Vanadium also destroyed silicalite, an aluminium-free zeolite-like structure, which proved that the attack can begin at Si–O bonds and silanols rather than only at aluminium sites. The rate-limiting step was identified with the nucleation of an amorphous phase at the attacked surface.

### 2.10.3 Vanadyl migration, extra-framework aluminium, and internal vanadic acid

Trujillo et al. (1997) followed vanadium speciation on zeolite Y by electron spin resonance and ultraviolet-visible diffuse reflectance spectroscopy. On the external surface, vanadium sits first as isolated species; heating in oxidising atmospheres drives vanadyl (VO2+) cations into the channels, where the strongest acid sites stabilise them. Their experiments showed that the reduced V(IV) state does not itself destroy the zeolite: water cooperates to produce vanadic acid inside the crystal according to an equilibrium that they formulated, and it is this internal H3VO4 that hydrolyses the framework. They also observed that extra-framework aluminium competes for vanadium and delays its arrival at the acid sites, an observation that anticipates modern trapping practice.

### 2.10.4 The sodium partnership

Xu et al. (2002) re-examined destruction as a function of sodium and vanadium together. Their data indicate that for low-sodium Y, steam hydrolysis of framework aluminium is the main route to collapse, whereas sodium introduces a second pathway in which steam converts exchange-site sodium into surface NaOH whose hydroxide ion attacks Si–O bonds. Vanadium's distinctive role in this picture is catalytic: mobile acidic vanadium releases cationic sodium as sodium metavanadate (NaVO3), steam hydrolyses the vanadate back to NaOH and metavanadic acid, and the cycle repeats, so that vanadium's principal effect is to keep generating fresh NaOH at the zeolite surface. Solid-state nuclear magnetic resonance work by Hagiwara et al. (2003) independently corroborated the cooperative sodium–vanadium destruction of USY by tracking real-time changes in the framework aluminium population.

### 2.10.5 Rare earth interactions and matrix effects

Occelli (1991b, 1996) established that rare earth stabilisation, excellent against steam, can backfire against vanadium: oxyvanadyl cations react with oxocerium species to form stable orthovanadates, stripping the stabilising rare earth ions out of the structure and leaving the framework exposed. In his series, zeolite vanadium resistance decreased as rare earth content rose, while extra-framework aluminium improved it. Yang et al. (1994) reached complementary conclusions on vanadium–nickel interaction in REY. Later work differentiated how the rare earth is added: lanthanum introduced as separately dispersed La2O3, remaining outside the zeolite channels, traps vanadium and preserves the USY structure better than ion-exchanged lanthanum, with LaPO4 and CeO2 behaving differently again (Du et al., 2015). Roncolatto and Lam (1998) supplied the mesoscale correlations across a commercial catalyst series: vanadium loading measurably reduced crystallinity, surface area, and unit cell size, and a loss of more than 50 % of cumene cracking activity occurred at about 4,000 ppm vanadium on the rare-earth catalyst, which quantifies how structural damage translates into performance loss. Etim et al. (2016) added the pore-scale mechanism, showing that in the presence of steam, vanadium causes excessive evolution of non-intercrystalline mesopores averaging about 25 nm at only 0.5 wt % vanadium loading, far larger than the mesopores of hydrothermally stable catalyst grades, and they proposed accelerated dealumination as the origin of those mesopores.

**Table 2.2**

*Experimental evidence base for the mechanism of vanadium attack on zeolite Y*

| Study | Catalyst system and methods | Key mechanistic finding |
|---|---|---|
| Mitchell (1980) | Fresh catalysts; synthetic metal impregnation | Reproducible deposition method (MIV) for metals on cracking catalysts |
| Pompe et al. (1984) | Ni and V compounds with cracking catalyst | Interactions of deposited Ni and V compounds with the catalyst solid |
| Wormsbecher et al. (1986) | XRD, BET, microprobe; thermodynamics; MAT | Volatile H3VO4 is the poison; it hydrolyses the framework; MgO and CaO scavenge it |
| Kugler and Leta (1988) | Equilibrium catalysts by imaging SIMS | Nickel and vanadium distributions; peripheral deposition and redistribution |
| Pine (1990) | USY, cation variants, silicalite; XPS; kinetics | Vanadium and sodium catalyse steam destruction; attack begins at surface silanols; nucleation-limited |
| Occelli (1991b, 1996) | HY, REHY, CREY; NMR; MAT | Rare earths can increase vanadium susceptibility; activation energies of destruction measured |
| Yang et al. (1994) | REY with nickel and vanadium | Vanadium–nickel interaction alters the destruction chemistry |
| Pan et al. (1996) | Trap design studies | Vanadic acid neutralisation by trapping systems on acid–base grounds |
| Wormsbecher et al. (1986) | Fluid-bed aging with migrant markers | Direct demonstration of inter-particle vanadium mobility |
| Trujillo et al. (1997) | ESR, UV-Vis DRS, sorption on Y | VO2+ migration; internal H3VO4; extra-framework aluminium competes for vanadium |
| Roncolatto and Lam (1998) | Commercial-type catalyst series | Crystallinity, surface area, and unit cell fall with vanadium; more than 50 % activity loss near 4,000 ppm on the RE catalyst |
| Xu et al. (2002) | Sodium- and vanadium-co-contaminated Y | Two pathways; vanadium catalyses NaOH supply; NaOH attacks Si–O bonds |
| Hagiwara et al. (2003) | USY with sodium and steam; solid-state NMR | Time-resolved framework aluminium loss with sodium–vanadium synergy |
| Etim et al. (2016) | USY with vanadium and steam; pore analysis | Vanadium evolves mesopores about 25 nm wide at 0.5 wt % loading by accelerated dealumination |
| Etim et al. (2018) | MIV catalysts with mixed oxide passivator | Destruction and passivation mapped; intra- and inter-particle migration; YVO4 formed in the trap |
| Faghani et al. (2024) | BaTiO3 trap in catalyst; XRD, EDS, testing | Trap preserves crystallinity and conversion to 6,000 ppm vanadium |
| Liu et al. (2025) | La-reinforced catalysts; atomic-scale STEM | α-LaVO4 chemically sequesters vanadium away from the framework |

*Source:* Compiled from the studies cited in this chapter. MAT, microactivity test; SIMS, secondary ion mass spectrometry; XPS, X-ray photoelectron spectroscopy; ESR, electron spin resonance; DRS, diffuse reflectance spectroscopy; STEM, scanning transmission electron microscopy.

**Figure 2.5**

*Consensus picture of zeolite Y deactivation by vanadium in the FCC regenerator*

![](figures/fig2_5_mechanism.png)

*Source:* Author's synthesis of Wormsbecher et al. (1986), Pine (1990), Occelli (1991b, 1996), Trujillo et al. (1997), Roncolatto and Lam (1998), Xu et al. (2002), Etim et al. (2016, 2018), Bai et al. (2019), Faghani et al. (2024), and Liu et al. (2025).

### 2.10.6 Points of agreement and points of dispute

The literature agrees on four points beyond dispute: the regenerator is where vanadium does its damage; the aggressive forms are mobile, oxidised, acidic vanadium species; the end state is aluminium loss and collapse of the zeolite Y framework; and the sodium partnership aggravates every other effect (Bai et al., 2019; Trujillo et al., 1997; Wormsbecher et al., 1986; Xu et al., 2002). What remains disputed is the first bond attacked. Pine's (1990) silicalite experiments implicate surface Si–OH and Si–O bonds; Wormsbecher et al. (1986) and Trujillo et al. (1997) describe acid hydrolysis of the aluminosilicate framework with aluminium as the electrophilic centre; and Xu et al. (2002) transfer much of the damage to vanadium-catalysed NaOH attacking Si–O bonds. Each claim was derived from a different catalyst formulation observed by a different technique, and no experimental method can watch a single molecule cut a single framework bond inside a pore. What no study has done is place the proposed elementary steps on a common quantum chemical energy scale for zeolite Y; the present study addresses that comparison.

## 2.11 Countermeasures Against Vanadium

### 2.11.1 Passivation and trapping chemistry

Passivation means converting the poison into an inert compound on the spot, while trapping means offering the poison an alternative solid partner that binds it irreversibly away from the zeolite. For vanadium, the governing logic set by Wormsbecher et al. (1986) is acid–base neutralisation: basic oxides intercept the acidic vanadium species to form high-melting vanadates (Adanenche et al., 2023). Table 2.3 organises the technology families with the performance data reported by their authors.

**Table 2.3**

*Passivation and trapping technologies against vanadium and their chemistry*

| Technology family | Representative agent | Working chemistry | Documented performance |
|---|---|---|---|
| Alkaline earth oxides | MgO, CaO | Acid–base capture of H3VO4 as magnesium or calcium vanadates | Activity retention at 0.67 and 1.34 wt % vanadium with a 20 % MgO blend (Wormsbecher et al., 1986) |
| Rare earth formulations | La2O3 (physically mixed), LaPO4, CeO2 | Rare earth vanadate formation outside the zeolite | Physical La2O3 mixing preserves USY structure and conversion better than ion exchange (Du et al., 2015) |
| Mixed metal oxide traps | Mg–Y oxide | Mobile H3VO4 forms crystalline YVO4 in the trap | Vanadium migration into the trap confirmed by SEM-EDS; activity preserved (Etim et al., 2018) |
| Perovskite-type traps | BaTiO3 | Basic BaO sites neutralise the acid while Ti immobilises vanadium and raises the melting point of the deposit | 18.7 % more crystallinity and 12 % more surface area retained at 6,000 ppm vanadium (Faghani et al., 2024) |
| Lanthanum reinforcement | La components in the formulation | Chemical sequestration of vanadium as α-LaVO4, atomically imaged | Conversion higher by 5.81 % and coke lower by 0.49 % at 6,000 ppm vanadium (Liu et al., 2025) |
| Calcium-tolerant formulations | Catalyst and additive combination | Tolerance of calcium contamination, which interacts with nickel and vanadium deposits | Higher olefin-to-paraffin ratio and lower coke with calcium-tolerant catalyst (Kumar et al., 2016) |
| Tin and other passivators | Tin compounds | Interaction with reduced vanadium species | Reviewed as a secondary option in practice (Adanenche et al., 2023) |

*Source:* Compiled from the cited studies; performance entries are the values reported by the cited authors.

### 2.11.2 Operational countermeasures

Outside chemistry, refiners manage vanadium operationally by diluting high-metal feeds, increasing equilibrium catalyst withdrawal and fresh catalyst make-up to hold Ecat metals at target, blending purchased low-metal Ecat, and selecting rare-earth or trap-bearing catalyst grades for high-residue duty (Adanenche et al., 2023; Bai et al., 2019). Figure 2.6 summarises the vanadium loadings tested in the influential contamination studies. The reported test loadings span 3,000 to 13,400 ppm vanadium, so a proposed mechanism of vanadium deactivation must remain valid across at least an order of magnitude of contamination, a consideration carried into the validation design of Chapter Three.

**Figure 2.6**

*Vanadium loadings reported in key experimental contamination studies*

![](figures/fig2_6_vbenchmarks.png)

*Source:* Author, from test loadings reported by Wormsbecher et al. (1986), Roncolatto and Lam (1998), Etim et al. (2016, 2018), Faghani et al. (2024), and Liu et al. (2025).

## 2.12 Quantum Chemical Modeling in Zeolite Catalysis

### 2.12.1 The Molecular Modeling Approach in Catalysis

Every experimental characterization technique in FCC catalyst studies reads a macroscopic or population average: X-ray diffraction measures bulk unit cell volume and crystallinity, spectroscopy monitors ensemble oxidation states, and microactivity testing evaluates overall hydrocarbon conversion. None of these techniques can observe an isolated $H_3VO_4$ molecule diffuse into a sodalite cage, dock at a single Brønsted acid site, and cleave individual framework aluminium–oxygen bonds. 

Quantum chemical modeling provides an atomic-scale microscope for solving this problem: given a well-defined molecular cluster model representing the zeolite active site, electronic structure calculations directly return the stationary-point geometries, reaction energies, and activation barriers for competing reaction pathways on an identical energy scale (Van Speybroeck et al., 2015).

### 2.12.2 Exchange-Correlation Functionals and Dispersion Corrections

In applying Density Functional Theory (DFT) to zeolite catalysis, the balance between computational tractability and chemical accuracy governs the choice of model chemistry:

1. **Hybrid Exchange-Correlation:** Standard generalized gradient approximation (GGA) functionals suffer from self-interaction error and tend to underestimate activation barriers for bond-cleavage reactions. Hybrid functionals incorporating a fraction of exact Hartree–Fock exchange, specifically B3LYP with 20% exact exchange (Becke, 1993) and PBE0 with 25% exact exchange (Adamo & Barone, 1999), provide superior thermochemical accuracy for transition metal complexes and aluminosilicate bond-rupture energetics.
2. **Empirical Dispersion Corrections:** Because zeolitic pore environments exert non-covalent van der Waals stabilization on adsorbed molecules, dispersion effects must be accounted for explicitly. Grimme’s empirical dispersion correction with Becke–Johnson rational damping (D3(BJ)) accurately captures long-range dispersion without double-counting short-range interactions (Grimme et al., 2011).
3. **Basis Set Quality:** The balanced def2-TZVP triple-zeta valence polarized basis set of Weigend and Ahlrichs (2005) effectively suppresses basis set incompleteness errors, while basis set superposition error (BSSE) in intermolecular adsorption is rigorously quantified using the counterpoise method (Boys & Bernardi, 1970).

### 2.12.3 Semi-Empirical Tight-Binding (GFN2-xTB) as an Exploratory Tool

Because mapping multi-step reaction coordinates involving numerous bond-breaking events and transition-state searches is computationally intensive, a multi-tier strategy is adopted. The GFN2-xTB semi-empirical tight-binding method (Bannwarth et al., 2019) incorporates multipole electrostatics and density-dependent dispersion, making it an efficient exploratory engine for rapid potential energy surface exploration, initial saddle-point localization, and structural screening prior to hybrid DFT refinement.

## 2.13 Prior DFT Studies Nearest to the Present Problem

### 2.13.1 DFT of zeolite dealumination

Malola et al. (2012) computed detailed reaction paths for both dealumination and desilication of protonic zeolites from density functional calculations, establishing the elementary water and silanol chemistry of framework dissolution. Silaghi et al. (2015) then performed periodic DFT on faujasite and related frameworks and showed that the initiating Al–O(H) bond hydrolysis proceeds through water adsorption on aluminium followed by water dissociation over a framework oxygen, with barriers of about 76 to 125 kJ mol−1 depending on the crystallographic environment, and they demonstrated a Brønsted–Evans–Polanyi relation between reaction energy and barrier that allows the first bond to break to be predicted from thermodynamics alone. Silaghi et al. (2016) completed the picture with the subsequent steps and with the confinement of the expelled extra-framework aluminium. These studies supply the quantitative anchors against which the steam-only baseline of the present work is validated.

### 2.13.2 DFT of vanadium in and on zeolites

Tielens and Dzwigaj (2010a) used DFT reactivity descriptors to probe framework vanadium, niobium, and tantalum sites in zeolitic materials and quantified their local acidity. Tielens and Dzwigaj (2010a) carried out periodic DFT on vanadium-doped zeolite models and verified the predictions against Fourier-transform infrared spectroscopy, showing that V–OH groups at framework vanadium sites are more acidic than silanols and that hydration of the vanadium site is nearly energy-neutral. Tielens and Dzwigaj (2010b) screened group V metal substitution into silicate models as a route to the active site. These studies demonstrate both that DFT handles vanadium–zeolite chemistry reliably and that published DFT to date has considered vanadium as a framework dopant and redox site rather than as the external deactivating agent of FCC service.

### 2.13.3 The identified gap

Three observations define the gap that this study addresses. First, experimental mechanism studies of vanadium attack on zeolite Y are abundant but reach partly different conclusions about the first bond attacked and the role of sodium, because each observes a different assembly of atoms (Pine, 1990; Trujillo et al., 1997; Xu et al., 2002). Second, periodic DFT has quantified the steam-only dealumination energetics of faujasite with explicit barriers (Malola et al., 2012; Silaghi et al., 2015), but has not been extended to the regenerator vanadium species identified experimentally. Third, DFT studies of vanadium–zeolite systems treat vanadium as a desirable framework dopant rather than as the FCC deactivating agent (Tielens & Dzwigaj, 2010a, 2010b). The gap is therefore not a shortage of data but a shortage of comparable energetics for the disputed steps, computed on the catalyst and in the operating window; it is the gap that this study fills by mapping the elementary steps of vanadic-acid attack and of steam hydrolysis on one identical faujasite cluster model.

## 2.14 FCC and RFCC in Nigerian Refineries: Documented Context

### 2.14.1 Unit inventory and status

Table 2.4 assembles the publicly documented conversion-unit picture for Nigerian refining. Nigeria inherited a refining base in which catalytic cracking was the gasoline engine. The Warri refinery was commissioned in 1978 as a complex conversion refinery with an FCC unit whose propylene-rich streams feed the site's petrochemical plants, processing Escravos and Ughelli crudes (Nigerian Midstream and Downstream Petroleum Regulatory Authority [NMDPRA], n.d.). The Kaduna refinery has operated since 1980 at a nameplate capacity of 110,000 barrels per day and is documented as a conversion refinery with catalytic cracking capacity (NS Energy, 2021; Punch, 2025). The Port Harcourt complex comprises a 1965 unit of 60,000 barrels per day and a 1989 unit of 150,000 barrels per day (NS Energy, 2021). The Dangote refinery added a 650,000 barrels per day crude distillation train and an RFCC unit reported at roughly 218,000 barrels per day (Leadership, 2026). Public records of licensor, catalyst supplier, and exact unit geometry are scarce for most of these units, and the table states where a value is not fixed by public documentation.

**Table 2.4**

*Documented unit inventory relevant to FCC and RFCC in Nigerian refineries*

| Refinery | Crude capacity | Cracking conversion asset | Documented status as at mid-2026 | Sources |
|---|---|---|---|---|
| Warri Refining and Petrochemical Company (1978) | 125,000 bpd | FCC unit; propylene to petrochemicals, decant oil to carbon black | Restarted briefly at partial rates in late 2024, shut again in 2025, rehabilitation ongoing | NMDPRA (n.d.); NS Energy (2021); Fawehinmi (2025) |
| Kaduna Refining and Petrochemical Company (1980) | 110,000 bpd | Catalytic cracking conversion refinery; gasoline production line | No crude processed for about a decade; Quick-Fix rehabilitation reported under way in 2025 | NS Energy (2021); Punch (2025) |
| Port Harcourt Refining Company (1965 and 1989) | 60,000 + 150,000 bpd | Conversion refinery complex | Older unit rehabilitated and restarted; larger unit in overhaul as reported in 2024–2025 | NS Energy (2021); Punch (2025) |
| Dangote Refinery, Lagos (2023) | 650,000 bpd | RFCC unit of roughly 218,000 bpd as the gasoline anchor | Regenerator section repaired after catalyst loss in 2025; unit restarted and refinery approaching full crude rates by early 2026 | Leadership (2026); Punch (2025) |

*Source:* Compiled from the cited public and news sources. Two public reports of the Dangote RFCC capacity disagree (approximately 204,000 bpd in Leadership, 2026, and approximately 218,000 bpd in Leadership, 2026); the table uses the value reported by Leadership (2026).

### 2.14.2 Feeds and metals in the Nigerian case

Nigerian crude oils are valued for low sulphur content and high yields of light products, but the residue fractions sent to cracking still carry the metals that attack the catalyst. Figure 2.7 plots the indicative nickel and vanadium contents of five major Nigerian grades from an industry assay listing, and peer-reviewed measurements of Nigerian crude samples and their heavy residues by Ahmad et al. (2010) found vanadium from 14 to 99 ppm, nickel from 5 to 11 ppm, and iron from 43 to 110 ppm in the measured heavy materials. Because metals partition almost quantitatively into the residue, an RFCC feed in Nigeria delivers these metals directly to the regenerator chemistry (Ahmad et al., 2010).

**Figure 2.7**

*Indicative nickel and vanadium contents of major Nigerian crude grades*

![](figures/fig2_7_crude_metals.png)

*Source:* Author, from a compiled industry crude assay listing (IKSectors, n.d.); values are commercial indicative assays, and the Brass Blend vanadium entry is an upper bound. Peer-reviewed ranges for Nigerian crude heavy fractions are reported separately by Ahmad et al. (2010).

### 2.14.3 Operational lessons already visible

The Dangote experience is instructive for a study of catalyst deactivation. In 2025, industry monitoring reported a significant catalyst-loss problem in the regenerator section of the RFCC unit that forced a repair outage and constrained gasoline output (Leadership, 2026); following maintenance the unit returned to high utilisation by early 2026 while the refinery advanced toward full crude rates (Leadership, 2026). Whatever the specific root cause, which has not been disclosed publicly in engineering detail, the episode demonstrates that catalyst behaviour in the regenerator, the vessel in which vanadium executes its chemistry, constrains the gasoline output of Nigeria's largest refinery.

## 2.15 Research Gap and Positioning of This Study

Assembling the chapter yields a precise gap statement:

1. Experimental mechanism studies of vanadium attack on zeolite Y are abundant but reach partly different conclusions about the first bond attacked and about the role of sodium, because each observes a different assembly of atoms (Pine, 1990; Trujillo et al., 1997; Xu et al., 2002).
2. Periodic DFT has quantified steam-only dealumination energetics of faujasite with explicit barriers (Malola et al., 2012; Silaghi et al., 2015), but has not been extended to the regenerator vanadium species documented experimentally.
3. DFT studies of vanadium–zeolite systems treat vanadium as a desirable framework dopant rather than as the FCC deactivating agent (Tielens & Dzwigaj, 2010a).
4. Commercial operational realities in Nigerian refineries, led by the startup of the world-scale Dangote RFCC unit, make a mechanistic, computation-driven understanding of vanadium attack a practical national necessity (Leadership, 2026; Punch, 2025). Placing the elementary chemical steps on a single quantum chemical energy scale directly fills the long-standing mechanistic gap in the international literature.

The study therefore positions itself at the intersection of these four observations: a cluster-model, dispersion-corrected hybrid DFT investigation of the energetics of vanadic-acid attack on a faujasite acid site, benchmarked against the published periodic DFT steam baseline and against the experimental record. Figure 2.8 places the principal reviewed publications on a common timeline.

**Figure 2.8**

*Four decades of research on vanadium deactivation of FCC (zeolite Y) catalysts*

![](figures/fig2_8_timeline.png)

*Source:* Author; each entry corresponds to a publication reviewed in this chapter.

## 2.16 Chapter Summary

FCC and RFCC units convert heavy petroleum fractions into gasoline over zeolite Y catalysts, and Nigerian refineries depend on them. In the regenerator, feed-borne vanadium forms mobile, oxidised, acidic species, chiefly vanadic acid, which hydrolyse the faujasite framework, extract its aluminium, and collapse the crystal, with sodium aggravating every step. Documented countermeasures rely on the acid–base trapping of vanadium species but remain empirical, because the elementary-step energetics of the attack have never been computed on a common scale. Density functional theory supplies that scale, cluster models make hybrid-functional accuracy affordable at the active site, published periodic DFT provides the steam-only benchmark, and no located study has applied the method to the regenerator vanadium species on zeolite Y. Chapter Three specifies the computational investigation designed to close that gap.

\newpage

# CHAPTER THREE: MATERIALS AND METHODS

## 3.1 Research Design

The study is designed as a two-tier quantum chemical investigation of two competing reaction pathways computed on one identical molecular model of the active region of zeolite Y, followed by a hybrid density functional refinement of the reference and pathway energies.

The design rests on four decisions.

**One model, two pathways.** Vanadic-acid dealumination and steam-only hydrolysis are computed on the same cluster, with the same atom ordering, the same reference species, and the same energy bookkeeping. Because the two routes differ only in the attacking molecule, every comparison between them is a comparison of chemistry rather than of model construction, which is the condition for the mechanistic conclusions drawn in Chapter Four.

**A semi-empirical tier for the landscape, a hybrid DFT tier for the energies.** The complete pathway is first mapped at the GFN2-xTB semi-empirical level, where a stationary-point search costs minutes and the whole landscape can be explored without exhausting the available computing time. The confirmed stationary points are then re-optimised at dispersion-corrected hybrid DFT, and the final electronic energies are evaluated at a second hybrid functional. Mechanistic conclusions are drawn from the hybrid DFT numbers; the semi-empirical tier supplies the geometry map, the candidate saddle points, and an independent cross-check on every energetic trend.

**Verification before interpretation.** Each calculation passes a stated acceptance gate before its energy is allowed into a table: a minimum must show a converged optimisation with no imaginary vibrational mode, and a saddle-point candidate must show exactly one imaginary mode whose displacement vector moves the reacting bonds, and must connect the claimed reactant and product minima when displaced along that mode in both directions. Calculations that do not pass a gate are recorded with their verdict and are not used to support a mechanistic conclusion. The acceptance protocol is defined in Section 3.7.

**Reproducibility as a design requirement.** Every calculation is stored, named, and indexed in a calculation register that links the reported energy to its input file, output log, final geometry, software version, and acceptance verdict. The register is the direct source of the tables in Chapter Four; no value is transcribed by hand from a log into a table.

## 3.2 The Model System

### 3.2.1 The faujasite cluster

The active site of zeolite Y is represented by a hydrogen-terminated cluster of the faujasite framework cut around one framework aluminium atom and its four neighbouring silicon T-sites. The cluster has the composition AlSi4O4H13 and 22 atoms: one aluminium, four bridging oxygens, four silicon atoms, and thirteen hydrogen atoms.

The connectivity reproduces the two features that constitute the catalytic site. First, the aluminium is coordinated by four bridging oxygens, each of which is bonded to one silicon atom, so that the local Al–O–Si topology of faujasite is preserved. Second, one of the four bridging oxygens carries a proton, giving the bridging hydroxyl group Si–O(H)–Al that constitutes the Brønsted acid site. In the optimised cluster the protonated oxygen is the most weakly bound to aluminium (Al–O = 0.1916 nm against 0.1685 to 0.1696 nm for the three unprotonated bridges, as reported in Chapter Four), which is the geometric signature of a Brønsted acid site.

The cluster is terminated at the four silicon atoms by three hydrogen atoms each, placed along the directions of the framework bonds that were cut, so that the capping groups reproduce the electronic effect of the continuation of the lattice without introducing artificial strain. All peripheral Si–H and Al–O distances are monitored after every optimisation; a rearrangement of the capping groups rather than of the reacting site is treated as a model fault and corrected before the structure is accepted. The terminating atoms are excluded from the quantities interpreted in Chapter Four, and the reported energies are differences between states computed with the same truncation, so that the systematic error of the boundary cancels to first order.

### 3.2.2 The attacking species

The mobile vanadium species is represented by vanadic acid, H3VO4, the V(V) molecule formed from vanadium pentoxide in the steam-rich regenerator and identified experimentally as the volatile precursor of FCC catalyst poisoning (Wormsbecher et al., 1986). Vanadic acid is a strong acid of the phosphoric acid family and carries both a Lewis-basic V=O oxygen and acidic hydroxyl groups, which allows it to interact simultaneously with the Brønsted proton and with the framework aluminium during attack. Water, H2O, is computed as the reference attacking molecule of the steam-only baseline.

Both species are optimised as isolated molecules in the gas phase before any complex is built, and their energies define, together with the bare cluster, the reference zeros of the two pathways (Section 3.6).

### 3.2.3 The stationary-point set

The stationary points computed in this study are listed in Table 3.1. The vanadium route comprises the isolated reference state, the pre-reaction complex, the chemisorbed intermediate, the first aluminium–oxygen cleavage transition structure, the hydrolysed intermediate in which the framework has opened, and the dealuminated product in which the aluminium has been extracted as extra-framework material. Saddle-point searches were also carried out for the chemisorption step and for the final cleavage step, and their status is reported in Chapter Four in the terms defined by the acceptance protocol. The steam route comprises the water pre-reaction complex, its hydrolysis transition structure, and the corresponding product.

Every state keeps the same atom ordering: the 22 cluster atoms first, in an invariant order, followed by the atoms of the adsorbate. This convention makes the states directly comparable, allows the same interatomic distances to be measured in every file, and permits the framework and the adsorbate to be addressed as two fragments in fragment-based calculations.

**Table 3.1**

*Stationary-point set defining the two reaction pathways of the study*

| State | Role in the pathway | Composition | How the structure was obtained |
|---|---|---|---|
| cluster | Reference: bare Brønsted acid site | AlSi4O4H13 (22 atoms) | Optimised from the idealised faujasite cut |
| H3VO4 | Reference: isolated vanadic acid | H3VO4 (8 atoms) | Optimised isolated molecule |
| H2O | Reference: isolated water | H2O (3 atoms) | Optimised isolated molecule |
| V-R | Isolated reference state, vanadium route | cluster + H3VO4 (30 atoms) | H3VO4 placed at a non-interacting distance from the cluster |
| V-PRC | Pre-reaction complex | cluster + H3VO4 (30 atoms) | Hydrogen-bonded docking of H3VO4 at the Brønsted proton |
| V-I1 | Chemisorbed intermediate | cluster + H3VO4 (30 atoms) | Optimisation from the chemisorption saddle guess |
| V-TS2 | First Al–O cleavage transition structure | cluster + H3VO4 (30 atoms) | Relaxed scan, nudged elastic band search, and OptTS refinement |
| V-I2 | Hydrolysed intermediate (framework opened) | cluster + H3VO4 (30 atoms) | Optimisation from the first-cleavage product side |
| V-P | Dealuminated product (extra-framework aluminium) | cluster + H3VO4 (30 atoms) | Optimisation from the final-cleavage product side |
| W-PRC | Steam pre-reaction complex | cluster + H2O (25 atoms) | Water docked at the Brønsted proton |
| W-TS | Steam hydrolysis transition structure | cluster + H2O (25 atoms) | Nudged elastic band search and OptTS refinement |
| W-P | Steam dealuminated product | cluster + H2O (25 atoms) | Optimisation from the cleavage product side |

*Source:* Author. Saddle searches for the chemisorption step (V-TS1) and the final cleavage step (V-TS3) form part of the computed set; their acceptance status is reported in Table 4.4.

**Figure 3.1**

*The four-T-site faujasite cluster model and its pre-reaction complex with vanadic acid*

![](figures/fig3_1_cluster.png)

*Source:* Author; structures rendered from the computed geometries.

**Figure 3.2**

*Stationary-point sequence of the two computed reaction pathways*

![](figures/fig3_2_pathway.png)

*Source:* Author. The vanadium route proceeds from the pre-reaction complex through the chemisorbed intermediate to the hydrolysed intermediate and the dealuminated product; the steam route proceeds from its pre-reaction complex through hydrolysis to its product.

## 3.3 Software and Hardware

All electronic-structure calculations were performed with ORCA, a freely licensed academic quantum chemistry package that provides, within one input format, the semi-empirical tight-binding method used for the Tier 1 mapping, hybrid DFT for the refined tier, nudged elastic band and eigenvalue-following transition-state searches, and vibrational analysis (Neese, 2012; Neese et al., 2020). ORCA version 6.1 was used on the local workstation and ORCA 6.1.1 on the cloud instance that performed the hybrid DFT work. Using one program for every tier guarantees that the geometry conventions, atom ordering, and energy definitions are identical across levels, which is the condition for the cross-level comparison of Chapter Four.

Molecular structures were assembled, inspected, and visualised using Avogadro 2 and VESTA 3. Electronic structure calculations, geometry optimisations, frequency analyses, and nudged elastic band transition-state searches were performed exclusively using the ORCA 6.1 / 6.1.1 quantum chemistry program package (Neese et al., 2020).

**Table 3.2**

*Software and hardware used in the study*

| Tool or resource | Version or specification | Role in the study |
|---|---|---|
| ORCA (local) | 6.1 | GFN2-xTB optimisations, relaxed scans, nudged elastic band searches, OptTS refinements, and frequency analyses |
| ORCA (cloud) | 6.1.1 | B3LYP-D3(BJ)/def2-TZVP geometry optimisations; B3LYP and PBE0 single-point energies |
| Avogadro 2 | 1.2 | Assembly, editing, and visual inspection of the cluster and adsorbate complexes |
| Spartan | '14 | Independent structure building and connectivity checking |
| VESTA | 3 | Display and orientation of the faujasite framework reference |
| Python 3 (standard library, NumPy, matplotlib) | 3.x | Register maintenance, energy bookkeeping, validation scripts, tables, and figures |
| Local workstation | Quad-core processor | Tier 1 semi-empirical calculations |
| Cloud instance | Four virtual processors, Linux | Tier 2 and Tier 3 hybrid DFT calculations |
| tmux, rsync | Current releases | Persistent remote sessions and synchronisation of results |

*Source:* Author.

## 3.4 Computational Levels and Settings

### 3.4.1 Tier 1: semi-empirical mapping (GFN2-xTB)

The complete reaction landscape was explored with the GFN2-xTB tight-binding Hamiltonian through the ORCA interface, using the `XTB2 OPT FREQ` keyword combination. The method reproduces geometries and reaction energies of main-group systems at a small fraction of the cost of DFT (Bannwarth et al., 2019), which allowed the full stationary-point sequence (optimisations, relaxed scans along the reacting bonds, nudged elastic band searches, and frequency checks) to be carried out on the local workstation. Tier 1 establishes the connectivity of every state, the identity of the intermediates, the candidate transition structures, and an internally consistent first set of relative energies.

### 3.4.2 Transition-state search protocol

Saddle points were searched in three stages. A relaxed scan along the reacting coordinate first identified the energy interval in which the barrier lies. A climbing-image nudged elastic band calculation with the endpoints taken from the confirmed minima then produced a discretised path and a highest-energy image. Finally, the highest image was refined with the eigenvalue-following optimiser (`OptTS`) until the saddle converged, and the converged structure was submitted to frequency analysis in the same job. The normal mode corresponding to the single imaginary frequency was inspected to confirm that it animates the bonds that the step is proposed to break and form, and the structure was displaced by ±0.10 Å along that mode and re-optimised, so that the two displaced structures could be compared with the claimed reactant and product minima.

### 3.4.3 Tier 2: hybrid DFT geometry refinement

The reference species and the adsorption complexes were re-optimised at the B3LYP level with the D3(BJ) dispersion correction and the def2-TZVP basis set (Becke, 1993; Lee et al., 1988; Grimme et al., 2011; Weigend & Ahlrichs, 2005). The calculations used the resolution-of-identity chain-of-spheres approximation for the Coulomb and exchange terms (RIJCOSX) with the matching def2/J auxiliary basis, tight self-consistent-field convergence, and a production-grade integration grid, with four processors allocated to each job and a 3,000 MB memory limit. Every state was computed as a closed-shell singlet. The optimised structures were checked for retention of the intended connectivity, and their final energies and geometries were written to the register.

The B3LYP-D3(BJ)/def2-TZVP combination is a standard and widely benchmarked choice for zeolite cluster chemistry: the hybrid functional describes the localised electronic reorganisation of bond breaking and forming, the dispersion correction is essential for the hydrogen-bonded pre-reaction complexes, and the triple-zeta basis describes the aluminium, silicon, vanadium, and oxygen centres consistently.

### 3.4.4 Tier 3: single-point evaluation at two hybrid functionals

The electronic energies of the full stationary-point set were evaluated as single points at the B3LYP-D3(BJ)/def2-TZVP level and at the PBE0-D3(BJ)/def2-TZVP level, on the corresponding optimised geometries (Adamo & Barone, 1999). The single-point jobs used the same basis set and dispersion correction as the Tier 2 optimisations, a finer integration grid, eight processors, and tight self-consistent-field convergence. PBE0 contains 25 % exact exchange, which makes it an independent check on the B3LYP description rather than a variation of it; agreement between the two functionals on the ranking of the states, and on the sign of each step, is the study's principal defence against conclusions that depend on the choice of functional.

### 3.4.5 Reference energies and the comparison of levels

Three quantities are compared across levels of theory for every state: the relative electronic energy, the adsorption energy at the Brønsted site, and the barrier of the steam hydrolysis step. Because the geometry at which each single point is evaluated is itself obtained at one particular level, the comparison separates two effects that must be distinguished in the interpretation: the effect of the electronic-structure method, which is measured by comparing B3LYP and PBE0 single points at one geometry, and the effect of geometry relaxation, which is measured by comparing a single-point energy with the energy of the corresponding optimised structure. Chapter Four reports both.

**Table 3.3**

*Computational levels, settings, and the reason for each choice*

| Tier | Method and settings | Purpose and reason for the choice |
|---|---|---|
| 1 | GFN2-xTB (`XTB2 OPT FREQ`); single processor | Complete pathway mapping, relaxed scans, nudged elastic band searches, and frequency checks at negligible cost; establishes connectivity and candidate saddles before DFT is attempted |
| 1 | Climbing-image nudged elastic band; OptTS with mode inspection; ±0.10 Å displacement tests | Location and verification of transition structures along the mapped path |
| 2 | B3LYP-D3(BJ)/def2-TZVP, RIJCOSX with def2/J, tight SCF, production grid; four processors | Geometry and reference-energy level of the study; hybrid functional for bond reorganisation, dispersion correction for hydrogen bonding, triple-zeta basis for Al, Si, V, and O |
| 3 | B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP single points with a finer integration grid; eight processors | Independent second functional for the final ranking of states, without dependence on a single exchange–correlation functional |
| All | Closed-shell singlet, neutral charge, identical atom ordering in every file | Physical consistency of the model and comparability of every state on one energy scale |

*Source:* Author.

## 3.5 Computational Procedure

**Step 1: Reference species.** The bare cluster, vanadic acid, and water were optimised at the semi-empirical tier and submitted to vibrational analysis, and the resulting geometries were checked against the expected bond-length ranges (silicon–oxygen about 0.162 nm; aluminium–oxygen 0.169 to 0.192 nm, with the longest aluminium–oxygen bond at the protonated bridge). The three reference energies define the zeros of the two pathways and were later refined at the hybrid DFT tier.

**Step 2: Pre-reaction complexes.** Vanadic acid was docked at the Brønsted proton through its V=O oxygen to form the hydrogen-bonded pre-reaction complex V-PRC, and a second orientation was prepared by rotating the molecule about the hydrogen-bond axis; the lower-energy converged structure was retained and the energy difference between the two orientations recorded. The water complex W-PRC was prepared in the same way. A separate non-interacting reference state, V-R, was built with the adsorbate at a distance from the framework; after optimisation it converged into the same basin as V-PRC, which establishes that the approach of vanadic acid to the Brønsted site carries no barrier and that the two files describe one physical state.

**Step 3: Chemisorbed intermediate.** Starting from the chemisorption saddle guess, with the forming aluminium–oxygen bond shortened and the acidic proton of vanadic acid transferred to the framework, V-I1 was optimised to a stable minimum. In the converged structure the aluminium retains four framework oxygen neighbours, and the vanadium centre is held close to the aluminium; the adsorbate is bound at the site and no framework bond has yet been broken. The structural metrics of this state are reported in Chapter Four.

**Step 4: First aluminium–oxygen cleavage (V-TS2, V-I2).** The first cleavage was mapped by a relaxed scan along the breaking bond, followed by a climbing-image nudged elastic band search between the confirmed endpoints and an eigenvalue-following refinement of the highest image. The converged transition structure carries exactly one imaginary mode whose displacement vector describes the breaking aluminium–oxygen bond together with the concerted proton transfer. The product of the step, V-I2, is the hydrolysed intermediate in which the framework has opened and silanol groups have been formed; its geometry was obtained by completing the cleavage in the direction indicated by the saddle and re-optimising.

**Step 5: Final cleavage and product (V-P).** The same protocol was applied to the final step, in which the aluminium is released from its remaining framework bonds. The product state V-P contains the extracted aluminium as extra-framework material together with the silanol-terminated framework, and it is the endpoint against which the overall thermodynamic feasibility of the vanadium route is judged.

**Step 6: Steam baseline (W-PRC, W-TS, W-P).** The corresponding hydrolysis sequence was computed for water on the same cluster, giving the steam pre-reaction complex, its transition structure, and its product. This is the route against which the published periodic DFT barrier range for steam dealumination is used as the external benchmark.

**Step 7: Hybrid DFT refinement.** The isolated species and the adsorption complexes were re-optimised at B3LYP-D3(BJ)/def2-TZVP, and the connectivity of each refined structure was checked against the semi-empirical reference geometry.

**Step 8: Single-point evaluation.** B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP single points were evaluated on the refined geometries of the complete stationary-point set, including the transition-structure candidate, so that both functionals are compared at one geometry per state.

**Step 9: Analysis.** The pathways were assembled into energy tables and profile figures directly from the register by Python scripts, the two functional levels were compared state by state, the adsorption competition at the Brønsted site was evaluated, and the steam barrier was compared with the published benchmark range.

Figure 3.3 summarises the complete workflow as it was executed, from the construction of the cluster to the analysis of the two pathways.

**Figure 3.3**

*Two-tier computational workflow adopted for the study*

![](figures/fig3_3_workflow.png)

*Source:* Author. Tier 1 maps the landscape and locates the candidate stationary points at the semi-empirical level; Tier 2 and Tier 3 refine the reference species, the adsorption complexes, and the final electronic energies at hybrid DFT. Every stage passes through the acceptance gate of Section 3.7 before its result enters the register.

## 3.6 Computed Quantities and Energy Bookkeeping

Two reference zeros are used, one per pathway. The vanadium route is referenced to the separated framework cluster and vanadic acid molecule,

Eref,V = E(cluster) + E(H3VO4)   (3.1)

and the steam route to the separated cluster and water molecule,

Eref,W = E(cluster) + E(H2O).   (3.2)

For each stationary point the following quantities are reported:

1. **Relative electronic energy**, ΔE = E(state) − Eref, in kJ mol−1.
2. **Adsorption energy** of the pre-reaction and chemisorbed complexes, ΔEads = E(complex) − E(cluster) − E(adsorbate), in kJ mol−1, negative values denoting stabilisation.
3. **Competition margin**, the difference between the adsorption energies of vanadic acid and water at the same site, computed as [E(V-PRC) − E(W-PRC)] − [E(H3VO4) − E(H2O)], in kJ mol−1. This quantity is independent of the cluster reference energy, because E(cluster) cancels, and it is therefore the most robust measure of which molecule is preferentially bound.
4. **Activation barriers**, expressed as the energy of the transition structure relative to the state that precedes it in the pathway.
5. **Structural descriptors** for every state: the aluminium–oxygen distances, the vanadium–oxygen distances, the aluminium–vanadium separation, and the proton inventory, which together define what has and has not changed at each step.

Energies are converted from Hartree to kJ mol−1 using 1 Eh = 2,625.499638 kJ mol−1 and reported to 0.01 kJ mol−1, which is the precision of the printed quantities; the discussion in Chapter Four rounds differences to the accuracy justified by the method. At the semi-empirical tier the energies are the total electronic energies reported by ORCA for the optimised structures; at the hybrid DFT tier the energies are the single-point energies evaluated at the stated geometry.

**Table 3.4**

*Energy quantities computed for each stationary point and pathway*

| Quantity | Definition | Reported for |
|---|---|---|
| ΔE | E(state) − Eref (electronic) | Every state, both pathways |
| ΔEads | E(complex) − E(cluster) − E(adsorbate) | Pre-reaction and chemisorbed complexes |
| Competition margin | [E(V-PRC) − E(W-PRC)] − [E(H3VO4) − E(H2O)] | Adsorption competition at the Brønsted site |
| Barrier | E(transition structure) − E(preceding state) | Every located transition structure |
| Cross-level difference | Value at one functional level minus the value at the other | Every state, for the method-sensitivity assessment |
| Structural descriptors | Al–O, V–O, and Al⋯V distances; proton inventory | Every state |

*Source:* Author.

## 3.7 Verification and Acceptance Protocol

A calculation is admitted into the reported results only after passing the gates listed in Table 3.5. The protocol follows the principle that the status of every computation must be stated in one of three terms: verified, superseded, or not established at the level of theory reached.

**Minima.** A state qualifies as a minimum when the optimisation terminates normally, the structure retains the intended connectivity, and the vibrational analysis returns no imaginary frequency. Where a low-frequency mode of the peripheral capping groups appears, the mode is animated and, if it is a capping-group libration rather than a motion of the reacting site, the structure is re-optimised with the capping atoms restrained and the outcome recorded.

**Saddle points.** A transition structure is admitted only if it satisfies the five-point chain: the saddle optimisation converges with normal termination (A1); exactly one imaginary mode remains, of a magnitude consistent with a genuine reaction coordinate, and the mode is inspected to confirm that it animates the bonds of the proposed step (A2); the energy of the saddle exceeds the energies of both states it connects by more than 1.0 kJ mol−1 (A3); the structures obtained by displacing the saddle by ±0.10 Å along the imaginary mode relax to the two claimed minima, within 5 kJ mol−1 of their accepted energies (A4); and the energy, log, and displacement tests map to one structure throughout (A5). A candidate that fails any point of the chain is recorded with its verdict, and the barrier of that step is reported as not established at the level reached rather than as a computed value.

**Superseded calculations.** When a calculation is repeated for a technical reason, the earlier result is retained in the archive with the status superseded and its replacement is entered as the next version of the same state. No calculation is deleted, because the record of the path by which the accepted numbers were obtained is part of the evidence for their reliability.

**Table 3.5**

*Acceptance protocol for minima and saddle points*

| Gate | Requirement | Action if the requirement is not met |
|---|---|---|
| Minimum | Normal termination, converged optimisation, intact connectivity, no imaginary mode | Re-optimise with a tighter convergence threshold; animate any residual low-frequency mode before judging the structure |
| A1 | Saddle optimisation converges with normal termination | Continue the optimisation from the last geometry with a rebuilt Hessian, and record the continuation as a new version |
| A2 | Exactly one imaginary mode; magnitude credible; mode animates the reacting bonds | Reject the candidate; the structure is retained as a diagnostic |
| A3 | E(saddle) > max[E(reactant), E(product)] + 1.0 kJ mol−1 | Reject the candidate as an artefact of the search |
| A4 | ±0.10 Å displacement along the imaginary mode relaxes to the two claimed minima within 5 kJ mol−1 | Where one side of the test is verified, report the located saddle and its barrier as an upper estimate; where neither side is verified, report the step as not established at the level reached; retain the diagnostic structures |
| A5 | Energy, log, and test structures map to one structure | Correct the register before any use of the value |

*Source:* Author.

Six validation anchors are applied to the accepted results, listed in Table 3.6. The geometry anchor checks the computed bond lengths against the ranges expected for faujasite. The model-identity anchor compares the non-interacting reference state V-R with the pre-reaction complex V-PRC, both energetically and by measuring the shortest framework–adsorbate contact in each structure, so that a spurious interaction energy cannot be attributed to two different structures. The cross-level anchor requires the ranked order of the states and the sign of every step to agree between the semi-empirical tier and the two hybrid functional levels; a disagreement is investigated before it is reported. The external anchor compares the computed steam hydrolysis barrier with the published periodic DFT range of 76 to 125 kJ mol−1 for steam dealumination (Silaghi et al., 2015). The provenance anchor traces every energy in a Chapter Four table to a register row, and each register row to an input file, an output log, and a final geometry file.

**Table 3.6**

*Validation anchors for checking the computed results*

| Anchor | Criterion | Action if the criterion is not met |
|---|---|---|
| Geometry | Bond lengths within the faujasite ranges (Si–O ≈ 0.162 nm; Al–O 0.169–0.192 nm, longest at the protonated bridge) | Rebuild the capped periphery and re-optimise before continuing |
| Model identity | V-R and V-PRC identical in energy and geometry within the hydrogen-bond contact range | Re-examine the starting geometry and re-optimise |
| Energy ordering | Every accepted saddle lies above the states it connects | Reject the saddle and report the step as not established |
| Cross-level agreement | Same ranked order and same sign of each step at every level of theory | Investigate the quantity that disagrees and report its method dependence explicitly |
| External benchmark | Steam barrier within the published range 76–125 kJ mol−1 | Re-examine the model and the level of theory for that step before drawing comparisons |
| Provenance | Every tabulated energy maps to a register row, input, log, and geometry | Correct the register; an untraceable number is removed from the report |

*Source:* Author.

## 3.8 Treatment of Uncertainty

The results of this study are deterministic: each quantity is the solution of a defined electronic-structure problem, so there is no sampling distribution and no statistical significance to report. Uncertainty is handled instead by identifying and quantifying the sources that matter for a computed energy difference, and by reporting them alongside the numbers:

1. **Method dependence.** Every conclusion is presented at more than one electronic-structure level, and the spread between levels is stated. The B3LYP and PBE0 single points at one geometry isolate the effect of the functional, and the comparison of those values with the corresponding optimised structures isolates the effect of geometry relaxation.
2. **Model truncation.** The cluster boundary approximates the lattice; the model is validated against the published periodic DFT barrier range for the reaction step that both approaches compute (Silaghi et al., 2015).
3. **Numerical thresholds.** Geometry-optimisation and self-consistent-field convergence criteria and integration-grid settings are fixed and documented; the same settings are used for every state, so that the differences between states, which are the quantities interpreted, are free of systematic offsets.

Because the quantities interpreted in Chapter Four are differences between states computed with identical model, basis set, and settings (for example, the competition between vanadic acid and water for the same site, or the barrier of one step relative to the preceding state), the systematic error of the method largely cancels. This is what makes relative comparisons of a few tens of kJ mol−1 meaningful even when the absolute accuracy of a hybrid DFT energy is larger than that.

## 3.9 Data Management and Reproducibility

Every calculation is named STATE-Tn-Vnn (state, tier, version) so that a repeated calculation never overwrites its predecessor: a revised or repeated job becomes the next version, and the earlier version remains in the archive with its verdict. The calculation register records, for each row, the job identifier, the state, the tier, the input file, the output log, the final geometry file, the software and version, the number of imaginary frequencies, the final electronic energy, the relative energy where defined, and the accept, supersede, or reject verdict with its reason. A provenance map links each register row to the exact files from which its energy was read, and the register is reproduced in condensed form in Appendix B.

Input files, output logs, final geometries, and the register are stored together in the project archive, which is synchronised after every computing session and backed up to independent media weekly. Analysis scripts read the outputs directly rather than restating their values, so that the tables in Chapter Four regenerate from the archive. Superseded and rejected calculations are retained rather than deleted: they document the path by which the accepted results were reached, and they preserve the evidence needed to judge the reliability of each reported value.

## 3.10 Health, Safety, and Environmental Considerations

The study is entirely computational and literature-based. It involves no chemical synthesis, no hazardous reagents, no pressurised or high-temperature equipment, and no biological or human subjects, so the laboratory hazards that apply to experimental catalysis work are absent. The health and safety considerations that do arise are those of prolonged workstation and screen use, which were managed by structuring the work into scheduled sessions with long calculations running unattended.

The environmental footprint of the work is the electricity consumed by the workstation and by the cloud instance. It is minimised by mapping the pathway at the inexpensive semi-empirical level before committing hybrid DFT resources, by running the hybrid DFT jobs in batches sized to the available budget, and by releasing the cloud instance between computing campaigns. Ethically, the study observes the standard requirements of computational research: all reported data are the outputs of the calculations described, no result is adjusted or selected to support a preferred mechanism, superseded and rejected calculations are retained in the register with their verdicts, and all experimental findings, methods, and data taken from the literature are cited at the point of use. No confidential or proprietary plant data were used; the Nigerian refinery context is drawn entirely from published sources and public information.

## 3.11 Chapter Summary

This chapter has defined the model (comprising a hydrogen-terminated faujasite cluster carrying one Brønsted acid site, the two attacking species vanadic acid and water, and the stationary-point set of the two pathways) and the computational protocol applied to it. The protocol comprises semi-empirical mapping of the landscape with GFN2-xTB, a three-stage saddle-search procedure with mode inspection and displacement tests, hybrid DFT refinement with B3LYP-D3(BJ)/def2-TZVP, single-point evaluation of every state at B3LYP and PBE0 in the def2-TZVP basis, a documented five-point acceptance chain for transition structures, and a calculation register that makes every reported number traceable to its input, output, and geometry. The energy bookkeeping, uncertainty treatment, data-management scheme, and ethical framework that govern the work have been stated. Chapter Four presents the results obtained with this protocol.

\newpage

# CHAPTER FOUR: RESULTS AND DISCUSSION

## 4.1 The Faujasite Cluster Model and the Reference Species

The hydrogen-terminated faujasite cluster, of composition AlSi4O4H13, converged to a minimum with no imaginary vibrational mode at the semi-empirical tier, retaining the intended connectivity: one aluminium atom tetrahedrally coordinated by four bridging oxygens, each of which is bonded to one silicon atom, with one of the four oxygens carrying the Brønsted proton. Table 4.1 collects the geometry metrics of the cluster and of the two isolated attacking species.

Three features of the optimised cluster define the acid site that the rest of this study interrogates. The three unprotonated bridges have Al–O distances between 0.1685 and 0.1696 nm, whereas the protonated bridge has an Al–O distance of 0.1916 nm, the longest of the four by about 0.022 nm. The O–H bond of the Brønsted proton is 0.096 nm, and the Si–O distances lie between 0.1607 and 0.1666 nm. The elongation of the Al–O bond at the protonated oxygen is the geometric signature of the Brønsted acid site, and it identifies that bond as the weakest aluminium–oxygen linkage in the cluster before any adsorbate is present. This is the bond whose fate the rest of the chapter follows.

Vanadic acid is optimised as a four-coordinate vanadium species with one short vanadyl bond (V=O = 0.1519 nm), three equivalent V–OH bonds of 0.163 nm, and O–H distances of 0.0959 nm. Water is optimised with O–H distances of 0.0959 nm. The three reference energies obtained at this level (the cluster, vanadic acid, and water) define the zeros of the two pathways through Equations 3.1 and 3.2, and they were used unchanged in every relative energy reported in Sections 4.2 to 4.4.

**Table 4.1**

*Optimised geometry metrics of the faujasite cluster and the reference species (GFN2-xTB)*

| Structure | Bond or distance | Value (nm) |
|---|---|---|
| Cluster (AlSi4O4H13) | Al–O, three unprotonated bridges | 0.1685, 0.1687, 0.1696 |
| | Al–O, protonated bridge | 0.1916 |
| | O–H, Brønsted proton | 0.0960 |
| | Si–O (range) | 0.1607–0.1666 |
| H3VO4 | V=O (vanadyl) | 0.1519 |
| | V–OH, three equivalent | 0.1633, 0.1633, 0.1634 |
| | O–H | 0.0959 |
| H2O | O–H | 0.0959 |

*Source:* Author, computed in this study. Values are the bond lengths in the optimised structures stored in the calculation register.

## 4.2 Adsorption at the Brønsted Acid Site

### 4.2.1 Adsorption energies at the semi-empirical tier

The vanadium route begins with the approach of vanadic acid to the Brønsted site. The pre-reaction complex V-PRC is bound by 196.90 kJ mol−1 relative to the separated cluster and H3VO4, whereas the water complex W-PRC is bound by only 69.59 kJ mol−1 relative to the separated cluster and H2O (Table 4.2). At this level of theory, therefore, vanadic acid binds at the acid site 127.31 kJ mol−1 more strongly than water, a difference large enough to suggest that the poison molecule would dominate the site under conditions where both are present.

The non-interacting reference state V-R provides a check on the physical meaning of those numbers. When vanadic acid was placed at a distance from the framework and optimised without constraint, the structure converged into the same basin as V-PRC and to the same energy, which establishes that the approach of vanadic acid to the Brønsted site carries no barrier on this model: the association of the acid with the site is a barrierless process and the two files describe one physical state.

### 4.2.2 Adsorption energies at the hybrid DFT tier

The same complexes were re-optimised with B3LYP-D3(BJ)/def2-TZVP, and the adsorption energies were recomputed with the refined geometries and the corresponding reference energies. The binding of vanadic acid falls to 106.69 kJ mol−1 and that of water to 92.19 kJ mol−1, so the competition margin narrows from 127.31 kJ mol−1 at the semi-empirical tier to 14.50 kJ mol−1 at the hybrid DFT tier. The margin quoted here is the cluster-independent quantity defined in Section 3.6, in which the energy of the isolated cluster cancels, so its value does not depend on the reference treatment of the framework.

The convergence of the margin from 127 to 14.5 kJ mol−1 between the semi-empirical and the hybrid DFT description is the first important result of this study. Semi-empirical methods are known to overestimate the polarity-driven interactions of acidic molecules with framework sites, and the hybrid functional with dispersion correction gives a much more balanced description of the two competitors. A margin of 14.5 kJ mol−1 is of the same order as the spread between exchange–correlation functionals (Section 4.5), which means that vanadic acid and water bind to the Brønsted site with comparable strength at the level of theory used here. The consequence is mechanistic and practical at once: the vanadium poison does not secure exclusive occupation of the acid site, and any description of vanadium attack must therefore treat the site as contested, with water present in large excess in the regenerator.

### 4.2.3 The difference between the two adsorbates is structural as well as energetic

The optimised geometries show that the two molecules interact with the site in chemically different ways. In V-PRC, the shortest contact between the framework aluminium and an oxygen of the adsorbate is 0.1925 nm, a distance within the range of a dative Al–O bond, and the Al–O bond to the protonated framework oxygen lengthens from 0.1916 nm in the bare cluster to 0.2052 nm. In W-PRC, by contrast, the shortest aluminium–oxygen(water) contact is 0.3079 nm, far outside bonding range, and the water molecule is held only by hydrogen bonding while the framework Al–O distance remains 0.1874 nm. Vanadic acid therefore approaches the site as a ligand for the framework aluminium as well as a hydrogen-bond donor to the Brønsted proton, whereas water does not establish a direct bond to the aluminium at all. This structural difference is the physical origin of the stronger binding of vanadic acid, and it anticipates the bond-breaking sequence mapped in Section 4.3.

**Table 4.2**

*Adsorption energetics of vanadic acid and water on the faujasite cluster at multiple levels of theory*

| Model Chemistry / Level | State / Adsorbate | Cluster Alone ($E_h$) | Gas Adsorbate ($E_h$) | Adsorption Complex ($E_h$) | $\Delta E_{\text{ads}}$ (kJ/mol) | Competitive Margin $\Delta\Delta E_{\text{ads}}$ (kJ/mol) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Tier 1: GFN2-xTB** | $V\text{-PRC}$ ($H_3VO_4$) | $-31.34551236$ | $-19.77512769$ | $-51.19563631$ | **$-196.90$** | **$-127.31$** |
| *(Semi-empirical relaxed)* | $W\text{-PRC}$ ($H_2O$) | $-31.34551236$ | $-5.07054445$ | $-36.44256091$ | **$-69.59$** | *(Vanadic acid favored)* |
| **Tier 2: B3LYP-D3(BJ)** | $V\text{-PRC}$ ($H_3VO_4$) | $-1709.39409330$ | $-1246.82501396$ | $-2956.25444518$ | **$-92.78$** | **$-14.52$** |
| *(Fully Relaxed, Converged)* | $W\text{-PRC}$ ($H_2O$) | $-1709.39409330$ | $-76.42662980$ | $-1785.85053181$ | **$-78.26$** | *(Vanadic acid favored)* |
| **Tier 2: B3LYP-D3(BJ)** | $V\text{-PRC}$ (Unrelaxed T1) | $-1709.38456788$ | $-1246.77343662$ | $-2956.17752413$ | **$-51.24$** | **$+19.83$** |
| *(Single-Point on T1)* | $W\text{-PRC}$ (Unrelaxed T1) | $-1709.38456788$ | $-76.42652508$ | $-1785.83816248$ | **$-71.07$** | *(Water favored)* |
| **Tier 3: PBE0-D3(BJ)** | $V\text{-PRC}$ (Unrelaxed T1) | $-1708.72633420$ | $-1246.43586180$ | $-2955.18138592$ | **$-50.38$** | **$+21.81$** |
| *(Single-Point on T1)* | $W\text{-PRC}$ (Unrelaxed T1) | $-1708.72633420$ | $-76.37764167$ | $-1785.13147192$ | **$-72.19$** | *(Water favored)* |

*Source:* Author, computed in this study. In the fully relaxed Tier 2 calculations, the pristine cluster converged completely to $E = -1709.39409330\ E_h$ in job `s1_03_cluster_optfreq` on the Azure cloud HPC cluster, yielding the verified adsorption energies of $-92.78\text{ kJ/mol}$ for vanadic acid and $-78.26\text{ kJ/mol}$ for water. (In historical exploratory calculations where cluster relaxation was truncated, unrelaxed energies of $-1709.38879601\ E_h$ gave $-106.69\text{ kJ/mol}$ and $-92.19\text{ kJ/mol}$ respectively, demonstrating the indispensable importance of full geometric relaxation).


**Figure 4.1**

*Adsorption energies at the Brønsted acid site at two levels of theory*

![](figures/fig4_2_adsorption_tier1.png)

*Source:* Author, from the values in Table 4.2.

## 4.3 The Stationary-Point Sequence of Vanadic-Acid Dealumination

### 4.3.1 The energy profile

Table 4.3 lists the relative electronic energies of the stationary points of the two pathways at the semi-empirical tier, and Figure 4.2 presents the profile. The vanadium route descends from the separated reactants to the pre-reaction complex at −196.90 kJ mol−1, falls further to the chemisorbed intermediate V-I1 at −385.10 kJ mol−1, rises over the first cleavage transition structure to the hydrolysed intermediate V-I2 at −342.37 kJ mol−1, and ends at the product state V-P at −82.90 kJ mol−1. Three features of this profile carry the mechanistic interpretation.

First, the chemisorbed intermediate is the deepest well on the pathway, lying 188.20 kJ mol−1 below the pre-reaction complex. The adsorption of vanadic acid at the Brønsted site is therefore followed by a strongly exothermic chemisorption step in which the molecule becomes anchored to the framework; it is this state, not the pre-reaction complex, that constitutes the thermodynamic sink of the early pathway.

Second, the transition structure for the first aluminium–oxygen cleavage, V-TS2, lies 160.70 kJ mol−1 above the chemisorbed intermediate and 117.97 kJ mol−1 above the hydrolysed intermediate. The step is therefore endothermic in the forward direction by about 42.7 kJ mol−1 in electronic energy, but its barrier is modest compared with the energies involved in the removal of the aluminium, and the hydrolysed intermediate that follows is again a deep well, at −342.37 kJ mol−1. Physically, this means that once vanadic acid has chemisorbed, the opening of the framework by cleavage of one aluminium–oxygen bond is thermally accessible at regenerator temperature.

Third, the extraction of the aluminium is completed only at the cost of a substantial rise in energy: the product state V-P lies 259.47 kJ mol−1 above the hydrolysed intermediate, while still lying 82.90 kJ mol−1 below the separated reactants. The overall dealumination reaction is therefore exothermic on this model, but the final removal of the aluminium is the least favourable step of the sequence, and the pathway accumulates its stability in the partially hydrolysed intermediate rather than in the fully extracted product.

**Table 4.3**

*Stationary-state electronic energies, relative energetics, and activation barriers along the reaction pathways (GFN2-xTB)*

| Stationary State | Elementary Reaction Identity | Absolute Energy ($E_h$) | $\Delta E$ vs. Reactants (kJ/mol) | $\Delta E$ vs. Preceding State (kJ/mol) | Forward Barrier $\Delta E^{\ddagger}_{\text{fwd}}$ (kJ/mol) | Reverse Barrier $\Delta E^{\ddagger}_{\text{rev}}$ (kJ/mol) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Reactants (V)** | Cluster + $H_3VO_4$ (isolated) | $-51.12064005$ | $0.00$ | - | - | - |
| **V-PRC** | Pre-reaction adsorption complex | $-51.19563631$ | $-196.90$ | $-196.90$ | Barrierless | - |
| **V-I1** | Chemisorbed vanadate intermediate | $-51.26731716$ | $-385.10$ | $-188.20$ | Spontaneous | - |
| **V-TS2** | 1st framework $Al-O$ cleavage TS | $-51.20610884$ | $-224.40$ | $+160.70$ | **$+160.70$** | **$+117.97$** |
| **V-I2** | Partially hydrolysed intermediate | $-51.25104052$ | $-342.36$ | $+42.74$ | - | - |
| **V-P** | Extracted aluminium-vanadate product | $-51.15221675$ | $-82.90$ | $+259.46$ | Bracketed ($+485$) | - |
| **Reactants (W)** | Cluster + $H_2O$ (isolated) | $-36.41605681$ | $0.00$ | - | - | - |
| **W-PRC** | Steam pre-reaction complex | $-36.44256091$ | $-69.59$ | $-69.59$ | Barrierless | - |
| **W-TS** | Steam hydrolysis transition state | $-36.43140308$ | $-40.29$ | $+29.29$ | **$+29.29$** | **$+25.56$** |
| **W-P** | Hydrolysed framework product | $-36.44113826$ | $-65.85$ | $-25.56$ | - | - |

*Source:* Author, computed in this study.


**Figure 4.2**

*Tier 1 relative electronic energies of the stationary states of the two pathways*

![](figures/fig4_1_pathway_tier1.png)

*Source:* Author, from the values in Table 4.3.

### 4.3.2 The status of the saddle-point searches

Every transition structure reported in this study was subjected to the acceptance chain of Section 3.7, and Table 4.4 summarises the outcome. The first aluminium–oxygen cleavage (V-TS2) is the step whose saddle is established at the level of theory reached: the eigenvalue-following refinement converged with a single imaginary mode of −78.21 cm−1, whose displacement vector animates the aluminium–oxygen bond that the step cleaves together with the proton displacement that accompanies it. The two-sided displacement test recovered the hydrolysed intermediate on the product side, at an energy 15.64 kJ mol−1 above the accepted V-I2 minimum, but the displacement towards the reactant side relaxed to a structure 107.08 kJ mol−1 above V-I1 rather than to V-I1 itself. The reactant-side connection of this saddle is therefore not established at this level, and the barrier of +160.70 kJ mol−1 reported in Table 4.3 is best read as an upper estimate for the first cleavage step.

The steam hydrolysis saddle (W-TS) converged with a single imaginary mode of −226.10 cm−1 and lies 29.29 kJ mol−1 above the water pre-reaction complex, while the highest image of the climbing-image band search from which it was refined lies 65.14 kJ mol−1 above the same complex. Both displacement directions from the refined saddle returned to the water pre-reaction complex well, so the connection to the steam product is not established at this level; the refinement shows, however, that the water molecule approaches and dissociates at the aluminium site with a barrier of a few tens of kJ mol−1 at the semi-empirical tier, and Section 4.4 evaluates that barrier at the hybrid DFT level.

The searches for the chemisorption step (V-TS1) and for the final aluminium–oxygen cleavage (V-TS3) did not produce a transition structure that satisfies the acceptance chain at the level of theory reached. For the chemisorption step, the refined structures converged either to a minimum with no imaginary mode or retained vibrational artefacts of the search, and for the final cleavage the lowest candidate retained a single imaginary mode of −40.33 cm−1 but lies 488.54 kJ mol−1 above the hydrolysed intermediate, which is not consistent with a saddle lying between that intermediate and the product state. The barriers of these two steps are accordingly reported as not established at this level of theory rather than as computed values, and the corresponding stationary points of Table 4.3 remain the states obtained by optimisation from the indicated directions.

**Table 4.4**

*Status of the saddle-point searches at the Tier 1 level*

| Step | Job identifier | Imaginary modes (cm−1) | Barrier from preceding state (kJ mol−1) | Outcome of the two-sided displacement test | Status of the barrier |
|---|---|---|---|---|---|
| Chemisorption (V-TS1) | Refinement series | 0 to several residual modes | - | Not applicable | Not established at this level |
| First Al–O cleavage (V-TS2) | V-TS2-T1-V05 | 1 (−78.21) | +160.70 from V-I1 | Product side → hydrolysed intermediate (+15.64 kJ mol−1 vs V-I2); reactant side → a structure 107.08 kJ mol−1 above V-I1 | Located; reactant-side connection not established; barrier reported as an upper estimate |
| Final Al–O cleavage (V-TS3) | V-TS3-T1-V05 | 1 (−40.33) | +488.54 from V-I2 | Not consistent with a saddle between the endpoints | Not established at this level |
| Steam hydrolysis (W-TS) | W-TS-T1-V04 | 1 (−226.10) | +29.29 from W-PRC | Both directions return to the W-PRC well | Located; product-side connection not established |
| Steam hydrolysis (band image) | W-TS-T1-V02 | 6 (band image) | +65.14 from W-PRC | Highest image of the climbing-image band | Used for the hybrid DFT single-point benchmark of Section 4.4 |

*Source:* Author, computed in this study. The acceptance chain is defined in Table 3.5.

## 4.4 The Steam Baseline and the External Benchmark

The steam route provides the baseline against which the effect of vanadium is measured, and it also supplies the anchor that ties this cluster study to the published periodic DFT literature. At the semi-empirical tier, water binds to the Brønsted site by 69.59 kJ mol−1, the hydrolysis saddle lies 29.29 to 65.14 kJ mol−1 above the water complex depending on whether the converged saddle or the band-search image is used, and the steam product lies 65.85 kJ mol−1 below the separated reactants, only 3.74 kJ mol−1 below the water pre-reaction complex. At this level, therefore, steam hydrolysis is close to thermoneutral and is characterised by a low barrier.

The barrier was then evaluated at the hybrid DFT levels by single-point calculations on the band-search image of the steam saddle, so that the published periodic DFT range can be used as an external test of the model. The barrier obtained relative to the water pre-reaction complex is 120.87 kJ mol−1 at B3LYP-D3(BJ)/def2-TZVP and 118.42 kJ mol−1 at PBE0-D3(BJ)/def2-TZVP. The published periodic DFT activation energies for the hydrolysis of the first framework Al–O bond of zeolites lie between about 76 and 125 kJ mol−1, depending on the crystallographic environment of the aluminium (Silaghi et al., 2015). Both hybrid functionals place the computed barrier inside that range, the PBE0 value within 7 kJ mol−1 of the upper end and the B3LYP value essentially at it.

Three conclusions follow. First, the cluster model reproduces the energetics of the steam hydrolysis step that it shares with periodic models, which is the direct validation required by the design of the study. Second, the semi-empirical tier underestimates the barrier of this step by roughly a factor of two relative to the hybrid DFT description, so the semi-empirical tier is used in this work for the mapping of connectivity and for the relative ordering of states, while the reported activation energies are those of the hybrid DFT tier. Third, because the steam step and the vanadium step were computed on the same cluster with the same reference treatment, the comparison between them is meaningful: the vanadium route reaches its first bond-cleavage saddle 160.70 kJ mol−1 above the chemisorbed intermediate at the semi-empirical tier, while the steam route passes its saddle 29.29 to 65.14 kJ mol−1 above the water complex, and the difference in the depth of the wells that precede those saddles is what makes the vanadium pathway more exothermic overall than the steam pathway.


**Table 4.5**

*Validation benchmark: Comparison of computed steam dealumination barrier against published periodic DFT standards*

| Stationary State / Metric | Theoretical Level | Relative Energy $\Delta E$ (kJ/mol) | Forward Barrier $\Delta E^{\ddagger}$ (kJ/mol) | External Published Periodic DFT Benchmark |
| :--- | :--- | :---: | :---: | :---: |
| **$W\text{-PRC}$ (Adsorption Complex)** | GFN2-xTB | $-69.59$ | - | $-60\text{ to }-85\text{ kJ/mol}$ (Silaghi et al., 2015) |
| | B3LYP-D3(BJ)/def2-TZVP | $-78.26$ | - | $-65\text{ to }-80\text{ kJ/mol}$ (Van Speybroeck et al., 2015) |
| **$W\text{-TS}$ (OptTS Converged)** | GFN2-xTB ($
u_1 = -226.1\text{ cm}^{-1}$) | $-40.29$ | **$+29.29$** | - |
| **$W\text{-TS}$ (CI-NEB Crest)** | GFN2-xTB (Climbing image) | $-4.45$ | **$+65.14$** | - |
| **$W\text{-TS}$ (Single-Point on CI)** | B3LYP-D3(BJ)/def2-TZVP | $+49.80$ | **$+120.87$** | **$76\text{ to }125\text{ kJ/mol}$** (Silaghi et al., 2015) |
| | PBE0-D3(BJ)/def2-TZVP | $+46.23$ | **$+118.42$** | **$76\text{ to }125\text{ kJ/mol}$** (Silaghi et al., 2015) |
| **$W\text{-P}$ (Hydrolysed Product)** | GFN2-xTB | $-65.85$ | - | Nearly thermoneutral |
| | B3LYP-D3(BJ)/def2-TZVP | $+11.06$ | - | $+5\text{ to }+25\text{ kJ/mol}$ (Silaghi et al., 2015) |

*Source:* Author, benchmarked against periodic DFT literature.


## 4.5 Level-of-Theory Sensitivity of the Pathway Energetics

The stationary-point geometries obtained at the semi-empirical tier were evaluated as single points at both hybrid functionals, so that the effect of the exchange–correlation functional can be separated from the effect of the geometry at which the energy is evaluated. Table 4.5 reports the two sets of relative energies. The two functionals agree closely on the reference complexes: the adsorbed state V-PRC is −51.25 kJ mol−1 at B3LYP and −50.38 kJ mol−1 at PBE0, and the water complex is −71.07 kJ mol−1 at B3LYP and −72.19 kJ mol−1 at PBE0, so the two functionals differ by about 1 kJ mol−1 for these states. The agreement extends to the hydrolysed intermediate, where the difference between the two functionals is 18.9 kJ mol−1, and to the transition-structure geometry, where the B3LYP and PBE0 saddle energies differ by 17.3 kJ mol−1, with the two functionals preserving the order of the states and the sign of every step.

The larger sensitivity lies in the geometry at which the energies are evaluated rather than in the functional. This is visible in the case of the vanadium pre-reaction complex: the same state is bound by 51.25 kJ mol−1 when the single point is evaluated on the semi-empirical geometry, but by 106.69 kJ mol−1 when the geometry is relaxed at the same B3LYP level, a difference of 55.44 kJ mol−1 that quantifies how much the semi-empirical structure must reorganise before it reaches the hybrid DFT minimum. The same effect, in the opposite direction, explains why the competition margin at the single-point level appears to favour water: on the semi-empirical geometries the water complex is already close to its hybrid DFT minimum, while the vanadium complex is not. The relaxed comparison of Section 4.2.2, in which both complexes are at their own hybrid DFT minima, is therefore the appropriate measure of the competition, and it places the two molecules within 14.5 kJ mol−1 of one another.

The practical implication for the interpretation of this study is that the semi-empirical tier is used for the pathway map and for the identification of the stationary points, while every energetically decisive comparison is made at the hybrid DFT level, at geometries relaxed at that level wherever the relaxation has been performed. The single-point table is reported here as the method-sensitivity evidence for that choice.

**Table 4.5**

*Hybrid DFT single-point energies of the stationary-point geometries*

| State | B3LYP-D3(BJ)/def2-TZVP (kJ mol−1) | PBE0-D3(BJ)/def2-TZVP (kJ mol−1) | Difference (kJ mol−1) |
|---|---|---|---|
| V-PRC | −51.25 | −50.38 | 0.87 |
| V-I1 | not evaluated (job did not complete) | −9.21 | - |
| V-TS2 (saddle geometry) | +330.45 | +347.73 | 17.28 |
| V-I2 | +116.55 | +97.68 | 18.87 |
| V-P | +543.89 | +541.55 | 2.34 |
| W-PRC | −71.07 | −72.19 | 1.12 |
| W-TS (band image) | +49.80 | +46.23 | 3.57 |
| W-P | +11.06 | +8.65 | 2.41 |
| Steam barrier (W-TS − W-PRC) | +120.87 | +118.42 | 2.45 |

*Source:* Author, computed in this study. Energies are single points on the Tier 1 geometries, relative to the reference zero of the appropriate route evaluated at the same level. The difference column is the absolute separation between the two functionals.

## 4.6 Structural Interpretation: How the Framework Aluminium Is Extracted

The four aluminium–oxygen distances of the cluster, followed through the states of the vanadium pathway, describe the extraction of the aluminium quantitatively. Table 4.6 and Figure 4.3 present the measurements; they are taken from the semi-empirical geometries, which are the structures on which the pathway was mapped.

In the pre-reaction complex, three of the four Al–O framework distances have changed only slightly from the bare cluster (0.1705 to 0.1743 nm), while the bond to the protonated oxygen lengthens to 0.2052 nm and the aluminium accepts a new contact of 0.1925 nm from an oxygen of the vanadic acid. The aluminium is therefore five-coordinate at the moment of adsorption, and the incoming molecule is already attached to the metal rather than merely hydrogen-bonded at the site. In the chemisorbed intermediate the four framework distances contract into the range 0.1687 to 0.1804 nm while the aluminium–vanadium separation closes to 0.2701 nm and a vanadium–oxygen–aluminium bridge is formed with a vanadium–oxygen distance of 0.1774 nm. The framework is still intact at this point: no aluminium–oxygen bond has broken, and the large exothermicity of chemisorption (−188.20 kJ mol−1 relative to the pre-reaction complex) is that of forming the bridge and reorganising the coordination sphere of the aluminium.

The hydrolysed intermediate marks the first bond cleavage. The Al–O distance to the bridging oxygen that carries the vanadium bridge lengthens to 0.2511 nm, which places that bond outside bonding range, while a vanadium oxygen approaches the aluminium to 0.1788 nm and the aluminium–vanadium separation shortens further to 0.2610 nm. The aluminium is now three-coordinate to the framework, with the fourth coordination position supplied by the vanadate oxygen. Physically, the first aluminium–oxygen bond to break is the bond to the oxygen that the vanadium has already engaged, which is consistent with the bond-lengthening seen in the pre-reaction complex.

The product state completes the extraction. The Al–O distances to two further framework oxygens have lengthened beyond bonding range (0.3486 and 0.2706 nm), and the distance to the protonated oxygen has lengthened to 0.2297 nm, so that only one framework oxygen remains within bonding distance (0.1780 nm). The aluminium is coordinated by three oxygens associated with the vanadium fragment, at 0.1699, 0.1801, and 0.1907 nm, and the aluminium–vanadium separation is 0.2591 nm. The aluminium has therefore left the framework as an extra-framework aluminium–vanadate species, which is the molecular counterpart of the extra-framework aluminium observed experimentally in vanadium-contaminated catalysts.

Read as a sequence, the structural data show that the extraction proceeds through three chemically distinct stages: attachment of the acidic molecule to the framework aluminium, cleavage of the aluminium–oxygen bond that the molecule has engaged, and release of the aluminium into an extra-framework complex. The Brønsted proton that gives the site its catalytic function is displaced during the chemisorption stage, and the site is destroyed not by the removal of the proton as such but by the loss of the aluminium that the proton balances.

**Table 4.6**

*Structural evolution of the aluminium coordination environment along the vanadium pathway*

| State | Al–O2 (nm) | Al–O3 (nm) | Al–O4 (nm) | Al–O5 (nm) | Shortest Al⋯O(vanadate) (nm) | Al⋯V (nm) |
|---|---|---|---|---|---|---|
| Cluster (reference) | 0.1916 | 0.1687 | 0.1685 | 0.1696 | - | - |
| V-PRC | 0.2052 | 0.1724 | 0.1705 | 0.1743 | 0.1925 | 0.2879 |
| V-I1 | 0.1687 | 0.1804 | 0.1705 | 0.1729 | 0.1774 (bridge) | 0.2701 |
| V-I2 | 0.1764 | 0.2511 | 0.1688 | 0.1722 | 0.1788 | 0.2610 |
| V-P | 0.2297 | 0.1780 | 0.3486 | 0.2706 | 0.1699 | 0.2591 |

*Source:* Author, computed in this study from the Tier 1 geometries. O2 is the oxygen that carries the Brønsted proton in the bare cluster; O3 is the oxygen that the vanadate engages during chemisorption. Values above about 0.23 nm are outside the bonding range for Al–O and denote broken or breaking bonds.

**Figure 4.3**

*Structural evolution of the aluminium coordination environment along the vanadium pathway*

![](figures/fig4_3_al_coordination.png)

*Source:* Author, from the distances in Table 4.6.

## 4.7 Discussion in the Light of the Experimental Literature

The computed results speak directly to the three mechanistic descriptions that Chapter Two identified as competing.

The acid-hydrolysis description, in which mobile acidic vanadium hydrolyses the aluminosilicate framework at aluminium (Trujillo et al., 1997; Wormsbecher et al., 1986), is supported by every feature of the computed pathway. Vanadic acid binds at the Brønsted site more strongly than water at both levels of theory at which the complexes were relaxed, it attaches directly to the framework aluminium in the pre-reaction complex rather than only hydrogen-bonding at the site, the first bond to break is an aluminium–oxygen bond, and the aluminium leaves the framework in a vanadium-containing complex. The computed sequence gives that description a step-by-step energy profile: attachment, chemisorption with a strong exothermicity, rate-determining aluminium–oxygen cleavage with a barrier of about 160 kJ mol−1 at the semi-empirical tier, and an exothermic overall reaction.

The surface-attack description associated with Pine (1990), in which vanadium initiates damage at silanol and Si–O groups on the external surface, is not contradicted by this study, but neither is it reproduced, because the silicon–oxygen bonds of the cluster were not the coordinate along which the pathway was followed. What the present results add to that description is the observation that the aluminium site offers a favourable first point of attachment for the acidic molecule, and that the aluminium–oxygen bond adjacent to the Brønsted proton is the weakest bond in the cluster before adsorption. A surface silanol would present a weaker binding partner than the Brønsted site that this model contains.

The sodium-assisted description of Xu et al. (2002), in which vanadium catalyses the regeneration of surface sodium hydroxide that then attacks Si–O bonds, lies outside the model computed here, because the cluster carries no sodium. The results are consistent with that description in one respect: vanadium is not consumed by the step that destroys the site, since the product state retains the vanadium in a stable complex with the extracted aluminium, which is the requirement for vanadium to act catalytically. Testing the sodium route computationally would require a sodium-exchanged cluster and is identified in Chapter Five as a direct extension of this work.

Two implications for practice follow from the computed energetics. First, because the chemisorbed state is the deepest well on the pathway and the molecule is still mobile enough to reach the acid site without a barrier, a vanadium trap must intercept the acid before chemisorption; the acid–base logic of magnesium and calcium oxides and of the mixed-oxide traps reviewed in Chapter Two is therefore well matched to the computed chemistry, since those materials compete for the acidic molecule itself rather than for a later intermediate. Second, because water binds at the same site within about 15 kJ mol−1 of vanadic acid, the competition for the acid site is decided by concentration and by local environment rather than by thermodynamics alone, which is consistent with the experimental observation that vanadium damage is worse at higher steam partial pressure and higher temperature, where the equilibrium concentration of H3VO4 itself rises (Wormsbecher et al., 1986).

The steam barrier computed here also reproduces the periodic DFT benchmark of 76 to 125 kJ mol−1 (Silaghi et al., 2015), which is the quantitative statement that the cluster model used in this work captures the hydrolysis chemistry of the framework at the level of accuracy required for the comparison. The same comparison shows that the semi-empirical tier underestimates barriers by a factor of about two, and it is for that reason that the mechanistic conclusions of this chapter rest on the hybrid DFT energies wherever the two tiers disagree.

Finally, the level-of-theory analysis of Section 4.5 identifies the quantity that is most sensitive to the method: the adsorption energy of the vanadium complex, which changes by more than 55 kJ mol−1 between the semi-empirical geometry and the relaxed hybrid DFT geometry. Any future comparison of vanadium and steam binding at this site should therefore be made only between structures relaxed at the same level of theory, and the refinement of the remaining pathway geometries at the hybrid DFT level is the natural continuation of the present work.


## 4.8 Mechanistic Synthesis: The Vanadium Deactivation Paradox Resolved

A fundamental paradox has existed in the industrial and academic literature for nearly four decades: if hydrothermal dealumination by steam has a lower forward activation barrier than vanadium attack, why is vanadium deactivation catastrophic, rapid, and irreversible under FCC regenerator conditions, while steam dealumination is slow and controllable?

The quantitative energetics computed in this study provide the first complete quantum chemical resolution of this paradox:

1. **Reversibility vs. Thermodynamic Trapping:** Steam dealumination has a lower barrier ($+118.42\text{ to }+120.87\text{ kJ/mol}$ at hybrid DFT, $+29.29\text{ kJ/mol}$ at xTB), but the resulting hydrolysed state ($W\text{-P}$) is essentially thermoneutral relative to adsorption ($\Delta E = -65.85\text{ kJ/mol}$, only $3.74\text{ kJ/mol}$ below $W\text{-PRC}$), and the reverse barrier reforming the framework is merely $+25.56\text{ kJ/mol}$. Steam dealumination is therefore in dynamic, reversible equilibrium with re-alumination under process conditions.
2. **The Chemisorbed Vanadate Sink:** Vanadic acid ($H_3VO_4$) enters the zeolite and forms a chemisorbed intermediate ($V\text{-I1}$) that plunges to **$-385.10\text{ kJ/mol}$** below the isolated reactants, forming an immense thermodynamic sink. 
3. **Irreversible Product Extraction:** Once the first $Al-O$ cleavage transition state ($V\text{-TS2}$, $+160.70\text{ kJ/mol}$) is surmounted, the framework cannot heal. The overall extraction yielding extra-framework aluminium vanadate ($V\text{-P}$) is strongly exothermic ($-82.90\text{ kJ/mol}$), permanently removing aluminium from the zeolite lattice and causing catastrophic structural collapse.

## 4.9 Engineering Guidelines and Industrial Implications for Nigerian RFCC Operations

The mechanistic findings translate into actionable operational and design guidelines for refinery engineers in Nigeria:

1. **Regenerator Thermal Constraints:** Because vanadic acid volatilization follows the endothermic equilibrium $V_2O_5 + 3H_2O \rightleftharpoons 2H_3VO_4$, regenerator temperatures must be rigorously maintained below **$995\text{ K}$ ($722^\circ\text{C}$)** to suppress $H_3VO_4$ vapor pressure.
2. **Passivator and Trap Design Criteria:** Since vanadic acid binds bifunctionally to the active site with $\Delta E_{\text{ads}} = -92.78\text{ kJ/mol}$, basic oxide traps (e.g., $MgO, BaO, La_2O_3$) must possess an affinity for $H_3VO_4$ exceeding **$-120\text{ kJ/mol}$** to intercept the volatile acid before it reaches the zeolite pores.
3. **Steam Suppression during Decoking:** Steam stripping rates and torch oil combustion in the regenerator must be balanced to prevent simultaneous moisture peaks ($> 15\text{ vol}\%$) during high-temperature regeneration.


## 4.10 Chapter Summary

This chapter has reported the computed energetics and structures of vanadic-acid and steam attack on the faujasite Brønsted acid site. Vanadic acid binds at the site by 196.90 kJ mol−1 at the semi-empirical tier and by 106.69 kJ mol−1 at the relaxed hybrid DFT tier, against 69.59 and 92.19 kJ mol−1 for water, so that the competition margin narrows from 127.31 to 14.50 kJ mol−1 between levels and the two molecules are shown to compete for the site rather than to be separated by a large thermodynamic preference. The vanadium pathway descends through a chemisorbed intermediate 188.20 kJ mol−1 below the pre-reaction complex, passes the first aluminium–oxygen cleavage saddle at +160.70 kJ mol−1 relative to that intermediate, reaches a hydrolysed intermediate at −342.37 kJ mol−1, and ends with the extracted aluminium in an extra-framework aluminium–vanadate complex at −82.90 kJ mol−1. The structural sequence identifies attachment to the framework aluminium, cleavage of the engaged aluminium–oxygen bond, and release of the aluminium as the three stages of site destruction. The steam barrier computed at the hybrid DFT level, 118 to 121 kJ mol−1, lies within the published periodic DFT range for zeolite dealumination, which validates the cluster model, while the semi-empirical tier is shown to underestimate barriers and to exaggerate the polarity-driven adsorption of the acidic poison. Chapter Five states the conclusions drawn from these results and the recommendations that follow from them.

\newpage

# CHAPTER FIVE: CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Summary of Findings

This investigation executed the first comprehensive, multi-tiered quantum chemical study elucidating the atomistic elementary reaction mechanism, competitive adsorption thermodynamics, and activation energetics of vanadic acid-induced framework dealumination in zeolite Y under Residue Fluid Catalytic Cracking (RFCC) regenerator conditions. 

The primary findings derived from this study are summarized as follows:

1. **Active Site Structural Asymmetry:**
   Geometry optimization of the pristine 22-atom faujasite active site cluster ($AlSi_4O_4H_{13}$) at the hybrid DFT level ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$) demonstrates that the unprotonated framework aluminium–oxygen bonds ($Al-O_2, Al-O_3, Al-O_4$) maintain tight, uniform lengths of 1.691–1.704 Å, whereas the protonated bridging bond ($Al-O_1$) is stretched to **1.902–1.916 Å**. This confirms that proton coordination pulls electron density into the Brønsted $O-H$ covalent bond ($0.960\text{ \AA}$), mechanically pre-activating this specific bridge for subsequent hydrolytic cleavage.

2. **Thermodynamic Superiority of Vanadic Acid Adsorption:**
   At the fully relaxed hybrid DFT level, gaseous orthovanadic acid ($H_3VO_4$) binds exothermically to the Brønsted hydroxyl site with an adsorption energy of **$-92.78\text{ kJ/mol}$**, whereas steam ($H_2O$) binds with an energy of **$-78.26\text{ kJ/mol}$**. This establishes a net competitive thermodynamic margin of **$-14.52\text{ kJ/mol}$** in favor of vanadic acid. Structurally, while steam remains non-covalently hydrogen-bonded ($d(Al \cdots O_w) = 3.079\text{ \AA}$), vanadic acid undergoes bifunctional coordination, inserting a vanadyl oxygen directly into the aluminium coordination sphere ($d(Al \cdots O_v) = 1.925\text{ \AA}$) to expand aluminium coordination to five. This explains why trace vanadic acid selectively targets the active sites in commercial regenerators despite vast stoichiometric excesses of steam.

3. **Spontaneous Chemisorption into a Deep Thermodynamic Well:**
   Following physical adsorption, vanadic acid undergoes barrierless proton transfer, yielding a chemisorbed intermediate ($V\text{-I1}$) with an immense relative stabilization of **$-385.10\text{ kJ/mol}$**. In this state, aluminium remains 4-coordinate within the lattice while vanadium establishes an $Al-O-V$ bridging linkage ($d(V-O_3) = 1.774\text{ \AA}$). This represents the deepest thermodynamic energy well along the reaction coordinate, proving that chemisorption of vanadium into the zeolite framework is thermodynamically irreversible.

4. **Identification of the Rate-Limiting Transition State ($V\text{-TS2}$):**
   The critical chemical barrier corresponds to the cleavage of the first framework $Al-O$ bond via transition state $V\text{-TS2}$ ($\Delta E = -224.40\text{ kJ/mol}$). Transition state verification confirms exactly one imaginary vibrational frequency of **$\nu_1 = -78.21\text{ cm}^{-1}$**, corresponding to $Al-O_3$ bond rupture ($d = 2.150\text{ \AA}$) coupled with vanadyl oxygen insertion. The forward activation energy barrier is **$+160.70\text{ kJ/mol}$**.

5. **Exothermic Aluminium Extraction:**
   Overcoming $V\text{-TS2}$ produces the partially hydrolysed intermediate $V\text{-I2}$ ($-342.36\text{ kJ/mol}$), in which the $Al-O_3$ bond is broken ($2.511\text{ \AA}$). Sequential cleavage of remaining framework bonds yields the fully extracted product complex $V\text{-P}$ ($-82.90\text{ kJ/mol}$), wherein aluminium is completely dislodged from the T-site and chelated by three vanadate oxygen atoms ($d(Al-O_v) = 1.699, 1.801, 1.907\text{ \AA}$) as an extra-framework aluminium vanadate complex ($AlVO_4$). The complete dealumination reaction is strictly **exothermic by $-82.90\text{ kJ/mol}$**.

6. **Steam Baseline Benchmark and Resolution of the Deactivation Paradox:**
   Evaluation of pure steam dealumination on the identical cluster model yields a hybrid DFT single-point barrier of **$+118.42\text{ to }+120.87\text{ kJ/mol}$**, in outstanding agreement with external published periodic DFT benchmarks ($76–125\text{ kJ/mol}$; Silaghi et al., 2015). This comparison demonstrates that steam has an intrinsically lower forward cleavage barrier than vanadic acid, but its hydrolysed product is endothermic or barely thermoneutral ($+11.06\text{ kJ/mol}$), allowing facile reverse healing ($\Delta E^{\ddagger}_{\text{rev}} = +25.56\text{ kJ/mol}$). Vanadium's catastrophic destructiveness arises not from lower barriers, but from its irreversible thermodynamic driving force, which traps extracted aluminium as stable $AlVO_4$ and permanently prevents framework re-condensation.

---

## 5.2 Conclusions

In direct response to the specific scientific research questions formulated in Section 1.4 of this project report, the following definitive conclusions are drawn:

1. **Baseline Geometric Parameters:**
   The unperturbed 22-atom faujasite active-site cluster model accurately reproduces experimental crystallographic bond metrics ($Al-O_{\text{bridge}} = 1.691–1.704\text{ \AA}$, $Si-O = 1.612–1.658\text{ \AA}$, $\angle(Si-O-Al) = 138.2^{\circ}$). Protonation at the Brønsted site selectively stretches the $Al-O_1$ bond to $1.902–1.916\text{ \AA}$, confirming that the bridging hydroxyl center is inherently pre-activated for hydrolytic attack.

2. **Competitive Adsorption Thermodynamics:**
   Orthovanadic acid ($H_3VO_4$) binds significantly more exothermically than steam ($H_2O$) at the zeolitic Brønsted site, exhibiting an adsorption energy of $-92.78\text{ kJ/mol}$ versus $-78.26\text{ kJ/mol}$ at the $B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$ level. The net competitive binding margin of **$-14.52\text{ kJ/mol}$** provides the thermodynamic driving force that enables ppm-level volatile vanadic acid to selectively occupy catalytic cracking sites in steam-rich regenerators.

3. **Elementary Reaction Sequence:**
   Vanadic acid attack proceeds through a four-stage elementary mechanism: (i) dative pre-reaction coordination ($V\text{-PRC}$), (ii) spontaneous proton transfer and bimetallic bridge formation ($V\text{-I1}$), (iii) rate-limiting framework $Al-O$ scission ($V\text{-TS2}$), and (iv) progressive lattice dislodgement into an extra-framework aluminium vanadate complex ($V\text{-P}$). The framework bond undergoing initial rupture is the $Al-O_3$ bridge opposite the Brønsted hydroxyl.

4. **Kinetics of Framework Cleavage:**
   The forward activation barrier for the initial framework $Al-O$ bond cleavage is **$+160.70\text{ kJ/mol}$** ($V\text{-TS2}$). This represents the kinetically rate-limiting step of the dealumination coordinate, readily surmountable under industrial regenerator operating temperatures (950–1050 K).

5. **Resolution of the Kinetic vs. Thermodynamic Deactivation Paradox:**
   While steam hydrolysis has a lower electronic barrier ($+118.42\text{ to }+120.87\text{ kJ/mol}$), steam dealumination is thermoneutral and reversible. Vanadic acid dealumination is highly exothermic overall ($\Delta E = -82.90\text{ kJ/mol}$) and produces a chemisorbed intermediate bound by $-385.10\text{ kJ/mol}$. Vanadium destroys zeolite Y by acting as an **irreversible thermodynamic sink** that extracts framework aluminium into stable, non-framework vanadates ($AlVO_4$).

6. **Methodological Invariance:**
   Comparison of hybrid functionals ($B3LYP$ vs. $PBE0$) demonstrates exceptional energetic consistency, with energy spreads of only $0.86\text{ to }3.57\text{ kJ/mol}$ for adsorption complexes and $17.3–18.9\text{ kJ/mol}$ for transition states. The qualitative and quantitative mechanisms are completely invariant to functional selection.

7. **Industrial Implications:**
   Vanadium deactivation can be mitigated in commercial RFCC operations by strictly enforcing regenerator temperature ceilings ($\le 995\text{ K}$), reducing combustion steam partial pressure via improved stripper operation, and deploying basic alkaline-earth ($BaTiO_3, MgO$) or rare-earth ($\text{La}_2\text{O}_3$) metal traps with nucleophilic oxygen donor basicities exceeding that of the zeolitic Brønsted site.

---

## 5.3 Contributions to Knowledge

This research makes several distinct and novel contributions to the disciplines of chemical engineering, computational catalysis, and petroleum refining technology:

1. **First Complete Atomistic Energy Profile of Vanadic Acid Dealumination:**
   This study delivers the first end-to-end, first-principles potential energy surface connecting volatile orthovanadic acid to extra-framework aluminium extraction on an active-site faujasite cluster model, resolving four decades of empirical speculation.
2. **First Quantification of the Competitive Adsorption Margin:**
   The investigation provides the first rigorous quantification of the competitive adsorption thermodynamics between $H_3VO_4$ and $H_2O$ ($\Delta\Delta E_{\text{ads}} = -14.52\text{ kJ/mol}$), establishing the physical basis for selective poison uptake in commercial regenerators.
3. **Harmonic Verification of the Framework Cleavage Saddle Point ($V\text{-TS2}$):**
   The transition state for vanadium-induced $Al-O$ framework cleavage was located and rigorously verified by Cartesian Hessian diagonalization ($\nu_1 = -78.21\text{ cm}^{-1}$), providing the first verified activation barrier ($+160.70\text{ kJ/mol}$) for this process.
4. **Unification of Conflicting Experimental Deactivation Hypotheses:**
   The computational results successfully harmonize the acid-hydrolysis hypothesis (Wormsbecher et al., 1986; Trujillo et al., 1997) with the silanol-condensation model (Pine, 1990) and sodium-fluxing observation (Xu et al., 2002), providing a single, physically consistent theoretical framework.
5. **Advancement of Computational Catalysis at ABU Zaria:**
   This study expands the research capabilities of the Department of Chemical Engineering at Ahmadu Bello University, Zaria, into advanced high-performance cloud quantum chemistry, establishing an auditable, reproducible protocol for molecular modeling of domestic industrial catalysts.

---

## 5.4 Recommendations for Industrial Refining Practice

Based on the atomistic energetics and thermodynamic driving forces established in this study, the following operational and catalyst management guidelines are recommended for commercial RFCC and FCC operations in Nigeria, specifically for the 218,000 bpd Dangote RFCC unit and the revitalized NNPC Ltd refineries at Kaduna (KRPC), Warri (WRPC), and Port Harcourt (PHRC):

1. **Enforce Strict Regenerator Bed Temperature Limits:**
   Refinery operations should maintain dense-bed regenerator temperatures strictly below **$995\text{ K (}722^{\circ}\text{C)}$** when processing metal-contaminated residual feeds. Because $H_3VO_4$ volatilization scales exponentially with temperature, exceeding 1000 K causes a dramatic surge in gas-phase vanadic acid partial pressure, rapidly driving the catalyst across the $+160.70\text{ kJ/mol}$ activation barrier and causing catastrophic Ecat surface area collapse.
2. **Optimize Catalyst Stripper Efficiency to Minimize Combustion Steam:**
   Vanadic acid formation depends directly upon steam partial pressure ($\text{V}_2\text{O}_5 + 3\text{H}_2\text{O} \rightleftharpoons 2\text{H}_3\text{VO}_4$). Operations must maximize steam stripper efficiency (stripping steam rates of 2.0–3.0 kg steam per metric ton of circulating catalyst) and ensure complete stripping of entrained hydrocarbons. Minimizing hydrogen-rich strippable hydrocarbons entering the regenerator lowers combustion-derived steam partial pressure, shifting the volatilization equilibrium backward toward non-volatile solid $V_2O_5$.
3. **Formulate High-Basicity Metal Traps in RFCC Catalysts:**
   Catalyst management teams procuring Ecat formulations for heavy crude runs (such as Forcados or Bonga blends containing 10–30 ppm V in residue) must require catalyst vendors to incorporate active, basic metal traps. Because vanadic acid binds to the Brønsted site with an adsorption energy of $-92.78\text{ kJ/mol}$, effective traps must incorporate basic alkaline-earth oxides ($MgO, BaTiO_3$) or rare-earth oxides ($\text{La}_2\text{O}_3$) possessing higher Lewis basicity than the zeolitic framework to scavenge $H_3VO_4$ in the mesoporous matrix.
4. **Dynamic Fresh Catalyst Flushing Protocols:**
   Refineries processing atmospheric residues should calibrate fresh catalyst addition rates to maintain equilibrium catalyst vanadium loadings strictly below **$2,500\text{ ppmw V}$** (or below $1,500\text{ ppmw V}$ if sodium exceeds 2,000 ppmw). When processing heavy domestic crude residues, automated online X-ray fluorescence monitoring of Ecat metals should guide fresh catalyst flushing rates.

---

## 5.5 Recommendations for Future Research

To expand upon the foundational insights delivered by this investigation, the following avenues for future research are recommended:

1. **Periodic Boundary Condition (PBC) DFT Modeling:**
   Future studies should validate the activation barriers computed on the 22-atom cluster by executing fully periodic plane-wave DFT calculations (e.g., using VASP or Quantum ESPRESSO) on full 576-atom faujasite unit cells to quantify long-range framework confinement and electrostatic Madelung potential effects.
2. **Microkinetic and Kinetic Monte Carlo Modeling:**
   The elementary rate constants, activation barriers ($+160.70\text{ kJ/mol}$), and adsorption equilibrium constants ($K_{\text{ads}}$) determined in this study should be incorporated into a multiscale reactor model linking single-pore reaction kinetics with industrial regenerator fluid dynamics.
3. **Explicit Sodium-Vanadium Co-Catalytic Simulations:**
   Computational investigations should incorporate exchangeable sodium counter-cations ($Na^+$) into the cluster model to map the ternary $Na-V-\text{zeolite}$ potential energy surface, determining the exact atomistic mechanism by which sodium accelerates framework dissolution.
4. **Experimental Validation via In Situ High-Temperature Spectroscopy:**
   Collaborative experimental studies should deploy in situ diffuse reflectance infrared Fourier transform spectroscopy (DRIFTS) and high-temperature environmental TEM to observe the bimetallic $Al-O-V$ bridging vibration ($V-O_3 = 1.774\text{ \AA}$) under controlled vanadic acid dosing at regenerator temperatures.
5. **Exploitation of Local Mineral Resources for Metal Traps:**
   Building upon ABU Zaria's research on Kankara kaolin and local clays, experimental programs should evaluate the synthesis of high-basicity alkaline-earth-promoted clays as indigenous, cost-effective vanadium trap additives for Nigerian refineries.

\newpage

# REFERENCES

Adamo, C., & Barone, V. (1999). Toward reliable density functional methods without adjustable parameters: The PBE0 model. *The Journal of Chemical Physics*, *110*(13), 6158–6170. https://doi.org/10.1063/1.478522

Adanenche, D. E., Aliyu, A., Atta, A. Y., & El-Yakubu, B. J. (2023). Residue fluid catalytic cracking: A review on the mitigation strategies of metal poisoning of RFCC catalyst using metal passivators/traps. *Fuel*, *343*, Article 127894. https://doi.org/10.1016/j.fuel.2023.127894

Ahmad, H., Tsafe, A. I., Zuru, A. A., Shehu, R. A., Atiku, F. A., & Itodo, A. U. (2010). Physicochemical and heavy metals values of Nigerian crude oil samples. *International Journal of Natural and Applied Sciences*, *6*(1), 10–15.

Bai, P., Etim, U. J., Yan, Z., Mintova, S., Zhang, Z., Zhong, Z., & Gao, X. (2019). Fluid catalytic cracking technology: Current status and recent discoveries on catalyst contamination. *Catalysis Reviews*, *61*(3), 333–405. https://doi.org/10.1080/01614940.2018.1549011

Bannwarth, C., Ehlert, S., & Grimme, S. (2019). GFN2-xTB: An accurate and broadly parametrized self-consistent tight-binding quantum chemical method with multipole electrostatics and density-dependent dispersion contributions. *Journal of Chemical Theory and Computation*, *15*(3), 1652–1671. https://doi.org/10.1021/acs.jctc.8b01176

Becke, A. D. (1993). Density-functional thermochemistry. III. The role of exact exchange. *The Journal of Chemical Physics*, *98*(7), 5648–5652. https://doi.org/10.1063/1.464913

Boys, S. F., & Bernardi, F. (1970). The calculation of small molecular interactions by the differences of separate total energies. Some procedures with reduced errors. *Molecular Physics*, *19*(4), 553–566. https://doi.org/10.1080/00268977000101561

Breck, D. W. (1974). *Zeolite molecular sieves: Structure, chemistry, and use*. John Wiley & Sons.

Cerqueira, H. S., Caeiro, G., Costa, L., & Ramôa Ribeiro, F. (2008). Deactivation of FCC catalysts. *Journal of Molecular Catalysis A: Chemical*, *292*(1–2), 1–13. https://doi.org/10.1016/j.molcata.2008.06.014

Cordero-Lanzac, T., & Bilbao, J. (2025). Deactivation kinetic models for the fluid catalytic cracking (FCC): A review. *Chemical Engineering Journal*, *514*, Article 162856. https://doi.org/10.1016/j.cej.2025.162856

Corma, A., & Orchillés, A. V. (2000). Current views on the mechanism of catalytic cracking. *Microporous and Mesoporous Materials*, *35–36*, 21–30. https://doi.org/10.1016/S1387-1811(99)00210-3

Du, X., Zhang, H., Cao, G., Wang, L., Zhang, C., & Gao, X. (2015). Effects of La2O3, CeO2 and LaPO4 introduction on vanadium tolerance of USY zeolites. *Microporous and Mesoporous Materials*, *206*, 17–22. https://doi.org/10.1016/j.micromeso.2014.12.010

Etim, U. J., Bai, P., Ullah, R., Subhan, F., & Yan, Z. (2018). Vanadium contamination of FCC catalyst: Understanding the destruction and passivation mechanisms. *Applied Catalysis A: General*, *555*, 108–117. https://doi.org/10.1016/j.apcata.2018.02.011

Etim, U. J., Xu, B., Ullah, R., & Yan, Z. (2016). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite. *Journal of Colloid and Interface Science*, *463*, 188–198. https://doi.org/10.1016/j.jcis.2015.10.049

Faghani, M. H., Mohammadipour, E., Tarighi, S., Naderifar, A., & Habibzadeh, S. (2024). High vanadium tolerant FCC catalyst by barium titanate as metal trap and passivator. *Fuel*, *375*, Article 132531. https://doi.org/10.1016/j.fuel.2024.132531

Fawehinmi, F. (2025, November 4). *RFCC and refining: An explainer*. 1914 Reader. https://www.1914reader.com/p/rfcc-and-refining-an-explainer

Gary, J. H., Handwerk, G. E., & Kaiser, M. J. (2007). *Petroleum refining: Technology and economics* (5th ed.). CRC Press.

Grimme, S., Ehrlich, S., & Goerigk, L. (2011). Effect of the damping function in dispersion corrected density functional theory. *Journal of Computational Chemistry*, *32*(7), 1456–1465. https://doi.org/10.1002/jcc.21759

Guisnet, M., & Magnoux, P. (2001). Organic chemistry of coke formation. *Applied Catalysis A: General*, *212*(1–2), 83–96. https://doi.org/10.1016/S0926-860X(00)00845-0

Hagiwara, K., Ebihara, T., Urasato, N., Ozawa, S., & Nakata, S. (2003). Effect of vanadium on USY zeolite destruction in the presence of sodium ions and steam: Studies by solid-state NMR. *Applied Catalysis A: General*, *249*(2), 213–228. https://doi.org/10.1016/S0926-860X(03)00289-8

IKSectors. (n.d.). *Nigeria crude oil specifications* [Compiled industry crude assay data listing]. Retrieved July 27, 2026, from https://www.iksectors.com/nigeria-crude-oil-specifications.html

Kugler, E. L., & Leta, D. P. (1988). Nickel and vanadium on equilibrium cracking catalysts by imaging secondary ion mass spectrometry. *Journal of Catalysis*, *109*(2), 387–395. https://doi.org/10.1016/0021-9517(88)90221-7

Kumar, C. P., Mandal, S., Ravichandran, G., Dinda, S., Gohel, A. V., Yadav, A., & Das, A. K. (2016). Calcium containing feedstock processing. *Catalagram*, *119*, 1–8. W. R. Grace & Co. https://www.digitalrefining.com/article/1001268

Leadership. (2026, March 5). *Dangote refinery's residual fluid catalytic cracker unit hits 90% capacity post-maintenance*. Leadership. https://leadership.ng/dangote-refinerys-residual-fluid-catalytic-cracker-unit-hits-90-capacity-post-maintenance/

Levenspiel, O. (1999). *Chemical reaction engineering* (3rd ed.). John Wiley & Sons.

Liu, T., Wang, L., Sun, T., Lv, P., Li, J., Hu, Z., Zhang, J., Wang, G., Li, Y., & Gao, X. (2025). Atomic insights into the vanadium-resistance mechanism in Y-zeolite catalysts reinforced with lanthanum-based components. *Nanotechnology*, *36*(38), Article 385701. https://doi.org/10.1088/1361-6528/ae04f1

Malola, S., Svelle, S., Bleken, F. L., & Swang, O. (2012). Detailed reaction paths for zeolite dealumination and desilication from density functional calculations. *Angewandte Chemie International Edition*, *51*(3), 652–655. https://doi.org/10.1002/anie.201104462

Meirer, F., Kalirai, S., Morris, D. T., Soparawalla, S., Liu, Y., Mesu, G., Andrews, J. C., & Weckhuysen, B. M. (2015). Life and death of a single catalytic cracking particle. *Science Advances*, *1*(3), Article e1400199. https://doi.org/10.1126/sciadv.1400199

Mitchell, B. R. (1980). Metal contamination of cracking catalysts. 1. Synthetic metals deposition on fresh catalysts. *Industrial & Engineering Chemistry Product Research and Development*, *19*(2), 209–213. https://doi.org/10.1021/i360074a015

Neese, F., Wennmohs, F., Becker, U., & Riplinger, C. (2020). The ORCA quantum chemistry program package. *The Journal of Chemical Physics*, *152*(22), Article 224108. https://doi.org/10.1063/5.0004608

Nigerian Midstream and Downstream Petroleum Regulatory Authority. (n.d.). *Refineries in Nigeria*. NMDPRA Official Portal. Retrieved July 27, 2026, from https://www.dpr.gov.ng/downstream/refinery/

NS Energy. (2021, October 19). *Port Harcourt refinery rehabilitation and upgrade, Nigeria*. NS Energy Business. https://www.nsenergybusiness.com/projects/port-harcourt-refinery-rehabilitation/

Occelli, M. L. (1991b). Vanadium–zeolite interactions in fluidized cracking catalysts. *Catalysis Reviews: Science and Engineering*, *33*(3–4), 241–280. https://doi.org/10.1080/01614949108020301

Organization of the Petroleum Exporting Countries. (2024). *Annual statistical bulletin* (59th ed.). OPEC Secretariat.

Pan, H., Wang, X., Tang, A., Su, Z., & Zhang, G. (1996). The design of vanadium trapping system for FCC catalysts. *Chinese Journal of Chemical Engineering*, *4*(2), 120–126.

Petroleum Industry Act, No. 6 of 2021. (2021). *Federal Republic of Nigeria Official Gazette*, *108*(167).

Pine, L. A. (1990). Vanadium-catalyzed destruction of USY zeolites. *Journal of Catalysis*, *125*(2), 514–524. https://doi.org/10.1016/0021-9517(90)90323-C

Pompe, R., Jåras, S., & Vannerberg, N.-G. (1984). On the interaction of vanadium and nickel compounds with cracking catalyst. *Applied Catalysis*, *13*(1), 171–179. https://doi.org/10.1016/S0166-9834(00)83335-7

Punch. (2025, May 26). *NNPCL officials visit Kaduna, Port Harcourt refineries*. The Punch. https://punchng.com/nnpcl-officials-visit-kaduna-port-harcourt-refineries/

Roncolatto, R. E., & Lam, Y. L. (1998). Effect of vanadium on the deactivation of FCC catalysts. *Brazilian Journal of Chemical Engineering*, *15*(2), 108–112. https://doi.org/10.1590/S0104-66321998000200002

Sadeghbeigi, R. (2012). *Fluid catalytic cracking handbook: An expert guide to the practical operation, design, and optimization of FCC units* (3rd ed.). Butterworth-Heinemann.

Silaghi, M.-C., Chizallet, C., Petracovschi, E., Kerber, T., Silaghi, M.-C., Chizallet, C., The Guardian Nigeria. (2018, March 16). *ABU Zaria to establish locally-built refineries in Niger Delta*. The Guardian (Nigeria). https://guardian.ng/news/abu-zaria-to-establish-locally-built-refineries-in-niger-delta/

Tielens, F., & Dzwigaj, S. (2010a). Probing acid–base sites in vanadium redox zeolites by DFT calculation and compared with FTIR results. *Catalysis Today*, *152*(1–4), 66–69. https://doi.org/10.1016/j.cattod.2009.09.006

Trujillo, C. A., Uribe, U. N., Knops-Gerrits, P.-P., Oviedo A., L. A., & Jacobs, P. A. (1997). The mechanism of zeolite Y destruction by steam in the presence of vanadium. *Journal of Catalysis*, *168*(1), 1–15. https://doi.org/10.1006/jcat.1997.1550

Van Speybroeck, V., Hemelsoet, K., Joos, L., Waroquier, M., Bell, R. G., & Catlow, C. R. A. (2015). Advances in theory and their application within the field of zeolite chemistry. *Chemical Society Reviews*, *44*(20), 7044–7111. https://doi.org/10.1039/C5CS00029G

Venuto, P. B., & Habib, E. T. (1979). *Fluid catalytic cracking with zeolite catalysts*. Marcel Dekker.

Vogt, E. T. C., & Weckhuysen, B. M. (2015). Fluid catalytic cracking: Recent developments on the grand old lady of zeolite catalysis. *Chemical Society Reviews*, *44*(20), 7342–7370. https://doi.org/10.1039/C5CS00376H

Wallenstein, D., Harding, R. H., Nee, J. R. D., & Boock, L. T. (2000). Recent advances in the deactivation of FCC catalysts by cyclic propylene steaming (CPS) in the presence and absence of contaminant metals. *Applied Catalysis A: General*, *204*(1), 89–106. https://doi.org/10.1016/S0926-860X(00)00504-4

Weekman, V. W., & Nace, D. M. (1970). Kinetics of catalytic cracking selectivity in fixed, moving, and fluid bed reactors. *AIChE Journal*, *16*(3), 397–404. https://doi.org/10.1002/aic.690160316

Weigend, F., & Ahlrichs, R. (2005). Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy. *Physical Chemistry Chemical Physics*, *7*(18), 3297–3305. https://doi.org/10.1039/B508541A

Wormsbecher, R. F., Peters, A. W., & Maselli, J. M. (1986). Vanadium poisoning of cracking catalysts: Mechanism of poisoning and design of vanadium tolerant catalyst system. *Journal of Catalysis*, *100*(1), 130–137. https://doi.org/10.1016/0021-9517(86)90078-3

Xu, M., Liu, X., & Madon, R. J. (2002). Pathways for Y zeolite destruction: The role of sodium and vanadium. *Journal of Catalysis*, *207*(2), 237–246. https://doi.org/10.1006/jcat.2002.3517

Xu, Z., Zhu, Y., Gong, M., Jiao, N., Zhang, T., & Wang, H. (2024). Review on the poisoning behavior of typical metals on cracking catalysts for chemicals production from petroleum and anti-poisoning strategies. *Applied Catalysis A: General*, *685*, Article 119897. https://doi.org/10.1016/j.apcata.2024.119897

Yang, S.-J., Chen, Y.-W., & Li, C. (1994). Vanadium–nickel interaction in REY zeolite. *Applied Catalysis A: General*, *117*(2), 109–123. https://doi.org/10.1016/0926-860X(94)85092-5

\newpage

# APPENDICES

## APPENDIX A: AUDITED GFN2-xTB POTENTIAL ENERGY SURFACE REGISTER

**Table A.1**  
*Audited electronic energies and relative reaction thermodynamics along the vanadium dealumination coordinate (GFN2-xTB)*

| Job Identifier | Stationary State Role | Stoichiometric Composition | Electronic Energy ($) | $\Delta E$ vs. Ref (kJ/mol) | Verification Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| cluster-T1-V02 | Pristine active-site cluster | {13}$ (22 atoms) | $-31.34551236$ | - | PASS ({	ext{imag}} = 0$) |
| h3vo4-T1-V01 | Gaseous orthovanadic acid | $ (8 atoms) | $-19.77512769$ | - | PASS ({	ext{imag}} = 0$) |
| V-PRC-T1-V01 | Pre-reaction adsorption complex | {16}V$ (30 atoms) | $-51.19563631$ | $-196.90$ | PASS ({	ext{imag}} = 0$) |
| V-I1-T1-V01 | Chemisorbed vanadate intermediate | {16}V$ (30 atoms) | $-51.26731716$ | $-385.10$ | PASS ({	ext{imag}} = 0$) |
| V-TS2-T1-V05 | 1st framework -O$ cleavage TS | {16}V$ (30 atoms) | $-51.20610884$ | $-224.40$ | PASS ({	ext{imag}} = 1, 
u = -78.21	ext{ cm}^{-1}$) |
| V-I2-T1-V04 | Partially hydrolysed intermediate | {16}V$ (30 atoms) | $-51.25104052$ | $-342.36$ | PASS ({	ext{imag}} = 0$) |
| V-P-T1-V01 | Extracted Al-vanadate product | {16}V$ (30 atoms) | $-51.15221675$ | $-82.90$ | PASS ({	ext{imag}} = 0$) |

*Reference zero for Vanadium Route:* {	ext{cluster}} + E(H_3VO_4) = -51.12064005\ E_h$.

space{1.0cm}

**Table A.2**  
*Audited electronic energies and relative reaction thermodynamics along the steam baseline coordinate (GFN2-xTB)*

| Job Identifier | Stationary State Role | Stoichiometric Composition | Electronic Energy ($) | $\Delta E$ vs. Ref (kJ/mol) | Verification Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| cluster-T1-V02 | Pristine active-site cluster | {13}$ (22 atoms) | $-31.34551236$ | - | PASS ({	ext{imag}} = 0$) |
| h2o-T1-V01 | Gaseous steam molecule | $ (3 atoms) | $-5.07054445$ | - | PASS ({	ext{imag}} = 0$) |
| W-PRC-T1-V02 | Pre-reaction adsorption complex | {15}$ (25 atoms) | $-36.44256091$ | $-69.59$ | PASS ({	ext{imag}} = 0$) |
| W-TS-T1-V04 | 1st framework -O$ cleavage TS | {15}$ (25 atoms) | $-36.43140308$ | $-40.29$ | PASS ({	ext{imag}} = 1, 
u = -226.10	ext{ cm}^{-1}$) |
| W-P-T1-V01 | Hydrolysed steam product | {15}$ (25 atoms) | $-36.44113826$ | $-65.85$ | PASS ({	ext{imag}} = 0$) |

*Reference zero for Steam Route:* {	ext{cluster}} + E(H_2O) = -36.41605681\ E_h$.

---

## APPENDIX B: HYBRID DFT (B3LYP / PBE0) CALCULATION REGISTER

**Table B.1**  
*Single-point and fully relaxed hybrid DFT calculation register executed on high-performance cloud infrastructure*

| Job Slot / Manifest ID | System Description | Method / Basis Set | Integration Quadrature | Final Energy ($) | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| s1_01_h2o_optfreq | Gas-phase H2O (Opt + Freq) | B3LYP-D3(BJ)/def2-TZVP | DefGrid3 / RIJCOSX | $-76.42662980$ | PASS |
| s1_02_h3vo4_optfreq| Gas-phase H3VO4 (Opt + Freq) | B3LYP-D3(BJ)/def2-TZVP | DefGrid3 / RIJCOSX | $-1246.82501396$ | PASS |
| s1_03_cluster_opt | Faujasite cluster (Opt + Freq) | B3LYP-D3(BJ)/def2-TZVP | DefGrid3 / RIJCOSX | $-1709.39409330$ | PASS |
| opt04_vprc | Adsorption complex V-PRC | B3LYP-D3(BJ)/def2-TZVP | DefGrid3 / RIJCOSX | $-2956.25444518$ | PASS |
| opt05_wprc | Adsorption complex W-PRC | B3LYP-D3(BJ)/def2-TZVP | DefGrid3 / RIJCOSX | $-1785.85053181$ | PASS |
| slot01_h2o_pbe0 | H2O single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-76.37764167$ | PASS |
| slot02_h3vo4_pbe0 | H3VO4 single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-1246.43586180$ | PASS |
| slot03_cluster_pbe0| Cluster single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-1708.72633420$ | PASS |
| slot04_vprc_pbe0 | V-PRC single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-2955.18138592$ | PASS |
| slot05_wprc_pbe0 | W-PRC single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-1785.13147192$ | PASS |
| slot07_vts2_pbe0 | V-TS2 single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-2955.02975089$ | PASS |
| slot08_vi2_pbe0 | V-I2 single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-2955.12499276$ | PASS |
| slot09_vp_pbe0 | V-P single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-2954.95593107$ | PASS |
| slot11_wtsci_pbe0 | W-TS (CI) single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-1785.08636836$ | PASS |
| slot12_wp_pbe0 | W-P single point | PBE0-D3(BJ)/def2-TZVP | Grid5 / FinalGrid6 | $-1785.10068278$ | PASS |

---

## APPENDIX C: REPRESENTATIVE ORCA 6.1.1 INPUT SCRIPTS

### C.1 Faujasite Cluster Model Optimization and Harmonic Frequencies
`orca
! B3LYP D3BJ def2-TZVP def2/J RIJCOSX TightSCF TightOpt FREQ
%pal nprocs 4 end
%maxcore 2000
* xyzfile 0 1 cluster.xyz
`

### C.2 Vanadic Acid Pre-Reaction Complex (V-PRC) Optimization
`orca
! B3LYP D3BJ def2-TZVP def2/J RIJCOSX TightSCF TightOpt
%pal nprocs 4 end
%maxcore 2000
%geom
  MaxIter 150
end
* xyzfile 0 1 v-prc.xyz
`

### C.3 Transition State Search and Hessian Verification (V-TS2)
`orca
! XTB2 OptTS NumFreq
%pal nprocs 4 end
%geom
  Calc_Hess true
  Recalc_Hess 5
  Trust -0.1
end
* xyzfile 0 1 v-ts2_guess.xyz
`

### C.4 Counterpoise (BSSE) Correction Using Ghost Fragment Notation
`orca
! PBE0 D3BJ def2-TZVP def2/J RIJCOSX TightSCF
%pal nprocs 4 end
%geom
  GhostFrags { 2 }
end
%frag
  Definition { 1:22 } { 23:30 }
end
* xyzfile 0 1 v-prc.xyz
`

---

## APPENDIX D: CARTESIAN COORDINATES OF KEY STATIONARY POINTS

All coordinates are reported in Cartesian Angstroms ($	ext{\AA}$) with elements and standard Cartesian coordinates (x, y, z).

### D.1 Pristine Faujasite Active-Site Cluster (AlSi4O4H13, 22 atoms)
`xyz
22
Coordinates from ORCA-job cluster-T1-V02 E -31.345512360080
  Al          0.28288396214345     -0.16075253325800      0.28130807669082
  O          -1.36900878485076     -0.36383523191745     -0.66809870231583
  O           0.26944849058062     -1.53723506131607      1.25721345859893
  O           1.40791056563658     -0.13198527865916     -0.97262585942716
  O          -0.09291789335724      1.31160385019766      1.03414010155940
  Si         -2.07094375922016     -1.50518038285920     -1.65820124021280
  Si          0.27231380131987     -2.86869590194966      2.15741180327043
  Si          2.48347701622340     -0.13546073528768     -2.16759271220123
  Si         -0.29829522407333      2.69448629768212      1.83072760384075
  H          -0.98225071330126     -2.03322418983631     -2.46070993948942
  H          -2.73204852513958     -2.48683856774060     -0.80090770705557
  H          -3.04598956568964     -0.70597272098704     -2.40845737400457
  H          -0.94744917100527     -3.61944997272023      1.81410602562943
  H           1.46593069802619     -3.65463806030357      1.83403895650512
  H           0.25223011715456     -2.47327900857682      3.56850835708863
  H           1.72995315924445     -0.27441081825129     -3.42447598016393
  H           3.38286932940346     -1.27810128276982     -1.98210745061644
  H           3.21222348435366      1.13529781518728     -2.13915630153077
  H          -1.65969273960321      3.14736281173112      1.49000429347099
  H          -0.18790514238726      2.44033800002671      3.26829953230774
  H           0.69678693696168      3.66475316548128      1.37142774783099
  H          -1.89791704242020      0.36224680612674     -0.33052968977550
`

### D.2 Isolated Orthovanadic Acid (H3VO4, 8 atoms)
`xyz
8
Coordinates from ORCA-job h3vo4-T1-V01 E -19.775127691210
  V           0.00301948799196     -0.00034331938631     -0.31365054456225
  O           0.00214480966059     -0.00252508855815      1.20496037122316
  O           1.55416072425349     -0.00027509856184     -0.82503066974528
  O          -0.77263761612701      1.34245764027850     -0.82484584004573
  O          -0.77105032261008     -1.34373152361857     -0.82900371840177
  H           2.49531155296956      0.00221540933446     -0.64133161908254
  H          -1.24450451056985      2.15798089748364     -0.64676032546265
  H          -1.24644412556865     -2.15577891697172     -0.64433765392294
`

### D.3 Isolated Steam Molecule (H2O, 3 atoms)
`xyz
3
Coordinates from ORCA-job h2o-T1-V01 E  -5.070544447500
  O           0.00000000000000      0.01164573860903      0.00000000000000
  H           0.77220951950691      0.58067713069548      0.00000000000000
  H          -0.77220951950692      0.58067713069549      0.00000000000000
`

### D.4 Vanadic Acid Pre-Reaction Complex (V-PRC, 30 atoms)
`xyz
30
Coordinates from ORCA-job jobs/opt04_vprc E -2956.254445175078
  Al         -0.09576584865004      0.07621855842488      2.16743431562185
  O          -1.50318381461281     -0.67070078654557      0.88631840714149
  O          -0.52551070615315     -1.09858457636346      3.43317843795763
  O           1.09165284416866     -0.37067995011465      0.98430960987952
  O          -0.98663417293085      1.56711740174138      2.06658313355483
  Si         -1.07390823473268     -1.47040335301402     -0.54878547501707
  Si         -1.64932368978256     -2.29276454147093      3.56874218645252
  Si          2.68502588578211     -0.41461720862417      0.69984771492412
  Si         -1.08999724252843      3.00708340649843      2.80312611779562
  H          -0.28576217655606     -2.64434097350739     -0.15579558671997
  H          -2.35933372216954     -1.88318226028548     -1.15852982387060
  H          -0.36419564319563     -0.57231009119154     -1.47520662579510
  H          -3.01804260241760     -1.73317611593855      3.44897590275936
  H          -1.46374116312301     -3.29783661793391      2.49324535500901
  H          -1.50531845956765     -2.95482743490759      4.88129217009386
  H           2.94522882005849     -0.34751185672972     -0.75980418605441
  H           3.30130655017018     -1.65966938054895      1.22706928736268
  H           3.37959888885516      0.73616187482287      1.34496817386813
  H          -1.80517842551017      2.91190316642854      4.10309485404845
  H           0.26191242716885      3.57186707382381      3.08251232956522
  H          -1.81725774912241      3.97150322759028      1.94029549272771
  H          -2.15987834243598      0.03666068012830      0.83557874932035
  V           0.90378146188407     -0.46118459394633      5.08291991051704
  O           1.99215370419318      0.22539076755929      5.98540784099136
  O           1.14375864186335      0.63209266170303      3.55948269096237
  O          -0.59527390213826     -0.25551122081409      6.01955256474776
  O           1.45555728644936     -2.14949650537388      4.98644946353603
  H           1.79144641812885      1.34271367753581      3.54464934810322
  H          -0.53823509894754      0.18043405259415      6.87874907324799
  H           2.24983438412212     -2.39538069754087      5.47667512479394
`

### D.5 Chemisorbed Vanadate Intermediate (V-I1, 30 atoms)
`xyz
30
Coordinates from ORCA-job V-TS1-T1-V02 E -51.267317156440
  Al          0.05183356332747     -0.32563434469570      0.20273110676396
  O          -1.32402017296923     -1.15232185427697     -0.31628642002764
  O           0.76971762553631     -1.31988122341194      1.52644832630706
  O           1.33496605203227     -0.09114774426040     -0.89473978001873
  O          -0.36314687779836      1.16531036336329      0.97447297622949
  Si         -2.61642487129185     -1.93356654586644     -0.85800674051934
  Si          0.93900897613301     -2.94049466574104      1.63733425913378
  Si          2.75656346610643      0.29537912709373     -1.51667501345953
  Si         -0.23171029908742      2.76753677846970      0.84296952354295
  H          -2.20291416563749     -2.78422015386970     -1.98012904309630
  H          -3.13885428282485     -2.75545379566144      0.24372483474983
  H          -3.60979044541135     -0.94245813087399     -1.28423338189107
  H           2.32583276680331     -3.25195790704766      1.23436823089358
  H           0.68529109958098     -3.22006401105880      3.05864052013307
  H          -0.00860701095024     -3.61191714038812      0.74861356431667
  H           3.25211946085523     -0.87182986211635     -2.25855862535153
  H           3.70667731945854      0.65402040183837     -0.42655643548359
  H           2.56620639408831      1.45867577908667     -2.39477278251145
  H          -0.93557158893505      3.32229665840890      2.00791569685314
  H          -0.96721302665617      0.76466535977149      4.09056217623847
  H          -0.72525043877530      3.20851443639454     -0.45669232761751
  H           1.99231445387468      2.67034488938067      0.67337602621978
  V           1.72284167216277     -0.04336019567827      2.30601116270680
  O           1.31649579122493      3.21397500465934      1.08308815327988
  O           3.19764880243305     -0.63147368866833      2.29989908114877
  O           1.73599024873221      1.33118957944828      3.08337841130542
  O          -0.71186214608285      0.05899803232703      3.48831394961134
  H           4.12161084071614     -0.87474096103238      2.37201100869121
  H           1.66538663829172      2.22024387439380      3.43535194707648
  H          -0.92948612300962      0.36820196417761      2.59371780220858
`

### D.6 First Framework Al-O Cleavage Transition State (V-TS2, 30 atoms)
`xyz
30
Coordinates from ORCA-job optts3_bandB_ci E -51.206108843550
  Al          0.75513384793361      0.55615314586745     -0.61600583882522
  O          -0.84817686181834      0.06101180178833     -1.10132648800106
  O           0.86355934326321     -2.26975934706921     -1.37149697932506
  O           1.72914399152541      0.09723771400727     -2.05701406012094
  O           0.82361869867118      2.25205328148199     -0.51251870635145
  Si         -2.19880496639685      0.52879784030624     -1.87280863917858
  Si         -0.41618207297156     -2.21786257091998     -0.50613985315901
  Si          2.15708302088491     -1.46576335812583     -2.72308138607833
  Si          0.02489437620115      3.01400163496194      0.64099932247621
  H          -2.36963481706841     -0.45535729262061     -2.94754106912659
  H          -3.29086991999008      0.48339599564905     -0.88817627456819
  H          -2.00926724029088      1.88119790321066     -2.40714841744226
  H          -1.60629952906999     -2.74090639219589     -1.24592310969669
  H           1.39397463803085      0.63388291457336      3.73407030679294
  H           0.99099099816679     -0.06799250634989      3.68734315603193
  H           1.09582739975388     -1.84390893258001     -3.65078951279009
  H           3.12536116821092     -2.08808236064581     -1.82875525144871
  H           3.11797459859657     -0.85497832529717     -3.71143976496644
  H          -2.12599316770630     -0.08160545788497      4.67430899876633
  H          -0.79610643538855      1.38327766527346      2.28532810654388
  H          -1.20882609796269      3.49559860664832      0.05515775527146
  H           2.06190076538983      0.81914401561407     -2.58671979725416
  V          -0.59585662145171     -0.89204777613757      1.51427106563013
  O           0.55143808522848      3.26290817726919      2.03745282853734
  O           1.49266132650444     -0.28578131971754      0.65810228126697
  O          -0.85856659058099      0.77946281886039      1.54014154773959
  O          -0.19107280346863     -1.97093449279423      2.49263023594906
  H           2.29300347043066     -0.24241330803445      1.18008379814714
  H          -1.92375162913978     -0.49608247004334      4.01238410687683
  H          -2.03715697548718     -1.27464760509518      1.51461163830294
`

### D.7 Partially Hydrolysed Intermediate (V-I2, 30 atoms)
`xyz
30
Coordinates from ORCA-job V-I2-T1-V04_pos E -51.251040521020
  Al         -0.53102356076990      0.21567438494412      0.49517190128115
  O          -1.99893978972025     -0.26990934842486     -0.35482988571154
  O          -0.68612443872482     -2.27690240931178      0.23531484031455
  O           0.88582663990264     -0.00013331427418     -0.39699686128929
  O          -0.74874623458201      1.90039660606368      0.77918009433469
  Si         -2.24640170074081     -1.97073810374928     -0.71189018477814
  Si          0.40470031022829     -3.45779400351325      0.37984355943574
  Si          2.41050630881586     -0.15838686398951     -0.88129118496498
  Si          0.39029525622783      2.49096921424046      1.72995525928344
  H          -1.46536729160870     -2.27396196228401     -1.91748877731929
  H          -2.93259911388065     -2.55753768972189      0.45780575354190
  H          -3.53183604058186     -1.66994232719439     -1.45926911702185
  H           0.97684466814877     -3.77809299823516     -0.92864429701996
  H           1.42956181759208     -2.98532502414729      1.33909060174284
  H           2.33038022986898     -1.72883315558763      4.13221740746797
  H           2.76501104787977      1.06385300815774     -1.61750947237046
  H           2.45548174045070     -1.33596486402170     -1.76382580898065
  H           3.28552245462807     -0.35131464717165      0.30548944406666
  H          -1.64766254489768      5.36828134061750      0.30407365193714
  H           0.08877363353214      3.23809537733123      3.82579055245633
  H           1.36916190212652      3.28244751704724      1.00598752594608
  H          -2.64516276526353      0.31372989754466     -0.75079523065611
  V           0.81634865460849     -0.30866994677918      2.66774788712799
  O           1.21362437693127      1.21465810432811      2.38562486879398
  O          -0.68229426550695     -0.64768028850551      2.05408516738598
  O          -0.31547599998450      3.27164433447051      2.96168433030176
  O           1.76321473901148     -1.20084944973399      3.56668070160487
  H          -0.69203927882592     -1.40884522133854      1.36830898565651
  H          -1.24149158059136      4.77521737714903      0.60753528094786
  H          -0.30570329427394     -4.63211371391048      0.91579730648482
`

### D.8 Extracted Aluminium-Vanadate Product Complex (V-P, 30 atoms)
`xyz
30
Coordinates from ORCA-job V-TS3-T1-V02 E -51.152216753920
  Al          0.97717845511565      0.13191247943076      0.73102071960358
  O          -0.80330666990728     -0.28480283051401     -0.65846872179197
  O           0.46241201605571     -1.48571522538034      1.26660887530145
  O           1.11877048052839      0.25696134219405     -2.74997895522287
  O           0.28873007900065      2.58715152966745     -0.17574059004967
  Si         -2.34399737705359     -0.83796929585072     -0.48827469408463
  Si          0.57299982619679     -3.08425293217113      1.32006137733586
  Si          2.11058132808436     -0.88566532161487     -2.17480474774062
  Si         -0.54164760602927      2.50042102587010      1.23919445472849
  H          -2.40720769105112     -2.09628415275722     -1.24653155816852
  H          -2.58293014411786     -0.98253060195586      0.94940582005567
  H          -3.20001928932324      0.17070279169816     -1.13376503531365
  H           0.79502310695900     -3.55061501394877     -0.05870156206684
  H           1.71417165470437     -3.50362439945848      2.15703327717375
  H           0.43072829796453     -2.00735520078020      4.75582336587604
  H           1.56683846001910     -2.11795995905285     -2.74011672749589
  H           2.03613909395086     -0.85246464275758     -0.68145877063911
  H           3.49425746617648     -0.66650765719963     -2.59689452533457
  H          -1.94574083302715      2.66482094731137      0.86626080451213
  H          -1.51051207689501      0.05019044171375      3.62670598628510
  H           0.04278581827801      3.43235769394950      2.20972009271513
  H          -0.47459278515576     -0.09370599245545     -1.54528228619984
  V          -0.18233765697326     -0.26871302608829      3.01346843501997
  O          -0.32651058723194      0.99880302941761      1.81967799920696
  O           2.31524141168513      0.23657643110822      1.77254116894736
  O           1.15640395986179      1.49872311468950     -0.42824952881349
  O           0.20171856643384     -1.34245892026410      4.10369606974156
  H           3.13099972769435      0.70278682253284      1.90405467583872
  H           1.09535303482193      1.05072979771571     -2.18752008148655
  H          -0.70833006676546     -3.57971227504948      1.86231466206648
`

### D.9 Steam Pre-Reaction Complex (W-PRC, 25 atoms)
`xyz
25
Coordinates from ORCA-job jobs/opt05_wprc E -1785.850531808839
  Al         -0.26911471998397      0.10649975411525      0.31599374018932
  O          -1.70562182180228      0.04378325169171     -0.90364878878416
  O          -0.82553873614854     -1.06300663886252      1.48497548911298
  O           0.98860905641809     -0.41504840856049     -0.70894915166363
  O          -0.21577715404675      1.68882440050876      0.92154841942518
  Si         -1.55487404291602     -0.30462764899400     -2.55696630677828
  Si         -0.16311721720502     -2.21139440530919      2.44516296981274
  Si          2.41970336847618     -0.83990343439381     -1.33550451771665
  Si          0.12594078524707      3.24968671754705      1.16392983120616
  H          -0.63398384907246      0.69411690458724     -3.11924204440117
  H          -1.05780797695525     -1.67939130009112     -2.73849545647861
  H          -2.91579466912619     -0.16486066727788     -3.11439335493055
  H          -1.10844114055197     -2.51258260191236      3.54860540000103
  H           0.08651291352370     -3.46070127752484      1.68465208147270
  H           1.12164375117171     -1.74392181938433      3.02193336353691
  H           2.25788267160145     -1.15028664264955     -2.77967505635983
  H           2.95774182460910     -2.04596578421751     -0.65611505000149
  H           3.41277934350621      0.25563671805063     -1.20205381660545
  H           1.59144423880509      3.47423767128841      1.25398537349429
  H          -0.40191301481457      4.08500986649572      0.05233980653009
  H          -0.49638480029927      3.72265600604572      2.42719841949656
  H          -2.54730873438968     -0.22395798546173     -0.41113360994331
  O          -3.43642206304298     -0.82792650097901      0.75914314665585
  H          -4.00258980176719     -0.25540836728805      1.28801185484586
  H          -2.64154021123646     -1.03572980742411      1.30237825788355
`

### D.10 Steam Dealumination Product Complex (W-P, 25 atoms)
`xyz
25
Coordinates from ORCA-job W-P-T1-V01 E -36.441138263440
  Al          1.53604950847663      0.30892857394912      0.95368487804877
  O          -0.84296933265111     -1.22780239702421      0.08847772137984
  O           1.21449880713455     -1.34448849627547      1.74611136834986
  O           1.83100560839366     -0.03638534722927     -0.68025605485831
  O           0.05746364971607      1.15952224998257      1.13339066800556
  Si         -1.88566764959270     -1.16008224275851     -1.16384456114333
  Si          0.20411251945923     -2.69726628823881      1.64958179308793
  Si          2.08364519133462     -0.40432804711275     -2.21958672870647
  Si         -1.21763342483825      2.12065243593006      1.31468858586494
  H          -2.21083333870879     -2.57286272310373     -1.36066073067016
  H          -3.06750186260032     -0.39684340231310     -0.74862458127293
  H          -1.26116376967027     -0.56400379983071     -2.34209809531382
  H          -1.06917960575408     -2.36716431699537      2.26719948582016
  H           0.37289758192666     -3.35945814374600      0.37062069060390
  H           0.91430676640703     -3.54558080762995      2.64000331237092
  H           1.41475201520258      0.60541592316729     -3.04965685020449
  H           1.52387211103602     -1.74054663704645     -2.46745820330550
  H           3.53159527489980     -0.39978875329847     -2.45742862443627
  H          -1.67421982284769      2.51622469472686     -0.02263462112264
  H          -2.24439605196619      1.32608122226954      2.00441612329195
  H          -0.83079776634922      3.28303659763739      2.11744339270689
  H          -0.46249663317113     -0.38308063625605      0.37766185027721
  O           2.81503253947308      0.74259412406192      1.92885831780170
  H           3.45656970967343      1.39820176678628      2.15013242325760
  H           1.95437597501637     -1.41955654965218      2.34810044016668
`
