# CHAPTER ONE

# INTRODUCTION

## 1.1 Background of the Study

Nearly all of the transport fuel used in the world passes at least once through a fluid catalytic cracking (FCC) unit. The process converts heavy petroleum fractions, which have little commercial value as fuels, into gasoline, diesel and light olefins, and it does so at a scale that no other refinery process approaches. Where the feedstock is an atmospheric residue rather than a vacuum gas oil, the unit is described as a residue fluid catalytic cracking (RFCC) unit, and it is this variant that has grown fastest in refining capacity because residues are the cheapest barrel a refinery can buy (Adanenche et al., 2023).

The catalyst that does the work is a fine powder of about 60 micrometres in diameter, and the part of that powder that cracks molecules is a zeolite, almost always zeolite Y. Zeolite Y is a crystalline aluminosilicate with pores of about 0.74 nanometres across, and its activity comes from Brønsted acid sites formed wherever an aluminium atom replaces a silicon atom in the framework. Each such substitution leaves one negative charge that a proton must balance, and it is that proton which donates to a hydrocarbon and starts the cracking chain.

Residue feedstocks carry more than hydrocarbons. They carry nickel, vanadium, iron and sodium, bound inside large porphyrin and asphaltene molecules, and these metals deposit on the catalyst surface as the hydrocarbons crack. Vanadium is the most damaging of them to the zeolite itself. It is deposited on the catalyst particle during cracking, oxidised to vanadium pentoxide in the regenerator, and then, in the steam-rich atmosphere of the regenerator at temperatures near 1000 K, converted into a volatile acidic species that migrates through the catalyst particle and attacks the aluminosilicate framework (Wormsbecher et al., 1986; Trujillo et al., 1997).

The accepted picture of that attack is summarised in the following two reactions. The first is the oxidation and hydration step that generates the volatile acid:

V₂O₅(s) + 3H₂O(g) → 2H₃VO₄(g)                    (1.1)

The second is the hydrolysis of a framework aluminium oxygen bond by the vanadic acid that has formed:

≡Si–O–Al≡ + H₃VO₄ → ≡Si–OH + Al(OH)₃(VO(OH)₃)      (1.2)

Reaction (1.1) says that vanadium is only carried into the zeolite pore system in the presence of steam, and reaction (1.2) says that the entity that removes aluminium from the framework is an acid derived from vanadium and not steam alone. Both statements have been contested, and the contest is the reason this work was undertaken. Some careful experimental studies report that vanadium on its own has little effect on zeolite Y stability and that the true attacking agent is sodium hydroxide generated in the presence of sodium and steam (Xu et al., 2002). Others conclude that the destruction proceeds to the same extent in the presence of sodium whether or not vanadium is present at all. Others again, most recently, report severe framework collapse at vanadium loadings above about 1 wt% in steam, in sodium-containing samples (Liu et al., 2019). The disagreement is about which species actually breaks the aluminium oxygen bond, and it cannot be settled by further bulk characterisation alone, because the species involved exist for fractions of a second at concentrations far below what diffraction or spectroscopy can see.

Computational chemistry can see them. A quantum chemical calculation does not observe the system, it solves for the energy of a proposed arrangement of atoms, and it can therefore follow a reaction step by step, including the arrangements that are too short lived to isolate. Density functional theory (DFT) has been applied to zeolite dealumination for well over a decade and has produced a now standard description of how steam alone removes aluminium from a framework (Malola et al., 2012; Silaghi et al., 2016; Nielsen et al., 2019). What has not been produced is the equivalent description for the vanadium-catalysed route. The published DFT work on vanadium in zeolites concerns framework vanadium in the lattice itself (Tielens & Dzwigaj, 2010) rather than the incoming vanadic acid molecule that experimentalists implicate in deactivation.

This study addresses that gap. It builds a small but chemically faithful model of a zeolite Y Brønsted acid site, brings vanadic acid to it and separately brings water to it, and computes the energy of every arrangement along both routes using semi-empirical and density functional methods. The comparison between the two routes is the substance of the work, because the argument in the literature is precisely a comparison between them.

## 1.2 Statement of the Problem

Vanadium contamination destroys the zeolite Y component of RFCC catalysts and shortens catalyst life, but the literature does not agree on how it does so. Three positions can be distinguished. In the first, vanadic acid formed in the regenerator hydrolyses framework aluminium oxygen bonds directly, so vanadium is itself the attacking agent (Wormsbecher et al., 1986; Trujillo et al., 1997; Liu et al., 2019). In the second, vanadium does not open a new reaction route at all; its role is to release sodium from exchange sites and thereby to supply sodium hydroxide, which is the species that attacks the framework, so that in the absence of sodium vanadium is nearly harmless (Xu et al., 2002). In the third, the destruction in sodium-containing samples occurs to the same extent whether vanadium is present or not, which reduces vanadium to an spectator in the process.

These positions differ in what they predict about the first bond breaking step. If vanadic acid is the attacking agent, then the adsorption of vanadic acid on the acid site and the subsequent cleavage of an aluminium oxygen bond must be energetically more favourable than the corresponding steps for water. If vanadium acts only through sodium, then the vanadic acid molecule must be a comparatively poor attacker of the framework once sodium has been removed from consideration. This is a quantitative question with a computable answer, and no published study has computed it. The experimental techniques that have been applied to the problem, including X-ray diffraction, nitrogen physisorption, nuclear magnetic resonance and electron microscopy, describe the consequences of vanadium attack after the framework has already collapsed. They cannot resolve the energy of a single aluminium oxygen bond breaking in the presence of an adsorbate.

The problem this study addresses is therefore the absence of a molecular level energy profile for the reaction between vanadic acid and the Brønsted acid site of zeolite Y, and the absence of a like for like comparison between that profile and the corresponding one for steam.

## 1.3 Aim of the Study

The aim of this study is to determine, by quantum chemical calculation, whether vanadic acid attacks the Brønsted acid site of zeolite Y more strongly than steam does, and to establish what the computed energetics imply for the disputed mechanism of vanadium-assisted dealumination.

## 1.4 Objectives of the Study

The specific objectives are to:

1. construct a cluster model of a zeolite Y Brønsted acid site that is small enough for hybrid density functional calculation and large enough to preserve the essential coordination of aluminium and silicon;

2. map the stationary points on the reaction coordinate for the approach of vanadic acid (H₃VO₄) to that cluster, using the semi-empirical GFN2-xTB method for the exploratory search and DFT for refinement;

3. map the corresponding stationary points for the approach of a single water molecule, so that the two routes are treated identically;

4. compute the adsorption energy, the zero point corrected energy and the Gibbs energy at 298 K and at the temperature of an FCC regenerator, for both adsorbates;

5. test the sensitivity of the computed adsorption energies to the choice of density functional by repeating the single point energies with PBE0;

6. state, from the computed evidence, which of the competing mechanistic proposals the results support, and which parts of the reaction profile remain undetermined by the present calculations.

## 1.5 Research Questions

The study answers the following questions.

1. Which of the two adsorbates, vanadic acid or water, binds more strongly to the zeolite Y Brønsted acid site, and by how much?

2. What are the geometries and relative energies of the intermediates formed as each adsorbate approaches and reacts with the acid site?

3. Does the difference between the two adsorption energies survive when the density functional is changed?

4. How do the adsorption energies change when the temperature is raised from 298 K to the regenerator temperature of 1003 K?

5. Which of the three competing mechanistic positions in the literature is consistent with the computed energy profile?

## 1.6 Scope of the Study

The work covers the following.

**System.** A four tetrahedral atom cluster with the composition AlSi₄O₄H₁₃, cut from the faujasite framework, carrying one Brønsted acid site and terminated with hydrogen atoms. The two adsorbates studied are orthovanadic acid, H₃VO₄, and water, H₂O.

**Methods.** Geometry optimisation and frequency analysis at the GFN2-xTB level, at the B3LYP-D3(BJ)/def2-TZVP level and, for single point energies only, at the PBE0-D3(BJ)/def2-TZVP level. All calculations use the ORCA program package.

**Outputs.** Electronic energies, zero point energies, thermal enthalpies and Gibbs energies of the separated reference species and of the adsorption complexes; vibrational frequencies used to confirm that each structure is a minimum or a saddle point; and the geometric parameters that describe how each adsorbate sits on the acid site.

The following are outside the scope. The zeolite is represented by a cluster rather than a periodic crystal, so confinement effects arising from the full faujasite cage are not included. Only one Brønsted acid site environment is modelled. The solvent is not included, and no explicit steam atmosphere is simulated. Sodium, rare earth cations and extra-framework aluminium are not part of the model, and so the sodium-mediated mechanism of Xu et al. (2002) cannot be tested directly against the computations; only its central claim, that vanadium does not itself attack the framework, can be assessed. Counterpoise corrections to the adsorption energies are specified in the method but were not obtained in the completed calculations. Reaction rate constants and activation free energies are not reported.

## 1.7 Justification of the Study

The justification for this work rests on three arguments.

First, the dispute in the literature is quantitative and has not been settled by measurement. The techniques that could in principle resolve it, such as solid state nuclear magnetic resonance of aluminium and X-ray absorption spectroscopy, measure the state of the catalyst before and after steaming, not the energy of a bond breaking in the presence of an adsorbate. A calculation returns exactly that energy.

Second, the answer matters to design. Vanadium traps, which are added to cracking catalysts to capture vanadium before it reaches the zeolite, are selected largely by experiment. A trap is effective if it reacts with the migrating vanadium species more readily than the zeolite does. Knowing the binding energy of vanadic acid on the zeolite acid site gives a numerical target for a trap, and knowing whether the attacking species is vanadic acid or sodium hydroxide tells designers whether they should be trapping vanadium or managing sodium.

Third, the same problem has been solved for steam. The dealumination of zeolites by water has been studied by periodic DFT and by ab initio molecular dynamics, and the steps, the barriers and the role of additional water molecules are established (Malola et al., 2012; Silaghi et al., 2016; Nielsen et al., 2019; Stanciakova et al., 2019). The vanadium route has no equivalent treatment. Extending an established approach to an unstudied but industrially important reactant is a proportionate use of computational resources and a well defined contribution to knowledge.

Zaria and the wider Nigerian refining sector have a direct interest in the question. Nigerian refineries process heavy residues with high metal content, and the corrosion and catalyst consumption that follow from vanadium contamination have been documented in the Nigerian literature (Adanenche et al., 2023). A molecular explanation of the attack, and a numerical binding energy that a trap material must beat, is of practical value here as much as anywhere.

## 1.8 Limitations of the Study

The limitations of the work are stated plainly because several of them affect what can be concluded from the results.

The cluster model is finite. Terminating the framework with hydrogen atoms removes the mechanical constraint that the surrounding crystal would impose on the reacting site, and a four tetrahedral atom cluster is small. Cluster models of this size are known to exaggerate the flexibility of the site, and the energies reported here are therefore expected to differ from periodic values by amounts larger than the method error.

The calculations were performed in the gas phase. In an operating regenerator the zeolite pore system is filled with steam at pressures of the order of a bar, and both the adsorption energies and the reaction barriers are sensitive to the presence of additional water molecules, as the ab initio molecular dynamics literature shows.

Themost demanding parts of the reaction profile were not completed. Within the time and computing budget available, the geometries and frequencies of the adsorption complexes, the first chemisorbed intermediate and both reference species were obtained at the B3LYP level, but the second intermediate, the product of the reaction and the transition state for the first bond cleavage did not reach their convergence criteria at that level. The heavy computational burden of DFT for the larger structures made it impossible to complete these within the time allocated. The transition state and product energies reported at the semi-empirical level are used with that qualification stated wherever they appear.

The counterpoise correction for basis set superposition error is specified in the method but the corrected values were not obtained, so the reported adsorption energies are uncorrected and are expected to overstate the binding strength by an amount that is not quantified here.

The model does not contain sodium. The second mechanistic school holds that sodium is essential, and the present calculations cannot test that claim; they can only test whether vanadic acid is intrinsically capable of attacking the framework in the absence of sodium.

Finally, the absence of a dispersion corrected periodic treatment means the results are best read as a comparison between two adsorbates treated identically, rather than as absolute thermodynamic quantities. The difference between the vanadic acid and water adsorption energies is the more reliable of the two outputs because most of the systematic error cancels between the two.
