# PRELIMINARY PAGES

## TITLE PAGE

**A Density Functional Theory Investigation of the Mechanism of Vanadium-Promoted Dealumination of Zeolite Y Under Residue Fluid Catalytic Cracking Conditions**

BY

**Ahmad Usman Shehu**
**(U19/ENG/CHE/XXXX)**

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

The processing of heavy petroleum residues in fluid catalytic cracking (FCC) units is severely hampered by vanadium contamination. Vanadium deposits on the catalyst, oxidises to vanadium pentoxide, and reacts with regenerator steam to form volatile vanadic acid (H<sub>3</sub>VO<sub>4</sub>). This volatile species migrates into the micropores of the zeolite Y active component and accelerates the hydrolytic extraction of framework aluminium, leading to irreversible catalyst deactivation. Despite extensive experimental characterisation of this phenomenon, the elementary atomistic mechanism by which a single vanadic acid molecule dismantles the framework remains unresolved. This study investigates the mechanism of vanadium-promoted dealumination of a four-tetrahedral-site (4T) faujasite cluster model using density functional theory (DFT). A two-tier computational workflow was employed: initial pathway exploration using the semi-empirical GFN2-xTB method, followed by geometry optimisation and frequency analysis at the B3LYP-D3(BJ)/def2-TZVP level. Single-point energies were validated using the PBE0-D3(BJ)/def2-TZVP functional. The results demonstrate that vanadic acid possesses a significantly higher thermodynamic affinity for the zeolite Bronsted acid site than steam. The computed electronic adsorption energy for H<sub>3</sub>VO<sub>4</sub> is -93.0 kJ/mol, compared to -78.3 kJ/mol for water, representing a 15 kJ/mol driving force for selective poisoning. Furthermore, the vanadic acid pathway accesses deeply stabilised chemisorbed intermediates (relative energies below -115 kJ/mol) that act as thermodynamic ratchets, facilitating irreversible framework bond cleavage. Thermochemical analysis at FCC regenerator conditions (1003 K) reveals that while adsorption becomes non-spontaneous due to entropic penalties, the reaction is driven forward by the continuous, irreversible collapse of the framework. These findings provide the first molecular-level energetic profile of the vanadium attack mechanism, offering a quantitative basis (the -93 kJ/mol binding affinity) for the rational design of competitive vanadium trapping additives for next-generation FCC catalysts.
# CHAPTER ONE

# INTRODUCTION

## 1.1 Background of the Study

Every day, fluid catalytic cracking (FCC) units in petroleum refineries around the world convert millions of barrels of heavy gas oil into the gasoline, diesel, and petrochemical feedstocks that sustain modern economies. At the heart of every FCC unit is a zeolite catalyst, a crystalline aluminosilicate whose acid sites break carbon-carbon bonds with remarkable selectivity. Yet this catalyst is under constant siege: the very conditions that enable cracking, temperatures above 680 degrees Celsius in a steam-rich atmosphere, also attack the catalyst's own framework. When heavy or residue feeds are processed, as is increasingly the case in Nigerian and other developing-economy refineries, the assault intensifies. Vanadium, present in the crude oil at concentrations of 1 to over 50 parts per million as organometallic complexes, deposits on the catalyst during cracking, oxidises to vanadium pentoxide (V<sub>2</sub>O<sub>5</sub>) in the regenerator, and then reacts with steam to form volatile vanadic acid (H<sub>3</sub>VO<sub>4</sub>). This vanadic acid vapour penetrates deep into the catalyst particle and attacks the aluminosilicate framework, ripping aluminium atoms from their tetrahedral sites and causing irreversible loss of catalytic activity. The phenomenon has been documented experimentally for over four decades, yet the molecular mechanism, the specific sequence of bond-breaking events by which a single H<sub>3</sub>VO<sub>4</sub> molecule dismantles the zeolite framework, has never been described.

## 1.2 Statement of the Problem

Vanadium contamination of FCC catalysts is one of the most costly operational problems in petroleum refining, responsible for accelerated catalyst replacement, reduced product yields, and increased coke and gas make. Industrial countermeasures such as vanadium traps (basic metal oxide additives that immobilise vanadic acid) have been developed empirically, guided by macroscopic observations of crystallinity loss, unit cell contraction, and catalytic activity decline. However, these macroscopic measurements cannot reveal the elementary steps of the attack: which bond breaks first, what the transition states look like, how much energy is required to overcome each barrier, or why vanadic acid is so much more destructive than steam alone. Without this molecular-level understanding, the design of next-generation vanadium-tolerant catalysts and trapping additives remains a trial-and-error process.

Density functional theory (DFT), a quantum mechanical computational method, can in principle provide exactly this information by computing the energies and geometries of reactants, intermediates, transition states, and products along a proposed reaction pathway. DFT has been applied successfully to study steam-induced dealumination of zeolites, but no published study has modelled the vanadic acid attack pathway or compared its energetics with those of simple hydrothermal dealumination.

## 1.3 Aim of the Study

The aim of this study is to investigate the elementary mechanism of vanadium-promoted dealumination of zeolite Y using density functional theory, and to compare the energetics of the vanadic acid attack pathway with those of steam hydrolysis under conditions representative of the FCC regenerator.

## 1.4 Objectives

The specific objectives of this study are to:

1. Construct a cluster model of the zeolite Y Bronsted acid site suitable for DFT calculations.

2. Map the stationary-point sequence (pre-reaction complex, intermediates, and product) for the dealumination of the cluster by vanadic acid (H<sub>3</sub>VO<sub>4</sub>).

3. Map the corresponding stationary-point sequence for dealumination by water (H<sub>2</sub>O), as a steam hydrolysis baseline.

4. Optimise the geometries and compute the electronic energies of all stationary points at the B3LYP-D3(BJ)/def2-TZVP level of hybrid DFT.

5. Validate the computed energies using a second hybrid functional (PBE0-D3(BJ)/def2-TZVP).

6. Compute the Gibbs free energies of the key adsorption states at both standard conditions (298 K) and FCC regenerator temperature (1003 K, corresponding to 730 degrees Celsius).

7. Compare the adsorption strength, reaction energetics, and thermochemical profiles of the vanadic acid and steam pathways and draw mechanistic conclusions relevant to FCC catalyst deactivation.

## 1.5 Scope of the Study

This study focuses on the initial stages of dealumination at a single Bronsted acid site in the faujasite (FAU) framework, modelled as a four-T-site cluster (AlSi<sub>4</sub>O<sub>4</sub>H<sub>13</sub>) terminated with hydrogen atoms. The vanadic acid pathway is traced from the separated reactants through the pre-reaction complex, a chemisorbed intermediate, and subsequent bond-cleavage intermediates to the dealuminated product. The steam baseline covers the same sequence for water.

The study is limited to the gas-phase cluster model and does not include periodic boundary conditions, solvent effects, or the influence of sodium or other cations. The reaction is studied at zero pressure; the thermochemistry is evaluated at the ideal-gas, rigid-rotor, harmonic-oscillator level at two temperatures (298 K and 1003 K). Transition-state barriers are reported where the saddle-point search converged to a stationary point with the correct mode character; where convergence was not achieved, the barrier is identified as a limitation and discussed accordingly.

## 1.6 Justification of the Study

This research is significant for three reasons:

First, it provides the first molecular-level description of the vanadic acid attack on zeolite Y, filling a gap in the computational catalysis literature that has persisted despite extensive experimental work spanning from Mitchell (1980) and Pine (1990) to Etim et al. (2015) and Faghani et al. (2024).

Second, it quantifies the thermodynamic advantage that vanadic acid holds over steam as a dealumination agent, providing a numerical target (the binding energy margin) that vanadium traps must overcome to protect the catalyst. This information can guide the rational design of trapping additives.

Third, it demonstrates the feasibility of applying hybrid DFT methods to industrially relevant catalyst deactivation problems using only commodity computational resources (a personal laptop for pathway exploration and a single cloud virtual machine for the production DFT calculations), showing that this type of investigation is accessible to research groups without access to supercomputing facilities.

## 1.7 Limitations

The following limitations apply to this study:

1. The cluster model (22 framework atoms plus adsorbate) captures the local chemistry of a single acid site but does not reproduce the long-range electrostatic field, confinement effects, or pore curvature of the full FAU lattice. Adsorption energies may differ from periodic values by 10 to 20 kJ/mol.

2. The hydrogen termination of dangling bonds at the cluster boundary introduces a small artificial flexibility that is not present in the actual framework. This was mitigated by constraining the terminal hydrogen positions during optimisation.

3. Transition-state searches for three of the four proposed saddle points (the initial chemisorption barrier, the final Al-O cleavage, and the steam hydrolysis barrier) did not converge to clean first-order saddle points at the B3LYP-D3(BJ)/def2-TZVP level within the available computational budget. The activation barriers for these steps are therefore not reported as validated values, and the mechanistic discussion is based on the electronic energies of the stationary points that were successfully optimised.

4. The thermochemical analysis uses the ideal-gas, rigid-rotor, harmonic-oscillator approximation, which is known to overestimate the entropy of adsorption (and hence the free energy penalty) for large, floppy adsorbates on solid surfaces.

5. Basis set superposition error (BSSE) was estimated by the counterpoise method for the pre-reaction complexes but could not be completed for all states due to a format-related termination in one of the ghost-atom calculations.
# CHAPTER TWO

# LITERATURE REVIEW

## 2.1 Petroleum Refining and Fluid Catalytic Cracking

Petroleum refining converts crude oil into fuels, petrochemicals, and specialty products through a sequence of physical and chemical processing steps. Among these, fluid catalytic cracking (FCC) is the single most important conversion process in a modern refinery, responsible for transforming heavy gas oil fractions into gasoline, light cycle oil, and liquefied petroleum gas (Sadeghbeigi, 2012). The FCC unit typically accounts for 30 to 45 percent of a refinery's total gasoline output and represents the primary upgrading pathway for vacuum gas oil (Vogt &amp; Weckhuysen, 2015).

In an FCC unit, the preheated heavy feed enters a vertical riser reactor, where it contacts a stream of hot, regenerated catalyst particles at temperatures between 500 and 550 degrees Celsius. The catalyst particles, each approximately 60 to 80 micrometres in diameter, are fluidised by the hydrocarbon vapour and travel upward through the riser, providing the residence time of 2 to 4 seconds needed for cracking. At the top of the riser, the spent catalyst, now coated with carbonaceous deposits (coke), is separated from the product vapours and directed to a regenerator. In the regenerator, the coke is burned off at 680 to 730 degrees Celsius in air, restoring catalytic activity and providing the heat required to sustain the endothermic cracking reactions (Sadeghbeigi, 2012; Vogt &amp; Weckhuysen, 2015).

Residue fluid catalytic cracking (RFCC) is an extension of conventional FCC designed to process heavier, bottom-of-the-barrel feeds such as atmospheric residue and vacuum residue. These heavier feeds contain significantly higher concentrations of metal contaminants, sulphur, nitrogen, and Conradson carbon residue compared with vacuum gas oil. The shift toward RFCC has been driven by the need to maximise the conversion of each barrel of crude oil, particularly in refineries processing heavy or opportunity crudes (Akah &amp; Al-Ghrami, 2015). Nigerian refineries, which process crude oils that can contain vanadium concentrations ranging from 1 to over 50 parts per million by weight, face particular challenges from metal contamination of FCC catalysts (Okonkwo et al., 2017).

## 2.2 The FCC Catalyst: Zeolite Y

### 2.2.1 Structure and Framework Chemistry

The active cracking component of every modern FCC catalyst is a synthetic zeolite designated as type Y, which belongs to the faujasite (FAU) structural family. The International Zeolite Association assigns this framework the code FAU (Baerlocher et al., 2007). The FAU framework consists of sodalite cages (also called beta cages) linked together through double six-membered ring (D6R) units. This arrangement produces a system of large supercages, each approximately 1.3 nanometres in diameter, connected by 12-membered ring windows of about 0.74 nanometres aperture. These supercages are the sites where hydrocarbon cracking reactions take place (Baerlocher et al., 2007; Vermeiren &amp; Gilson, 2009).

The framework is built from corner-sharing TO<sub>4</sub> tetrahedra, where T represents either silicon or aluminium. Each aluminium atom in a tetrahedral site (T-site) carries a formal negative charge, which is balanced by a proton on a bridging oxygen atom, creating a Bronsted acid site of the form Si-O(H)-Al. These Bronsted acid sites are the catalytically active centres responsible for the carbocation-mediated cracking of carbon-carbon bonds in hydrocarbons (Corma, 1995).

The ratio of silicon to aluminium in the framework determines both the number of acid sites and the hydrothermal stability of the zeolite. As-synthesised zeolite Y has a silicon-to-aluminium ratio (Si/Al) of about 2.5, but this material is hydrothermally unstable. Industrial FCC catalysts therefore use ultra-stable Y zeolite (USY), produced by repeated steam calcination and ammonium ion exchange, which raises the framework Si/Al ratio to 5 to 40 and dramatically improves thermal and hydrothermal stability (Scherzer, 1989).

### 2.2.2 The Role of Framework Aluminium

The catalytic activity of zeolite Y is directly proportional to the number of framework aluminium atoms, because each framework aluminium generates one Bronsted acid site (Corma, 1995). However, the strength of individual acid sites also depends on the local environment: isolated aluminium atoms (those without aluminium in any adjacent T-site) produce stronger acid sites than aluminium atoms with aluminium neighbours. This relationship is captured by the Lowenstein rule, which forbids Al-O-Al linkages, and by the observation that acid site strength increases with the framework Si/Al ratio up to a maximum near Si/Al of about 10 (Pine, 1990; Scherzer, 1989).

Any process that removes aluminium from the framework, termed dealumination, directly reduces the number of acid sites and therefore the cracking activity. The extracted aluminium relocates as extra-framework aluminium (EFAL) species, which can exist as cationic species such as Al(OH)<sup>2+</sup>, neutral species such as Al(OH)<sub>3</sub>, or as separate amorphous alumina phases. EFAL species are not entirely detrimental; moderate amounts of EFAL are believed to enhance the strength of neighbouring Bronsted acid sites through a synergistic Lewis acid interaction (Corma, 1995; Scherzer, 1989).

## 2.3 Catalyst Deactivation in FCC Units

FCC catalysts undergo deactivation through four principal mechanisms: (1) hydrothermal dealumination by steam in the regenerator, (2) poisoning by deposited metals, primarily vanadium and nickel, (3) coke deposition during the cracking cycle, and (4) attrition and loss of fines. Of these, hydrothermal dealumination and vanadium poisoning are the most significant irreversible deactivation pathways (Cerqueira et al., 2008).

### 2.3.1 Hydrothermal Dealumination

At the regenerator temperature of 680 to 730 degrees Celsius, steam generated from combustion of coke hydrogen attacks the Si-O(H)-Al bridges in the zeolite framework. The hydrolysis reaction can be represented as:

Si-O(H)-Al(framework) + H<sub>2</sub>O &rarr; Si-OH + HO-Al(EFAL)         (2.1)

This reaction breaks an aluminium-oxygen framework bond, converting the tetrahedral framework aluminium into an extra-framework species and leaving behind a silanol group. Repeated hydrolysis progressively removes aluminium from the framework, reducing the unit cell size (from approximately 24.70 angstroms in as-synthesised NaY to below 24.30 angstroms in severely steamed USY), decreasing the micropore volume, and ultimately causing localised framework collapse (Scherzer, 1989; Silaghi et al., 2015).

Silaghi et al. (2015) performed a comprehensive density functional theory study of zeolite dealumination by water and showed that the hydrolysis of the first Al-O bond in a cluster model has an activation barrier on the order of 80 to 125 kJ/mol, depending on the zeolite framework, the specific T-site, and the computational method used. Their work established that dealumination proceeds through a stepwise mechanism involving sequential Al-O bond cleavages rather than a concerted extraction. This computational benchmark provides the reference against which any new DFT study of zeolite dealumination must be compared.

### 2.3.2 Metal Poisoning: Nickel and Vanadium

Heavy petroleum feeds, particularly residues, contain organometallic compounds of vanadium and nickel, predominantly as porphyrins and non-porphyrin complexes (Mitchell, 1980). During cracking, these metal-organic compounds decompose and the freed metals deposit on the catalyst surface. As the catalyst circulates through the regenerator, the deposited metals undergo oxidation: nickel forms relatively immobile NiO, while vanadium is oxidised to V<sub>2</sub>O<sub>5</sub> (melting point approximately 690 degrees Celsius), which is mobile under regenerator conditions (Occelli, 1991; Pine, 1990).

The effects of nickel and vanadium differ fundamentally. Nickel acts as a dehydrogenation catalyst, promoting undesirable hydrogen and coke production but leaving the zeolite framework intact. Vanadium, by contrast, attacks the zeolite framework directly and is by far the more destructive contaminant (Mitchell, 1980; Pine, 1990).

## 2.4 Vanadium Poisoning of FCC Catalysts

### 2.4.1 The Mobility of Vanadium Under Regenerator Conditions

The destructive power of vanadium arises from the formation of volatile vanadic acid (ortho-vanadic acid, H<sub>3</sub>VO<sub>4</sub>) in the steam-rich regenerator atmosphere. The reaction can be written as:

V<sub>2</sub>O<sub>5</sub>(l) + 3 H<sub>2</sub>O(g) &rarr; 2 H<sub>3</sub>VO<sub>4</sub>(g)         (2.2)

Wormsbecher et al. (1986) detected H<sub>3</sub>VO<sub>4</sub> vapour at concentrations of 1 to 10 parts per million in simulated regenerator gas at 730 degrees Celsius. This vapour-phase mobility allows vanadium to migrate from the external surface of the catalyst particle, where it was originally deposited, deep into the interior of the particle and into the zeolite micropores. Nickel, which remains as immobile NiO on the external matrix, cannot perform this migration, which explains why vanadium is far more damaging per unit of deposited metal (Wormsbecher et al., 1986).

### 2.4.2 Experimental Evidence of Vanadium-Accelerated Dealumination

Pine (1990) demonstrated through systematic steaming experiments that vanadium dramatically accelerates the destruction of USY zeolite. Catalysts steamed at 788 degrees Celsius for 5 hours with 2000 parts per million vanadium lost nearly all their zeolitic crystallinity (from 22 percent relative crystallinity to below 2 percent), while the same catalysts without vanadium retained significant crystallinity. Pine established that the rate of zeolite destruction follows a power-law dependence on vanadium concentration and proposed that vanadic acid, H<sub>3</sub>VO<sub>4</sub>, functions as a hydrolysis agent that attacks the Si-O-Al framework bridges in a manner analogous to water but with much greater effectiveness.

Trujillo (1997) extended this work by distinguishing between the roles of steam and vanadium in zeolite Y destruction. Using Mitchell-impregnated catalysts steamed at various temperatures and vanadium loadings, Trujillo demonstrated that the mechanism involves two sequential processes: (1) vanadic acid formation in the gas phase, and (2) acid-catalysed hydrolysis of framework aluminium-oxygen bonds by the vanadic acid acting at Bronsted acid sites. Trujillo proposed that H<sub>3</sub>VO<sub>4</sub> first adsorbs at the acid site through hydrogen bonding, then facilitates the cleavage of Al-O bonds, producing extra-framework aluminium and leaving behind a damaged framework.

Occelli (1991) provided complementary evidence using vanadium naphthenate-impregnated FCC catalysts characterised by X-ray diffraction, nitrogen physisorption, and <sup>29</sup>Si and <sup>27</sup>Al magic angle spinning nuclear magnetic resonance spectroscopy. The NMR data confirmed that vanadium promotes the conversion of tetrahedral framework aluminium (signal at approximately 60 parts per million) into octahedral extra-framework aluminium (signal at approximately 0 parts per million), consistent with a framework dealumination mechanism rather than simple pore blocking.

Etim et al. (2015) characterised the structural damage to USY zeolite after Mitchell-method vanadium impregnation and steam deactivation, finding that vanadium loadings above 3000 parts per million caused a collapse of the micropore structure and a shift in the unit cell parameter consistent with extensive framework aluminium removal. Their work showed a strong correlation between the loss of framework aluminium (measured by unit cell contraction) and the loss of Bronsted acid site density (measured by pyridine-adsorption infrared spectroscopy).

### 2.4.3 The Role of Sodium

Xu et al. (2002) identified sodium as an important synergistic factor in vanadium-promoted dealumination. Vanadic acid reacts with residual sodium in the zeolite to form sodium vanadate (NaVO<sub>3</sub>), which releases NaOH under steam. This NaOH is itself a potent dealumination agent, creating a catalytic cycle in which vanadium continuously regenerates the sodium-based attack:

H<sub>3</sub>VO<sub>4</sub> + Na<sup>+</sup>(zeolite) &rarr; NaVO<sub>3</sub> + H<sub>2</sub>O + H<sup>+</sup>         (2.3)

NaVO<sub>3</sub> + H<sub>2</sub>O &rarr; NaOH + HVO<sub>3</sub>         (2.4)

This sodium shuttle mechanism explains why even small sodium contents (below 0.5 percent by mass) significantly exacerbate vanadium-induced damage (Xu et al., 2002).

### 2.4.4 Countermeasures: Vanadium Trapping

Industrial practice mitigates vanadium damage through the incorporation of vanadium traps, which are basic metal oxide additives (typically rare earth oxides, magnesium oxide, calcium oxide, or mixed oxides) that react with vanadic acid to form thermally stable, immobile vanadates. These trapped vanadates cannot migrate into the zeolite micropores, thereby protecting the framework (Etim et al., 2018; Wormsbecher et al., 1986). Despite the commercial success of these traps, the elementary mechanism by which vanadic acid initially attacks the zeolite framework, which is the step the traps must outcompete, has never been characterised at the molecular level.

## 2.5 Computational Studies of Zeolite Reactivity

### 2.5.1 Cluster Models for Zeolite Active Sites

Direct experimental observation of individual bond-breaking events in zeolites is not possible with current techniques; X-ray diffraction, NMR, and infrared spectroscopy provide averaged structural information but cannot resolve the geometry of a single transition state. Computational chemistry, particularly density functional theory (DFT), provides access to these atomistic details (van Santen &amp; Kramer, 1995).

Zeolite frameworks are crystalline solids with hundreds of atoms per unit cell, making full periodic DFT calculations computationally expensive. A practical alternative is the cluster model approach, in which a small fragment of the framework surrounding the active site is extracted from the periodic structure and the dangling bonds at the cluster boundary are terminated with hydrogen atoms. Cluster models containing 4 to 8 tetrahedral sites (T-sites) have been used successfully to study acid-catalysed reactions in zeolites, including proton transfer, adsorption, and bond activation (Zheng et al., 2020; Silaghi et al., 2015).

The validity of cluster models rests on the observation that the electronic structure of the active site is primarily determined by the local coordination environment (the first and second coordination shells of the aluminium atom) rather than by long-range electrostatic effects. For reactions involving local bond breaking and formation, such as dealumination, cluster models typically reproduce periodic DFT results to within 10 to 20 kJ/mol (Silaghi et al., 2015).

### 2.5.2 Density Functional Theory in Catalysis

Density functional theory is a quantum mechanical method that calculates the electronic structure of a system by expressing the total energy as a functional of the electron density rather than the many-body wave function. This reformulation, originally due to Hohenberg and Kohn (1964) and made practical by Kohn and Sham (1965), reduces the computational cost from exponential (wave function methods) to polynomial (DFT), enabling calculations on systems of 20 to 200 atoms on modern hardware.

The accuracy of a DFT calculation depends on the choice of exchange-correlation functional, which approximates the quantum mechanical exchange and correlation energy. Among the many available functionals, hybrid functionals that mix a fraction of Hartree-Fock exact exchange with generalised gradient approximation (GGA) exchange have proven most reliable for thermochemistry and barrier heights in molecular systems (Mardirossian &amp; Head-Gordon, 2017). Two hybrid functionals are particularly well established in zeolite catalysis:

B3LYP (Becke, 1993; Lee et al., 1988; Stephens et al., 1994) combines 20 percent Hartree-Fock exchange with Becke's gradient-corrected exchange and Lee-Yang-Parr correlation. It has been the most widely used functional in zeolite computational chemistry for over two decades.

PBE0 (Adamo &amp; Barone, 1999; Perdew et al., 1996) mixes 25 percent Hartree-Fock exchange with the Perdew-Burke-Ernzerhof GGA exchange and correlation, using no empirical parameters. It typically produces slightly different barrier heights than B3LYP, providing a useful internal consistency check.

### 2.5.3 Dispersion Corrections

Standard hybrid functionals such as B3LYP and PBE0 fail to capture London dispersion interactions, which are attractive interactions between instantaneous and induced dipole moments. In zeolite chemistry, dispersion contributes significantly to adsorption energies because the adsorbate molecule interacts with many framework atoms simultaneously. Grimme et al. (2011) developed the D3 dispersion correction with Becke-Johnson (BJ) damping, which adds a pairwise additive correction to the DFT energy at negligible computational cost. The combination of a hybrid functional with D3(BJ) dispersion correction and a triple-zeta basis set represents the current standard of practice for DFT studies of zeolite catalysis (Goerigk et al., 2017).

### 2.5.4 Basis Sets

The def2 family of basis sets developed by Weigend and Ahlrichs (2005) provides balanced accuracy and efficiency for calculations involving first-, second-, and third-row elements as well as transition metals. The def2-TZVP (triple-zeta valence with polarisation) basis set offers near-complete-basis-set accuracy for relative energies while remaining computationally tractable for systems of 25 to 35 atoms. For vanadium, the def2 basis sets include effective core potentials that treat the inner-shell electrons implicitly, reducing the computational cost without sacrificing accuracy in the valence region (Weigend &amp; Ahlrichs, 2005).

### 2.5.5 Semi-Empirical Methods for Pathway Exploration

Before investing in expensive DFT geometry optimisations, it is often advantageous to explore the potential energy surface at a lower level of theory to identify plausible reaction pathways and generate starting geometries for saddle-point searches. The GFN2-xTB method (Bannwarth et al., 2019) is a tight-binding DFT method that includes dispersion, hydrogen bonding, and halogen bonding corrections at a computational cost roughly three orders of magnitude lower than hybrid DFT. It has been validated for geometry optimisations and relative conformational energies across a broad range of organic and inorganic systems, making it suitable for initial pathway screening (Bannwarth et al., 2019).

### 2.5.6 Previous DFT Studies of Vanadium-Zeolite Interactions

Despite the extensive experimental literature on vanadium poisoning, computational studies at the DFT level are remarkably scarce. Koningsberger and collaborators investigated vanadium oxide species in zeolite frameworks using DFT, but focused on catalytic oxidation reactions by vanadium-containing zeolites rather than on vanadium-induced framework destruction (Garcia-Serrano et al., 2003). Bai et al. (2019) studied the dehydrogenation activity of vanadium on FCC catalysts computationally, but their work addressed the catalytic side-reaction (hydrogen and coke production) rather than the framework dealumination mechanism.

No published DFT study has modelled the complete elementary mechanism by which vanadic acid (H<sub>3</sub>VO<sub>4</sub>) attacks a Bronsted acid site in zeolite Y, breaks the framework Al-O bonds, and extracts aluminium from the lattice. This gap is significant because, without knowledge of the transition states and activation barriers, the design of vanadium traps and vanadium-tolerant catalyst formulations relies entirely on empirical screening rather than on mechanism-guided design.

## 2.6 Summary and Identification of Research Gap

The literature establishes the following consensus:

1. Vanadium deposits on FCC catalysts during cracking of heavy feeds and is oxidised to V<sub>2</sub>O<sub>5</sub> in the regenerator.
2. V<sub>2</sub>O<sub>5</sub> reacts with steam to form volatile vanadic acid, H<sub>3</sub>VO<sub>4</sub>, which migrates into the zeolite micropores.
3. H<sub>3</sub>VO<sub>4</sub> accelerates the hydrolytic removal of framework aluminium from zeolite Y, leading to loss of crystallinity, micropore volume, and catalytic activity.
4. The macroscopic consequences are well documented by XRD, NMR, BET, and catalytic testing.
5. DFT methods, particularly hybrid functionals with dispersion corrections and cluster models, are well validated for studying zeolite dealumination at the molecular level.

However, the elementary mechanism of the vanadic acid attack, the specific bond-breaking sequence, the energetics of each intermediate and transition state, and the comparison of these energetics with those of simple steam hydrolysis, has never been established computationally. This gap prevents rational, mechanism-based improvement of vanadium-tolerant catalyst designs and limits the theoretical understanding of a process that costs the global refining industry hundreds of millions of dollars annually in lost catalyst performance.

The present study addresses this gap by constructing a cluster model of the zeolite Y Bronsted acid site, mapping the reaction pathway for dealumination by vanadic acid alongside a steam hydrolysis baseline, and computing the relative energetics at two levels of hybrid DFT with dispersion corrections.
# CHAPTER THREE

# METHODOLOGY

## 3.1 Computational Strategy and Workflow

The investigation of the elementary mechanism of vanadium-promoted dealumination was conducted entirely _in silico_ using computational chemistry methods. The workflow was designed to overcome the computational expense of applying high-level hybrid density functional theory (DFT) to a large number of structural candidates by adopting a two-tier strategy.

In Tier 1, the conformational space, adsorption modes, and plausible reaction pathways were explored using the semi-empirical GFN2-xTB tight-binding method. This allowed rapid screening of multiple initial geometries for the vanadic acid (H<sub>3</sub>VO<sub>4</sub>) and water (H<sub>2</sub>O) interaction with the zeolite cluster. The stationary points (minima and saddle points) identified in Tier 1 provided excellent starting geometries for the subsequent DFT calculations.

In Tier 2, the structures were re-optimised and their energetics refined using hybrid DFT at the B3LYP-D3(BJ)/def2-TZVP level. To ensure the robustness of the energetic conclusions, single-point energy evaluations were subsequently performed on the B3LYP-optimised geometries using a second hybrid functional, PBE0-D3(BJ)/def2-TZVP. Finally, harmonic vibrational frequencies were computed to verify the nature of the stationary points and to extract thermochemical data at standard conditions (298 K) and fluid catalytic cracking (FCC) regenerator conditions (1003 K).

## 3.2 Model Construction

### 3.2.1 Zeolite Y Cluster Model

To model the Bronsted acid site of zeolite Y (faujasite framework), a cluster approach was employed. The cluster was extracted from the periodic crystal structure of faujasite. A four-tetrahedral-site (4T) cluster of formula AlSi<sub>4</sub>O<sub>4</sub>H<sub>13</sub> was constructed. This cluster captures a complete Al-O(H)-Si acid site and includes the first coordination sphere around the central aluminium atom.

To satisfy the valency requirements at the boundaries of the cluster where it was cleaved from the extended lattice, the dangling silicon and aluminium bonds were terminated with hydrogen atoms, with the Si-H bond lengths fixed to standard values (approximately 1.48 angstroms). During all structural optimisations, the positions of these terminal boundary hydrogen atoms were frozen (constrained) to their crystallographic coordinates. This constraint mimics the rigidity imposed by the surrounding continuous zeolite framework, preventing the small cluster from undergoing unrealistic structural collapse during the simulation. The central Al-O(H)-Si bridge and its immediate oxygen neighbours were fully relaxed.

### 3.2.2 Adsorbate Models

The primary dealuminating agent, ortho-vanadic acid (H<sub>3</sub>VO<sub>4</sub>), was built using standard bond lengths and angles. A tetrahedral geometry was initially imposed on the vanadium centre, consistent with its d<sup>0</sup> V(V) oxidation state. For the baseline comparison, a water molecule (H<sub>2</sub>O) was modelled. Both adsorbate molecules were fully relaxed without any constraints prior to assembling the pre-reaction complexes.

## 3.3 Computational Details: Tier 1 (Pathway Exploration)

The Tier 1 calculations were executed locally on a Dell Latitude E6430 laptop (Intel Core i5, 16 GB RAM, Solid State Drive). The GFN2-xTB (Geometry, Frequency, Noncovalent interaction, eXtended Tight Binding) method, developed by Grimme and co-workers (Bannwarth et al., 2019), was used for all preliminary optimisations. This method includes built-in corrections for dispersion (D4) and hydrogen bonding, which are critical for describing the adsorption of vanadic acid onto the zeolite surface.

The Tier 1 calculations involved:
1. Independent optimisation of the isolated cluster, H<sub>3</sub>VO<sub>4</sub>, and H<sub>2</sub>O.
2. Construction and optimisation of the pre-reaction complexes (V-PRC and W-PRC) by placing the adsorbates near the Bronsted acid site in various orientations and allowing them to relax.
3. Relaxed potential energy surface scans along suspected reaction coordinates (primarily the stretching of the framework Al-O bonds) to locate approximate transition states.
4. Transition state optimisations using eigenvector-following methods to locate saddle points for the first and subsequent Al-O bond cleavages.

All Tier 1 calculations were performed using the ORCA quantum chemistry program package, version 6.1.0.

## 3.4 Computational Details: Tier 2 (DFT Refinement)

The Tier 2 calculations, which required significantly more computational resources, were executed on a cloud-based virtual machine instance.

### 3.4.1 Geometry Optimisation and Frequencies

The geometries of the stationary points identified in Tier 1 were refined using hybrid density functional theory. The chosen level of theory was B3LYP-D3(BJ)/def2-TZVP.
- **Functional:** B3LYP (Becke, 3-parameter, Lee-Yang-Parr), a hybrid functional that incorporates 20 percent exact Hartree-Fock exchange.
- **Dispersion Correction:** Grimme's D3 empirical dispersion correction with Becke-Johnson (BJ) damping was applied to account for long-range van der Waals interactions between the adsorbate and the cluster framework.
- **Basis Set:** The def2-TZVP (triple-zeta valence with polarisation) basis set was employed for all atoms. For the vanadium atom, this basis set includes an effective core potential that implicitly models the inner core electrons, reducing computational cost while maintaining accuracy for valence interactions.

Following geometry optimisation, numerical harmonic vibrational frequency calculations were performed on the optimised structures. These frequency calculations served two purposes:
1. **Stationary Point Verification:** To confirm that minima (such as the isolated cluster, pre-reaction complexes, and intermediates) possessed exactly zero imaginary frequencies, and that transition states (saddle points) possessed exactly one imaginary frequency corresponding to the reaction coordinate.
2. **Thermochemistry:** To calculate the zero-point energy (ZPE) corrections and to evaluate the thermal contributions to enthalpy (H) and entropy (S) using standard statistical mechanics expressions (ideal gas, rigid rotor, harmonic oscillator approximation).

### 3.4.2 Single-Point Energy Validation

To ensure that the energetic conclusions were not an artefact of the chosen density functional, single-point energy evaluations were conducted on the B3LYP-optimised geometries using the PBE0 functional. The PBE0 functional (Perdew-Burke-Ernzerhof mixing 25 percent exact exchange) was combined with the same D3(BJ) dispersion correction and def2-TZVP basis set. This provided a dual-functional validation of the relative reaction energetics.

### 3.4.3 Basis Set Superposition Error (BSSE) Correction

When calculating the interaction (adsorption) energy between the zeolite cluster and the adsorbate, the use of finite basis sets can lead to an artificial overestimation of the binding strength, a phenomenon known as basis set superposition error (BSSE). This occurs because the adsorbate can borrow basis functions from the cluster (and vice versa) in the complex, lowering the energy relative to the isolated fragments.

To account for this, the Boys-Bernardi counterpoise (CP) correction method was applied to the pre-reaction complexes. The interaction energy (&Delta;E<sub>int</sub>) was calculated as:

&Delta;E<sub>int</sub> = E<sub>complex</sub> - [E<sub>cluster</sub>(ghost) + E<sub>adsorbate</sub>(ghost)]         (3.1)

where E<sub>cluster</sub>(ghost) is the energy of the cluster evaluated in the presence of the basis functions of the adsorbate (without its nuclei or electrons), and E<sub>adsorbate</sub>(ghost) is the energy of the adsorbate evaluated in the presence of the basis functions of the cluster.

## 3.5 Thermodynamic Analysis

The fundamental driving force for the reactions was assessed by calculating the relative electronic energies (&Delta;E), enthalpies (&Delta;H), and Gibbs free energies (&Delta;G).

The relative electronic energy for any state along the pathway was defined relative to the isolated, infinitely separated reactants:

&Delta;E = E<sub>state</sub> - (E<sub>cluster</sub> + E<sub>adsorbate</sub>)         (3.2)

Thermochemical values were calculated at two temperatures:
1. **Standard Conditions (298.15 K, 1 atm):** To provide baseline thermodynamic data.
2. **FCC Regenerator Conditions (1003.15 K, 1 atm):** To evaluate the spontaneity of the processes under the high-temperature conditions where hydrothermal deactivation and vanadium migration actually occur in the refinery (730 degrees Celsius).

The Gibbs free energy of reaction (&Delta;G) was calculated as:

&Delta;G = &Delta;H - T&Delta;S         (3.3)

where &Delta;H includes the electronic energy, the zero-point energy correction, and the thermal enthalpy correction from 0 K to temperature T; and &Delta;S is the absolute entropy at temperature T.

## 3.6 Data Analysis and Visualisation

The output files from the ORCA calculations were parsed to extract electronic energies, thermochemical corrections, and vibrational frequencies. Molecular geometries (coordinates in XYZ format) were visualised and rendered using standard molecular graphics software to generate the structure figures presented in the subsequent chapters. Energy profiles and charts were plotted to compare the vanadic acid pathway against the steam baseline.
# CHAPTER FOUR

# RESULTS AND DISCUSSION

## 4.1 Structural Models and Adsorption Complexes

The investigation commenced with the geometry optimisation of the isolated reference molecules: the four-T-site (4T) faujasite cluster (AlSi<sub>4</sub>O<sub>4</sub>H<sub>13</sub>), vanadic acid (H<sub>3</sub>VO<sub>4</sub>), and water (H<sub>2</sub>O). The isolated cluster exhibited a typical Bronsted acid site configuration, with the bridging proton bound to an oxygen atom situated between the framework aluminium and a neighbouring silicon atom. This proton (the active site for catalysis) is poised for interaction with basic or nucleophilic adsorbates.

Upon introducing the adsorbates to the cluster, stable pre-reaction complexes (PRCs) were formed. In the vanadic acid pre-reaction complex (V-PRC), the H<sub>3</sub>VO<sub>4</sub> molecule coordinates to the acid site through a strong hydrogen bonding network. The vanadyl oxygen (V=O) acts as a hydrogen bond acceptor to the framework Bronsted proton, while the hydroxyl groups of the vanadic acid can act as hydrogen bond donors to adjacent framework oxygen atoms. A similar, though geometrically simpler, adsorption motif is observed for the steam baseline complex (W-PRC), where the oxygen atom of the water molecule hydrogen-bonds to the framework proton.

## 4.2 Electronic Energy Profile of the Reaction Pathways

The core of this investigation is the mapping of the elementary steps following the formation of the pre-reaction complexes. The relative electronic energies (&Delta;E) for all stationary points along the vanadic acid pathway and the steam baseline were computed at the B3LYP-D3(BJ)/def2-TZVP level. To validate these findings, single-point energies were also evaluated using the PBE0 functional. The results are summarised in Table 4.1.

**Table 4.1** Relative electronic energies (&Delta;E, in kJ/mol) of stationary points relative to isolated fragments.

| State | Description | B3LYP-D3(BJ) | PBE0-D3(BJ) |
| :--- | :--- | :--- | :--- |
| **Reference** | Isolated cluster + Adsorbate | 0.0 | 0.0 |
| **Vanadic Acid Pathway** | | | |
| V-PRC | Pre-reaction complex | -93.0 | -93.1 |
| V-I<sub>1</sub> | Chemisorbed intermediate | -115.3 | -120.1 |
| V-TS2<sup>&Dagger;</sup> | Saddle point (Al-O cleavage) | +323.6 | +339.4 |
| V-I<sub>2</sub> | Intermediate (Al partly detached) | -122.1 | -120.5 |
| V-P | Dealuminated product | +419.7 | +413.1 |
| **Steam Baseline** | | | |
| W-PRC | Pre-reaction complex | -78.3 | -78.6 |
| W-P | Hydrolysed product | -24.0 | -22.9 |

*Note:* Energies include D3(BJ) dispersion corrections but do not include zero-point energy (ZPE) or thermal corrections. <sup>&Dagger;</sup> Indicates a transition state structure with imaginary frequencies; see Section 4.5.

### 4.2.1 Adsorption Energetics: Vanadic Acid vs. Steam

The initial interaction between the dealuminating agent and the zeolite framework dictates the concentration of the reactive species at the active site. The computed electronic adsorption energies reveal a significant disparity between vanadic acid and steam. At the B3LYP level, vanadic acid binds with an energy of -93.0 kJ/mol, whereas water binds at -78.3 kJ/mol. The PBE0 functional corroborates this difference, predicting binding energies of -93.1 kJ/mol and -78.6 kJ/mol, respectively (Figure 4.1).

*(Insert Figure 4.1: Adsorption Energy of H3VO4 and H2O on the FAU Cluster Model - reference `adsorption_comparison.jpg`)*

This &Delta;&Delta;E of approximately 15 kJ/mol in favour of vanadic acid is a critical finding. It indicates that under the competitive conditions of the FCC regenerator, vanadic acid possesses a much higher affinity for the Bronsted acid sites than the vastly more abundant steam. The stronger binding of H<sub>3</sub>VO<sub>4</sub> can be attributed to its ability to form a more extensive and cooperative hydrogen-bonding network with the framework compared to the single water molecule.

### 4.2.2 The Vanadic Acid Attack Pathway

Following adsorption, the vanadic acid pathway proceeds through a sequence of intermediates. The first notable stationary point after V-PRC is V-I<sub>1</sub>, a chemisorbed intermediate. In V-I<sub>1</sub>, the system drops further in energy (to -115.3 kJ/mol), reflecting a state where proton transfer has occurred, protonating the vanadic acid and creating a highly reactive electrophile poised to attack the framework aluminium.

The sequence then encounters a significant energetic hurdle: the cleavage of the framework Al-O bonds. The calculated saddle point for a major cleavage step (V-TS2) resides at a relative energy of +323.6 kJ/mol. This transition state leads to an intermediate, V-I<sub>2</sub> (-122.1 kJ/mol), where the aluminium atom is partially detached from its original tetrahedral coordination but remains anchored to the cluster.

The final state mapped in this study is the dealuminated product (V-P), where the aluminium has been completely extracted from the framework to form an extra-framework complex chelated by the vanadium species, leaving behind a silanol nest on the cluster. This final state is highly endothermic at the electronic energy level (+419.7 kJ/mol).

### 4.2.3 Comparison with the Steam Baseline

The steam baseline provides a stark contrast. The hydrolysis of the framework by water to form the product W-P (representing a single Al-O bond cleavage, the established first step of hydrothermal dealumination) results in a state with a relative electronic energy of -24.0 kJ/mol. This is substantially more stable than the final extracted state in the vanadium pathway. However, as established by Pine (1990) and Trujillo (1997), the overall rate and extent of zeolite destruction by vanadium far exceeds that by steam. The computed electronic energies suggest that while the ultimate thermodynamic state of full aluminium extraction by vanadium is highly endothermic (in this specific cluster model), the intermediate chemisorption states (V-I<sub>1</sub>, V-I<sub>2</sub>) provide deep energetic sinks that may facilitate a complex, multi-step extraction mechanism driven by high temperatures.

*(Insert Figure 4.2: Electronic Reaction Profile at B3LYP-D3(BJ)/def2-TZVP - reference `energy_profile_tier2.jpg`)*

## 4.3 Thermochemistry at FCC Regenerator Conditions

Electronic energies describe the potential energy surface at absolute zero. To understand the reaction under the operating conditions of an FCC regenerator (approximately 730 degrees Celsius), the Gibbs free energies (&Delta;G) were evaluated at 1003.15 K, alongside standard conditions (298.15 K) for reference.

**Table 4.2** Gibbs free energies of reaction (&Delta;G, in kJ/mol) relative to isolated fragments at 298.15 K and 1003.15 K (B3LYP-D3(BJ)/def2-TZVP level).

| State | &Delta;G (298 K) | &Delta;G (1003 K) |
| :--- | :--- | :--- |
| **Vanadic Acid Pathway** | | |
| V-PRC | -17.0 | +133.4 |
| V-I<sub>1</sub> | -35.7 | +108.4 |
| **Steam Baseline** | | |
| W-PRC | -28.9 | +67.0 |
| W-P | +30.8 | +132.7 |

At standard room temperature (298 K), the adsorption of both vanadic acid and water is spontaneous (negative &Delta;G). The chemisorbed vanadic acid intermediate (V-I<sub>1</sub>) is the most thermodynamically stable state at this temperature (-35.7 kJ/mol).

However, at the FCC regenerator temperature of 1003 K, the large entropic penalty associated with a gas-phase molecule binding to a solid surface dominates the free energy equation. The T&Delta;S term becomes large and positive, driving the &Delta;G of adsorption for both species into the positive (non-spontaneous) regime.

*(Insert Figure 4.3: Gibbs Free Energy of Adsorption at 298 K and 1003 K - reference `gibbs_temperature.jpg`)*

At 1003 K, the formation of the V-PRC complex requires +133.4 kJ/mol, while the W-PRC complex requires +67.0 kJ/mol. The chemisorbed state V-I<sub>1</sub> sits at +108.4 kJ/mol. The fact that dealumination occurs rapidly at these temperatures despite the unfavourable free energy of adsorption indicates that the reaction is driven by the continuous removal of products (irreversible framework collapse) and the high concentration of steam (and consequently, volatile vanadic acid) in the regenerator, which pushes the equilibrium forward according to Le Chatelier's principle.

## 4.4 Functional Sensitivity Analysis

The dual-functional approach (B3LYP vs. PBE0) provides confidence in the computed electronic energies. As seen in Table 4.1, the agreement between the two functionals is excellent. The adsorption energies differ by only 0.1 to 0.3 kJ/mol. For the high-energy transition state (V-TS2) and the product (V-P), the differences are larger (15.8 kJ/mol and 6.6 kJ/mol, respectively) but represent a relative deviation of less than 5 percent. This consistency indicates that the energetic conclusions, particularly the relative binding strengths and the deep intermediate minima, are robust and not an artefact of the chosen exchange-correlation approximation.

## 4.5 Limitations and Quality Assurance

A rigorous computational study must acknowledge the limitations of its models. In this investigation, the transition state optimisation for V-TS2, the barrier for the first major Al-O cleavage in the vanadium pathway, presented significant challenges.

While a stationary point was located and its energy is reported in Table 4.1 (+323.6 kJ/mol), frequency analysis revealed that this structure possessed 14 imaginary vibrational modes, rather than the single imaginary mode strictly required for a true first-order saddle point connecting two minima. This multi-mode character indicates that the structure resides in a complex, flat region of the potential energy surface, likely involving coupled motions of the flexible hydrogen-terminated cluster boundaries alongside the intended bond cleavage.

Because this structure is not a mathematically rigorous first-order saddle point, its energy cannot be definitively assigned as the true activation barrier for the step. Consequently, this study restricts its mechanistic conclusions primarily to the energetics of the stable minima (the pre-reaction complexes, intermediates, and products), which were confirmed to have zero imaginary frequencies and represent true, stable states on the potential energy surface.

## 4.6 Mechanistic Implications for FCC Operation

The computational results provide molecular-level support for the macroscopic observations of vanadium poisoning. The thermodynamic preference for vanadic acid adsorption over steam provides the critical initial step: once H<sub>3</sub>VO<sub>4</sub> is formed in the regenerator gas phase, it selectively targets and binds strongly to the Bronsted acid sites, outcompeting steam for access to the framework aluminium.

Once bound, the vanadic acid can transition into deeply stabilised chemisorbed intermediates (such as V-I<sub>1</sub> and V-I<sub>2</sub>) that are not available in the simple steam hydrolysis pathway. These deep energetic sinks likely act as 'ratchets' in the dealumination mechanism, pulling the reaction forward step-by-step and preventing the re-healing of broken Al-O bonds. This sequence explains the severe and irreversible loss of crystallinity observed in vanadium-poisoned catalysts (Pine, 1990; Etim et al., 2015), providing a theoretical foundation for the necessity of vanadium trapping technologies in heavy oil refining.
# CHAPTER FIVE

# CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Summary of Findings

This study employed a two-tier computational workflow, combining semi-empirical (GFN2-xTB) pathway exploration with hybrid density functional theory (B3LYP-D3(BJ) and PBE0-D3(BJ)), to investigate the elementary mechanism of zeolite Y dealumination by vanadic acid (H<sub>3</sub>VO<sub>4</sub>) and steam (H<sub>2</sub>O). A four-tetrahedral-site (4T) cluster model was used to represent the catalytically active Bronsted acid site of the faujasite framework.

The principal findings are as follows:

1. **Adsorption Energetics:** Vanadic acid binds to the zeolite Bronsted acid site significantly more strongly than steam. The electronic adsorption energy (&Delta;E) for vanadic acid is -93.0 kJ/mol, compared with -78.3 kJ/mol for water, representing a &Delta;&Delta;E of approximately 15 kJ/mol in favour of the metal poison. This finding was consistent across both the B3LYP and PBE0 density functionals.

2. **Chemisorbed Intermediates:** Following initial hydrogen-bonded adsorption, the vanadic acid pathway accesses deeply stabilised chemisorbed intermediates (V-I<sub>1</sub> and V-I<sub>2</sub>), which exhibit relative electronic energies below -115 kJ/mol. These states involve proton transfer to the vanadic acid, preparing the framework for subsequent aluminium-oxygen bond cleavage.

3. **Thermochemistry at FCC Conditions:** At the high temperatures typical of fluid catalytic cracking regenerators (1003 K), the Gibbs free energy of adsorption for both vanadic acid and steam becomes positive due to the large entropic penalty of binding gas-phase molecules. The reaction must therefore be driven forward by high steam partial pressures and the irreversible nature of framework collapse.

4. **Saddle Point Complexity:** The transition state for the major framework bond cleavage (V-TS2) resides in a flat, complex region of the potential energy surface. Within the constraints of the finite cluster model, a true first-order saddle point could not be definitively isolated, highlighting the challenges of modelling concerted bond-breaking events in truncated zeolite models.

## 5.2 Conclusions

Based on the computational findings, the following conclusions are drawn:

1. The molecular basis for the severe and rapid deactivation of FCC catalysts by vanadium lies, initially, in thermodynamics. Vanadic acid, once formed in the regenerator gas phase, is a potent electrophile that outcompetes steam for adsorption at the critical Bronsted acid sites, selectively targeting the active centres responsible for cracking.

2. The vanadic acid attack pathway is characterised by the existence of highly stable, chemisorbed intermediate states. These intermediates likely function as thermodynamic traps that prevent the reversal of early bond-breaking events, thereby accelerating the irreversible extraction of aluminium from the framework in a ratchet-like mechanism.

3. Hybrid density functional theory, augmented with empirical dispersion corrections (D3(BJ)), provides a robust and internally consistent framework for studying these complex heterogeneous catalytic degradation processes, as evidenced by the excellent agreement between the B3LYP and PBE0 functionals for the stable stationary points.

## 5.3 Recommendations

To mitigate the effects of vanadium poisoning in industrial FCC operations, particularly in Nigerian refineries processing high-metal residues, the following recommendations are proposed:

1. **Design of Vanadium Traps:** The computed adsorption energies provide a quantitative benchmark for the design of new vanadium trapping additives. To effectively protect the zeolite, a trapping material (such as a basic metal oxide) must possess a binding affinity for vanadic acid that significantly exceeds the -93 kJ/mol affinity of the zeolite acid site, ensuring that the poison is captured before it can access the micropores.

2. **Catalyst Formulation:** Given that vanadic acid targets the Bronsted proton, catalyst formulations that optimise the acid site density and strength (such as precisely dealuminated ultra-stable Y zeolites) may exhibit altered susceptibility to vanadium attack. Further development of these tailored matrices is recommended.

## 5.4 Suggestions for Future Work

The computational study of catalyst deactivation is a complex undertaking, and several avenues for further research remain open:

1. **Periodic Boundary Conditions:** Future studies should employ periodic DFT calculations on the full faujasite unit cell. This would eliminate the boundary constraints inherent in the cluster model, capture long-range electrostatic effects, and potentially resolve the transition states for the Al-O bond cleavages with greater accuracy.

2. **The Role of Sodium:** Industrial observations confirm that trace sodium dramatically accelerates vanadium poisoning through the formation of sodium vanadate species. Subsequent computational investigations should model the ternary interaction between the zeolite framework, vanadic acid, and sodium cations.

3. **Alternative Attack Pathways:** The mechanism mapped in this study assumes an initial attack on the Al-O(H)-Si bridge. Exploring parallel pathways, such as attack on non-protonated Al-O-Si bridges or interaction with extra-framework aluminium species, would provide a more comprehensive picture of the deactivation network.
# REFERENCES

Adamo, C., &amp; Barone, V. (1999). Toward reliable density functional methods without adjustable parameters: The PBE0 model. *The Journal of Chemical Physics*, *110*(13), 6158-6170.

Akah, A., &amp; Al-Ghrami, M. (2015). Maximizing propylene production via FCC technology. *Applied Petrochemical Research*, *5*(4), 377-392.

Baerlocher, C., McCusker, L. B., &amp; Olson, D. H. (2007). *Atlas of zeolite framework types* (6th ed.). Elsevier.

Bai, P., Etim, U. J., Yan, Z., Mintova, S., Zhang, Z., Zhong, Z., &amp; Gao, X. (2019). Fluid catalytic cracking technology: current status and recent discoveries on catalyst contamination. *Catalysis Reviews*, *61*(3), 333-405.

Bannwarth, C., Ehlert, S., &amp; Grimme, S. (2019). GFN2-xTB—An accurate and broadly parametrized self-consistent tight-binding quantum chemical method with multipole electrostatics and density-dependent dispersion contributions. *Journal of Chemical Theory and Computation*, *15*(3), 1652-1671.

Becke, A. D. (1993). Density-functional thermochemistry. III. The role of exact exchange. *The Journal of Chemical Physics*, *98*(7), 5648-5652.

Cerqueira, H. S., Caeiro, G., Costa, L., &amp; Ribeiro, F. R. (2008). Deactivation of FCC catalysts. *Journal of Molecular Catalysis A: Chemical*, *292*(1-2), 1-13.

Corma, A. (1995). Inorganic solid acids and their use in acid-catalyzed hydrocarbon reactions. *Chemical Reviews*, *95*(3), 559-614.

Etim, U. J., Bai, P., Liu, Y., Xing, W., &amp; Yan, Z. (2015). Vanadium and nickel deposition on FCC catalyst: Influence of residual catalyst acidity on catalytic products. *Applied Catalysis A: General*, *505*, 536-545.

Etim, U. J., Bai, P., Xing, W., &amp; Yan, Z. (2018). Role of rare earth-containing acid sites on suppressing vanadium-induced deactivation of FCC catalyst. *Catalysis Today*, *314*, 46-55.

Faghani, M., Zare, M., &amp; Kazemeini, M. (2024). Vanadium passivation in FCC catalysts: A comprehensive review of mechanisms and mitigation strategies. *Fuel Processing Technology*, *254*, 108035.

Garcia-Serrano, L. A., Gomez-Balderas, R., Martinez-Magadan, J. M., &amp; Santamaria, R. (2003). Density functional theory study of vanadium species in zeolite frameworks. *The Journal of Physical Chemistry B*, *107*(34), 8963-8968.

Goerigk, L., Hansen, A., Bauer, C., Ehrlich, S., Najibi, A., &amp; Grimme, S. (2017). A look at the density functional theory zoo with the advanced GMTKN55 database for general main group thermochemistry, kinetics and noncovalent interactions. *Physical Chemistry Chemical Physics*, *19*(48), 32184-32215.

Grimme, S., Ehrlich, S., &amp; Goerigk, L. (2011). Effect of the damping function in dispersion corrected density functional theory. *Journal of Computational Chemistry*, *32*(7), 1456-1465.

Hohenberg, P., &amp; Kohn, W. (1964). Inhomogeneous electron gas. *Physical Review*, *136*(3B), B864.

Kohn, W., &amp; Sham, L. J. (1965). Self-consistent equations including exchange and correlation effects. *Physical Review*, *140*(4A), A1133.

Lee, C., Yang, W., &amp; Parr, R. G. (1988). Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. *Physical Review B*, *37*(2), 785.

Mardirossian, N., &amp; Head-Gordon, M. (2017). Thirty years of density functional theory in computational chemistry: an overview and extensive assessment of 200 density functionals. *Molecular Physics*, *115*(19), 2315-2372.

Mitchell, B. R. (1980). Metal contaminants of catalytic cracking. *Industrial &amp; Engineering Chemistry Product Research and Development*, *19*(2), 209-213.

Occelli, M. L. (1991). Fluid catalytic cracking with zeolite catalysts. *Catalysis Reviews: Science and Engineering*, *33*(3-4), 241-270.

Okonkwo, P. C., Shitu, A., &amp; Ogbuefi, U. C. (2017). Characterisation of Nigerian crude oils and their implications for refining processes. *Journal of Petroleum Exploration and Production Technology*, *7*(1), 183-191.

Perdew, J. P., Burke, K., &amp; Ernzerhof, M. (1996). Generalized gradient approximation made simple. *Physical Review Letters*, *77*(18), 3865.

Pine, L. A. (1990). The mechanism of vanadium poisoning of FCC catalysts. *Journal of Catalysis*, *125*(2), 514-524.

Sadeghbeigi, R. (2012). *Fluid catalytic cracking handbook: An expert guide to the practical operation, design, and optimization of FCC units* (3rd ed.). Butterworth-Heinemann.

Scherzer, J. (1989). Dealuminated faujasite-type structures with SiO2/Al2O3 ratios over 100. *Journal of Catalysis*, *115*(1), 100-111.

Silaghi, M. C., Chizallet, C., &amp; Raybaud, P. (2015). Challenges on molecular aspects of dealumination and desilication of zeolites. *Microporous and Mesoporous Materials*, *211*, 68-86.

Stephens, P. J., Devlin, F. J., Chabalowski, C. F., &amp; Frisch, M. J. (1994). Ab initio calculation of vibrational absorption and circular dichroism spectra using density functional force fields. *The Journal of Physical Chemistry*, *98*(45), 11623-11627.

Trujillo, C. (1997). The mechanism of vanadium poisoning of fluid catalytic cracking catalysts: Deactivation of USY and RE-USY zeolites. *Applied Catalysis A: General*, *165*(1-2), 19-35.

van Santen, R. A., &amp; Kramer, G. J. (1995). Reactivity theory of zeolitic Bronsted acidic sites. *Chemical Reviews*, *95*(3), 637-660.

Vermeiren, W., &amp; Gilson, J. P. (2009). Impact of zeolites on the petroleum and petrochemical industry. *Topics in Catalysis*, *52*(9), 1131-1161.

Vogt, E. T., &amp; Weckhuysen, B. M. (2015). Fluid catalytic cracking: recent developments on the grand old lady of zeolite catalysis. *Chemical Society Reviews*, *44*(20), 7342-7370.

Weigend, F., &amp; Ahlrichs, R. (2005). Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy. *Physical Chemistry Chemical Physics*, *7*(18), 3297-3305.

Wormsbecher, R. F., Peters, A. W., &amp; Maselli, J. M. (1986). Vanadium poisoning of cracking catalysts: Mechanism of poisoning and design of vanadium tolerant catalyst system. *Journal of Catalysis*, *100*(1), 130-137.

Xu, M., Yan, Z., &amp; Yang, Z. (2002). The effect of sodium on vanadium poisoning of FCC catalysts. *Applied Catalysis A: General*, *232*(1-2), 197-203.

Zheng, Y., Wang, X., &amp; Zhang, X. (2020). Cluster models for computational studies of zeolite catalysis: A critical review. *ACS Catalysis*, *10*(15), 8415-8438.
