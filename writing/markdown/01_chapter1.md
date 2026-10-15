# 1.0 INTRODUCTION

## 1.1 Background of the Study

Residue fluid catalytic cracking (RFCC) converts heavy refinery feedstocks into lighter products. Its catalyst contains Zeolite Y, whose acid sites support the cracking reactions. Metals carried in residue feed, including vanadium, accumulate on the catalyst during operation and are associated with loss of zeolite activity during regeneration (Adanenche et al., 2023; Wormsbecher, Peters, & Maselli, 1986).

Steam can remove aluminium from the Zeolite Y framework during regeneration. Each framework aluminium atom is associated with a Brønsted acid site, so removal of framework aluminium reduces the number of sites available for cracking. This loss of framework aluminium is called dealumination (Malola, Svelle, Lønstad Bleken, & Swang, 2012).

Researchers have proposed different explanations for the additional damage associated with vanadium. Wormsbecher et al. (1986) proposed that vanadium oxide reacts with steam to form volatile vanadic acid, which then attacks the zeolite. Pine (1990) argued that steam drives the destruction and that vanadium acts as a catalyst. Xu, Liu, and Madon (2002) proposed a sodium-mediated route in which vanadium helps release sodium that forms sodium hydroxide. The proposed mechanisms therefore assign different roles to vanadic acid, steam, and sodium.

Wormsbecher et al. (1986) estimated that vanadic acid was present at low parts-per-million levels under the regenerator conditions they considered. Their estimate was made for a system with high steam content and a total pressure of about 2 atm. This large difference in gas abundance makes it important to compare vanadic acid and water at the same model acid site, while recognising that adsorption energy alone cannot establish a reaction rate.

## 1.2 Statement of the Problem

Vanadium is associated with accelerated loss of Zeolite Y activity, but the molecular mechanism remains disputed. A direct vanadic-acid mechanism requires vanadic acid to interact with the framework and proceed through bond cleavage, while steam is present at much higher concentration. A sodium-mediated mechanism provides a different explanation that does not require vanadic acid to dominate acid-site occupation.

The literature reviewed here did not provide a like-for-like density functional theory (DFT) comparison of vanadic acid and water adsorption at one Zeolite Y Brønsted acid site. Such a comparison can clarify the electronic and thermochemical preference of the model site. It cannot, on its own, establish the mechanism operating in a catalyst particle or determine the rate of dealumination.

## 1.3 Aim and Objectives of the Study

The aim of this study was to compare vanadic acid and water at a model Zeolite Y Brønsted acid site and assess what the calculated adsorption, pathway, and thermochemical results implied for the proposed dealumination mechanism. The work was organised around four objectives:

1. construct and optimise a local Zeolite Y cluster model and initial vanadic-acid and water adsorption structures in ORCA;
2. refine the accepted structures and quantify the electronic adsorption energies of both adsorbates;
3. determine whether transition-state searches yielded validated candidates for the first framework Al–O cleavage steps in the vanadic-acid and water routes; and
4. calculate harmonic Gibbs energies at 298.15 K and 1003.15 K and evaluate conditional competitive site occupation using RFCC gas partial pressures from the literature.

## 1.4 Scope of the Study

The calculations used a gas-phase cluster with formula AlSi₄O₄H₁₃. The cluster represented one framework aluminium atom, four neighbouring silicon atoms, the bridging oxygen atoms, terminal hydrogen atoms, and one Brønsted acid proton. Vanadic acid, H₃VO₄, and water, H₂O, were compared at the same model site. GFN2-xTB was used to screen structures. Accepted geometries were refined with B3LYP-D3(BJ)/def2-TZVP, and PBE0-D3(BJ)/def2-TZVP single-point calculations were used to check the electronic adsorption comparison.

Harmonic Gibbs energies were evaluated at 298.15 K and 1003.15 K. A formal competitive-site estimate was made at 1003.15 K using the reported partial pressures of steam and vanadic acid. This estimate was treated as conditional on the ideal-gas harmonic model and the assumed single-site equilibrium expression. Candidate transition states were searched for in the vanadic-acid route and a water-hydrolysis control.

The study did not include a periodic Zeolite Y crystal, explicit pore confinement, sodium, nickel, or the wider catalyst matrix. It also did not include experimental measurements. The calculations were therefore limited to a local model and did not represent the complete RFCC regenerator environment.

## 1.5 Justification of the Study

A direct comparison at the same model acid site isolates one part of the proposed vanadic-acid mechanism: how the electronic adsorption and harmonic thermochemistry of vanadic acid compare with those of water. The comparison provides a basis for interpreting the relative roles of the two molecules without assuming that stronger electronic binding necessarily means faster dealumination.

The results also help define the next computational steps. A local cluster can identify whether the proposed species interact with the acid site, while transition-state validation and a larger pore model are needed to assess framework damage. The distinction is relevant to studies of vanadium tolerance and passivation in RFCC catalysts (Adanenche et al., 2023; Etim et al., 2018).

## 1.6 Limitations of the Study

The cluster represented only the local acid site, and its terminal hydrogen atoms were fixed during optimisation. The absolute DFT adsorption energies were not counterpoise-corrected because the attempted fragment calculations did not produce a complete correction. The high-temperature thermochemical and site-occupation estimates used an ideal-gas harmonic treatment that omitted pore confinement and local concentration effects. GFN2-xTB produced a candidate saddle point for one vanadic-acid step, but its DFT refinement did not pass the vibrational test; no DFT activation barrier was therefore established.

## 1.7 Organisation of the Thesis

Chapter Two reviews Zeolite Y, steam dealumination, vanadium-related mechanisms, and previous computational studies. Chapter Three describes the cluster model, electronic-structure calculations, pathway searches, and thermochemical site-occupation calculation. Chapter Four presents and discusses the resulting geometries, adsorption energies, transition-state assessments, and thermochemistry in objective order. Chapter Five gives the conclusions and recommendations.
