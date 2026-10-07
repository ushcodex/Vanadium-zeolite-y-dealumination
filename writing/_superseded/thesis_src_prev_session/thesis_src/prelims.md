# PRELIMINARY PAGES

## TITLE PAGE

**A COMPARATIVE DENSITY FUNCTIONAL THEORY STUDY OF VANADIC ACID AND STEAM ADSORPTION ON THE BRØNSTED ACID SITE OF ZEOLITE Y: EVIDENCE FOR THE MECHANISM OF VANADIUM-PROMOTED DEALUMINATION IN RESIDUE FLUID CATALYTIC CRACKING**

BY

**AHMAD USMAN SHEHU**
**(U19CE1068)**

A RESEARCH PROJECT SUBMITTED TO THE DEPARTMENT OF CHEMICAL ENGINEERING, FACULTY OF ENGINEERING, AHMADU BELLO UNIVERSITY, ZARIA

IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF BACHELOR OF ENGINEERING (B.ENG.) IN CHEMICAL ENGINEERING

OCTOBER, 2026

---

## DECLARATION

I declare that the work in this project report entitled "A Comparative Density Functional Theory Study of Vanadic Acid and Steam Adsorption on the Brønsted Acid Site of Zeolite Y: Evidence for the Mechanism of Vanadium-Promoted Dealumination in Residue Fluid Catalytic Cracking" was carried out by me in the Department of Chemical Engineering, Ahmadu Bello University, Zaria. The information derived from the literature has been duly acknowledged in the text and a list of references provided. No part of this project report was previously presented for another degree or diploma at this or any other institution.

_________________________
Ahmad Usman Shehu
(Student)

_________________________
Date

---

## CERTIFICATION

This project report entitled "A Comparative Density Functional Theory Study of Vanadic Acid and Steam Adsorption on the Brønsted Acid Site of Zeolite Y: Evidence for the Mechanism of Vanadium-Promoted Dealumination in Residue Fluid Catalytic Cracking" by Ahmad Usman Shehu meets the regulations governing the award of the degree of Bachelor of Engineering (B.Eng.) in Chemical Engineering of Ahmadu Bello University, Zaria, and is approved for its contribution to knowledge and literary presentation.

_________________________
Project Supervisor

_________________________
Date

_________________________
Head of Department

_________________________
Date

_________________________
External Examiner

_________________________
Date

---

## DEDICATION

This work is dedicated to my parents, whose patience and sacrifice made it possible, and to every student who has ever tried to explain a chemical bond to a computer.

---

## ACKNOWLEDGEMENTS

I am grateful to my project supervisor for insisting on evidence over assertion, and for the many corrections that followed. The habit of asking a result to justify itself has been the most useful thing I have learned.

I thank the Head of Department and the academic and technical staff of the Department of Chemical Engineering, Ahmadu Bello University, Zaria, for the environment in which the work was done, and for access to the computing facilities that carried the density functional part of the study.

I acknowledge the authors whose published work forms the foundation of this thesis, and in particular the group whose first principles treatment of zeolite dealumination by steam provided the benchmark against which the present calculations were set.

I thank my colleagues in the department for the arguments that sharpened the introduction and for the willingness to read drafts that were not yet good. Finally, I thank my family for their support throughout.

---

## LIST OF TABLES

| Table | Title | Page |
|---|---|---|
| 3.1 | Composition of the model systems used in this study | 24 |
| 3.2 | Input file for the geometry optimisation and frequency analysis of the vanadic acid adsorption complex | 26 |
| 3.3 | Measured wall clock times for the principal calculations | 29 |
| 3.4 | Fragment definition required by ORCA for a counterpoise calculation | 34 |
| 3.5 | Summary of the computational parameters used in this study | 36 |
| 4.1 | Computed reference energies at the B3LYP-D3(BJ)/def2-TZVP level | 39 |
| 4.2 | Stationary points on the vanadium route at the GFN2-xTB level | 42 |
| 4.3 | Stationary points on the steam route at the GFN2-xTB level | 42 |
| 4.4 | Adsorption of vanadic acid and of water on the zeolite Y Brønsted acid site | 46 |
| 4.5 | Enthalpy and entropy of adsorption extracted from the computed Gibbs energies | 48 |
| 4.6 | Comparison of the two density functionals on identical geometries | 50 |
| 4.7 | Density functional stationary points including those that did not meet the acceptance gate | 52 |
| 4.8 | The density functional ladder for the vanadium route | 54 |

---

## LIST OF FIGURES

| Figure | Title | Page |
|---|---|---|
| 2.1 | The faujasite structure of zeolite Y | 10 |
| 2.2 | Atomistic models of the faujasite framework with and without framework aluminium | 11 |
| 2.3 | Reaction paths for dealumination and desilication | 13 |
| 2.4 | Reaction steps and intermediate configurations for dealumination and desilication | 14 |
| 2.5 | Mechanisms of vanadium poisoning of cracking catalysts | 16 |
| 2.6 | Effect of calcination temperature on the mobility of vanadium species | 18 |
| 2.7 | Kerr's scheme for zeolite dealumination and hydronium attack | 19 |
| 2.8 | Effect of vanadium on the hydrothermal stability of catalysts | 21 |
| 3.1 | The two level computational workflow used in this study | 23 |
| 4.1 | The cluster models used in this work | 40 |
| 4.2 | The complete semi-empirical reaction profiles at the GFN2-xTB level | 43 |
| 4.3 | Adsorption of vanadic acid and of steam on the zeolite Y Brønsted acid site | 47 |
| 4.4 | Gibbs energy of adsorption against temperature | 49 |
| 4.5 | The level 2 ladder for the vanadium route | 55 |

Page numbers refer to the printed document and should be checked against the final pagination before submission.

---

## ABSTRACT

Vanadium in residue fluid catalytic cracking feedstock deposits on the catalyst, oxidises to vanadium pentoxide in the regenerator, and converts to volatile vanadic acid in the presence of steam. The published literature does not agree on whether vanadic acid is itself the species that hydrolyses the aluminosilicate framework, or whether the destructive agent is instead sodium hydroxide released by vanadium, with vanadium acting only indirectly. This study brings quantitative evidence to that dispute by computing the adsorption of vanadic acid and of water on a faujasite Brønsted acid site on identical terms.

A four tetrahedral atom cluster of composition AlSi₄O₄H₁₃, containing one Brønsted acid site, was constructed and optimised. Orthovanadic acid and water were each brought to the site. The potential energy surface was explored with the semi-empirical GFN2-xTB method, and stationary points were refined at the B3LYP-D3(BJ)/def2-TZVP level with geometry optimisation and frequency analysis. The electronic energies were cross-checked with PBE0-D3(BJ)/def2-TZVP single points. All calculations were performed with the ORCA program package.

The electronic adsorption energy of vanadic acid is −93.01 kJ mol⁻¹ and that of water is −78.32 kJ mol⁻¹, so vanadic acid is preferred at the acid site by 14.69 kJ mol⁻¹. PBE0 gives −93.07 and −78.62 kJ mol⁻¹, preserving the margin to within 0.25 kJ mol⁻¹. The optimised vanadic acid complex is not purely hydrogen bonded: one vanadic oxygen lies 1.925 Å from the framework aluminium, so chemisorption has already begun at the adsorption step. Conversion of the adsorption complex to the chemisorbed intermediate releases a further 22.37 kJ mol⁻¹, and in that intermediate all four framework oxygen contacts to the aluminium are retained, so the framework is intact but the aluminium environment is changed. The chemisorbed state has no counterpart on the steam route. Under standard state conditions the entropy penalty of adsorption is larger for vanadic acid, so the margin narrows and reverses with rising temperature; the thermodynamic argument for vanadium must therefore rest on the adsorption enthalpy and on the chemistry that follows adsorption.

The saddle point for the first aluminium oxygen cleavage was not established at the density functional level, where the attempted transition state optimisation returned fourteen imaginary modes, and the dealuminated product was computed as strongly endothermic on the cluster model, a result attributed to the absence of pore confinement, solvating water, matrix silicon for healing the vacancy and configurational entropy. The full reaction profile for both routes was obtained at the semi-empirical level, where the vanadium route descends to a chemisorbed intermediate 188 kJ mol⁻¹ below the adsorption complex that the steam route does not reach, and where the two routes are shown to be mechanistically distinct at every step.

The study concludes that vanadic acid is a chemically competent attacker of the faujasite framework and is thermodynamically preferred at the acid site over water, but that the preference is modest and the extraction step remains unestablished on this model. The zeolite side of the competition between a vanadium trap and the catalyst is quantified at −81.75 kJ mol⁻¹ after zero point correction, providing a numerical screening threshold for the rational design of vanadium traps.

**Keywords:** zeolite Y, vanadic acid, dealumination, density functional theory, GFN2-xTB, residue fluid catalytic cracking, vanadium passivation

---

## LIST OF ABBREVIATIONS AND SYMBOLS

| Symbol or abbreviation | Meaning |
|---|---|
| B3LYP | Becke three parameter exchange with Lee, Yang and Parr correlation density functional |
| D3(BJ) | Grimme's third generation dispersion correction with Becke-Johnson damping |
| def2-TZVP | Triple zeta valence polarised basis set |
| DFT | Density functional theory |
| ΔE | Electronic energy of reaction |
| ΔG | Gibbs energy of reaction |
| ΔH | Enthalpy of reaction |
| Eh | Hartree, the atomic unit of energy, equal to 2625.4996 kJ mol⁻¹ |
| FCC | Fluid catalytic cracking |
| GFN2-xTB | Geometry, frequency, non-covalent, second generation extended tight binding |
| IRC | Intrinsic reaction coordinate |
| kJ mol⁻¹ | Kilojoule per mole |
| NEB | Nudged elastic band |
| PBE0 | Parameter free hybrid functional of Perdew, Burke and Ernzerhof with 25 per cent exact exchange |
| PRC | Pre-reaction complex, the adsorption complex formed before reaction |
| RFCC | Residue fluid catalytic cracking |
| RIJCOSX | Resolution of identity approximation with chain of spheres exchange |
| TS | Transition state |
| V-I1, V-I2 | First and second intermediates on the vanadium route |
| V-P, V-PRC, V-TS2 | Product, pre-reaction complex and second transition state on the vanadium route |
| W-P, W-PRC, W-TS | Product, pre-reaction complex and transition state on the steam route |
| ZPE | Zero point energy |
| ν̃ | Wavenumber in reciprocal centimetres |
