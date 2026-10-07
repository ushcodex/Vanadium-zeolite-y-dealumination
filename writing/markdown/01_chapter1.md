# CHAPTER ONE

# INTRODUCTION

## 1.1 Background of the Study

Somewhere inside the regenerator of a residue fluid catalytic cracking unit, at roughly 730 °C, in a gas that is one part in five steam, a few parts per million of an acid decide how much of a refinery's catalyst survives the day. The acid is vanadic acid, H₃VO₄. Its vanadium arrived in the crude oil locked inside porphyrin rings, rode the feed into the riser, was burned off with the coke, and met steam in the regenerator. What it does next has been argued about since 1986, and the argument is not academic. Zeolite Y is the component that does the cracking, it is the most expensive part of the catalyst, and vanadium shortens its life.

Fluid catalytic cracking converts heavy petroleum fractions into gasoline, diesel and light olefins, and it is regarded as the cash cow of the refinery because the fuel it produces alone accounts for 35 to 50 per cent of the total gasoline produced globally (Adanenche et al., 2023). Residue fluid catalytic cracking, usually shortened to RFCC, is the variant that accepts atmospheric residue and other heavy, metal bearing feedstocks. Refiners accept those feedstocks because they are cheaper and because they widen refining margin, and they pay for that choice in catalyst. Residue carries vanadium, nickel, sodium and iron. Nickel and vanadium both promote dehydrogenation, which raises coke and hydrogen yields and overloads the wet gas compressor and the air blower. Vanadium does something worse than that: it destroys the zeolite (Wormsbecher, Peters, & Maselli, 1986).

The active zeolite is Y, a crystalline aluminosilicate with the faujasite structure. Its cracking power comes from Brønsted acid sites, which are hydroxyl bridges formed where a silicon atom in the framework has been replaced by an aluminium atom plus a compensating proton. Removing aluminium from the framework removes those sites. The removal is called dealumination, and steam alone can do it, slowly, whenever the catalyst is regenerated (Malola, Svelle, Lønstad Bleken, & Swang, 2012).

The open question is what vanadium adds to a process that already happens without it. Wormsbecher et al. (1986) proposed that vanadium pentoxide and steam form volatile vanadic acid, that vanadic acid is a strong acid analogous to phosphoric acid, and that it hydrolyses the framework. Trujillo et al. (1997) accepted the chemistry but pointed out a difficulty: a regenerator contains about 60 ppm of sulfur oxides, which form a stronger acid at a higher concentration, so why would the weaker and rarer vanadic acid be the destructive agent? Their answer was that vanadic acid concentrates locally inside the zeolite. Pine (1990) and later Xu, Liu, and Madon (2002) went further and argued the opposite case. Pine showed that vanadium attacks silicalite, a zeolite with almost no aluminium, which means the attack need not be on aluminium at all, and that the activation energy of destruction is the same whether vanadium is present or not. Xu et al. (2002) concluded that vanadium does not open a new destructive pathway at all: it releases sodium from exchange sites as sodium metavanadate, the metavanadate hydrolyses to sodium hydroxide, and the hydroxide attacks the framework exactly as it would without vanadium. On that reading, steam and sodium do the damage and vanadium is a facilitator.

Forty years of experiments have not settled this, largely because the decisive quantity is hard to measure. What matters is not whether vanadic acid can attack a framework in principle, but how strongly it holds the acid site compared with water, because water is present at a partial pressure several orders of magnitude higher. That comparison is a binding energy, and a binding energy is precisely what quantum chemistry can compute. This project computes it.

## 1.2 Statement of the Problem

Refineries processing residue lose zeolite Y activity faster than steam alone would explain, and they spend money on vanadium traps and passivators to limit the loss. Those additives are chosen largely by trial, because the molecular step that vanadium is supposed to perform has never been quantified. Specifically, no published value exists for the difference in binding strength between vanadic acid and water at a faujasite Brønsted acid site under one consistent model and level of theory. Without that number the two rival explanations cannot be separated, because the vanadic acid hypothesis requires vanadic acid to win the site against an overwhelming excess of steam, while the sodium route does not. The problem this project addresses is therefore narrow and testable: at the level of adsorption thermodynamics, does vanadic acid bind a faujasite Brønsted acid site strongly enough to justify treating it as the destructive agent rather than as a spectator?

## 1.3 Aim of the Study

The aim of this study is to evaluate the first step of the vanadic acid hypothesis for zeolite Y dealumination by computing the adsorption thermodynamics of vanadic acid and water at a faujasite Brønsted acid site, and to compare the two within a single consistent computational model.

## 1.4 Objectives of the Study

The objectives are to:

1. construct a four tetrahedral site cluster model of the faujasite Brønsted acid site and optimise it together with the vanadic acid and water adsorbates;
2. screen candidate geometries and reaction pathways with the semi empirical GFN2 xTB method;
3. refine the accepted geometries with dispersion corrected hybrid density functional theory at B3LYP D3(BJ)/def2 TZVP;
4. verify the refined energetic conclusions with PBE0 D3(BJ)/def2 TZVP single point calculations;
5. compute harmonic vibrational frequencies to test whether each reported structure is a true minimum;
6. evaluate Gibbs free energies at 298.15 K and at 1003.15 K, the latter representing regenerator temperature;
7. compare the binding of vanadic acid with that of water, and estimate what the computed difference implies for site occupancy under regenerator conditions;
8. report, without exaggeration, which parts of the vanadic acid pathway this model could and could not establish.

## 1.5 Scope of the Study

The study is entirely computational. No laboratory work was carried out. The zeolite is represented by a gas phase cluster of formula AlSi₄O₄H₁₃ cut from the faujasite framework, carrying one Brønsted acid site and terminated with hydrogen atoms at the cut edges. Only one crystallographic site and one acid site are modelled. The comparison is between two adsorbates, vanadic acid and water. Sodium, nickel, rare earth cations, extra framework aluminium and the surrounding matrix or binder are outside the scope, as are periodic boundary conditions, solvent or confinement effects, and explicit treatment of the liquid like vanadium pentoxide phase. Thermochemistry uses the ideal gas, rigid rotor, harmonic oscillator approximation. Reported wall clock work was split between a Dell Latitude E6430 laptop and a cloud virtual machine.

## 1.6 Justification of the Study

Three reasons justify the work. First, it addresses a specific gap that experiment has left open: the relative binding strength of vanadic acid and steam at the site where the damage is supposed to start. Second, it tests the vanadic acid hypothesis quantitatively rather than restating it, and it reports a result that does not support the hypothesis in its simple form. A negative or qualified result is still useful, because it redirects effort toward the sodium route that Pine (1990) and Xu et al. (2002) advocated. Third, the project is relevant to Nigerian refining. Adanenche et al. (2023) list the Dangote refinery at Lagos among the largest upcoming refineries with FCC units worldwide over the 2021 to 2025 outlook period, so vanadium tolerance in residue cracking is a local operating question and not only a foreign one. The computational approach itself also has local precedent in this department, where density functional theory has been applied to solvent design on ordinary workstations (Uzochukwu et al., 2023).

## 1.7 Limitations of the Study

The limitations are stated here rather than buried, because several of them determine how far the results can be pushed.

1. A cluster of four tetrahedral sites captures the local chemistry of one acid site but carries no long range electrostatic field and no pore confinement. Both are known to matter in zeolites.
2. The cut edges are capped with hydrogen atoms whose positions were frozen during optimisation. This keeps the cluster from collapsing, but it adds artificial stiffness and leaves out the way a real framework would relax.
3. The cluster reference optimisation retained one spurious imaginary mode of 4.64 cm⁻¹. This is below the level at which any chemical motion can be assigned, but it means the reference is a very flat minimum rather than a perfectly clean one.
4. No counterpoise correction for basis set superposition error was obtained. All four counterpoise jobs failed at the input stage, so the reported binding energies are uncorrected and are therefore upper bounds on the magnitude of binding.
5. No activation barrier is reported. The candidate saddle for framework bond cleavage carried fourteen imaginary modes and so is not a first order saddle point. One intermediate reached its cycle limit without converging, and the product calculation did not terminate.
6. The model contains no sodium. Because the main rival explanation requires sodium, this study can only test the vanadic acid pathway, not directly compare the two.
7. Gibbs free energies come from a gas phase harmonic treatment. At 1003 K the harmonic approximation is strained and the entropy of a gas phase adsorption event is not what a molecule adsorbed in a pore experiences.

## 1.8 Definition of Terms

Because this project sits between chemical engineering and quantum chemistry, the terms used repeatedly are defined here.

**Zeolite Y:** a crystalline aluminosilicate with the faujasite structure, made of silica and alumina tetrahedra linked through oxygen atoms, used as the active component of cracking catalysts.

**Brønsted acid site:** a hydroxyl group bridging a framework aluminium and a neighbouring silicon, written Al(OH)Si. It is the site that protonates a hydrocarbon and starts cracking.

**Dealumination:** removal of aluminium from the framework by hydrolysis. Each aluminium removed destroys one Brønsted acid site and leaves a cluster of four hydroxyls called a silanol nest.

**Extra framework aluminium:** aluminium that has been removed from the framework but remains inside the pores as a mobile hydrated species.

**Fluid catalytic cracking (FCC):** the refinery process that cracks heavy oil fractions over a circulating solid catalyst. **Residue fluid catalytic cracking (RFCC):** the version that feeds atmospheric residue.

**Regenerator:** the vessel in which coke is burned off the circulating catalyst with air. It is hot, oxidising and full of steam, and it is where most vanadium damage occurs.

**Unit cell size:** the edge length of the zeolite cubic unit cell, measured by X ray diffraction. It rises with framework aluminium content, so it is used as a proxy for how much aluminium remains.

**Density functional theory (DFT):** a family of quantum mechanical methods that obtain the energy and electron distribution of a molecule from its electron density rather than from a many electron wavefunction.

**Functional:** the part of a DFT calculation that approximates how exchange and correlation energies depend on the density. B3LYP and PBE0 are two widely used functionals.

**Basis set:** the set of mathematical functions used to build the electron density. def2 TZVP is a triple zeta valence basis with polarisation functions.

**Dispersion correction:** an added term, here Grimme's D3 with Becke Johnson damping, that accounts for weak long range attraction that plain functionals miss.

**Semi empirical method:** a method that replaces parts of the quantum mechanical calculation with parameters fitted to data. GFN2 xTB is a modern tight binding example, roughly a thousand times cheaper than DFT.

**Stationary point:** a geometry at which the energy has zero gradient. A **minimum** has no imaginary vibrational frequencies; a **first order saddle point**, the transition state of a reaction step, has exactly one.

**Imaginary frequency:** a negative computed vibrational frequency. It signals that the structure is not a minimum in that direction of motion. One imaginary frequency is the signature of a transition state; several mean the structure is not the saddle point being sought.

**Hartree (Eh):** the atomic unit of energy used by quantum chemistry programs. One Hartree is 2625.50 kJ mol⁻¹.
