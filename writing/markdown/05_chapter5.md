# CHAPTER FIVE

# CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Summary of the Work

This project set out to test the first step of the vanadic acid hypothesis for the destruction of zeolite Y by vanadium in residue fluid catalytic cracking. A four tetrahedral site faujasite cluster carrying one Brønsted acid site was optimised with vanadic acid and, as a control, with water, using a two tier workflow. Tier 1 screened geometries with the semi empirical GFN2 xTB method on a Dell Latitude E6430 laptop. Tier 2 refined the accepted geometries with B3LYP D3(BJ)/def2 TZVP, checked them with PBE0 D3(BJ)/def2 TZVP single points, and computed harmonic frequencies for thermochemistry at 298.15 K and 1003.15 K.

Seven states passed every acceptance test: the three reference species, both pre reaction complexes, the chemisorbed intermediate V-I1 and the hydrolysed steam product W-P. Three states did not. The candidate saddle point V-TS2 failed to converge and returned fourteen imaginary modes, the intermediate V-I2 reached its cycle limit without converging, and the extracted product V-P did not terminate. No activation barrier is therefore reported for any step of the vanadium route.

## 5.2 Conclusions

1. Vanadic acid binds a faujasite Brønsted acid site more strongly than water does. The computed electronic adsorption energies are 93.0 kJ mol⁻¹ for vanadic acid and 78.3 kJ mol⁻¹ for water at B3LYP D3(BJ)/def2 TZVP, and 93.1 and 78.6 kJ mol⁻¹ at PBE0 D3(BJ)/def2 TZVP. The two functionals agree to within 0.3 kJ mol⁻¹, so the ranking is not an artefact of the functional.

2. The margin in favour of vanadic acid is 14.7 kJ mol⁻¹ at B3LYP and 14.4 kJ mol⁻¹ at PBE0. This quantity can be written without the cluster reference energy, so it is unaffected by the imperfectly converged cluster reference, and it is the most reliable number produced by this work.

3. That margin is too small to do the job the vanadic acid hypothesis asks of it. At 1003 K it corresponds to a ratio of binding constants of about 5.8, while steam in a regenerator outnumbers vanadic acid by four to five orders of magnitude. A two site Langmuir estimate using the computed ratio puts vanadic acid on about 0.03 per cent of the Brønsted sites at 10 ppm, and on about one site in twenty thousand at the 1.7 ppm that Trujillo et al. (1997) calculated. On the evidence of the adsorption step, the hypothesis as usually stated does not survive, unless vanadic acid reaches a local concentration inside the zeolite some ten thousand times its bulk gas concentration, which is the escape route that Trujillo et al. (1997) proposed but did not quantify.

4. The finding is closer to the position of Pine (1990) and Xu et al. (2002) than to that of Wormsbecher et al. (1986). Vanadium is not chemically inert at the acid site, so it is not a pure spectator, but its binding preference is nowhere near large enough to make it the agent that decides the rate. This is consistent with Pine's observation that the activation energy of destruction is unchanged by vanadium, and with the conclusion of Xu et al. (2002) that vanadium acts by releasing sodium rather than by attacking the framework itself.

5. No activation barrier could be established for any step of the vanadium route, and none should be inferred from the energies reported here. The study therefore provides no computational support for a catalytic rate enhancement by vanadium, and it does not validate the mechanism as a whole.

6. The full sequence mapped in this model is not a downhill route to a dealuminated framework. The extracted product state came out about 420 kJ mol⁻¹ above the separated reactants, and the intermediate region between V-I1 and V-I2 is high and flat. This is consistent with the view that vanadium is regenerated rather than consumed, but the numbers behind it come from jobs that failed, so it is offered as an observation and not as a result.

7. The semi empirical screen overstated the gap between the two adsorbates by a factor of about nine, giving 127.3 kJ mol⁻¹ where density functional theory gives 14.7 kJ mol⁻¹. GFN2 xTB was adequate for finding geometries and inadequate for measuring this energy difference. A project that had reported the Tier 1 numbers as results would have concluded that the vanadic acid hypothesis was confirmed, and would have been wrong.

8. At 1003 K the computed Gibbs free energies are positive for every state, which would mean that nothing adsorbs at regenerator temperature. This is an artefact of the gas phase harmonic treatment, which charges the full translational entropy penalty to a molecule that in a real pore is already condensed. The ordering of states is unaffected, but the absolute values at 1003 K should not be quoted.

## 5.3 Recommendations

1. Trap developers should work to a specification rather than to a screening programme. The zeolite sets the bar at roughly 93 kJ mol⁻¹ for vanadic acid at a Brønsted site, or nearer 75 to 88 kJ mol⁻¹ after correction for basis set superposition error. Any candidate trap should be modelled against that number before it is synthesised, under conditions that include steam at 1003 K.

2. Refiners and catalyst suppliers should treat the sodium content of the catalyst as a first order variable when diagnosing vanadium damage, following Xu et al. (2002). The evidence that the vanadium effect collapses when exchangeable sodium is removed is experimental and strong, and it points at a control lever that costs less than increasing trap loading.

3. Research effort on the vanadic acid route should shift from asking whether vanadic acid attacks the framework to asking how much of it accumulates in the pores. The present work shows that accumulation of about four orders of magnitude over bulk is what the hypothesis requires. Either that accumulation is demonstrated or the hypothesis should be set aside.

4. Undergraduate computational projects in this department should be required to keep a job register and to report failures. The three failed states in this project are more informative than the seven successes, and a report that had quietly dropped them would have overstated what the work established.

## 5.4 Suggestions for Further Work

1. Add sodium. The strongest rival explanation cannot be tested without it. A cluster containing a sodium cation at a neighbouring exchange site would allow the metavanadate formation of equation 2.6 and the hydroxide attack of equations 2.7 and 2.8 to be modelled directly, which is the comparison that would actually settle the dispute.

2. Move to a periodic model. A full faujasite unit cell would remove the frozen boundary that is the most likely cause of the fourteen imaginary modes, would restore the long range electrostatic field and the pore confinement, and would allow local concentration inside the supercage to be addressed by computing adsorption from a physisorbed reference rather than from the gas phase.

3. Obtain the counterpoise correction. The four counterpoise jobs in this project failed on an input formatting error that is straightforward to fix, and the correction would convert the reported binding energies from upper bounds into defensible values.

4. Retry the saddle point with the caps released or with a larger cluster, and with a method that treats the boundary more honestly. Until a single imaginary mode is obtained and the two sided interval test passes, the barrier for framework bond cleavage in the presence of vanadic acid remains unknown.

5. Look beyond aluminium. Pine (1990) showed that vanadium attacks silicalite, which contains almost no aluminium, so a route that attacks silicon oxygen bonds deserves the same computational treatment that this study gave to the aluminium oxygen bridge.
