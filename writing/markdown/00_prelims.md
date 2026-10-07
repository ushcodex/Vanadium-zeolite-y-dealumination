[TITLEPAGE]
A DENSITY FUNCTIONAL THEORY EVALUATION OF THE VANADIC ACID HYPOTHESIS FOR ZEOLITE Y DEALUMINATION UNDER RESIDUE FLUID CATALYTIC CRACKING REGENERATOR CONDITIONS

BY

Ahmad Usman SHEHU
U19CE1068

A RESEARCH PROJECT SUBMITTED TO THE DEPARTMENT OF CHEMICAL ENGINEERING,
FACULTY OF ENGINEERING, AHMADU BELLO UNIVERSITY, ZARIA,
IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF THE DEGREE OF
BACHELOR OF ENGINEERING (B.ENG.) IN CHEMICAL ENGINEERING

NOVEMBER, 2026
[/TITLEPAGE]

# DECLARATION

I declare that the work in this project report entitled "A Density Functional Theory Evaluation of the Vanadic Acid Hypothesis for Zeolite Y Dealumination Under Residue Fluid Catalytic Cracking Regenerator Conditions" was carried out by me in the Department of Chemical Engineering, Ahmadu Bello University, Zaria. The information derived from the literature has been duly acknowledged in the text and a list of references is provided. No part of this project report was previously presented for another degree or diploma at this or any other institution.

_______________________________
Ahmad Usman Shehu
(Student)

_______________________________
Date

# CERTIFICATION

This project report entitled "A Density Functional Theory Evaluation of the Vanadic Acid Hypothesis for Zeolite Y Dealumination Under Residue Fluid Catalytic Cracking Regenerator Conditions" by Ahmad Usman SHEHU (U19CE1068) meets the regulations governing the award of the degree of Bachelor of Engineering (B.Eng.) in Chemical Engineering of Ahmadu Bello University, Zaria, and is approved for its contribution to knowledge and literary presentation.

_______________________________
Project Supervisor

_______________________________
Date

_______________________________
Head of Department

_______________________________
Date

# DEDICATION

This work is dedicated to my parents, whose patience and investment made my education possible, and to every student who has been told that computational chemistry is too difficult to attempt on a laptop.

# ACKNOWLEDGEMENTS

I thank my project supervisor for steady guidance, for insisting that every number in this report be traceable to an output file, and for the freedom to pursue a topic that sits between chemical engineering and quantum chemistry.

I am grateful to the Head of Department and to the academic and non-academic staff of the Department of Chemical Engineering, Ahmadu Bello University, Zaria, for their contributions to my training. I thank the research group whose published computational work from this same department showed me that this kind of project could be done here.

I thank my family for their support throughout the period of this work, and my colleagues for many useful arguments about mechanisms, energies and units.

# ABSTRACT

Vanadium in residue feedstocks shortens the life of fluid catalytic cracking catalysts, and the reason has been disputed since 1986. One school holds that vanadium pentoxide reacts with regenerator steam to give volatile vanadic acid, H₃VO₄, which then attacks the zeolite Y framework. Another school holds that steam, aided by sodium, does the damage and that vanadium merely releases sodium from its exchange sites. A third position treats vanadium as a catalyst of ordinary steam dealumination. This project tests the first step of the vanadic acid hypothesis directly. A four tetrahedral site cluster of faujasite, AlSi₄O₄H₁₃, carrying one Brønsted acid site, was optimised with vanadic acid and, as a control, with water, using a two tier workflow. Tier 1 screened geometries with the semi empirical GFN2 xTB method on a Dell Latitude E6430 laptop. Tier 2 refined the accepted geometries with B3LYP D3(BJ)/def2 TZVP and checked them with PBE0 D3(BJ)/def2 TZVP single points plus harmonic frequency calculations at 298.15 K and 1003.15 K. Vanadic acid binds the acid site by 93.0 kJ mol⁻¹ and water by 78.3 kJ mol⁻¹ at B3LYP; the two functionals differ by no more than 0.3 kJ mol⁻¹. The 14.7 kJ mol⁻¹ advantage of vanadic acid is real, it survives removal of the cluster reference energy, and it is reproducible. It is also small. At 1003 K it corresponds to a binding constant ratio of about 5.8, while steam in a regenerator outnumbers vanadic acid by roughly four to five orders of magnitude. A two site Langmuir estimate using the computed ratio puts vanadic acid on well under one per cent of the Brønsted sites. Downstream of adsorption the study could not be completed: the candidate saddle for framework bond cleavage carried fourteen imaginary modes, one intermediate optimisation hit its cycle limit, and the product calculation was killed before termination, so no activation barrier is reported. Full aluminium extraction by a single vanadic acid molecule was endothermic in this model by about 420 kJ mol⁻¹. The honest conclusion is that binding thermodynamics alone does not validate the vanadic acid hypothesis as usually stated, that the screening method overstated the gap between the two adsorbates by about nine times, and that any vanadium specific chemistry must be looked for downstream of simple adsorption.
