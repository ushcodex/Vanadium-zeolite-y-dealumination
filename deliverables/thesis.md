# VANADIC ACID AND STEAM ATTACK ON ZEOLITE Y: A CLUSTER-BASED STUDY OF FRAMEWORK ALUMINIUM LOSS

Ahmad Usman Shehu

Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, Nigeria

A research project submitted in partial fulfilment of the requirements for the award of the Bachelor of Engineering degree in Chemical Engineering.

October 2026

# DECLARATION

I declare that this project presents my research and that the work of others has been acknowledged. Signature: __________________ Date: __________

# CERTIFICATION

This project has been examined and approved for the Department of Chemical Engineering, Ahmadu Bello University, Zaria. Supervisor: __________________ Signature/Date: __________ Head of Department: __________________ Signature/Date: __________

# DEDICATION

[Author to complete.]

# ACKNOWLEDGEMENTS

[Author to complete with the consent and correct names of contributors.]

# ABSTRACT

Vanadium deposited from heavy petroleum feeds can damage the zeolite Y component of residue fluid catalytic cracking catalysts during steam-rich regeneration. This study compared vanadic acid and water at a small aluminium-containing zeolite cluster using GFN2-xTB semi-empirical calculations and selected dispersion-corrected hybrid density functional theory (DFT) calculations. Electronic adsorption energies from geometry-optimised B3LYP calculations were −106.69 kJ mol⁻¹ for vanadic acid and −92.20 kJ mol⁻¹ for water, although their common cluster reference did not finish geometry optimisation. Their difference, −14.49 kJ mol⁻¹, cancels this reference but remains subject to model and method errors. A GFN2-xTB transition state for the first aluminium–oxygen cleavage step had a 160.70 kJ mol⁻¹ electronic barrier above its preceding intermediate and one imaginary vibrational mode. Other proposed vanadium steps and the steam comparison did not form a fully verified, consistently optimised DFT pathway. Therefore, the calculations support local vanadium binding and one plausible cleavage event, not a measured rate advantage or an industrial catalyst-life prediction. A consistent higher-level pathway, larger zeolite models and experimental validation are needed before process recommendations can be quantified.

Keywords: zeolite Y; vanadium; dealumination; fluid catalytic cracking; molecular simulation.

# CONTENTS

Declaration; Certification; Dedication; Acknowledgements; Abstract; Chapter One: Introduction; Chapter Two: Literature Review; Chapter Three: Materials and Methods; Chapter Four: Results and Discussion; Chapter Five: Engineering Interpretation; Chapter Six: Conclusions and Recommendations; References; Appendix A: Visualisation and export guide.

# LIST OF FIGURES

Figure 2.1. Schematic catalytic cracking cycle; Figure 3.1. Aluminium-centred cluster; Figure 3.2. Calculation and verification workflow; Figure 4.1. Adsorption energy comparison; Figure 4.2. Audited semi-empirical state energies.

# LIST OF TABLES

Table 2.1. Literature and unresolved question; Table 4.1. Adsorption energies; Table 4.2. State and verification summary.

# ABBREVIATIONS

DFT, density functional theory; FCC, fluid catalytic cracking; RFCC, residue fluid catalytic cracking; FAU, faujasite; GFN2-xTB, geometry, frequency and noncovalent interactions extended tight binding, second generation; TS, transition state; PRC, pre-reaction complex; EFAL, extra-framework aluminium.

# CHAPTER ONE: INTRODUCTION

## 1.1 Background

A cracking catalyst may appear intact as a powder while its most valuable internal structure is disappearing. In a residue fluid catalytic cracking regenerator, steam and deposited vanadium meet zeolite Y at high temperature. If framework aluminium leaves the zeolite, acid sites and accessible pores can be lost. The engineering question is not simply whether vanadium is present, but how it changes the sequence of bond-making and bond-breaking that damages the catalyst.

Residue fluid catalytic cracking converts heavy hydrocarbon fractions into lighter products using a circulating catalyst. Zeolite Y supplies many of its strong acid sites; the matrix and binder supply additional functions. Coke is burnt from spent catalyst in the regenerator, where steam and metal deposits can accelerate structural loss (Vogt & Weckhuysen, 2015; Adanenche et al., 2023). Vanadium and steam together have been implicated experimentally in zeolite damage, but bulk measurements cannot directly identify every short-lived atomic arrangement (Trujillo et al., 1997).

## 1.2 Problem and aim

Observed loss of crystallinity alone does not establish whether vanadium binds near aluminium, promotes an individual Al–O cleavage, or changes the overall activation barrier. The aim was to examine local vanadic-acid and water interactions with an aluminium-containing zeolite Y cluster and to distinguish demonstrated stationary points from unverified mechanistic proposals.

## 1.3 Objectives

The objectives were to construct a capped local zeolite cluster and molecular reactants; compare their calculated adsorption energies; locate candidate intermediates and transition states; check geometry convergence, vibrational modes and endpoint connectivity; compare selected structures at hybrid-DFT level; and identify what the resulting energies can and cannot imply for RFCC operation.

## 1.4 Scope, justification and limitations

The study addressed one local framework-Al environment with isolated H₃VO₄ and H₂O. It calculated gas-phase cluster electronic energies, not a periodic crystal, a circulating catalyst particle, a refinery material balance, or a measured reaction rate. A small model makes atomic changes interpretable and affordable, but neglects long-range confinement, sodium and rare-earth ions, multiple water molecules and catalyst heterogeneity. Transition-state energies at different methods or geometries were not treated as interchangeable. This scope matters because assigning a reliable mechanistic claim requires more than a visually plausible reaction path.

# CHAPTER TWO: LITERATURE REVIEW

## 2.1 From refinery feed to catalyst damage

Fluid catalytic cracking contacts vaporised feed with hot circulating catalyst for a short time, then burns coke from the catalyst before reuse. Residue feeds introduce more metal-bearing species than many distillate feeds. Vanadium deposited from the feed can move and react during regeneration. However, deposited metal concentration by itself is not a direct measure of zeolite damage: location, chemical form, water availability and protective additives also matter (Vogt & Weckhuysen, 2015; Bai et al., 2019; Xu et al., 2024).

Figure 2.1 shows the process locations relevant to the question. It is a conceptual schematic, not a plant-specific flowsheet.

[FIGURE:fig2_2_rfcc_schematic.png|Figure 2.1. Catalytic cracking and regeneration schematic. Source: project illustration; use as a conceptual diagram only.]

## 2.2 Why zeolite Y is vulnerable

Zeolite Y belongs to the FAU framework family: linked SiO₄ and AlO₄ tetrahedra create large cavities reached through 12-membered-ring openings. Substitution of Si⁴⁺ by Al³⁺ leaves a framework charge compensated by cations; hydrogen-form sites can donate protons and catalyse hydrocarbon cracking. Controlled dealumination can improve stability, whereas excessive loss of framework aluminium and micropore order depletes active sites (Breck, 1974; Vogt & Weckhuysen, 2015). The local hydrolysis step can be represented as ≡Si–O–Al≡ + H₂O → ≡Si–OH + HO–Al≡. This sketch conserves the immediate bond partners but is not a balanced equation for a whole catalyst particle. Subsequent rearrangement may generate extra-framework aluminium.

Steam hydrolysis depends on which framework oxygen reacts and the local acid environment. Calculations on zeolites show that aluminium removal can proceed by several steps, so a single bond-breaking energy cannot represent full extraction (Silaghi et al., 2015, 2016). This distinction is important when interpreting any short cluster pathway.

## 2.3 Vanadium under regenerator conditions

Vanadium-containing feed compounds deposit on the catalyst and oxidise during regeneration. A commonly discussed steam-associated volatile species is orthovanadic acid, represented by V₂O₅ + 3H₂O ⇌ 2H₃VO₄. This equilibrium expresses a proposed transport route; the abundance of gas-phase H₃VO₄ inside a real particle was not established here (Wormsbecher et al., 1986, 1996). The model therefore tests what could happen *if* H₃VO₄ reaches a site, not whether it is the dominant regenerator species.

Pine (1990) and Trujillo et al. (1997) linked vanadium, steam and zeolite destruction. Occelli (1991b) emphasised complex vanadium–zeolite interactions, while Xu et al. (2002) showed that sodium changes destruction pathways. More recent studies identified framework and pore changes following contamination and reviewed metal trapping or passivation approaches (Etim et al., 2016, 2018; Adanenche et al., 2023; Faghani et al., 2024). These studies establish the practical importance of vanadium but do not uniquely specify the coordinates and energies of each local Al–O cleavage transition state.

Table 2.1 links the principal evidence to the narrower computational question.

[TABLE:Table 2.1. Evidence and remaining mechanistic question|Evidence;What it establishes;What remains uncertain|Steam and vanadium experiments (Trujillo et al., 1997);Damage occurs under relevant exposures;Identity of each fleeting transition state|Sodium interaction (Xu et al., 2002);Co-contaminants alter destruction;Transferability to a sodium-free cluster|Structural analysis (Etim et al., 2016);Framework and pore changes after contamination;Individual activation barriers|Metal-trap reviews (Adanenche et al., 2023);Mitigation options exist;Site-level effects on local Al–O cleavage]

## 2.4 How molecular calculations address the gap

A stationary minimum is a stable geometry on a computed energy surface; a transition state is a first-order saddle between minima. A vibrational calculation tests whether a proposed transition state has exactly one imaginary frequency. Following that mode in both directions provides a stronger connection test. Semi-empirical GFN2-xTB is fast because it uses fitted approximations, making it useful for searching many geometries (Bannwarth et al., 2019). Hybrid DFT uses a more explicit electronic treatment and is more expensive; B3LYP and PBE0 are established choices, but neither guarantees accuracy for every vanadium-containing structure (Adamo & Barone, 1999; Neese et al., 2020). Dispersion correction accounts approximately for attractive interactions omitted by many density functionals (Grimme et al., 2010, 2011).

An adsorption energy is E(complex) − E(clean cluster) − E(free molecule), with a negative value indicating exothermic binding at that level of calculation. A step barrier is E(TS) − E(preceding minimum), not E(TS) minus a different route's isolated reactants. These are electronic energies. Entropy, steam partial pressure and temperature can change the free energy and therefore the population or rate. Single-point DFT energies evaluated on semi-empirical structures test method sensitivity, but they do not establish a DFT transition-state pathway. The specific gap addressed here is an auditable local comparison of H₃VO₄ and H₂O that clearly separates verified events from tentative ones.

# CHAPTER THREE: MATERIALS AND METHODS

## 3.1 Research design and model

A capped aluminium-centred FAU cluster, recorded as AlSi₄O₄H₁₃ in the calculation register, represented a local zeolite site. Separate water and orthovanadic acid molecules defined two reactant routes. Hydrogen caps terminate broken boundary bonds; they are modelling devices, not the full pore wall. Figure 3.1 shows the site model used to communicate the atomistic scope.

[FIGURE:fig3_1_cluster.png|Figure 3.1. Capped aluminium-containing local zeolite model. Source: project structural illustration; inspect coordinates before publication.]

The vanadium route was searched through an encounter complex, an intermediate, a proposed first cleavage saddle and a further intermediate/product. A separate water route provided a steam comparison. A reaction coordinate describes progress between structures, not elapsed plant time. Formally, each minimum and saddle was evaluated with E_rel = (E_state − E_cluster − E_molecule) × 2625.50 kJ mol⁻¹ Eh⁻¹. The two routes have different molecular reference zeros and must not be plotted as one common absolute energy scale.

## 3.2 Computing and calculation levels

Initial semi-empirical geometry searches and frequency calculations were run with ORCA using GFN2-xTB. The local workstation used for these runs was a Dell Latitude E6430 with 16 GB RAM and an SSD. Selected higher-level jobs were run separately on remote compute resources using B3LYP-D3(BJ)/def2-TZVP optimisations and B3LYP or PBE0 single points. The remote machine specification was not reliably established in the archived logs, so no unverified processor or memory specification is claimed. ORCA input files define actual keywords and should take precedence over any generic workflow description (Neese et al., 2020).

Figure 3.2 outlines the steps and decision points. An optimised geometry with no imaginary frequencies was treated as a minimum. A saddle required converged optimisation, one meaningful imaginary mode, a plausible bond-displacement animation, energy above both endpoints, and two-sided connectivity to distinct minima. A job ending in error was not counted as converged. Single-point energies were classified separately from optimised saddles.

[FIGURE:fig3_3_workflow.png|Figure 3.2. Structure search and validation workflow. Source: project workflow illustration.]

## 3.3 Analysis and uncertainty

Electronic energies were converted from hartree to kJ mol⁻¹. The adsorption comparison used consistently optimised B3LYP species, but the cluster reference terminated with a gradient error after two cycles. Accordingly, each absolute adsorption energy is provisional; the difference between vanadium and water adsorption cancels their shared cluster energy. No vibrational, thermal, entropic, solvation or basis-set-superposition correction was applied to the reported comparison. Because the one-sided water saddle connectivity test returned to the same basin, the steam saddle was not accepted as a complete comparison. The archived Tier 1 calculation register and raw ORCA outputs provide the trace for each quoted value.

# CHAPTER FOUR: RESULTS AND DISCUSSION

## 4.1 Adsorption

Table 4.1 presents electronic binding energies for the two optimised molecular complexes. Vanadic acid bound 14.49 kJ mol⁻¹ more strongly than water at this level. This difference does not demonstrate that vanadium occupies more sites in a regenerator: the molecular partial pressures, temperature and binding free energies have not been calculated. The shared cluster energy cancels algebraically in the difference, but geometry and functional errors remain.

[TABLE:Table 4.1. B3LYP-D3(BJ)/def2-TZVP electronic adsorption energies|Adsorbate;Adsorption energy (kJ mol⁻¹);Status|H₃VO₄;−106.69;Absolute value provisional: cluster reference did not converge|H₂O;−92.20;Absolute value provisional: same cluster reference|Vanadic acid minus water;−14.49;Shared cluster reference cancels]

Figure 4.1 makes the modest higher-level difference visible. The semi-empirical calculation instead gave −196.90 and −69.59 kJ mol⁻¹, a difference of −127.31 kJ mol⁻¹. The large change in that difference across methods cautions against claiming a robust magnitude for preferential adsorption.

[CHART:adsorption|Figure 4.1. Optimised B3LYP electronic adsorption energies, kJ mol⁻¹. Both absolute values use a provisional cluster reference.]

## 4.2 Candidate sequence and saddle checks

Table 4.2 distinguishes accepted minimum structures, the supported semi-empirical first cleavage saddle and unresolved candidates. Energies are relative to the isolated cluster plus the relevant molecule. They represent different reference zeros for water and vanadic acid. The 160.70 kJ mol⁻¹ first-cleavage barrier is the difference between the vanadium intermediate at −385.10 and the saddle at −224.40 kJ mol⁻¹, not a barrier relative to the free reactants.

[TABLE:Table 4.2. Selected GFN2-xTB structures and audit status|Route and state;Relative E (kJ mol⁻¹);Interpretation|Vanadium encounter complex;−196.90;Accepted minimum|Vanadium intermediate I1;−385.10;Accepted minimum|Vanadium first-cleavage saddle TS2;−224.40;Accepted saddle, one imaginary mode at −78.21 cm⁻¹|Vanadium intermediate I2;−342.36;Accepted minimum|Vanadium product candidate;−82.90;Accepted minimum, not a validated full pathway|Vanadium TS1 and TS3;not reported;Full accepted connecting saddles unavailable|Water complex;−69.59;Accepted minimum|Water saddle candidate;−40.29;One imaginary mode, but two-sided test failed|Water product;−65.85;Accepted minimum]

Figure 4.2 plots selected minima and the validated local saddle. Lines only guide the eye; they do not imply verified transitions between all adjacent plotted states. A saddle with one imaginary frequency and two-sided downhill relaxation supports a specific local step; it does not complete the entire extraction sequence. The accepted intermediate has four short framework Al–O contacts, not five framework neighbours: a nearby vanadic oxygen in another geometry must not be counted as an additional framework bond.

[CHART:pathway|Figure 4.2. Selected semi-empirical vanadium states relative to isolated cluster plus H₃VO₄. Segments are visual guides, not verified reaction paths.]

## 4.3 Higher-level sensitivity and comparison with literature

Hybrid-DFT single points on unrelaxed semi-empirical shapes differ sharply from the semi-empirical energies. For example, the B3LYP vanadium product single point lies about +543.9 kJ mol⁻¹ above its isolated reference; the water candidate saddle single point lies about +49.8 kJ mol⁻¹ relative to its own reference. These numbers cannot be substituted into the optimised semi-empirical reaction profile, and the failed B3LYP calculation on one intermediate prevents a complete same-level step-barrier estimate. They indicate structural and method sensitivity rather than a measured product thermodynamics or a validated DFT kinetic barrier.

Experimental evidence supports combined steam and vanadium damage (Pine, 1990; Trujillo et al., 1997), and recent work confirms the importance of metal tolerance (Etim et al., 2018; Xu et al., 2024). The present calculations narrow that picture to binding and one plausible local Al–O cleavage event, but cannot rank the complete vanadium route against steam. A faster overall reaction cannot be inferred from a single local barrier when the remaining saddles, temperature-dependent free energies and concentrations are unknown.

# CHAPTER FIVE: ENGINEERING INTERPRETATION

The findings separate three engineering quantities. Adsorption energy concerns local interaction strength; activation energy concerns an elementary step; catalyst life is an integrated plant outcome affected by feed metal loading, residence time, steam, catalyst formulation and replenishment. None follows numerically from another without a kinetic and transport model. The −14.49 kJ mol⁻¹ adsorption difference may motivate further work on where mobile vanadium contacts zeolite sites, but is not a specification for a metal trap or operating temperature. Monitoring feed metals and catalyst crystallinity remains a sensible established practice, independent of this model (Adanenche et al., 2023). Any claim of reduced catalyst consumption requires laboratory or plant evidence.

# CHAPTER SIX: CONCLUSIONS AND RECOMMENDATIONS

## 6.1 Conclusions

In the local capped-cluster model, geometry-optimised B3LYP electronic adsorption favoured H₃VO₄ over H₂O by 14.49 kJ mol⁻¹; the shared cluster reference error cancels from this difference, but not from the individual absolute values. A GFN2-xTB saddle for a local Al–O cleavage step was supported by one imaginary mode and endpoint checks, with an electronic barrier of 160.70 kJ mol⁻¹ above its preceding intermediate. The steam saddle and other proposed vanadium saddles were not fully validated, and hybrid-DFT single points did not establish a consistently optimised higher-level pathway. Consequently, the study did not prove that vanadium lowers the overall dealumination barrier compared with steam or predict an RFCC catalyst lifetime.

## 6.2 Recommendations

Complete a converged cluster reference and consistent geometry optimisation, frequencies and connection tests for every state at one higher-level method. Test alternative Al sites, larger FAU clusters or periodic models, explicit additional water molecules, sodium and rare-earth cations. Apply consistent basis-set-error and finite-temperature free-energy treatments before comparing rates. Check predicted structural changes against controlled steamed and vanadium-exposed catalyst measurements, including crystallinity, acid sites and aluminium coordination. Only after validation should a process model relate molecular findings to metal-trap choice or regenerator operation.

# REFERENCES
Adamo, C., & Barone, V. (1999). Toward reliable density functional methods without adjustable parameters: The PBE0 model. *The Journal of Chemical Physics*, *110*(13), 6158–6170. https://doi.org/10.1063/1.478522

Adanenche, D. E., Aliyu, A., Atta, A. Y., & El-Yakubu, B. J. (2023). Residue fluid catalytic cracking: A review on the mitigation strategies of metal poisoning of RFCC catalyst using metal passivators/traps. *Fuel*, *343*, Article 127894. https://doi.org/10.1016/j.fuel.2023.127894

Bai, P., Etim, U. J., Yan, Z., Mintova, S., Zhang, Z., Zhong, Z., & Gao, X. (2019). Fluid catalytic cracking technology: Current status and recent discoveries on catalyst contamination. *Catalysis Reviews*, *61*(3), 333–405. https://doi.org/10.1080/01614940.2018.1549011

Bannwarth, C., Ehlert, S., & Grimme, S. (2019). GFN2-xTB: An accurate and broadly parametrized self-consistent tight-binding quantum chemical method with multipole electrostatics and density-dependent dispersion contributions. *Journal of Chemical Theory and Computation*, *15*(3), 1652–1671. https://doi.org/10.1021/acs.jctc.8b01176

Breck, D. W. (1974). *Zeolite molecular sieves: Structure, chemistry, and use*. John Wiley & Sons.

Etim, U. J., Bai, P., Ullah, R., Subhan, F., & Yan, Z. (2018). Vanadium contamination of FCC catalyst: Understanding the destruction and passivation mechanisms. *Applied Catalysis A: General*, *555*, 108–117. https://doi.org/10.1016/j.apcata.2018.02.011

Etim, U. J., Xu, B., Ullah, R., & Yan, Z. (2016). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite. *Journal of Colloid and Interface Science*, *463*, 188–198. https://doi.org/10.1016/j.jcis.2015.10.049

Faghani, M. H., Mohammadipour, E., Tarighi, S., Naderifar, A., & Habibzadeh, S. (2024). High vanadium tolerant FCC catalyst by barium titanate as metal trap and passivator. *Fuel*, *375*, Article 132531. https://doi.org/10.1016/j.fuel.2024.132531

Grimme, S., Antony, J., Ehrlich, S., & Krieg, H. (2010). A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. *The Journal of Chemical Physics*, *132*(15), Article 154104. https://doi.org/10.1063/1.3382344

Grimme, S., Ehrlich, S., & Goerigk, L. (2011). Effect of the damping function in dispersion corrected density functional theory. *Journal of Computational Chemistry*, *32*(7), 1456–1465. https://doi.org/10.1002/jcc.21759

Neese, F., Wennmohs, F., Becker, U., & Riplinger, C. (2020). The ORCA quantum chemistry program package. *The Journal of Chemical Physics*, *152*(22), Article 224108. https://doi.org/10.1063/5.0004608

Occelli, M. L. (1991b). Vanadium–zeolite interactions in fluidized cracking catalysts. *Catalysis Reviews: Science and Engineering*, *33*(3–4), 241–280. https://doi.org/10.1080/01614949108020301

Pine, L. A. (1990). Vanadium-catalyzed destruction of USY zeolites. *Journal of Catalysis*, *125*(2), 514–524. https://doi.org/10.1016/0021-9517(90)90323-C

Silaghi, M.-C., Chizallet, C., Petracovschi, E., Kerber, T., Sauer, J., & Raybaud, P. (2015). Regioselectivity of Al–O bond hydrolysis during zeolites dealumination unified by Brønsted–Evans–Polanyi relationship. *ACS Catalysis*, *5*(1), 11–15. https://doi.org/10.1021/cs501474u

Silaghi, M.-C., Chizallet, C., Sauer, J., & Raybaud, P. (2016). Dealumination mechanisms of zeolites and extra-framework aluminum confinement. *Journal of Catalysis*, *339*, 242–255. https://doi.org/10.1016/j.jcat.2016.04.021

Trujillo, C. A., Uribe, U. N., Knops-Gerrits, P.-P., Oviedo A., L. A., & Jacobs, P. A. (1997). The mechanism of zeolite Y destruction by steam in the presence of vanadium. *Journal of Catalysis*, *168*(1), 1–15. https://doi.org/10.1006/jcat.1997.1550

Vogt, E. T. C., & Weckhuysen, B. M. (2015). Fluid catalytic cracking: Recent developments on the grand old lady of zeolite catalysis. *Chemical Society Reviews*, *44*(20), 7342–7370. https://doi.org/10.1039/C5CS00376H

Wormsbecher, R. F., Cheng, W.-C., Kim, G., & Harding, R. H. (1996). Vanadium mobility in fluid catalytic cracking. In P. O'Connor, T. Takatsuka, & G. L. Woolery (Eds.), *Deactivation and testing of hydrocarbon-processing catalysts* (ACS Symposium Series No. 634, pp. 283–295). American Chemical Society. https://doi.org/10.1021/bk-1996-0634.ch020

Wormsbecher, R. F., Peters, A. W., & Maselli, J. M. (1986). Vanadium poisoning of cracking catalysts: Mechanism of poisoning and design of vanadium tolerant catalyst system. *Journal of Catalysis*, *100*(1), 130–137. https://doi.org/10.1016/0021-9517(86)90078-3

Xu, M., Liu, X., & Madon, R. J. (2002). Pathways for Y zeolite destruction: The role of sodium and vanadium. *Journal of Catalysis*, *207*(2), 237–246. https://doi.org/10.1006/jcat.2002.3517

Xu, Z., Zhu, Y., Gong, M., Jiao, N., Zhang, T., & Wang, H. (2024). Review on the poisoning behavior of typical metals on cracking catalysts for chemicals production from petroleum and anti-poisoning strategies. *Applied Catalysis A: General*, *685*, Article 119897. https://doi.org/10.1016/j.apcata.2024.119897

# APPENDIX A: VISUALISATION AND EXPORT GUIDE

Open `simulation/xyz_seeds/cluster_AlSi4O4H13.xyz` and `simulation/xyz_seeds/V-PRC_start.xyz` in Avogadro for orientation only. These are starting coordinates, not necessarily final optimised structures. For a reported final structure, open the corresponding final `.xyz` geometry alongside its ORCA `.out` file in Avogadro or IQmol; check the output for normal termination and a converged optimisation. Open accepted transition-state outputs in ORCA-compatible vibrational viewers and animate the single imaginary mode before exporting any saddle image. ORCA output files from local Windows runs may be UTF-16 encoded. Export molecular images as PNG at 300 dpi or higher with element colours, Al–O distances and a scale indication. Use the figures in this manuscript as schematic communications, not as substituted raw simulation evidence. To remake Figures 4.1 and 4.2, use the numerical tables above or `simulation/analysis/tier1_summary.md` and export charts as SVG or high-resolution PNG. Export the edited Word document to PDF only after updating its automatic contents, page numbers, captions and institution-approved title-page details.
