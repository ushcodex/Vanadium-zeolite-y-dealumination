# CHAPTER THREE

# METHODOLOGY

## 3.1 Research Design

The study is entirely computational. It uses a two tier design, in which a cheap method explores the potential energy surface and an expensive method refines whatever the cheap method finds. The arrangement is shown in Figure 3.1. Tier 1 used the semi empirical GFN2 xTB method to optimise reactants and complexes, to scan for candidate saddle points, and to screen out structures that were not worth the cost of a density functional calculation. Tier 2 took the accepted Tier 1 geometries and refined them with dispersion corrected hybrid density functional theory, evaluated them again with a second functional, and computed harmonic frequencies for the thermochemistry. Nothing was carried into the second tier that had not passed a written acceptance test in the first.

[FIG: fig3_1_workflow.png | Figure 3.1: The two tier computational workflow used in this study | Source: author]

The reason for two tiers is arithmetic. A single density functional optimisation of the vanadic acid complex took about five and a half hours on the machine used, and a saddle point search took more than a day. GFN2 xTB completes the same size of job in minutes, so the search space can be explored broadly before anything expensive is attempted.

## 3.2 Hardware and Software

Tier 1 was run on the author's own Dell Latitude E6430 laptop with an Intel Core i5 processor, 16 GB of RAM and a solid state drive, using a single core. Tier 2 was run on a cloud virtual machine with four MPI ranks, because the density functional jobs did not fit the time available on the laptop.

All quantum chemical calculations were performed with ORCA 6.1 (Neese, 2025). Structures were built and edited in Spartan and Avogadro and exported as Cartesian coordinates. Energy differences, frequency counts and thermochemical corrections were extracted from the ORCA outputs with purpose written Python scripts that are included in the repository, so that every number in Chapter Four can be recomputed from the raw output files. All graphs and molecular pictures were drawn with the matplotlib library from the same scripts.

The file types used, and where each one is opened, are listed in Table 3.1.

[TBL: Table 3.1: File types used in this project and the software used to open them | Extension;What it holds;Open with | .mol;Structures with an explicit bond table, used for hand editing and visual checking;Spartan, Avogadro | .xyz;Cartesian coordinates only, used as ORCA and xTB input;ORCA, Avogadro, VMD | .inp;The ORCA input deck: method, basis set, job type, geometry;any text editor | .out;The ORCA log: energies, gradients, frequencies, thermochemistry;any text editor, or the audit scripts | _trj.xyz;Every geometry visited during an optimisation;VMD, Avogadro | .hess;The Hessian matrix and normal modes;ORCA, or read by the audit scripts | .gbw;The converged wavefunction, used to restart a job;ORCA only | .csv;The calculation register, manifests and the parsed results table;Excel, LibreOffice Calc, pandas]

One practical warning is worth recording, because it cost time. XYZ files carry no bond information, so a viewer guesses bonds from interatomic distances and will sometimes draw bonds that the calculation does not contain. The energies returned by ORCA and xTB depend only on the atomic positions, the charge and the spin multiplicity, so a wrongly drawn bond is a display artefact and not an error in the calculation. The bond tables in the .mol files are the authoritative statement of intended connectivity.

## 3.3 The Zeolite Model

### 3.3.1 Cluster selection

Zeolite Y was represented by a cluster of four tetrahedral sites cut from the faujasite framework, of formula AlSi₄O₄H₁₃. The cluster contains the aluminium atom, its four framework oxygens, the four silicon atoms bonded to those oxygens, and thirteen hydrogen atoms: twelve capping hydrogens, three on each silicon, plus the single Brønsted proton. Twenty two atoms in total. This size was chosen because it is the smallest fragment that contains a complete Al(OH)Si bridge with its full first coordination sphere, while remaining cheap enough for frequency calculations and for the more than one hundred geometry steps that a saddle point search requires.

The alternative would have been a periodic calculation on the full unit cell. That would have removed the boundary problem and included the long range electrostatic field and the pore confinement, both of which are real effects in a zeolite. It was not affordable within the resources available, and it would have made the saddle point searches, which needed many restarts, impractical. The cost of the choice is discussed in section 3.10.

### 3.3.2 Validation of the cluster

A cluster model is only worth using if it reproduces the feature that makes the material a catalyst, so the optimised cluster was checked against that requirement. The aluminium sits in a tetrahedral environment with aluminium oxygen distances of 1.9192, 1.7161, 1.6947 and 1.6953 Å. The three shorter distances are ordinary aluminium oxygen single bonds in a zeolite framework, and the long one, 1.9192 Å, is the bond to the oxygen that carries the proton. The same asymmetry appears on the silicon side: the three unprotonated bridging oxygens sit between 1.6159 and 1.6234 Å from their silicon, while the protonated one sits 1.7179 Å away. Both elongations are the structural signature of Brønsted acidity described in the literature, and finding them in the model is the evidence that the cluster reproduces the essential electronic feature of the real acid site.

### 3.3.3 Boundary treatment

Cutting a cluster out of an infinite framework leaves bonds dangling. Each dangling bond was capped with a hydrogen atom placed along the direction of the bond that was cut, at a silicon hydrogen distance of 0.148 nm, which is the standard silicon hydrogen bond length. During every optimisation the positions of those twelve capping hydrogens were frozen at their crystallographic coordinates, while the aluminium, its four oxygens, the four silicons and the Brønsted proton were allowed to relax. Freezing the caps mimics the rigidity that the surrounding framework imposes and stops the small cluster from folding in on itself in ways the real solid cannot. A frozen boundary is a blunt instrument, and it is one of the reasons the saddle point search in this work behaved badly, as Chapter Four records.

The three reference species optimised at the density functional level are shown in Figure 3.2.

[FIG: fig3_2_cluster.png | Figure 3.2: The four tetrahedral site faujasite cluster AlSi₄O₄H₁₃, vanadic acid and water, optimised at B3LYP D3(BJ)/def2 TZVP | Source: author, rendered from the optimised Cartesian coordinates]

## 3.4 The Adsorbates

Vanadic acid, H₃VO₄, was built with vanadium in tetrahedral coordination, with one vanadyl V=O bond and three V–OH bonds, consistent with vanadium in the +5 oxidation state with a d⁰ configuration. Water was built at its experimental geometry. Both were optimised in isolation, without constraints, before being placed near the acid site. Charge was zero and multiplicity was one throughout, since every species in this study is a closed shell singlet.

## 3.5 The Reaction Sequence

The pathway was defined before any calculation was run, and it is stated here as chemical equations rather than as a diagram, because the equations say exactly what bonds are supposed to change. The intact acid site is written Z–OH, where Z stands for the rest of the cluster.

The vanadic acid route is:

V₂O₅ + 3 H₂O ⇌ 2 H₃VO₄
(3.1)

Z–OH + H₃VO₄ → Z–OH···H₃VO₄
(3.2)

Z–OH···H₃VO₄ → V-I1
(3.3)

V-I1 → V-TS2‡ → V-I2
(3.4)

V-I2 → V-TS3‡ → V-P
(3.5)

Equation 3.1 is the regenerator reaction that makes the poison, taken from Wormsbecher et al. (1986), and is not calculated here. Equation 3.2 is the adsorption step that produces the pre reaction complex, V-PRC. Equation 3.3 is a rearrangement into a more strongly bound chemisorbed intermediate, V-I1. Equations 3.4 and 3.5 are the successive hydrolyses of framework aluminium oxygen bonds, each through a saddle point, ending at V-P, the state in which aluminium has been extracted from the framework. A dagger marks a saddle point.

The steam control route is the same sequence with water in place of vanadic acid:

Z–OH + H₂O → Z–OH···OH₂
(3.6)

Z–OH···OH₂ → W-TS‡ → W-P
(3.7)

W-P → Al(OH)₃ + 4 ≡Si–OH
(3.8)

Equation 3.6 gives the water pre reaction complex, W-PRC. Equation 3.7 is the first hydrolysis of a framework aluminium oxygen bond, and W-P is the hydrolysed product. Equation 3.8 is the continuation to full dealumination established by Malola et al. (2012) and is quoted for context rather than calculated here.

This study therefore models the vanadium route through to the extracted aluminium state and the steam route through its first hydrolysis. The comparison that matters most, and the one the design protects, is between equation 3.2 and equation 3.6: the same site, the same level of theory, two competing adsorbates.

## 3.6 Tier 1: Semi Empirical Screening

All Tier 1 calculations used GFN2 xTB (Bannwarth et al., 2019) as implemented in ORCA, run on the laptop. The method was chosen because it carries multipole electrostatics and a density dependent dispersion term, so it treats hydrogen bonding and weak adsorption far better than earlier semi empirical methods, and because it is fast enough that many starting geometries can be tried.

The Tier 1 procedure was:

1. Optimise the isolated cluster, vanadic acid and water to minima.
2. Build pre reaction complexes by placing the adsorbate near the Brønsted proton in several orientations and relaxing each one, keeping the lowest.
3. Locate approximate saddle points for each intended bond change with the nudged elastic band method, which connects two known minima by a chain of images and relaxes the chain until it lies along the lowest path.
4. Refine each band estimate with an eigenvector following saddle point optimisation, restarting from the improved geometry as often as needed.
5. Test every candidate against the acceptance rules in section 3.8 and record the outcome, including the failures.

Steps 3 to 5 were repeated over nine audit rounds. The register of every job run, including the ones that were superseded or excluded, is kept in the repository and is the source of the Tier 1 numbers quoted in Chapter Four.

## 3.7 Tier 2: Density Functional Refinement

### 3.7.1 Level of theory

Geometries carried forward from Tier 1 were re optimised with the B3LYP hybrid functional (Becke, 1993; Lee et al., 1988), the def2 TZVP basis set (Weigend & Ahlrichs, 2005) and Grimme's D3 dispersion correction with Becke Johnson damping (Grimme et al., 2011). This level is written B3LYP D3(BJ)/def2 TZVP throughout. For vanadium, def2 TZVP uses an effective core potential for the inner electrons, which lowers the cost without materially changing the valence chemistry.

B3LYP was chosen because it is the functional most often used for zeolite cluster work, so the numbers can be compared with the literature, and because it is well behaved for main group thermochemistry. The D3 term was not optional: adsorption is held together largely by hydrogen bonds and dispersion, and a functional without a dispersion term would have returned binding energies that were too small by tens of kilojoules per mole.

### 3.7.2 Frequencies and thermochemistry

Harmonic vibrational frequencies were computed at the optimised geometries. They serve two purposes. They decide whether a structure is a genuine minimum, which requires no imaginary frequencies, or a first order saddle point, which requires exactly one. And they supply the zero point energy and the thermal corrections that turn an electronic energy into an enthalpy and a Gibbs free energy.

### 3.7.3 Second functional check

Every optimised geometry was re evaluated with a single point calculation using the PBE0 hybrid functional (Adamo & Barone, 1999), the same def2 TZVP basis set and the same D3(BJ) correction. PBE0 mixes in 25 per cent exact exchange against B3LYP's 20 per cent and is built on a non empirical functional, so agreement between the two is meaningful evidence that a result belongs to the chemistry rather than to the functional. If the two functionals disagree by more than a few kilojoules per mole for a quantity, that quantity is not reported as established.

### 3.7.4 Attempted counterpoise correction

When two fragments are brought together and each is described with a finite basis set, each fragment can borrow basis functions from the other and appear to bind more strongly than it really does. This is basis set superposition error. The standard remedy is the Boys Bernardi counterpoise correction, in which each fragment is recomputed in the presence of the other fragment's basis functions but not its nuclei or electrons, giving

ΔE_int = E(complex) − [E(cluster with ghost adsorbate) + E(adsorbate with ghost cluster)]
(3.9)

Four counterpoise jobs were constructed and submitted, two for each complex. All four failed at the input stage with an ORCA parsing error, because the fragment definition block was placed after the geometry block. The failure was recorded rather than patched over, and the consequence is stated plainly: the binding energies reported in Chapter Four are not counterpoise corrected and are therefore upper bounds on the strength of binding. Since both complexes were treated the same way, the difference between them is affected much less than either absolute value.

## 3.8 Acceptance Rules for a Stationary Point

A number is only as good as the test the structure passed. Five rules were fixed in advance and applied without exception.

**A1.** The optimisation must terminate normally and report convergence.

**A2.** A minimum must have zero imaginary frequencies. A saddle point must have exactly one, and that mode must animate the bond change it is supposed to. Modes below 20 cm⁻¹ are treated as numerical noise; modes between 20 and 50 cm⁻¹ are accepted only if the recorded displacement vector animates the intended reaction.

**A3.** A saddle point must lie higher in energy than both of the states it connects, by more than 1.0 kJ mol⁻¹.

**A4.** Displacing the structure a small distance along its imaginary mode in each direction, and re optimising, must land on two different minima. This is the two sided interval test, and it is what proves a saddle point connects the states claimed for it.

**A5.** Every reported energy, log file and test result must map to one and only one structure.

## 3.9 Thermochemistry

The electronic energy of a state, ΔE, is reported relative to the isolated, infinitely separated reactants:

ΔE = E(state) − [E(cluster) + E(adsorbate)]
(3.10)

The enthalpy and Gibbs free energy add the zero point energy and the thermal corrections from the frequency calculation, evaluated in the ideal gas, rigid rotor, harmonic oscillator approximation:

ΔG(T) = ΔH(T) − TΔS(T)
(3.11)

Two temperatures were used. The first is 298.15 K, the standard state, which is the only temperature at which computed adsorption free energies can be compared with anything else. The second is 1003.15 K, which is 730 °C, the temperature used by Wormsbecher et al. (1986) for the regenerator and the temperature at which the steam concentration quoted in the literature applies.

One quantity deserves special mention because it is the most reliable number in this thesis. The difference between the two adsorption energies can be written so that the cluster energy cancels:

ΔE(V-PRC) − ΔE(W-PRC) = E(V-PRC) − E(W-PRC) − E(H₃VO₄) + E(H₂O)
(3.12)

Equation 3.12 does not contain the cluster energy at all. Since the cluster is the species whose optimisation was least clean, any error in the cluster reference moves both absolute binding energies but leaves their difference untouched. The comparison this study is built on is therefore more robust than either number taken alone.

## 3.10 Quality Assurance and Audit Trail

Every job, including the ones that failed, was logged in a register with its input file, output file, level of theory, termination status, imaginary mode count and final energy. Nothing was deleted. Scripts in the repository re read the raw output files and regenerate every table in Chapter Four, so a marker who wants to check a number can run one command and see it recomputed.

Two known weaknesses were carried into the results and are flagged wherever they matter. The frozen capping hydrogens make the cluster artificially stiff, and they also give it low frequency modes that are artefacts of the boundary rather than of the chemistry; this is the most likely reason the saddle point search returned a structure with fourteen imaginary modes. And the counterpoise correction was never obtained, so absolute binding energies carry an unquantified basis set superposition error, probably in the range of 5 to 20 kJ mol⁻¹ for a system of this size.
