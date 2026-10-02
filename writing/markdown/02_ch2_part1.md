# CHAPTER TWO

# 2.0 LITERATURE REVIEW

This chapter reviews the literature in an order that moves from the broad context of energy and petroleum down through refining and catalytic cracking to the specific subject of the study, and closes with the research gap the study addresses.

## 2.1 Energy and the Central Place of Petroleum

### 2.1.1 Petroleum in the global energy system

Modern economies run on energy carriers: electricity, liquid fuels, gases, and solids. Petroleum remains the single most important primary energy commodity in the world energy system, and oil-based transport fuels continue to dominate road and freight mobility in most of the world (International Energy Agency [IEA], 2024). Crude oil is valuable for two separate reasons. First, its molecules can be rearranged into engine-ready gasoline, diesel, kerosene, and gas. Second, its smaller fragments are the starting materials of the petrochemical industry, from which plastics, fertilizers, solvents, and drugs descend (Speight, 2014).

The petroleum industry is conventionally divided into three sectors. The upstream sector finds and produces crude oil and natural gas. The midstream sector moves them by pipeline, ship, and rail. The downstream sector converts crude oil, by refining and petrochemical processing, into final products (Gary et al., 2007). Refining is the physical and chemical rearrangement of crude oil into fuels and feedstocks that actually meet market specifications. Without refining capacity, a crude oil producer remains an importer of the fuels its own underground resources could have produced.

### 2.1.2 Petroleum in Nigeria and the refining question

Nigeria is one of the oldest and largest crude oil producers in Africa, with proven reserves of the order of thirty-seven billion barrels and a large suite of light, low-sulphur export grades such as Bonny Light, Escravos, Forcados, Qua Iboe Light, and Brass Blend (Organization of the Petroleum Exporting Countries [OPEC], 2024). In spite of this resource endowment, domestic refining fell far behind consumption for decades. The state-owned Nigeria LNG-era refineries at Port Harcourt, Warri, and Kaduna, with a combined nameplate crude distillation capacity of about 445,000 barrels per day, spent long periods shut down or running at a fraction of design output, while the country imported most of its premium motor spirit (NS Energy, 2021; Punch, 2025). The Petroleum Industry Act of 2021 restructured the sector, converting the Nigerian National Petroleum Corporation into a limited liability company and creating dedicated regulators for upstream and midstream or downstream activity (Petroleum Industry Act, 2021).

The refining map changed fundamentally with the commissioning of the privately owned Dangote refinery in Lagos, a single-train complex with a crude distillation capacity of 650,000 barrels per day, which exceeds the combined nameplate of all four state refineries (Leadership, 2026). Figure 2.1 compares the nameplate capacities documented publicly for the five plants.

**Figure 2.1**

*Crude distillation nameplate capacities of Nigerian refineries*

![](figures/fig2_1_refineries.png)

*Source:* Author, from data reported by the Nigerian Midstream and Downstream Petroleum Regulatory Authority (n.d.), NS Energy (2021), Punch (2025), and Leadership (2026).

Every one of these complexes depends on catalytic conversion units to produce gasoline. The state conversion refineries were each built with a fluid catalytic cracking (FCC) unit, and the Dangote complex is anchored at its gasoline heart by a very large residue fluid catalytic cracking (RFCC) unit, reported at roughly 218,000 barrels per day and among the largest of its kind (Leadership, 2026). The operating health of these cracking units is therefore directly tied to Nigerian gasoline supply, and, as later sections show, both unit types are vulnerable to the vanadium and nickel carried in heavy petroleum feeds.

## 2.2 Petroleum and Its Refining

### 2.2.1 The molecular make-up of crude oil

Crude oil is a mixture of tens of thousands of individual compounds, dominated by hydrocarbons, that is, molecules built only from carbon and hydrogen (Speight, 2014). Refiners classify the hydrocarbons into four families: paraffins (straight or branched chains), naphthenes (saturated rings), aromatics (benzene-type rings), and olefins (chain molecules with double bonds, rare in crude but abundant in cracked products). Interspersed among them are heteroatom compounds containing sulphur, nitrogen, and oxygen, and organometallic compounds containing metals, of which nickel and vanadium are the most abundant (Speight, 2014; Ahmad et al., 2010).

Two facts about the metals matter for this study. First, nickel and vanadium occur in crude largely bound in porphyrin-type structures, flat, ring-shaped organic ligands that cage a metal ion, inherited from chlorophyll-like biological matter, alongside less well-defined non-porphyrin complexes (Speight, 2014). Second, whatever their concentration in the whole crude, the heavy, high-boiling residue fractions concentrate the metals strongly, because the large metalloporphyrin molecules do not distil. Published determinations on Nigerian crude samples and their heavy residual oils report vanadium levels of about 14 to 99 parts per million and nickel around 5 to 11 parts per million in the measured heavy materials (Ahmad et al., 2010). Industry assay data for whole Nigerian crudes, shown in Figure 2.7 in Section 2.14, indicate vanadium contents of the order of fractions of a part per million up to about two parts per million by weight, with nickel several-fold higher. A refinery that feeds residue to its cracking unit is therefore feeding the most metal-rich fraction of the barrel to its most sensitive catalyst.

### 2.2.2 Separation processes: dividing without changing

Refining begins with separation, meaning processes that sort molecules without breaking them. After desalting to remove brine and solids, the crude distillation unit (CDU) separates the crude by boiling range into gases, naphtha, kerosene, diesel, and an atmospheric residue. The vacuum distillation unit (VDU) then separates the atmospheric residue under vacuum into vacuum gas oil (VGO) and vacuum residue (Gary et al., 2007). Hydrotreating processes purify these streams by reacting them with hydrogen over catalyst to strip sulphur and nitrogen, but they do not fundamentally change the size of the molecules.

### 2.2.3 Conversion processes: changing the molecules themselves

Conversion processes change molecular size and shape. Thermal conversion processes, including visbreaking and coking, use heat alone to break heavy residues into lighter products plus a solid carbon residue called coke. Catalytic conversion processes use catalysts to do this work faster, at milder conditions, and with far better control of which products form. The main catalytic conversion families are (Gary et al., 2007):

1. Fluid catalytic cracking (FCC), which converts VGO and residue into gasoline and propylene over an acidic solid catalyst.
2. Hydrocracking, which converts heavy fractions into diesel and jet range products over a dual function catalyst in high pressure hydrogen.
3. Catalytic reforming, which rearranges naphtha into high-octane aromatics and hydrogen.
4. Alkylation and polymerization, which combine small olefins into gasoline-range products, often consuming the olefins made by cracking units.

Of these, FCC is historically and economically dominant in gasoline-oriented refineries, earning it the enduring description of the heart of the refinery (Vogt and Weckhuysen, 2015).

## 2.3 Heterogeneous Catalysis: Concepts Required for This Study

### 2.3.1 Catalyst, activity, selectivity, stability

A catalyst is a substance that increases the rate of a chemical reaction without being consumed in the overall stoichiometry, by providing an alternative reaction path of lower activation energy (Levenspiel, 1999). Three properties define a catalyst's industrial worth:

1. Activity: how fast it converts feed at given conditions.
2. Selectivity: what fraction of reacted feed goes to the desired products rather than unwanted ones such as gas or coke.
3. Stability: how slowly it loses activity and selectivity with time.

In heterogeneous catalysis the catalyst is a solid and the reactants are fluids, so reaction proceeds through a sequence of steps: transport of molecules to the particle, diffusion into its pores, adsorption onto the active site, surface reaction, and desorption and escape of products (Levenspiel, 1999). Two concepts from this list recur throughout this thesis. Adsorption is the binding of a molecule to a surface; its energetic strength governs which species can occupy a site. The active site is the specific atomic arrangement on the solid where chemistry actually happens.

### 2.3.2 Acid catalysis on solids

Cracking catalysts are solid acids. An acid is any chemical species able to donate a proton (the Brønsted definition) or accept an electron pair (the Lewis definition). In zeolite Y the key Brønsted acid sites are bridging hydroxyl groups, written Si-O(H)-Al, in which a proton sits on an oxygen atom shared between a silicon and an aluminium atom of the framework. Lewis acidity in aged catalysts is associated mainly with coordinatively unsaturated aluminium species that have left the framework (Vogt and Weckhuysen, 2015). The distinction matters because Brønsted sites drive the core cracking chemistry, while both site types interact differently with the attacking vanadium species (Trujillo et al., 1997).

### 2.3.3 Catalyst deactivation

Industrial catalysts rarely die in a single event; they age through several parallel and interacting pathways. Following the standard classification applied to FCC by Cerqueira et al. (2008), deactivation falls into four families:

1. Coking: carbon-rich deposits accumulate on active sites and in pores during cracking, temporarily blinding the catalyst. Coke is burned off in the regenerator, so this deactivation is reversible (Guisnet and Magnoux, 2001).
2. Poisoning: impurity species from the feed bind to or react chemically with active components. Metal poisons such as nickel, vanadium, sodium, and iron cause permanent damage that regeneration cannot undo (Bai et al., 2019; Xu et al., 2024).
3. Hydrothermal and thermal degradation: high temperature, especially with steam, destroys the crystal structure and surface of the catalyst itself, by dealumination and sintering (Wallenstein et al., 2000; Silaghi et al., 2016).
4. Attrition and morphology changes: mechanical breakage and surface smoothing reduce fluidizability and access to the interior of the particle (Vogt and Weckhuysen, 2015).

Vanadium belongs simultaneously to the second and third families: it is a feed-borne poison, but its most feared effect is that it accelerates the hydrothermal destruction of the catalyst's own framework (Wormsbecher et al., 1986).

## 2.4 Catalytic Cracking and the Rise of Zeolite Catalysts

### 2.4.1 A short history

Cracking originally meant purely thermal cracking, in which heavy molecules are simply heated until they fragment by free-radical chemistry. Free radicals are neutral fragments carrying an unpaired electron, so thermal cracking is difficult to steer toward particular products. The alternative, catalytic cracking, was industrialized by Eugene Houdry in the 1930s over an acidic clay-derived solid, and it reached decisive efficiency when the Exxon fluid-bed process brought continuous catalyst circulation in 1942 (Venuto and Habib, 1979). The most consequential change came between 1962 and 1964, when Mobil introduced synthetic zeolites, first zeolite X and then the more stable zeolite Y, into cracking catalysts. The zeolite catalysts were so superior in activity and gasoline yield that the world's units were re-catalysted within a few years (Venuto and Habib, 1979; Vogt and Weckhuysen, 2015).

### 2.4.2 Carbenium ion chemistry of catalytic cracking

Acid-catalyzed cracking proceeds through carbenium ions, positively charged hydrocarbon fragments in which the charge sits on a trivalent carbon (Corma and Orchillés, 2000). The mechanism is conventionally described in three stages:

1. Initiation: carbenium ions are created from feed molecules, either by protonation of an olefin on a Brønsted site or by abstraction of a hydride ion (H-) from a paraffin.
2. Propagation: the ion rearranges by skeletal isomerization and, most importantly, breaks at the bond two positions from the charge, a step called beta-scission, producing one smaller olefin and one smaller carbenium ion that continues the chain.
3. Chain transfer and termination: hydrogen transfer reactions saturate olefins and release the site, or, undesirably, build up hydrogen-deficient aromatic species that are the seeds of coke.

Because carbenium chemistry is controlled by the number, strength, and accessibility of Brønsted acid sites, any agent that removes acid sites or destroys the crystal that hosts them, as vanadium does, directly attacks the economics of gasoline production (Corma and Orchillés, 2000; Cerqueira et al., 2008).

## 2.5 The Fluid Catalytic Cracking Process

### 2.5.1 Process description

Figure 2.2 summarizes the working principle of a modern FCC or RFCC unit. Preheated feed is atomized with dispersion steam into the base of a tall vertical pipe called the riser, where it meets hot regenerated catalyst at around 700 °C. The oil evaporates and cracks during a few seconds of upward travel at roughly 500 to 560 °C, depositing coke on the catalyst as it reacts (Sadeghbeigi, 2012; Olugbenga and Oluwaseyi, 2023). At the riser top, cyclones and a disengaging stripper separate product vapours from spent catalyst; the vapours pass to the main fractionator for separation into fuel gas, liquefied petroleum gas (LPG), gasoline, light cycle oil, and a heavy slurry cut. The spent, coked catalyst flows by gravity to the regenerator, a fluidized bed into which air is blown. Burning of the coke at about 690 to 760 °C releases the heat that drives the whole process and reheats the catalyst, which then returns to the riser base (Sadeghbeigi, 2012). The unit is therefore auto-thermal: the coke laid down in the riser is the fuel of the regenerator.

**Figure 2.2**

*Block flow concept of a residue fluid catalytic cracking (RFCC) unit*

![](figures/fig2_2_rfcc_schematic.png)

*Source:* Author's schematic based on Sadeghbeigi (2012), Adanenche et al. (2023), and Vogt and Weckhuysen (2015). Temperature ranges are discussed in Section 2.5.1 and Figure 2.4.

### 2.5.2 Catalyst circulation and equilibrium catalyst

A commercial unit circulates an enormous catalyst inventory continuously between riser and regenerator at a catalyst-to-oil weight ratio typically between about 4 and 10 (Sadeghbeigi, 2012). Because fines are lost through the cyclones and aged catalyst is intentionally withdrawn, operators add fresh catalyst every day. The circulating blend, a statistical mixture of catalyst of all ages, is called equilibrium catalyst, commonly abbreviated Ecat or e-cat. Feed-borne metals that are not removed in any product accumulate on Ecat day after day; vanadium levels of thousands of parts per million on Ecat are routine in residue operations, and modern trapping technology is credited with allowing operation at up to about 7000 ppm vanadium on Ecat while retaining useful activity (Bai et al., 2019; Etim et al., 2018).

### 2.5.3 Kinetic description of cracking

Because the feed is a continuum of thousands of compounds, FCC kinetics is handled by lumped models, in which molecules are grouped into a few fictitious lumps whose interconversion follows simple rate laws. The classical Weekman and Nace (1970) three-lump model treats gas oil converting to gasoline, which itself converts to gas plus coke, with all steps first order and with catalyst activity decaying exponentially with coke content. Jacob, Gross, Voltz, and Weekman (1976) extended the concept to a ten-lump scheme, and many later workers have developed five-lump and kinetic Monte Carlo variants; a recent dedicated review collects the deactivation kinetic equations used across the field (Cordero-Lanzac and Bilbao, 2025). A typical activity decay law is first order in coke, written as phi = exp(-alpha C_c), where phi is the remaining activity fraction, C_c the coke content on catalyst, and alpha an empirical constant (Weekman and Nace, 1970; Olanrewaju et al., 2015). Nigerian researchers have contributed notably to this line of work: Olanrewaju, Okonkwo, and Aderemi (2015), the latter two of Ahmadu Bello University Zaria, built a transient five-lump model of an industrial riser in COMSOL Multiphysics that incorporated intraparticle mass transfer resistance and predicted a residence time of 2 seconds with a gasoline yield of 45 percent, while Olugbenga and Oluwaseyi (2023) simulated the FCC unit of a Nigerian refining and petrochemical company in Aspen HYSYS and recommended a reactor plenum temperature of 560 °C for optimum naphtha production. Together, these studies define the process window within which the deactivation chemistry examined in this thesis occurs.

## 2.6 The FCC Catalyst and Its Zeolite Y Component

### 2.6.1 Anatomy of the catalyst particle

The substance circulated in an FCC unit looks like a free-flowing beige powder of microspheres, each roughly 40 to 150 micrometres in diameter (Sadeghbeigi, 2012). Each microsphere is a composite with four functional ingredients, illustrated conceptually in Plate 2.1:

1. Zeolite Y crystals, typically 10 to 40 percent by weight, providing most of the Brønsted acidity and therefore most of the small-molecule cracking activity (Sadeghbeigi, 2012; Vogt and Weckhuysen, 2015).
2. An active matrix of amorphous silica-alumina, which pre-cracks the largest molecules that cannot enter the zeolite and contributes to bottoms conversion.
3. A filler, typically kaolin clay, providing body and heat capacity at low cost; Nigerian kaolins have been studied extensively for exactly this purpose (Salahudeen et al., 2015a, 2015b, 2017; Aderemi et al., 2001).
4. A binder, usually a silica or alumina sol, which glues the assembly into an attrition-resistant sphere.

Metals arriving with the feed deposit first on the outer surface of the microspheres. Imaging secondary ion mass spectrometry has shown that nickel and vanadium on industrial equilibrium catalyst concentrate toward the particle rim when metals loadings are high (Kugler and Leta, 1988). Vanadium, however, does not stay put; under regenerator conditions it becomes mobile and redistributes within and between particles, reaching zeolite crystallites deep inside the spheres (Wormsbecher et al., 1996; Trujillo et al., 1997), a point illustrated by the inward-migrating red markers in Plate 2.1.

**Plate 2.1**

*Conceptual cross-section of a metal-contaminated FCC catalyst microsphere*

![](figures/plate2_1_particle.png)

*Source:* Author's conceptual schematic (not a micrograph) based on Sadeghbeigi (2012) and Vogt and Weckhuysen (2015); the rim deposition and inward migration pattern follows Kugler and Leta (1988) and Meirer et al. (2015).

### 2.6.2 Zeolite Y structure and acidity

Zeolite Y crystallizes in the faujasite (FAU) framework type. Its framework is built from corner-sharing tetrahedra of SiO4 and AlO4; each tetrahedral site, called a T-site, is occupied by silicon or aluminium, and because AlO4 carries one unit of negative charge relative to SiO4, each framework aluminium must be balanced by a positive charge nearby: a sodium ion in as-synthesized NaY, a proton in the catalytically active HY form, or rare earth cations in the stabilized REY form (Breck, 1974). A chemical rule named after Löwenstein, an empirical statement that Al-O-Al linkages are disfavoured, restricts how aluminium atoms may be distributed among T-sites (Breck, 1974).

The tetrahedra assemble into cage units shown in Figure 2.3. Sodalite cages, also called beta cages, link through double six-membered rings (D6R) to enclose a three-dimensional network of very large cavities called supercages, each about 1.3 nm across and connected to four neighbours through twelve-membered ring windows of about 0.74 nm free diameter (Vogt and Weckhuysen, 2015; Baerlocher and McCusker, n.d.). The faujasite entry of the International Zeolite Association structure database quantifies this geometry: a cubic unit cell of edge 2.4345 nm, a framework density of 13.3 T-sites per 1000 cubic angstroms, a largest sphere of 1.12 nm fitting inside the supercage (11.24 angstroms), a largest diffusible sphere of 0.74 nm passing the windows (7.35 angstroms), and an accessible pore volume of 27.4 percent of the crystal (Baerlocher and McCusker, n.d.). These windows admit the single-ring and branched molecules valuable for cracking while excluding the largest resid molecules, which must first be cracked on the matrix. The catalytically important Brønsted hydroxyl groups sit on oxygen bridges facing into these cages.

**Figure 2.3**

*Building units and framework views of faujasite (FAU), the framework of zeolite Y*

![](figures/fig2_3_iza.png)

*Source:* Database images of the International Zeolite Association Structure Commission (Baerlocher and McCusker, n.d.): (a) framework viewed along [111], the large central opening marking one supercage window; (b) framework viewed along [110]; (c) polyhedral (tiling) view, in which each truncated-octahedron outline is a sodalite cage and the hexagonal prisms linking the cages are double six-rings; (d) the d6r and sod composite building units (not to scale).

### 2.6.3 From NaY to USY and REY: stabilization and unit cell size

As-synthesized NaY is neither acidic nor stable enough for regenerator steam. Two modifications define commercial catalyst zeolites. First, exchange of sodium by ammonium ions followed by calcination and steaming yields ultrastable Y (USY), in which steam has deliberately stripped out part of the framework aluminium, shrinking the unit cell, increasing the silicon-to-aluminium ratio, and leaving behind a minority of strong Brønsted sites plus some extra-framework aluminium (Vogt and Weckhuysen, 2015). Second, ion exchange with rare earth cations such as La3+ and Ce4+ yields rare-earth-exchanged Y (REY), in which bulky polycationic rare earth species anchored in the sodalite cages brace the framework against dealumination and raise activity retention, though with a penalty in gasoline octane and in vanadium tolerance discussed later (Occelli, 1991a, 1996; Akah, 2017; Du et al., 2015).

Because each framework aluminium carries a longer Al-O bond than the Si-O bond, the cubic unit cell edge of faujasite contracts measurably as aluminium is removed; X-ray diffraction therefore offers a unit cell size measurement that tracks framework aluminium density and, by correlation, activity, selectivity, and stability (Vogt and Weckhuysen, 2015; Roncolatto and Lam, 1998). Table 2.1 collects the zeolite characteristics most relevant to this study.

**Table 2.1**

*Key structural and catalytic characteristics of zeolite Y relevant to FCC service*

| Characteristic | Typical value or description | Relevance |
|---|---|---|
| Framework type | FAU (faujasite) | Defines cage and window geometry |
| T-site composition | SiO4 and AlO4 tetrahedra; Si/Al of parent Y roughly 1.5 to 3, higher after dealumination | Sets charge and acid site density |
| Supercage diameter | About 1.3 nm | Admits cracked intermediates |
| Window | Twelve-membered ring, about 0.74 nm | Controls molecular access |
| Unit cell edge | Faujasite-type catalysts near 2.45 to 2.47 nm, contracting on dealumination | Diagnostic of framework Al loss |
| Active site | Bridging Si-O(H)-Al hydroxyl | Brønsted cracking site attacked by V |
| Stabilized forms | USY and REY (La, Ce exchanged) | Different steam and V tolerance |

*Source:* Compiled from Breck (1974), Vogt and Weckhuysen (2015), Baerlocher and McCusker (n.d.), Akah (2017), and Roncolatto and Lam (1998).

## 2.7 From FCC to RFCC: Heavier Feeds, Heavier Problems

Residue fluid catalytic cracking applies the same circulating-solid principle to the bottom of the barrel, that is, to atmospheric or vacuum residues. These feeds differ from VGO in several documented ways (Adanenche et al., 2023; Bai et al., 2019; Sadeghbeigi, 2012):

1. Conradson carbon residue: the empirical measure of a feedstock's tendency to lay down coke, routinely several weight percent in residues versus fractions of a percent in VGO. Higher coke means higher regenerator temperature and more steam exposure for the catalyst.
2. Asphaltenes: the polar, aromatic, high molecular weight fraction that is the least reactive and most coke-forming part of the feed.
3. Metals: nickel and vanadium concentrated in the residue, exactly as described in Section 2.2.1 for Nigerian fractions (Ahmad et al., 2010).
4. Sulphur and nitrogen: higher contents that load the flue gas treatment and the product slate.

Process answers include improved feed atomization and riser termination devices, catalyst coolers for regenerator heat removal, two-stage regeneration, and SOx and NOx control additives (Adanenche et al., 2023). Catalyst answers include more accessible matrix porosity for precracking, lower sodium levels, rare earth stabilization, and the metals traps and passivators examined in Section 2.11 (Bai et al., 2019). Because the RFCC duty intensifies both coke burning and steam exposure, vanadium, whose destructive chemistry requires regenerator temperature and steam, is the defining contamination problem of RFCC operations (Etim et al., 2018; Faghani et al., 2024).

## 2.8 Deactivation of FCC Catalysts in Service

### 2.8.1 Reversible deactivation: coke

During riser cracking, hydrogen-deficient aromatic species accumulate on the catalyst as coke, burying acid sites and blocking pore mouths within seconds of contact (Guisnet and Magnoux, 2001). Every operating unit is designed around this deactivation: the regenerator exists to burn it off. Nitrogen bases in feed act similarly, but reversibly, by neutralizing acidity until the regenerator burns them away (Cerqueira et al., 2008).

### 2.8.2 Irreversible deactivation: hydrothermal dealumination

In the regenerator, steam partial pressures of the order of one fifth to one third of atmosphere at about 700 to 760 °C hydrolyse the framework Al-O bonds of the zeolite, converting framework aluminium into extra-framework species and shrinking the unit cell, an aging mode reproduced in laboratories by steaming protocols such as cyclic propylene steaming (Wallenstein et al., 2000; Sadeghbeigi, 2012). The molecular steps of this hydrolysis have been computed in detail by periodic DFT: the first Al-O(H) bond breaking proceeds through water adsorption on and dissociation over the aluminium site, with activation energies between about 76 and 125 kJ/mol depending on the position of aluminium in the framework (Malola et al., 2012; Silaghi et al., 2015, 2016). This literature is central to the present project, because the baseline question of the thesis is how vanadium changes these very same steps.

### 2.8.3 Poisoning by metals: an overview

The metal poisons of cracking catalysts behave differently, and the differences are essential context for vanadium (Bai et al., 2019; Xu et al., 2024):

- Nickel deposits on the catalyst and acts as an unwanted dehydrogenation catalyst, stripping hydrogen from hydrocarbons to make hydrogen gas and extra coke. Its action is mostly catalytic rather than structural, and it can be passivated by antimony or bismuth compounds blended with the feed or catalyst, though antimony brings its own emissions issues (Adanenche et al., 2023).
- Sodium neutralizes Brønsted acid sites by ion exchange and acts as a flux that dissociates framework bonds, and is a powerful partner of vanadium in accelerating structural collapse (Xu et al., 2002; Hagiwara et al., 2003).
- Iron forms low-melting, glass-like surface nodules especially in tight-oil and resid feeds, physically blocking pore mouths of the particle (Bai et al., 2019; Meirer et al., 2015).
- Vanadium combines the worst of both worlds: it dehydrogenates like nickel, at roughly one quarter of nickel's activity per unit of metal, and simultaneously destroys the zeolite framework itself in an irreversible, steam-accelerated reaction (Bai et al., 2019; Etim et al., 2018).

Figure 2.4 places the regenerator temperature regime against the melting point of vanadium pentoxide, approximately 690 °C (Faghani et al., 2024). Industrial regeneration operates at and above the temperature where V2O5 melts and where its acid derivative becomes mobile, which is consistent with the experimental finding that vanadium damage is effected in the regenerator rather than in the riser (Wormsbecher et al., 1986; Occelli, 1991b).

**Figure 2.4**

*Thermal landscape of FCC operation relative to the melting point of vanadium pentoxide*

![](figures/fig2_4_temperature.png)

*Source:* Author. Riser values from Sadeghbeigi (2012) and Olugbenga and Oluwaseyi (2023); regenerator values from Sadeghbeigi (2012); model regenerator from Wormsbecher et al. (1986); V2O5 melting point from Faghani et al. (2024).

\newpage
