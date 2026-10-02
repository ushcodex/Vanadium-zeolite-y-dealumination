---
lang: en
---

**A DENSITY FUNCTIONAL THEORY (DFT) INVESTIGATION OF THE MECHANISM OF ZEOLITE Y DEACTIVATION BY VANADIUM IN RESIDUE FLUID CATALYTIC CRACKING (RFCC) UNITS OF NIGERIAN REFINERIES**

*A Final Year Research Project Report*

Submitted to the Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, Kaduna State, Nigeria, in partial fulfilment of the requirements for the award of the Bachelor of Engineering (B.Eng.) degree in Chemical Engineering.

July 2026

\newpage

# TABLE OF CONTENTS

CHAPTER ONE: INTRODUCTION

1.1 Background to the Study
1.2 Statement of the Problem
1.3 Aim of the Study
1.4 Objectives of the Study
1.5 Research Questions
1.6 Justification of the Study
1.7 Scope of the Study
1.8 Limitations of the Study
1.9 Definition of Key Technical Terms

CHAPTER TWO: LITERATURE REVIEW

2.1 Energy and the Central Place of Petroleum
2.2 Petroleum and Its Refining
2.3 Heterogeneous Catalysis: Concepts Required for This Study
2.4 Catalytic Cracking and the Rise of Zeolite Catalysts
2.5 The Fluid Catalytic Cracking Process
2.6 The FCC Catalyst and Its Zeolite Y Component
2.7 From FCC to RFCC: Heavier Feeds, Heavier Problems
2.8 Deactivation of FCC Catalysts in Service
2.9 Vanadium Chemistry in the FCC Unit
2.10 The Mechanism of Zeolite Y Deactivation by Vanadium: The Experimental Evidence
2.11 Countermeasures Against Vanadium
2.12 Learning from the Molecule: Quantum Chemical Methods and DFT
2.13 Prior DFT Studies Nearest to the Present Problem
2.14 FCC and RFCC in Nigerian Refineries: Documented Context
2.15 Related Studies Connected with Ahmadu Bello University, Zaria
2.16 Research Gap and Positioning of This Study
2.17 Chapter Summary

CHAPTER THREE: MATERIALS AND METHODS

3.1 Research Design
3.2 The Model System
3.3 Software Tools
3.4 Computational Levels and Settings
3.5 Step-by-Step Procedure
3.6 Computed Quantities and Energy Bookkeeping
3.7 Validation Plan
3.8 Statistical Treatment and Uncertainty
3.9 Computing Resources and Schedule
3.10 Data Management and Reproducibility
3.11 Risk Register
3.12 Health, Safety, Environmental, and Ethical Considerations
3.13 Chapter Summary

CHAPTER FOUR: RESULTS AND DISCUSSION

4.1 Reference Species and the Faujasite Cluster Model
4.2 Adsorption of Vanadic Acid and Water at the Brønsted Site
4.3 Stationary-Point Energetics of the Vanadic Acid Pathway
4.4 Steam Baseline and the Benchmark Cross-Check
4.5 Comparative Discussion: Adsorption, Thermodynamic Access, and the Role of Vanadium
4.6 Status of Saddle-Point Localization at Tier 1
4.7 Level-of-Theory Qualification and Uncertainty
4.8 Chapter Summary

REFERENCES

\newpage

# LIST OF FIGURES

Figure 2.1: Crude distillation nameplate capacities of Nigerian refineries
Figure 2.2: Block flow concept of a residue fluid catalytic cracking unit
Figure 2.3: Building units and framework views of faujasite (FAU), the framework of zeolite Y
Figure 2.4: Thermal landscape of FCC operation relative to the melting point of vanadium pentoxide
Figure 2.5: Consensus picture of zeolite Y deactivation by vanadium in the FCC regenerator
Figure 2.6: Vanadium loadings reported in key experimental contamination studies
Figure 2.7: Indicative nickel and vanadium contents of major Nigerian crude grades
Figure 2.8: Four decades of research on vanadium deactivation of FCC (zeolite Y) catalysts
Figure 3.1: The four-T-site faujasite cluster model and its pre-reaction complex with vanadic acid
Figure 3.2: Stationary-point sequence of the reaction pathways to be computed
Figure 3.3: Two-tier computational workflow adopted for this study
Figure 4.1: Computed Tier 1 adsorption strength on the FAU cluster (GFN2-xTB)
Figure 4.2: Tier 1 relative electronic energies of stationary states vs isolated fragments

# LIST OF TABLES AND PLATES

Plate 2.1: Conceptual cross-section of a metal-contaminated FCC catalyst microsphere
Table 1.1: Objectives, linked methods, and expected output of this study
Table 2.1: Key structural and catalytic characteristics of zeolite Y relevant to FCC service
Table 2.2: Experimental evidence base for the mechanism of vanadium attack on zeolite Y
Table 2.3: Passivation and trapping technologies against vanadium and their chemistry
Table 2.4: Documented unit inventory relevant to FCC and RFCC in Nigerian refineries
Table 2.5: Related studies connected with Ahmadu Bello University, Zaria
Table 3.1: Stationary-point set defining the two reaction pathways of this study
Table 3.2: Software tools, versions, and their role in the workflow
Table 3.3: Computational levels, settings, and the reason for each choice
Table 3.4: Energy quantities to be computed for each stationary point and pathway
Table 3.5: Validation anchors for checking the computed results
Table 3.6: Work schedule for the project
Table 3.7: Risk register and mitigation plan
Table 4.1: Optimized reference species and cluster geometry metrics at GFN2-xTB
Table 4.2: Tier 1 adsorption energies at the cluster Brønsted acid site
Table 4.3: Tier 1 relative electronic energies of stationary states for the two pathways
Table 4.4: Saddle-search audit at Tier 1 closeout (GFN2-xTB)

\newpage

# CHAPTER ONE

# 1.0 INTRODUCTION

## 1.1 Background to the Study

There is a quiet war fought every day inside a gasoline factory, and its weapons are too small to see. Somewhere in a refinery, a stream of black, tarry residue that most people would dismiss as useless is sprayed onto a cloud of white powder finer than table salt. In a few seconds of violent, searing contact, big molecules shatter into the small, valuable ones that move cars, motorcycles, and generators. The white powder does not get used up in this transaction; it rides round and round a closed loop of steel, being burned clean and sent back to work, millions of times. But the powder is dying slowly. Hidden inside the black residue are traces of a metal that spreads like rust through the pores of the powder, dissolving its internal architecture grain by grain. That metal is vanadium, and understanding exactly how it kills the powder at the level of atoms and bonds is the story this project sets out to tell, using the mathematics of quantum mechanics as a microscope.

The white powder of the opening picture is the fluid catalytic cracking (FCC) catalyst, and the unit that circulates it is one of the largest and most important conversion processes in petroleum refining. FCC presently produces the majority of the world's gasoline as well as a large fraction of the propylene used for polymers (Vogt and Weckhuysen, 2015). The active heart of the modern FCC catalyst is zeolite Y, a crystalline aluminosilicate of the faujasite (FAU) structure type whose cages and pores are about the size of the molecules it cracks (Breck, 1974; Venuto and Habib, 1979). When refiners process heavier fractions such as atmospheric or vacuum residue, in a mode called residue fluid catalytic cracking (RFCC), the catalyst is exposed to organometallic contaminants that concentrate in the heavy end of crude oil, notably nickel, iron, sodium, and above all vanadium (Bai et al., 2019; Adanenche et al., 2023).

Decades of experimental work have established that vanadium is uniquely aggressive toward zeolite Y. Under the hot, steam-filled conditions of the FCC regenerator, vanadium is converted into mobile, acidic species including vanadium pentoxide (V2O5) and vanadic acid (H3VO4), which attack the bonds of the zeolite framework, strip aluminum atoms from it, and permanently collapse its crystalline structure (Wormsbecher et al., 1986; Pine, 1990; Occelli, 1991b; Trujillo et al., 1997; Xu et al., 2002). The consequences are loss of conversion, worse product selectivity, higher catalyst consumption, and direct economic loss to refiners (Cerqueira et al., 2008; Etim et al., 2018; Faghani et al., 2024). Nigeria's refining industry has entered a new era with the 650,000 barrels per day Dangote refinery, whose gasoline block is anchored on a large RFCC unit of roughly 218,000 barrels per day that has already experienced catalyst related upsets (Leadership, 2026; Sahara Reporters, 2025). Understanding vanadium behaviour in RFCC service is therefore directly relevant to the reliable operation of the country's flagship refining assets.

What remains missing in the open literature, in spite of almost forty years of experimental studies, is a first principles, molecule level account of the elementary chemical steps by which vanadium species attack the faujasite framework: which bonds break first, how strongly vanadic acid binds to the acid sites of the zeolite, and how the energetics of its action differ from those of steam alone. Density functional theory (DFT), a quantum mechanical modelling method that computes the energy of electrons in molecules and solids, is the standard modern tool for answering exactly this class of question (Hohenberg and Kohn, 1964; Kohn and Sham, 1965; Sholl and Steckel, 2009). DFT has already been used to map the hydrolysis of aluminium-oxygen bonds during steam dealumination of zeolites (Malola et al., 2012; Silaghi et al., 2015, 2016) and to characterize vanadium sites inside zeolite frameworks (Tielens, 2009; Tielens and Dzwigaj, 2010a), but it has not, to the knowledge available to this study, been applied to the elementary attack of regenerator-borne vanadic acid on zeolite Y itself. That open space is where this project works.

## 1.2 Statement of the Problem

Nigerian refineries convert the heavier fractions of crude oil into gasoline and petrochemical feedstocks using FCC and RFCC technology. Nigerian crude oils are light and sweet, yet their residual fractions still carry the nickel and vanadium that concentrate in all heavy petroleum, and published analyses of Nigerian crude samples report vanadium contents in the tens of parts per million in the heavier fractions (Ahmad et al., 2010). In RFCC service, these metals accumulate on the catalyst until the zeolite Y component is destroyed, forcing refiners to compensate with constant fresh catalyst addition, metals traps, or premature catalyst replacement (Adanenche et al., 2023; Faghani et al., 2024). At the Dangote refinery, the RFCC regenerator has already required repair attention associated with catalyst performance problems (Sahara Reporters, 2025), underlining that catalyst health is an operational, economic, and energy security issue for Nigeria.

The problem attacked in this project is the incompleteness of the mechanistic picture. Experimental techniques such as X-ray diffraction, electron microscopy, and solid state nuclear magnetic resonance can show the damage after it happens, and spectroscopy can track the vanadium species present, but the elementary bond breaking and bond making steps inside the zeolite pore during attack happen too fast and at too small a scale to be watched directly (Meirer et al., 2015; Hagiwara et al., 2003). Competing mechanistic claims exist in the literature about whether vanadium attacks the silanol surface bonds first, whether it works through acid hydrolysis of aluminium containing bonds, whether its true role is to catalyse the formation of sodium hydroxide that then attacks silicon-oxygen bonds, and whether extra-framework aluminium protects or does not protect the lattice (Pine, 1990; Trujillo et al., 1997; Xu et al., 2002; Occelli, 1996). These questions can be answered quantitatively by computing the energies of the proposed steps, yet no published DFT study has done so for the zeolite Y and regenerator vanadium species system. Nigerian RFCC operations therefore rely on mechanistic understanding that is partly inferred and partly disputed, and mitigation measures such as metal traps and rare earth formulations are selected largely by experience rather than by computed design rules.

## 1.3 Aim of the Study

The aim of this study is to investigate, using density functional theory, the molecular mechanism by which vanadium species deactivate the zeolite Y component of fluid catalytic cracking catalysts under regenerator conditions relevant to residue fluid catalytic cracking in Nigerian refineries.

## 1.4 Objectives of the Study

The specific objectives are as follows:

1. To critically review and organize the experimental literature on the deactivation of zeolite Y by vanadium in FCC and RFCC service, identifying the proposed mechanisms, the evidence behind them, and the points of disagreement.
2. To construct and validate a hydrogen-terminated faujasite cluster model bearing one Brønsted acid site, together with the reactant species vanadic acid (H3VO4) and water (H2O), suitable for quantum chemical calculation.
3. To map, at the GFN2-xTB semi-empirical level, the complete stationary-point sequence of vanadic-acid-assisted dealumination of the cluster (adsorption complex, intermediates, transition structures, and the dealuminated product), and the corresponding steam-only hydrolysis baseline.
4. To refine the energetics of all stationary points at dispersion-corrected hybrid DFT, quantify adsorption strengths with counterpoise corrections and charge-transfer descriptors, and rank the two pathways against the published steam dealumination benchmark.

## 1.5 Research Questions

The study is guided by the following questions:

1. How strongly does vanadic acid bind to the Brønsted acid site of the faujasite framework compared with water, and what does that imply for access of the two species to the framework under regenerator steam?
2. Does vanadic acid lower the energies and barriers of the stepwise cleavage of framework aluminium-oxygen bonds relative to steam alone, and by how much?
3. What do the computed geometries and charge transfers along the pathway reveal about how vanadium participates in the extraction of framework aluminium from the zeolite?

## 1.6 Justification of the Study

This study is justified on the following grounds:

1. National relevance. The commissioning and stabilization of the Dangote refinery RFCC unit, together with the rehabilitation of the state-owned FCC assets at Warri, Kaduna, and Port Harcourt, make catalyst longevity a Nigerian industrial priority (Leadership, 2026; Punch, 2025). A mechanistic, computation-driven understanding of vanadium attack supports better catalyst selection, metals management, and trap design for these units.
2. Scientific relevance. The experimental mechanism literature is approximately forty years deep but remains contested in detail (compare Pine, 1990 with Xu et al., 2002), and no DFT study has yet placed the proposed elementary steps on a common energy scale for zeolite Y. Cluster-model DFT can arbitrate between mechanisms in a way that directly complements experiment, as demonstrated for steam dealumination by Silaghi et al. (2015, 2016).
3. Institutional relevance. The Department of Chemical Engineering at Ahmadu Bello University has an active record in FCC and catalyst related research, including RFCC metal poisoning reviews (Adanenche et al., 2023), FCC riser modelling (Olanrewaju et al., 2015), zeolite and catalyst precursor synthesis (Salahudeen et al., 2015a, 2015b, 2017), and quantum chemical studies using semi-empirical and DFT methods (Uzochukwu et al., 2023). This project extends that record into computational catalysis of metal poisoning.
4. Economy and safety. The study requires no hazardous chemicals, no high pressure operation, and modest funding; its computing cost is bounded by design, as set out in Chapter Three.

## 1.7 Scope of the Study

1. The study is purely computational and literature-based. No experimental catalyst preparation, characterization, or pilot testing is undertaken.
2. The catalyst is represented by one hydrogen-terminated four-T-site cluster of the faujasite framework containing a single framework aluminium atom charge-balanced by one Brønsted proton. Periodic crystal calculations and molecular dynamics are outside the scope of this project.
3. The attacking species studied are vanadic acid (H3VO4), the mobile V(V) poison identified experimentally, with water (H2O) as the steam baseline. The reaction set comprises the full stationary-point sequence of vanadic-acid-assisted dealumination and the first steam hydrolysis step for comparison.
4. Computed quantities are adsorption energies with counterpoise correction, relative electronic and Gibbs free energies of all pathway states at 298 and 1003 K, barriers of the comparative hydrolysis transition structures, and Hirshfeld charge descriptors. Mapping is performed at the GFN2-xTB level, and all stationary points are refined at hybrid DFT (B3LYP-D3(BJ)/def2-SVP geometries and frequencies, with PBE0-D3(BJ)/def2-TZVP single-point energies).
5. The Nigerian application context is addressed through literature and public information on the FCC and RFCC assets at the Warri, Kaduna, Port Harcourt, and Dangote refineries, including feed metal levels documented for Nigerian crudes (Ahmad et al., 2010). No confidential plant data are used.

## 1.8 Limitations of the Study

1. A four-T-site cluster truncates the infinite zeolite lattice, so long-range electrostatic and confinement effects are approximated, not reproduced. Conclusions are therefore drawn from relative energetics within one identical model truncation, never from absolute values in isolation; periodic calculations are reserved for future work (Sauer, 1989; Van Speybroeck et al., 2015).
2. DFT results depend on the choice of exchange-correlation functional. This dependence is mitigated by confirming all conclusions at two hybrid functional levels and by benchmarking the steam baseline against published periodic DFT barriers (Sholl and Steckel, 2009; Silaghi et al., 2015).
3. The regenerator environment, with its temperature gradients, oxygen and steam partial pressures, and thousands of feed molecules, is idealized into the energetics of the selected chemical steps; the study computes energetics, not reactor performance.
4. Local computing hardware and intermittent electricity supply restrict heavy computation, so the study is limited to one pathway family plus its steam baseline. The sodium, vanadyl, and trapping chemistries reviewed in Chapter Two are reserved for future work.
5. Plant scale contamination data for Nigerian units are limited in the public domain, and the study relies on published analyses and press reports, which are individually cited wherever used (Ahmad et al., 2010; Sahara Reporters, 2025).

## 1.9 Definition of Key Technical Terms

For clarity throughout this report, the following terms are used with these meanings:

- Zeolite: a crystalline microporous aluminosilicate with a framework of corner-sharing SiO4 and AlO4 tetrahedra that forms cages and channels of molecular size (Breck, 1974).
- Zeolite Y: the synthetic faujasite (FAU) zeolite used in FCC catalysts, with a supercage of about 1.3 nm and twelve-membered ring windows of about 0.74 nm (Vogt and Weckhuysen, 2015).
- FCC: fluid catalytic cracking, the refinery conversion process that cracks heavy oil fractions over a circulating hot catalyst in a riser reactor.
- RFCC: residue fluid catalytic cracking, the variant of FCC designed to process atmospheric or vacuum residue feeds that contain metals and high Conradson carbon (Adanenche et al., 2023).
- Deactivation: the loss of catalyst activity or selectivity with time on stream, here by irreversible destruction of the zeolite component.
- Brønsted acid site: a proton donor site; in zeolite Y, the bridging Si-O(H)-Al hydroxyl group created to balance the negative charge of framework aluminium.
- Lewis acid site: an electron pair acceptor site, associated with coordinatively unsaturated metal or extra-framework aluminium species.
- Dealumination: the removal of aluminium atoms from the zeolite framework, typically by steam hydrolysis at regeneration temperature (Silaghi et al., 2016).
- Equilibrium catalyst (Ecat): the blend of fresh and aged catalyst actually circulating in an operating FCC unit, on which metals accumulate.
- Passivator and trap: additives that chemically bind contaminant metals into inert compounds, such as vanadates, so that they can no longer damage the zeolite (Adanenche et al., 2023).
- DFT: density functional theory, a quantum mechanical framework that computes molecular energies and structures from the electron density (Kohn and Sham, 1965).
- Cluster model: a finite, molecular-sized fragment cut from a crystal and chemically terminated, used to represent the local active region of a solid in quantum chemical calculations (Sauer, 1989).
- Transition structure: the highest-energy first-order saddle point along an elementary reaction step, identified by exactly one imaginary vibrational frequency (Jensen, 2017).

**Table 1.1**

*Objectives, linked methods, and expected output of this study*

| Objective | Main method | Expected output |
|---|---|---|
| Organize vanadium deactivation literature | Structured review of peer-reviewed studies | Evidence matrix (Chapter 2) |
| Build and validate the FAU cluster and reactants | Structure assembly in Avogadro and Spartan; GFN2-xTB and DFT geometry checks | Validated model set (Chapter 3) |
| Map the two reaction pathways | GFN2-xTB optimizations, relaxed scans, transition-state searches | Stationary-point geometry archive |
| Refine energetics and rank pathways | B3LYP-D3(BJ)/def2-SVP and PBE0-D3(BJ)/def2-TZVP in ORCA; counterpoise; Multiwfn charges | Energy, barrier, and charge tables with validation (Chapters 3 and 4) |

*Source:* Author. Methods are detailed step by step in Chapter Three.

\newpage
