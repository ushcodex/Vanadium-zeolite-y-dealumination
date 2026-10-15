# 1.0 INTRODUCTION

## 1.1 Background of the Study

Residue fluid catalytic cracking (RFCC) converts heavy petroleum fractions into lighter products. Its circulating catalyst contains zeolite Y, which provides much of the catalytic activity. Metals in residue feedstocks, including vanadium, build up on the catalyst during operation. Vanadium is associated with faster loss of zeolite activity during regeneration (Adanenche et al., 2023; Wormsbecher, Peters, & Maselli, 1986).

Zeolite Y is a crystalline aluminosilicate with the faujasite structure. Its framework contains aluminium and silicon atoms linked by oxygen atoms. A framework aluminium atom creates a Brønsted acid site, which helps crack hydrocarbons. When aluminium leaves the framework, the process is called dealumination, and the number of acid sites decreases (Malola, Svelle, Lønstad Bleken, & Swang, 2012).

Steam can remove framework aluminium during regeneration. Researchers disagree about the additional role of vanadium. Wormsbecher et al. (1986) proposed that vanadium pentoxide reacts with steam to form volatile vanadic acid, which then promotes framework damage. Trujillo et al. (1997) developed this explanation and proposed that vanadic acid concentrates inside the zeolite.

Other studies questioned whether vanadic acid directly causes dealumination. Pine (1990) found that vanadium also damaged silicalite, which contains little aluminium, and reported a similar activation energy with and without vanadium. Xu, Liu, and Madon (2002) proposed that vanadium releases sodium from the catalyst and that sodium hydroxide attacks the framework. These explanations leave an important question: how strongly does vanadic acid bind to a Zeolite Y acid site compared with water?

This project examined that question with a local computational model. It compared the calculated adsorption energies of vanadic acid and water at the same Brønsted acid site. The calculation was also used to assess whether the available thermochemical and reaction-path results could support conclusions about dealumination.

## 1.2 Statement of the Problem

Vanadium contamination reduces the activity of Zeolite Y catalysts, but the molecular cause remains disputed. One proposed explanation assigns a direct role to vanadic acid, while another assigns the main framework attack to steam and sodium. A comparison of vanadic acid and water adsorption energies at the same model acid site provides a focused test of the first step in the vanadic-acid explanation. This project addressed that comparison and assessed whether the calculations supported conclusions about later framework bond cleavage.

## 1.3 Aim of the Study

The aim of this study was to evaluate vanadic acid adsorption on a model Zeolite Y Brønsted acid site and compare its calculated adsorption energy with that of water under conditions relevant to an RFCC regenerator.

## 1.4 Objectives of the Study

The objectives were to:

1. construct and optimise a local Zeolite Y cluster model with one Brønsted acid site and vanadic-acid and water adsorption structures in ORCA;
2. refine the accepted structures and quantify the relative adsorption energies of vanadic acid and water;
3. assess the calculated thermochemical corrections at 298.15 K and 1003.15 K and determine whether they supported a quantitative estimate of competitive site occupancy; and
4. test whether the calculations established a validated vanadic-acid pathway for framework Al–O bond cleavage.

## 1.5 Scope of the Study

The study used a gas-phase cluster model, AlSi₄O₄H₁₃, containing one framework aluminium atom and four silicon atoms. It compared vanadic acid, H₃VO₄, and water, H₂O, at one Brønsted acid site. GFN2-xTB calculations in ORCA were used to screen initial geometries, which were then refined with B3LYP-D3(BJ)/def2-TZVP; PBE0-D3(BJ)/def2-TZVP single-point calculations checked the adsorption-energy comparison. Harmonic-frequency calculations supplied thermochemical corrections at 298.15 K and 1003.15 K.

The calculations did not include a full Zeolite Y crystal, pore confinement, explicit sodium, the surrounding catalyst matrix, or a liquid vanadium pentoxide phase. The RFCC gas composition was used to interpret the calculations but was not represented explicitly in the cluster model. Candidate structures beyond adsorption were examined, but the model did not produce a validated density-functional transition state for framework Al–O cleavage. No experimental measurements were included.

## 1.6 Significance of the Study

This study provides a direct comparison of vanadic acid and water adsorption energies at the same model acid site. It also separates conclusions supported by converged calculations from those that remain uncertain because of failed geometry or frequency tests. The results can guide later calculations that include the Zeolite Y pore, sodium, and the high steam concentration in an RFCC regenerator.

## 1.7 Limitations of the Study

The small cluster represented only the local acid site and omitted long-range electrostatic effects and pore confinement. The terminal hydrogen atoms were fixed during geometry optimisation, which may have affected the motion of the cluster boundary. No complete basis-set-superposition correction was obtained, so the absolute adsorption energies remained uncorrected. The harmonic gas-phase treatment also did not provide a reliable quantitative estimate of adsorption-site occupancy at regenerator temperature.

## 1.8 Definition of Terms

**Zeolite Y:** A crystalline aluminosilicate with the faujasite structure, used as an active component of fluid catalytic cracking catalysts.

**Brønsted acid site:** A proton attached to an oxygen atom between framework aluminium and silicon; it provides acidity for hydrocarbon cracking.

**Dealumination:** Removal of aluminium from the zeolite framework, which reduces the number of framework acid sites.

**Adsorption energy:** The energy change when a molecule binds to a surface or model site; a negative value indicates that the adsorbed structure has lower electronic energy than the separated species.

**Stationary point:** A structure at which the calculated energy gradient is zero. A minimum has no meaningful imaginary vibrational frequencies, while a first-order saddle point has one.

**Imaginary frequency:** A negative calculated vibrational frequency that indicates instability along a particular structural motion.
