# CHAPTER ONE: INTRODUCTION

## 1.1 Background to the Study

Petroleum refining remains the bedrock of global transportation fuels and petrochemical feedstocks, converting complex, heavy crude oils into high-value light distillates including motor gasoline, aviation kerosene, and diesel (Gary et al., 2007; Speight, 2014). Within modern conversion refineries, the Fluid Catalytic Cracking (FCC) unit and its residue-processing counterpart, the Residue Fluid Catalytic Cracking (RFCC) unit, represent the primary economic workhorses. Globally, over 400 commercial FCC and RFCC units process approximately 14 million barrels per day of heavy vacuum gas oils (VGO) and atmospheric distillation residues (Vogt & Weckhuysen, 2015). In the Federal Republic of Nigeria, the downstream refining sector has entered a transformative era marked by the commissioning and ramp-up of the 650,000 barrels per day Dangote Refinery at Lekki, Lagos. The core conversion engine of this facility is a 218,000 barrels per day RFCC unit - the single largest residual cracking reactor ever constructed globally (Leadership, 2026; Nigerian Eye, 2026). Simultaneously, ongoing revitalization initiatives spearheaded by the Nigerian National Petroleum Company Limited (NNPC Ltd) across the state-owned refineries - Kaduna Refining and Petrochemical Company (KRPC, 110,000 bpd), Port Harcourt Refining Company (PHRC, 210,000 bpd combined), and Warri Refining and Petrochemical Company (WRPC, 125,000 bpd) - depend critically on FCC and RFCC units to convert domestic heavy gas oils and atmospheric residues into premium motor spirit (allAfrica, 2025; Punch, 2025).

The catalytic heart of the FCC process is a multicomponent composite microsphere (50–100 $\mu$m in diameter) consisting of an active, crystalline faujasite zeolite (zeolite Y) embedded within an active alumina matrix, an amorphous silica-alumina binder, and an inert clay filler (Breck, 1974; Sadeghbeigi, 2012). Zeolite Y provides the supreme shape-selective Brønsted acidity required to crack high-molecular-weight hydrocarbons through carbenium ion mechanisms (Corma & Orchillés, 2000). In industrial practice, raw synthetic zeolite Na-Y is converted via ammonium exchange and high-temperature hydrothermal steaming into Ultra-Stable Y (USY), wherein a controlled fraction of framework aluminium is removed, shrinking the unit cell size ($a_0$) to 2.425–2.435 nm to enhance hydrothermal tolerance and gasoline selectivity (Scherzer, 1989; Venuto & Habib, 1979). Rare-earth cations such as lanthanum ($La^{3+}$) and cerium ($Ce^{3+}$) are frequently exchanged into the sodalite cages (forming Rare-Earth Y, REY or RE-USY) to bridge framework oxygen atoms, shield the lattice, and preserve acid site density under operational severity (Du et al., 2015; Occelli, 1996; Salahudeen et al., 2017).

In commercial FCC operations, the catalyst continuously circulates between a short-contact-time riser reactor (770–820 K, 1–3 seconds contact time) and an oxidative regenerator (950–1050 K) where carbonaceous coke deposits (typically 0.8–1.5 wt% of the spent catalyst) are burned off in an air- or oxygen-enriched blast (Sadeghbeigi, 2012; Vogt & Weckhuysen, 2015). Under conventional VGO feeds, hydrothermal deactivation is dominated by steam-induced dealumination: steam generated from hydrocarbon combustion hydrolyzes framework aluminium–oxygen ($Al-O$) bonds, gradually transforming framework aluminium into extra-framework aluminium (EFAL) species (Silaghi et al., 2015, 2016).

However, modern economic and energy security imperatives dictate the co-processing or full processing of heavy residual fractions (atmospheric towers bottoms, vacuum residues). These heavy petroleum cuts are deeply enriched in polyaromatic asphaltenes and oil-soluble organometallic contaminants, primarily nickel and vanadium coordinated within aromatic porphyrin and non-porphyrin macrocycles (Adanenche et al., 2023; Mitchell, 1980). While Nigerian crude oils (such as Bonny Light, Qua Iboe, and Forcados) are globally celebrated for their low sulphur and paraffinic light nature, their atmospheric and vacuum residues concentrate substantial levels of heavy metals. Rigorous geochemical assays of Nigerian crudes demonstrate that nickel and vanadium concentrate up to tens of parts per million in the heavy residual fractions (Ahmad et al., 2010).

When heavy residue feeds are injected into the RFCC riser, metalloporphyrin complexes deposit quantitatively onto the outer surfaces and within the mesopores of circulating catalyst particles. Upon entering the high-temperature (950–1050 K), steam-rich (10–25 vol% $H_2O$) oxidative environment of the regenerator, organic ligands combust, oxidizing nickel to nickel oxide ($NiO$), which acts primarily as an unselective dehydrogenation catalyst accelerating unwanted hydrogen and dry gas production (Kugler & Leta, 1988). Vanadium exhibits an entirely different and far more destructive behavior: it oxidizes to vanadium pentoxide ($V_2O_5$), which has a low melting point (963 K) that falls precisely within the operating temperature window of modern FCC regenerators (Occelli, 1991b; Wormsbecher et al., 1986). In the presence of regenerator steam, $V_2O_5$ reacts reversibly to form volatile, gaseous orthovanadic acid ($H_3VO_4$) according to the thermodynamic equilibrium (Wormsbecher et al., 1986):

$$\text{V}_2\text{O}_5\text{ (l, s)} + 3\text{ H}_2\text{O (g)} \rightleftharpoons 2\text{ H}_3\text{VO}_4\text{ (g)}$$

Volatile vanadic acid migrates rapidly across inter-particle void spaces and penetrates deep into the microporous 12-ring supercages of zeolite Y. Once inside the micropores, $H_3VO_4$ attacks the structural bonds of the zeolite, aggressively extracting framework aluminium, collapsing the crystalline lattice into amorphous silica-alumina, and permanently extinguishing catalytic activity (Pine, 1990; Trujillo et al., 1997; Xu et al., 2002). The consequences for refinery economics are severe: catalyst activity plummets, gasoline yield drops by 5–15%, slurry oil bottoms surge, and catalyst consumption rates triple or quadruple, costing commercial refiners millions of dollars annually in catalyst replenishment and chemical passivators (Adanenche et al., 2023; Cerqueira et al., 2008; Etim et al., 2018).

Despite forty years of empirical research, the fundamental, atomistic mechanism by which mobile vanadic acid attacks the zeolite framework remains an unresolved scientific question in heterogeneous catalysis. Experimental characterization tools (e.g., XRD, $^{27}Al$ and $^{29}Si$ MAS NMR, FTIR, and synchrotron X-ray microscopy) observe catalyst particles only before and after deactivation (Hagiwara et al., 2003; Meirer et al., 2015). Consequently, the literature remains fractured into conflicting mechanistic claims regarding whether vanadium attacks surface silanols first (Pine, 1990), undergoes proton-catalyzed acid hydrolysis of aluminium–oxygen bonds (Trujillo et al., 1997; Wormsbecher et al., 1986), or acts synergistically with sodium to form destructive eutectic melts (Xu et al., 2002). First-principles quantum chemical modeling using Density Functional Theory (DFT) provides the rigorous, non-empirical microscope needed to resolve these elementary reaction steps, quantify competitive adsorption against steam, and map the potential energy landscape of dealumination (Hohenberg & Kohn, 1964; Kohn & Sham, 1965; Sholl & Steckel, 2009). This investigation provides the first rigorous, multi-tier DFT and semi-empirical quantum chemical study elucidating the complete elementary mechanism of vanadic acid-induced dealumination on an active-site faujasite cluster model, benchmarked against steam hydrolysis on an identical energy scale.

---

## 1.2 Statement of the Problem

The transition of the Nigerian refining industry toward heavy residue processing - exemplified by the startup of the 218,000 bpd Dangote RFCC unit and the rehabilitation of the NNPC Ltd refineries at Kaduna, Warri, and Port Harcourt - has elevated catalyst deactivation by heavy metals from an academic concern to a critical operational and economic challenge (Adanenche et al., 2023; Fawehinmi, 2025; Leadership, 2026). While Nigerian crudes are predominantly light, their residues concentrate vanadium to levels (10–100 ppm in atmospheric residue) that rapidly poison circulating equilibrium catalysts (Ecat), exceeding the conservative operational threshold of 1000–1500 ppmw V on catalyst unless compensated by high fresh catalyst addition rates (Ahmad et al., 2010; Etim et al., 2018). Recent operational reports from the Dangote refinery indicate that catalyst management and regenerator stability have required intense operational adjustments during commissioning (Leadership, 2026; Sahara Reporters, 2025).

At the scientific level, the central problem is the **incompleteness and contradictory nature of the elementary mechanistic picture** governing vanadium attack on zeolite Y:

1. **The Site Access Dilemma (Competitive Adsorption):** Both steam ($H_2O$) and vanadic acid ($H_3VO_4$) co-exist in the regenerator gas phase. Under typical conditions, steam is present in vast stoichiometric excess (10–25 vol% vs. ppm levels of volatile $H_3VO_4$). Why and how does trace vanadic acid selectively target the catalytic Brønsted acid sites ($Si-O(H)-Al$) in the presence of overwhelming steam concentrations? The competitive adsorption thermodynamics ($\Delta E_{\text{ads}}$) of $H_3VO_4$ versus $H_2O$ at the faujasite Brønsted site have never been rigorously quantified on an identical quantum chemical cluster model.

2. **The Sequence of Elementary Bond Cleavage:** When vanadic acid binds to the active site, what is the sequence of bond scissions? Does proton transfer occur spontaneously? Which of the four crystallographically distinct $Al-O$ framework bonds ruptures first? Is the first bond cleavage or the subsequent extraction of aluminium the rate-limiting chemical barrier? Experimental NMR and XRD cannot track transition states ($TS$) or short-lived reaction intermediates, leaving the activation barrier ($\Delta E^{\ddagger}$) entirely unknown.

3. **Conflicting Mechanistic Paradigms:** The literature contains competing hypotheses that prescribe conflicting industrial mitigation strategies:
   - *The Acid Hydrolysis Model* (Wormsbecher et al., 1986; Trujillo et al., 1997) asserts that $H_3VO_4$ acts as a strong, mobile Brønsted acid that protonates bridging framework oxygens, lowering the barrier for subsequent hydrolytic bond scission.
   - *The Silanol Condensation Model* (Pine, 1990) argues that $H_3VO_4$ attacks defect silanol groups ($Si-OH$) on the mesoporous matrix, destroying the structural matrix before zeolite collapse occurs.
   - *The Sodium-Vanadate Fluxing Model* (Xu et al., 2002) claims that vanadium is innocuous on pristine protonic USY and causes destruction solely by forming low-melting sodium vanadate ($NaVO_3$) glasses that flux the silica framework.

4. **Absence of a Unified First-Principles Energy Benchmark:** Prior DFT studies in zeolite dealumination have focused almost exclusively on steam hydrolysis (Malola et al., 2012; Silaghi et al., 2015, 2016) or isolated vanadium species in redox zeolites (Tielens & Dzwigaj, 2010a). No published study has placed the elementary reaction coordinates of vanadic acid attack and steam dealumination onto a single, consistent electronic energy scale using identical basis sets, dispersion corrections, and faujasite cluster active-site models. Without this benchmark, the chemical superiority of vanadium passivators and metal traps cannot be rationally designed.

This project addresses these critical gaps by executing a systematic, multi-tiered quantum chemical investigation that determines the adsorption thermodynamics, maps the complete potential energy surface, identifies transition structures, and establishes the thermodynamic driving forces of vanadic acid-induced dealumination in zeolite Y.

---

## 1.3 Aim and Objectives of the Study

### 1.3.1 Aim
The primary aim of this study is to elucidate the elementary reaction mechanism, competitive adsorption thermodynamics, and activation energetics of vanadic acid-induced framework dealumination in zeolite Y under RFCC regenerator conditions using multi-tier quantum chemical simulations.

### 1.3.2 Objectives
To achieve this aim, the specific research objectives are to:

1. Synthesize and systematically evaluate the international and local experimental literature on vanadium poisoning, RFCC catalyst deactivation, and commercial mitigation strategies (chemical passivators and traps), with special emphasis on Nigerian refining contexts.
2. Construct and geometrically validate a representative, quantum-mechanically sound 22-atom cluster model ($AlSi_4O_4H_{13}$) of the faujasite active site featuring a single Brønsted acid hydroxyl group ($Si-O(H)-Al$), along with gas-phase models of the mobile attacking agents ($H_3VO_4$ and $H_2O$).
3. Formulate and map the complete elementary reaction pathway of vanadic acid attack using semi-empirical tight-binding theory (GFN2-xTB), identifying all stationary points (pre-reaction complexes, reaction intermediates, and final dealuminated products).
4. Locate, verify, and characterize the transition states along the reaction coordinates using Climbing Image Nudged Elastic Band (CI-NEB) and Transition State Optimization (OptTS) algorithms, enforcing a rigorous single imaginary frequency validation protocol.
5. Benchmark the steam dealumination pathway on the identical active-site cluster model to quantify the comparative intrinsic barrier of hydrothermal hydrolysis against published periodic DFT standards.
6. Refine the electronic energies and competitive adsorption thermodynamics ($\Delta E_{\text{ads}}$) of key stationary points using hybrid Density Functional Theory with empirical dispersion corrections ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$ and $PBE0\text{-}D3(BJ)/\text{def2-TZVP}$) implemented in ORCA 6.1.1 on high-performance cloud computing infrastructure.
7. Synthesize the computational energetics with industrial catalytic practice to formulate engineering guidelines for vanadium management, regenerator operational parameters, and metal trap design in Nigerian refineries.

---

## 1.4 Research Questions

In direct alignment with the stated objectives, this investigation seeks to answer the following specific scientific and engineering research questions:

1. What are the baseline equilibrium geometric parameters (bond lengths, bond angles, proton positions) of the unperturbed 22-atom faujasite active-site cluster model at the GFN2-xTB and hybrid DFT theoretical levels?
2. How does the adsorption energy ($\Delta E_{\text{ads}}$) of orthovanadic acid ($H_3VO_4$) at the Brønsted acid hydroxyl site compare with that of steam ($H_2O$), and what is the net competitive binding affinity margin that drives selective vanadium poisoning in steam-rich regenerator atmospheres?
3. What is the precise elementary sequence of reaction intermediates during vanadic acid attack, and which of the four framework aluminium–oxygen bonds undergoes initial hydrolytic cleavage?
4. What is the activation barrier ($\Delta E^{\ddagger}$) associated with the initial framework $Al-O$ bond rupture, and does it represent the kinetically rate-limiting step of the dealumination process?
5. How does the intrinsic energy barrier for steam-induced dealumination on the identical cluster model compare with published periodic DFT benchmarks, and what explains the dramatically greater destructiveness of vanadic acid in industrial units?
6. How sensitive are the computed stationary point energies and activation barriers to the choice of hybrid exchange-correlation functional ($B3LYP$ vs. $PBE0$) and geometry relaxation?
7. What are the direct operational implications of these atomistic energetics for commercial RFCC units in Nigeria, particularly concerning regenerator temperature limits, catalyst flushing rates, and the chemical selection of basic metal passivators?

---

## 1.5 Significance and Justification of the Study

This research holds profound academic, technological, and national economic significance for the Federal Republic of Nigeria, particularly within the context of the Petroleum Industry Act (PIA, 2021) and the revitalization of domestic refining capacity:

1. **Strategic National Economic Importance:**
   Nigeria consumes approximately 60–70 million liters of premium motor spirit daily, previously sustained by costly foreign imports and subsidy burdens that strained foreign exchange reserves. The commercial success of the 650,000 bpd Dangote Refinery and the revitalized NNPC Ltd refineries (KRPC, PHRC, WRPC) hinges upon the operational availability and selectivity of their RFCC units. Vanadium poisoning is the principal cause of premature catalyst failure in RFCC operations. Preventing vanadium-induced catalyst collapse directly preserves gasoline yield, minimizes slurry oil discard, and avoids millions of dollars in unexpected catalyst dump-and-fill operations.

2. **Advancing Fundamental Quantum Chemical Knowledge in Zeolite Catalysis:**
   While the experimental deactivation of zeolite Y by vanadium has been documented since 1986, this study provides the first comprehensive first-principles electronic energy profile connecting mobile vanadic acid to framework extraction. By computing the full reaction coordinate on an identical cluster and energy benchmark, this study provides the international catalysis community with an atomistic standard for vanadium attack, resolving long-standing academic debates between the acid-hydrolysis and silanol-attack paradigms.

3. **Rational Engineering Design of Catalyst Additives and Traps:**
   Industrial vanadium passivators (e.g., magnesium, calcium, barium, and lanthanum compounds) are currently deployed largely based on empirical Ecat testing rather than mechanistic design. By demonstrating that vanadic acid binds strongly through bifunctional coordination (Brønsted proton acceptance and dative $Al\cdots O$ interaction) with an adsorption margin of $-14.52\text{ kJ/mol}$ over steam, this study proves that effective metal traps must possess basicity and nucleophilic oxygen donors strong enough to chemically intercept $H_3VO_4$ prior to its chemisorption at the zeolite Brønsted site.

4. **Integration with ABU Zaria Catalysis Research Heritage:**
   The Department of Chemical Engineering at Ahmadu Bello University, Zaria, possesses an established legacy of research in zeolitic materials synthesis, clay mineral activation (Kankara kaolin), and reaction engineering (Aderemi et al., 2001; Bawa et al., 2017; Salahudeen et al., 2015a, 2015b, 2017; Uzochukwu et al., 2023). This study significantly expands this departmental heritage into high-performance computational quantum chemistry and molecular reaction engineering, providing a modern computational framework for designing indigenous catalyst matrices from local Nigerian raw materials.

---

## 1.6 Scope and Delimitations of the Study

To ensure scientific rigor, technical depth, and computational tractability, the scope of this research is defined and delimited as follows:

1. **Model Scope:**
   The active site of zeolite Y is modeled using a hydrogen-saturated 22-atom cluster ($AlSi_4O_4H_{13}$) centered on a single crystallographic aluminium atom (T-site) and its four coordinating bridging oxygen atoms, terminated by terminal silicon atoms carrying hydrogen caps. This model accurately represents the local electronic environment, orbital hybridization, and Brønsted acidity of the $O_1-H$ bridging hydroxyl group in the faujasite supercage without the prohibitive computational cost of fully periodic 576-atom unit cells.

2. **Chemical Scope:**
   The attacking vanadium species is modeled as monomeric gas-phase orthovanadic acid ($H_3VO_4$), which thermodynamic equilibria establish as the primary volatile, mobile species under typical regenerator steam partial pressures. Dimeric species ($H_4V_2O_7$) and solid polymeric $V_2O_5$ melts are outside the scope of this elementary reaction coordinate. The baseline comparative species is a single gas-phase water molecule ($H_2O$). Contaminant sodium ($Na^+$) synergistic fluxing reactions are delimited from the primary cluster, isolating the intrinsic acid-catalytic hydrolysis pathway.

3. **Methodological Scope:**
   Calculations are executed across a multi-tier hierarchy:
   - *Tier 1 (Exploratory PES):* Semi-empirical GFN2-xTB for unconstrained geometry optimizations, relaxed coordinate scans, and nudged elastic band (NEB) saddle searches.
   - *Tier 2 (Density Functional Theory):* Hybrid DFT utilizing Becke's 3-parameter exchange functional with Lee-Yang-Parr correlation ($B3LYP$), augmented with Grimme’s empirical dispersion corrections with Becke-Johnson damping ($D3(BJ)$) and Ahlrichs’ triple-$\zeta$ def2-TZVP basis set, implemented in ORCA 6.1.1 on high-performance cloud infrastructure.
   - *Tier 3 (Functional Benchmarking):* High-level single-point energy evaluations utilizing the parameter-free hybrid Perdew-Burke-Ernzerhof functional ($PBE0\text{-}D3(BJ)/\text{def2-TZVP}$) to evaluate functional sensitivity.
   - Transition states are formally accepted only upon confirming exactly one imaginary vibrational frequency corresponding to the nuclear reaction vector connecting the designated reactant and product minima.

---

## 1.7 Operational Definition of Terms

For the purpose of clarity, precision, and consistency throughout this project report, the following technical terms are operationally defined:

- **Brønsted Acid Site:** A localized proton-donating catalytic center in zeolite Y, formed by the bridging hydroxyl group ($Si-O(H)-Al$) wherein a proton neutralizes the net negative charge induced by the substitution of a tetravalent silicon atom ($Si^{4+}$) with a trivalent aluminium atom ($Al^{3+}$) in the silica framework.
- **Cluster Model:** A finite molecular fragment excised from a periodic crystalline lattice, terminated with capping atoms (typically hydrogen) to satisfy dangling valencies, used in quantum chemistry to compute local electronic structure and reaction pathways with high-level ab initio methods.
- **Counterpoise Correction (CP):** An established mathematical procedure (Boys & Bernardi, 1970) used to eliminate Basis Set Superposition Error (BSSE) in intermolecular interaction energy calculations by calculating fragment energies using the full ghost-orbital basis set of the dimer.
- **Dealumination:** The progressive chemical extraction of framework aluminium atoms from the tetrahedral zeolitic crystalline lattice, resulting in framework vacancy defects, unit cell shrinkage, loss of Brønsted acidity, and eventual structural collapse.
- **Equilibrium Catalyst (Ecat):** The steady-state blend of catalyst particles circulating within an operating FCC/RFCC inventory, representing an age distribution ranging from fresh catalyst to heavily deactivated particles carrying accumulated coke, nickel, vanadium, and iron.
- **Extra-Framework Aluminium (EFAL):** Non-crystalline aluminium species (e.g., $AlOOH$, $Al(OH)_3$, $[Al(OH)_2]^+$, $AlO^+$) that have been dislodged from framework positions by steam or acid attack, residing within the zeolite supercages or on the mesoporous matrix.
- **Faujasite (FAU):** The natural aluminosilicate mineral framework topology exhibiting face-centered cubic symmetry, composed of sodalite cages linked through hexagonal prisms, forming the crystalline structure of commercial synthetic Zeolite X and Zeolite Y.
- **Fluid Catalytic Cracking (FCC):** The catalytic refinery conversion process wherein heavy petroleum fractions are vaporized and contacted with fluidized zeolitic microspheres at elevated temperatures (750–820 K) to crack $C-C$ bonds into lighter, high-octane gasoline and light olefins.
- **GFN2-xTB:** A modern, self-consistent, tight-binding semi-empirical quantum mechanical method developed by Grimme and coworkers, incorporating multipole electrostatics and density-dependent dispersion corrections, calibrated for geometry optimizations and vibrational frequencies.
- **Imaginary Frequency:** A negative eigenvalue obtained from diagonalizing the mass-weighted second-derivative Cartesian Hessian matrix ($\nu < 0\text{ cm}^{-1}$), mathematically defining a first-order saddle point (transition state) on the potential energy surface.
- **Nudged Elastic Band (NEB):** A double-ended transition state search algorithm that optimizes a discrete chain of molecular geometric images connected by virtual spring forces to determine the minimum energy path (MEP) between two known local minima.
- **Orthovanadic Acid ($H_3VO_4$):** A volatile, tetrahedral oxyacid of pentavalent vanadium ($V^{5+}$), formed by the high-temperature reaction of vanadium pentoxide with steam in the FCC regenerator, acting as the primary mobile agent of zeolite dealumination.
- **Pre-Reaction Complex (PRC):** A stable, non-covalently bound adduct formed between an attacking gas-phase reactant and the zeolitic active site prior to the overcoming of any covalent bond-breaking activation barrier.
- **Residue Fluid Catalytic Cracking (RFCC):** An intensified FCC configuration designed to process atmospheric tower bottoms and heavy crude residues exhibiting high Conradson carbon residue (CCR $> 4\text{ wt}\%$) and elevated heavy metal concentrations ($Ni + V > 10\text{ ppm}$).
- **Transition State (TS):** The highest-energy stationary point along a reaction coordinate connecting reactants and products, characterized mathematically as a first-order saddle point possessing exactly one negative Hessian eigenvalue.
- **Ultra-Stable Y (USY):** A hydrothermally modified form of zeolite Y that has undergone controlled steam dealumination, exhibiting an expanded mesopore structure, lower framework aluminium content ($Si/Al > 5$), smaller unit cell size ($a_0 < 2.435\text{ nm}$), and superior thermal stability.

---

**Table 1.1**  
*Summary of specific research objectives, methodological tools, and primary project outputs*

| Objective Number | Focus Area | Primary Methodological Tools | Documented Project Output |
| :---: | :--- | :--- | :--- |
| **1** | Literature Synthesis & Deactivation Evidence | Systematic critical review; industrial assay analysis; archival extraction | Critical evidence matrix and gap synthesis (Chapter Two) |
| **2** | Active Site Model Construction & Validation | Molecular modeling (Avogadro, VESTA); GFN2-xTB & DFT geometry checks | Validated 22-atom cluster and adsorbate models (Chapter Three) |
| **3** | Reaction Coordinate Mapping | GFN2-xTB unconstrained optimizations; relaxed coordinate scans | Potential energy surface stationary-point library (Chapter Four) |
| **4** | Transition State Verification | Climbing Image NEB (CI-NEB); OptTS; Cartesian Hessian diagonalization | Rigorously verified transition states and activation barriers (Chapter Four) |
| **5** | Steam Baseline Benchmark | CI-NEB; OptTS; single-point DFT; periodic DFT literature comparison | Validated hydrothermal dealumination benchmark (Chapter Four) |
| **6** | Hybrid DFT Refinement | $B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$; $PBE0\text{-}D3(BJ)/\text{def2-TZVP}$; ORCA 6.1.1 HPC | Definitive adsorption margins and reaction thermodynamics (Chapter Four) |
| **7** | Industrial Refinery Synthesis | Mechanistic extrapolation; metals passivator evaluation | Engineering guidelines for Nigerian RFCC operation (Chapter Five) |

*Source:* Author (2026). Methods are formulated and detailed comprehensively in Chapter Three.
