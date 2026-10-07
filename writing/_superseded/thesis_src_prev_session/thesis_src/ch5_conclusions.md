# CHAPTER FIVE

# CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Summary of the Work

This study set out to determine whether vanadic acid attacks the Brønsted acid site of zeolite Y more strongly than steam does, in order to bring quantitative evidence to a mechanistic dispute that the experimental literature has not settled. The dispute is whether the entity that destroys the zeolite framework in a residue fluid catalytic cracking regenerator is vanadic acid derived from deposited vanadium or the hydroxide derived from sodium, and whether the bond broken is an aluminium oxygen bond or a silicon oxygen bond.

A four tetrahedral atom cluster of the faujasite framework with the composition AlSi₄O₄H₁₃, containing one Brønsted acid site, was built and optimised. Vanadic acid and water were each brought to that site, and the energy of every stationary point along both routes was computed using the semi-empirical GFN2-xTB method for exploratory work and the B3LYP-D3(BJ)/def2-TZVP level for the definitive calculations, with PBE0-D3(BJ)/def2-TZVP single point energies as a cross-check. All calculations used the ORCA program package. The semi-empirical and initial density functional work was performed on a Dell Latitude E6430 laptop, and the later density functional work on a four process virtual machine.

## 5.2 Conclusions

The following conclusions are drawn from the computed results. Each is stated at the confidence level that the evidence in Chapter Four supports, and the evidence on which each rests is identified.

**First, vanadic acid binds more strongly than water to the zeolite Y Brønsted acid site.** The electronic adsorption energy of vanadic acid on the cluster is −93.01 kJ mol⁻¹ and that of water is −78.32 kJ mol⁻¹ at the B3LYP-D3(BJ)/def2-TZVP level, so vanadic acid is preferred by 14.69 kJ mol⁻¹. The two values are reproduced to within 0.30 kJ mol⁻¹ by the PBE0 functional, and the difference between them to within 0.25 kJ mol⁻¹. This is the principal finding of the work. It is stated as an established result because both complexes converged, both returned zero imaginary modes, and two independently parameterised density functionals agree on it.

**Second, the preference is real but modest.** A margin of about 14.5 kJ mol⁻¹ is roughly six times the thermal energy at room temperature and would give a clear preference at equilibrium between two species competing for the same site, but it is small compared with the absolute binding energy of either adsorbate and falls within the uncertainty that the finite cluster and the finite basis set impose on the calculation. The correct statement is that vanadic acid is thermodynamically preferred at the acid site over water, not that it dominates the site.

**Third, the adsorption of vanadic acid is not a purely non-bonding interaction.** The optimised geometry of the vanadic acid complex shows a contact of 1.925 Å between one of the vanadic oxygen atoms and the framework aluminium, in addition to the four framework oxygen contacts. The incoming molecule has already begun to share electron density with the aluminium at the first step, so the state described as an adsorption complex is the beginning of chemisorption rather than a hydrogen bonded precursor.

**Fourth, vanadic acid forms a chemisorbed intermediate that water does not form.** The conversion of the adsorption complex V-PRC to the chemisorbed intermediate V-I1 releases 22.37 kJ mol⁻¹ at the B3LYP level and 27.07 kJ mol⁻¹ at the PBE0 level. In this intermediate all four framework oxygen contacts to the aluminium are retained, so the framework is still intact, but the adsorbate is firmly attached and the aluminium environment has changed. The chemistry of the vanadium route is therefore distinct from the chemistry of the steam route from the second step onward.

**Fifth, the temperature of the regenerator does not favour vanadium.** Under the standard state convention used in the calculation, the entropy loss on adsorption is larger for vanadic acid than for water, and at 298 K the Gibbs energy of adsorption of water becomes the more negative of the two. At 1003 K both Gibbs energies of adsorption are positive under that convention, which is largely an artefact of placing the adsorbate at one bar in the gas phase, but the comparison between the two routes is unaffected by that artefact: the margin between them widens against vanadic acid as temperature rises. Any thermodynamic argument that vanadium outcompetes water for the acid site must therefore rest on the enthalpy and on the events that follow adsorption, not on the adsorption equilibrium at regenerator temperature.

**Sixth, the semi-empirical treatment of the full pathway does not survive transfer to density functional theory.** The complete profile for both routes was obtained at the GFN2-xTB level and gave a vanadium barrier of 160.70 kJ mol⁻¹ and a steam barrier of 29.29 kJ mol⁻¹. When the corresponding states were recomputed by density functional theory, the second intermediate, the product and the saddle point all failed to meet the acceptance criteria. The saddle point in particular returned fourteen imaginary modes at the density functional level against one at the semi-empirical level. The semi-empirical profile is therefore a guide to the shape of the surface and to where to look, not a source of final numbers.

**Seventh, the extraction step is not established.** The dealuminated product computed at the density functional level lies far above the reactants on the cluster model, at about +415 to +420 kJ mol⁻¹ on the two attempted geometries, and neither optimisation converged. The same limitation applies to the steam route, where the single hydrolysis product lies 54.30 kJ mol⁻¹ above the water complex. These values are interpreted, with reasons given in Section 4.6.4, as a consequence of the model's lack of pore confinement, solvating water, matrix silicon for healing the vacancy and configurational entropy. They do not contradict the published periodic calculations that report a favourable overall extraction; they delimit what a gas phase cluster of this size can address.

**Eighth, the results support a limited version of the vanadium attack hypothesis and are consistent with the narrow claim made by the opposing school.** On the computed evidence, vanadic acid is a chemically competent attacker of the faujasite framework: it is preferred at the acid site over water, it makes direct contact with the aluminium at the first step, and it forms a stable chemisorbed intermediate. This is consistent with the accounts given by Wormsbecher et al. (1986) and Trujillo et al. (1997). The present work cannot demonstrate that vanadic acid dominates the process under operating conditions, because the model contains no sodium, no rare earth cations and no extra-framework aluminium. It is consistent with the specific claim of Xu et al. (2002) that, in the absence of sodium, vanadium has only a limited effect, in the sense that the computed preference for vanadic acid, while real, is modest.

**Ninth, a numerical target now exists for the design of vanadium traps.** A trap material protects the catalyst by binding the mobile vanadium species more strongly than the zeolite does. The zeolite side of that competition is now quantified at −81.75 kJ mol⁻¹ after zero point correction, or −95.48 kJ mol⁻¹ in enthalpy terms at 298 K. A candidate trap material can be screened by computing the same quantity for vanadic acid on its surface and retaining the material if the value is more negative than this.

## 5.3 Contributions to Knowledge

The work makes three contributions.

It provides, to the best of the author's knowledge and subject to the searches conducted, the first comparison at the density functional level between a molecular vanadic acid attacking species and water on the same faujasite Brønsted acid site using identical methods. The comparison is stated as a binding energy margin of about 14.5 kJ mol⁻¹, tested against two density functionals.

It documents the first steps of the vanadium route on a molecular model, including the observation that vanadic acid has already begun to coordinate to the framework aluminium in the adsorption complex, which is a structural criterion by which the two mechanistic hypotheses can be distinguished.

It establishes an internal verification standard for the project's computation archive, in the form of a stated acceptance chain for stationary points and a machine checked register that traces every reported energy back to the log file it came from.

This work is not the first computational study of zeolite dealumination. That distinction belongs to Malola et al. (2012), and the mechanism has since been extended across four frameworks by Silaghi et al. (2016) and revisited under realistic water loading by Nielsen et al. (2019). Nor is it the first computational study of vanadium in a zeolite; Tielens and Dzwigaj (2010) computed the acid base properties of vanadium framework sites by periodic density functional theory. The contribution of this work lies specifically in the attacking molecule rather than in the framework vanadium site, and in the comparison against water.

## 5.4 Recommendations

The recommendations that follow are directed at three audiences: the researcher who will continue this work, the designer of vanadium traps, and the department in which the work was carried out.

**For the continuation of the research.** The following steps are recommended in the order given, because each removes a limitation that currently bounds the conclusions.

First, apply the counterpoise correction that was specified in the method but not obtained. The procedure is documented in Section 3.9 and the input structure is defined in Table 3.4. The two-sided jobs for both complexes should be run before any further state is computed, because the 14.5 kJ mol⁻¹ margin is of the order of the basis set superposition error and the result should be reported on a corrected basis.

Second, enlarge the cluster. A model drawn from the twelve membered ring of the supercage, containing three or four aluminium sites, would include the confinement that the present model lacks and would allow the extraction energy to be recomputed under conditions where it is not dominated by the absence of the lattice.

Third, obtain the saddle point for the first aluminium oxygen cleavage at the density functional level by a route other than transition state optimisation from a semi-empirical starting structure. That approach failed here with fourteen imaginary modes. A grid based scan of the aluminium to vanadic oxygen distance, carried out at the density functional level and followed by a transition state refinement from the maximum of the scan, is a more robust route and is the one recommended.

Fourth, extend the model to include sodium. The mechanism proposed by Xu et al. (2002) turns on the mobility of sodium from the exchange site, and it cannot be tested on a model that contains no sodium. A sodium exchanged cluster with a vanadic acid molecule and a water molecule present would allow the competition between the two routes to be computed directly.

Fifth, perform a periodic calculation on the fully extracted product. This is the single change most likely to bring the computed extraction energy into agreement with the published values, and the published methodology of Silaghi et al. (2016) provides a template.

**For the design of vanadium traps.** A trap material should be screened computationally before it is tested. The screening quantity is the adsorption energy of vanadic acid on the candidate surface at the same level of theory used here, and the acceptance threshold is that it be more negative than about −95 kJ mol⁻¹. The experimental literature already indicates that a working trap forms a crystalline vanadate with the mobile species (Etim et al., 2018), which implies a much larger binding energy than the zeolite provides; the computed threshold turns that observation into a predictive criterion.

**For the department.** Molecular simulation of the kind used here has become affordable. The density functional calculations reported in this thesis were performed on a four process virtual machine and a laptop, with no specialised hardware and no commercial licence beyond the freely available program. Two recommendations follow. The first is that a short internal training session on quantum chemistry as a design tool would allow final year projects in catalysis to be extended from experimental characterisation into mechanism, which is where the industrial questions in this field now sit. The second is that the workflow used here, in which structures are generated at the semi-empirical level and judged at the density functional level, is efficient enough to be taught and reused. The programme files and verification scripts from this project are retained in the project archive and are available to any student who wishes to build on them.

## 5.5 Suggestions for Further Work

The following investigations follow directly from the present study.

The exchange of aluminium in a faujasite framework by silicon from the matrix is the step that heals the vacancy left by dealumination, and it is believed to be the reason why a partially dealuminated catalyst retains its crystallinity while losing its acidity. The competition between healing and further attack has not been modelled on the same cluster used here and would extend the picture from the attack to the recovery.

The behaviour of vanadic acid in the presence of more than one water molecule has not been examined. The literature establishes that additional water molecules cooperate in the hydrolysis of framework bonds by participating in proton shuttling, and it is reasonable to expect a similar cooperation between water and vanadic acid. A cluster carrying three or four water molecules in addition to the vanadic acid would test whether the vanadium route is similarly assisted.

The rate constants implied by the computed energies were not obtained, because the saddle point for the first bond cleavage was not established at a level at which a rate constant would mean anything. Once that saddle point is obtained, conventional transition state theory would give a rate constant and would allow the two routes to be compared as rates rather than as energies.

Finally, the comparison between vanadic acid and steam should be repeated on a second framework, such as mordenite or ZSM-5, for which published periodic data already exist. If the margin between the two adsorbates is similar across frameworks, the finding is a general property of aluminosilicate Brønsted acid sites. If it changes with framework, the change itself is informative about what controls the adsorption at the molecular level.
