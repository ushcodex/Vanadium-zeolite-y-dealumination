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
