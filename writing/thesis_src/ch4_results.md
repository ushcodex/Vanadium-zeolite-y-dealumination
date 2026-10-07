# CHAPTER FOUR

# RESULTS AND DISCUSSION

## 4.1 Introduction and Structure of the Chapter

This chapter reports what the calculations produced. It begins by establishing the reference energies and by showing that the cluster model is adequate for the purpose it was built for. It then presents the semi-empirical energy profile for both reaction routes, which is complete, and the density functional results for the adsorption step, which are the most reliable part of the work. It then tests the adsorption result against a second density functional, examines how the temperature of the regenerator changes the picture, and reports honestly what happened when the higher steps of the vanadium route were attempted at the density functional level. The chapter closes by comparing the numbers with the experimental and computational literature, by stating what the results do and do not say about the mechanistic dispute reviewed in Chapter Two, and by drawing out the implications for vanadium trap design.

Throughout the chapter, a result is described as established only when the geometry optimisation converged, the frequency calculation completed, and the imaginary mode count is consistent with the type of stationary point claimed. Results that fall short of that test are labelled as provisional or as not established, and no conclusion rests on them alone.

## 4.2 Reference Energies and Validation of the Cluster Model

### 4.2.1 Reference species

The reference energies for both routes are listed in Table 4.1. They are the electronic energies of the isolated cluster, the isolated water molecule and the isolated vanadic acid molecule, each at its own fully optimised geometry at the B3LYP-D3(BJ)/def2-TZVP level.

| Species | Log file | Atoms | Electronic energy, Eh | Optimisation cycles | Imaginary modes |
|---|---|---|---|---|---|
| Cluster, AlSi₄O₄H₁₃ | s1_03_cluster_optfreq.out | 22 | −1709.39409388 | 1 after restart | one at −4.64 cm⁻¹ |
| Water, H₂O | s1_01_h2o_optfreq.out | 3 | −76.42662980 | 4 | none |
| Vanadic acid, H₃VO₄ | s1_02_h3vo4_optfreq.out | 8 | −1246.82501396 | 14 | none |

Table 4.1: Computed reference energies at the B3LYP-D3(BJ)/def2-TZVP level. The reference zero for the vanadium route is E(cluster) + E(H₃VO₄) = −2955.81550333 Eh; for the steam route it is E(cluster) + E(H₂O) = −1785.82072368 Eh.

The water molecule optimised in four cycles to a structure with all real frequencies, which is the expected result for a three atom molecule and confirms that the calculation setup is behaving correctly. The vanadic acid molecule required fourteen cycles, which reflects the floppiness of the three hydroxyl groups around the vanadium centre rather than any difficulty with the calculation. Both molecules returned zero imaginary modes, so both are genuine minima and are suitable as reference states.

### 4.2.2 The cluster reference and its imaginary mode

The cluster reference requires comment because it was computed twice and because the accepted run contains a small imaginary mode.

The first attempt at the cluster optimisation ran for sixty six cycles and terminated normally, but the program did not report that the optimisation had converged: the root mean square gradient at the end was 0.000011, which is below the convergence threshold of 0.000030, so the structure was in practice converged even though the termination flag was not set. The job was then resumed from that geometry. The resumed run satisfied the convergence criteria in its first relaxation step and completed normally, giving an energy of −1709.39409388 Eh. The difference between the two runs is 0.0015 kJ mol⁻¹, which is negligible on the energy scale of this study, and it establishes that the reference is reproducible.

The resumed run reported one imaginary mode at −4.64 cm⁻¹. A frequency of this magnitude is not a chemically meaningful vibration. It is the numerical residue of the six translations and rotations that the harmonic treatment attempts to remove, and it arises because the optimisation reached the gradient threshold rather than the exact stationary point. For comparison, the lowest real vibrational mode of the cluster is at 27.58 cm⁻¹, so the spurious mode lies below the physical spectrum of the system. The cluster is therefore treated as a minimum in what follows, with the reservation that its energy carries an uncertainty of the order of the zero point energy of a mode at 5 cm⁻¹, which is less than 0.1 kJ mol⁻¹ and is immaterial to every conclusion drawn in this chapter.

### 4.2.3 Adequacy of the cluster

The cluster contains one aluminium atom in a tetrahedral environment formed by four framework oxygen atoms, each of which bridges to a silicon atom, and the bridging oxygen that carries the proton is a genuine Brønsted acid site. The aluminium oxygen bond lengths in the optimised cluster are 1.9192, 1.7160, 1.6947 and 1.6953 Å, as reported by the program in its internal coordinate output. The three shorter bonds are typical of an aluminium oxygen single bond in a zeolite framework, and the longer bond at 1.9192 Å is the one to the bridging oxygen that carries the proton. This elongation of the protonated bridging bond relative to the other three is exactly the structural signature of Brønsted acidity that the literature describes, and its presence in the model confirms that the cluster reproduces the essential electronic feature that makes zeolite Y an acid catalyst.

Figure 4.1 shows the three models used in this study side by side: the bare acid site, the site with water adsorbed and the site with vanadic acid adsorbed.

![Figure 4.1: The cluster models used in this work, drawn from the optimised B3LYP-D3(BJ)/def2-TZVP geometries. (a) the bare Brønsted acid site, (b) the water adsorption complex W-PRC, (c) the vanadic acid adsorption complex V-PRC.](figures/fig3_1_cluster_models.png)

## 4.3 The Semi-Empirical Energy Profile

### 4.3.1 Why the semi-empirical profile is reported and how it should be read

The complete reaction profile for both routes was obtained at the GFN2-xTB level. That level is not accurate enough to report final thermodynamic quantities, and the numbers in this section are not used to support any conclusion that the density functional results do not also support. They are reported for two reasons. They show the shape of the potential energy surface, which is what a subsequent DFT study needs to know before it can decide where to spend its computing budget. And they provide the starting geometries for the density functional work, so a reader who wants to repeat the work needs to see where the structures came from.

### 4.3.2 Energies of the stationary points

Table 4.2 lists every state on the vanadium route and Table 4.3 lists every state on the steam route, with the electronic energy, the energy relative to the appropriate reference zero, and the imaginary mode count.

| State | Role | Log file | Electronic energy, Eh | Relative energy, kJ mol⁻¹ | Imaginary modes |
|---|---|---|---|---|---|
| V-PRC | Adsorption complex | V-R-T1-V02.out | −51.19563631 | −196.90 | 0 |
| V-I1 | Chemisorbed intermediate | V-I1-T1-V01.out | −51.26731716 | −385.10 | 0 |
| V-TS2 | First aluminium oxygen cleavage saddle | optts3_bandB_ci.out | −51.20610884 | −224.40 | 1 at −78.21 cm⁻¹ |
| V-I2 | Opened framework intermediate | V-I2-T1-V04_pos.out | −51.25104052 | −342.37 | 0 |
| V-P | Dealuminated product | V-TS3-T1-V02.out | −51.15221675 | −82.90 | 0 |

Table 4.2: Stationary points on the vanadium route at the GFN2-xTB level. Reference zero: E(cluster) + E(H₃VO₄) = −51.12064005 Eh.

| State | Role | Log file | Electronic energy, Eh | Relative energy, kJ mol⁻¹ | Imaginary modes |
|---|---|---|---|---|---|
| W-PRC | Water adsorption complex | W-PRC-T1-V02.out | −36.44256091 | −69.59 | 0 |
| W-TS | Hydrolysis saddle | optts2_bandD_ci.out | −36.43140308 | −40.29 | 1 at −226.10 cm⁻¹ |
| W-P | Hydrolysis product | W-P-T1-V01.out | −36.44113826 | −65.85 | 0 |

Table 4.3: Stationary points on the steam route at the GFN2-xTB level. Reference zero: E(cluster) + E(H₂O) = −36.41605681 Eh.

### 4.3.3 The shape of the two profiles

Figure 4.2 plots both profiles on a common scale.

![Figure 4.2: The complete semi-empirical reaction profiles at the GFN2-xTB level, referred to the separated reactants in each case. Filled circles are the vanadium route and filled squares are the steam route.](figures/fig4_1_tier1_profile.png)

Four features of the plot matter.

The first is that both adsorbates bind to the acid site. Vanadic acid binds by 196.9 kJ mol⁻¹ relative to the separated species and water binds by 69.6 kJ mol⁻¹. At this level of theory the binding of vanadic acid is stronger by 127.3 kJ mol⁻¹. That value is much larger than the density functional value reported in Section 4.4, and the difference between them is one of the reasons the semi-empirical result is not used for the conclusion.

The second is that the vanadium route descends to a deep chemisorbed intermediate, V-I1, at 385.1 kJ mol⁻¹ below the separated reactants, a further 188.2 kJ mol⁻¹ below the adsorption complex. The steam route has no comparable well. Its only intermediate is the adsorption complex itself, and its product lies only 3.7 kJ mol⁻¹ below that complex.

The third is the barrier to the first aluminium oxygen cleavage on the vanadium route, which is the difference between V-TS2 and V-I1 and amounts to 160.70 kJ mol⁻¹. The corresponding barrier on the steam route is the difference between W-TS and W-PRC, which is 29.29 kJ mol⁻¹.

The fourth is that the two routes end at very different places. The vanadium product V-P lies 82.9 kJ mol⁻¹ below the separated reactants, so the overall extraction of aluminium by vanadic acid is exothermic at this level. The steam product W-P lies 65.85 kJ mol⁻¹ below the separated reactants, but only 3.7 kJ mol⁻¹ below the complex it formed from, so the hydrolysis step itself is close to thermoneutral.

### 4.3.4 Identity and validity of the saddle points

Two structures carried a single imaginary mode at the semi-empirical level and were examined as transition states.

The steam saddle, W-TS, has one imaginary mode at −226.10 cm⁻¹ and lies above both the complex it comes from, W-PRC, and the product it leads to, W-P, which satisfies the energy ordering criterion. Displacing the structure along the imaginary mode in both directions returned it to the W-PRC basin, at 1.35 and 1.34 kJ mol⁻¹ above the complex, which confirms that the saddle connects W-PRC to the product and does not lead anywhere else. On the internal criteria of this work the steam saddle is therefore accepted.

The vanadium saddle, V-TS2, has one imaginary mode at −78.21 cm⁻¹ and lies above both the intermediate it comes from, V-I1 at −385.10 kJ mol⁻¹, and the intermediate it leads to, V-I2 at −342.37 kJ mol⁻¹. The energy ordering criterion is satisfied. The two sided displacement test was not: displacing the structure along its imaginary mode in the positive direction moved the system to 107.08 kJ mol⁻¹ above V-I1, well outside the 5 kJ mol⁻¹ tolerance that the criterion requires. On the internal criteria of this work the saddle is therefore not fully established, and the barrier of 160.70 kJ mol⁻¹ is reported as a provisional estimate rather than a validated activation energy.

This is a genuine limitation and it is stated as such. It means that the first paragraph of any conclusion about kinetics on the vanadium route rests on a structure whose connection to the two states it is supposed to join was not proven at the level at which it was computed. The density functional attempt to settle the question is reported in Section 4.6.

### 4.3.5 Comparison of the two barriers and what it can and cannot mean

The vanadium barrier of 160.70 kJ mol⁻¹ is larger than the steam barrier of 29.29 kJ mol⁻¹ by a factor of five and a half. Read naively, this would suggest that steam is the faster attacking agent, which is the opposite of the industrial experience. That reading would be wrong, and it is worth explaining precisely why, because the point is central to the interpretation of this thesis.

The two numbers are not barriers to the same event. The steam barrier is the barrier to the first hydrolysis of an aluminium oxygen bond by a single water molecule, a process which the literature establishes needs three or four water molecules to complete and which involves only the rearrangement of a hydrogen bond and the insertion of an oxygen into the framework. The vanadium barrier is the barrier to the transformation of a physisorbed vanadic acid molecule into a chemisorbed intermediate in which the vanadium has bonded to a framework oxygen, a much larger structural change involving the coordination sphere of the vanadium atom. Comparing them is comparing the cost of opening a door with the cost of moving the wall that the door is set in.

What the comparison does establish is that the two adsorbates are not interchangeable. Vanadic acid and water reach different states, by different mechanisms, with different costs, and any argument that vanadium merely accelerates the steam reaction must explain how a species that binds three times more strongly and forms an intermediate 188 kJ mol⁻¹ deeper can nevertheless be a passive spectator.

## 4.4 Adsorption of Vanadic Acid and Steam at the Density Functional Level

### 4.4.1 The principal result

The most reliable result of this work is the comparison of the adsorption of vanadic acid and of water on the same Brønsted acid site, computed at the B3LYP-D3(BJ)/def2-TZVP level with full geometry optimisation and frequency verification for both complexes. Both complexes converged normally with zero imaginary modes, so both are genuine minima on the potential energy surface and the comparison between them is made on equal terms.

Table 4.4 gives the full thermodynamic comparison, and Figure 4.3 displays it.

| Quantity | Vanadic acid, H₃VO₄ | Steam, H₂O | Difference, vanadic acid minus steam |
|---|---|---|---|
| Electronic energy of adsorption, ΔE | −93.01 | −78.32 | −14.69 |
| ΔE corrected for zero point energy | −81.75 | −66.94 | −14.81 |
| Enthalpy of adsorption at 298.15 K | −95.48 | −80.80 | −14.69 |
| Gibbs energy of adsorption at 298.15 K | −17.05 | −28.87 | +11.82 |
| Gibbs energy of adsorption at 1003.15 K | +133.39 | +67.03 | +66.36 |

Table 4.4: Adsorption of vanadic acid and of water on the zeolite Y Brønsted acid site. All values in kJ mol⁻¹, computed at the B3LYP-D3(BJ)/def2-TZVP level from fully optimised and frequency verified geometries. The reference state is the separated cluster plus the free adsorbate, each at its own optimised geometry.

![Figure 4.3: Adsorption of vanadic acid and of steam on the zeolite Y Brønsted acid site. (a) the full thermodynamic series at the B3LYP-D3(BJ)/def2-TZVP level, (b) the comparison of the two density functionals for the electronic adsorption energy.](figures/fig4_2_adsorption.png)

The electronic adsorption energy of vanadic acid is −93.01 kJ mol⁻¹ and that of water is −78.32 kJ mol⁻¹. Vanadic acid binds more strongly by 14.69 kJ mol⁻¹. Correcting both for zero point energy changes the individual values to −81.75 and −66.94 kJ mol⁻¹ and leaves the difference essentially unchanged at 14.81 kJ mol⁻¹, which shows that the difference is a property of the electronic structure and not an artefact of vibrational averaging.

### 4.4.2 What the adsorption energies mean physically

Both adsorption energies are negative, so both adsorbates are held at the acid site by roughly 80 to 95 kJ mol⁻¹ of electronic energy. A binding energy in this range corresponds to a strong hydrogen bond or a weak dative bond rather than to a full chemical bond, which in the context of zeolite chemistry is the expected magnitude for a molecule sitting at a Brønsted acid site before any reaction has occurred. Neither adsorbate is merely condensed on the surface and neither is irreversibly bound at this step.

The geometries confirm this reading and reveal a feature that the energies alone would hide. In the optimised vanadic acid complex the aluminium atom has five contacts within 2.1 Å: four framework oxygen atoms at 1.705, 1.724, 1.743 and 2.052 Å, and one oxygen belonging to the vanadic acid at 1.925 Å. The presence of the 1.925 Å aluminium to vanadium-bound-oxygen distance means that the vanadic acid complex is not a pure hydrogen bonded precursor. The vanadium has already begun to coordinate to the aluminium through one of its oxygens, so the state described as an adsorption complex is better described as the first stage of chemisorption. This matters for the interpretation of the mechanism, because it means that the first aluminium oxygen bond is not simply approached by an intact molecule but is already being shared between the framework and the incoming vanadium before any bond is broken.

### 4.4.3 The result that contradicts the intuitive expectation

The Gibbs energy column of Table 4.4 carries a surprise. At 298.15 K the adsorption of water is more favourable than the adsorption of vanadic acid: −28.87 kJ mol⁻¹ against −17.05 kJ mol⁻¹, so the ordering is reversed with respect to the electronic energy. The reversal arises because the entropy penalty of bringing a molecule from the gas phase onto the surface is larger for the larger molecule, and the penalty is proportional to temperature.

Table 4.5 separates the enthalpy and the entropy contributions, which were extracted from the two computed Gibbs energies on the assumption that both the enthalpy and the entropy of adsorption are constant between 298 K and 1003 K.

| Route | Enthalpy of adsorption, kJ mol⁻¹ | Entropy of adsorption, J mol⁻¹ K⁻¹ | Entropy term at 1003 K, kJ mol⁻¹ |
|---|---|---|---|
| Vanadic acid | −80.7 | −213.4 | +214.1 |
| Steam | −69.4 | −136.0 | +136.5 |

Table 4.5: Enthalpy and entropy of adsorption extracted from the computed Gibbs energies at 298.15 K and 1003.15 K.

The result is unambiguous. Under the standard state convention used in the calculation, which treats the adsorbate as an ideal gas at one bar, the entropy loss on adsorption is 213 J mol⁻¹ K⁻¹ for vanadic acid against 136 J mol⁻¹ K⁻¹ for water, and at 1003 K the entropy term of 214 kJ mol⁻¹ overwhelms an enthalpy of only 81 kJ mol⁻¹, giving a positive Gibbs energy of adsorption. The calculated Gibbs energies of adsorption at 1003 K are therefore +133.4 and +67.0 kJ mol⁻¹ for vanadic acid and water respectively.

This finding must be interpreted with care, and two statements about it can be made without overreach. The first is technical. A positive Gibbs energy of adsorption at high temperature in this calculation is largely a consequence of the standard state convention, which places the adsorbate in the gas phase at one bar. Inside a working regenerator the adsorbate is not at one bar in the gas phase; it is a molecule that has diffused into a pore where its neighbours are other molecules and where its translational freedom is already restricted. The gas phase reference therefore overstates the entropy penalty of adsorption, and the positive values should not be read as a prediction that vanadic acid cannot adsorb on a working catalyst. The second statement is comparative and is the one that carries weight. The difference between the two routes at 298 K is only 11.8 kJ mol⁻¹ and it favours water, while the difference at 1003 K is 66.4 kJ mol⁻¹ and it favours water more strongly. Temperature does not amplify the advantage of vanadic acid; it erodes it.

The thermodynamic argument for vanadium as the attacking agent therefore cannot rest on the temperature dependence of adsorption. It must rest on the enthalpy of adsorption and on what happens after adsorption, which is what the next two sections examine.

![Figure 4.4: Gibbs energy of adsorption against temperature for vanadic acid and for water, from the two computed points at 298.15 K and 1003.15 K. The dashed line marks zero.](figures/fig4_3_gibbs_temperature.png)

## 4.5 Cross-Check with a Second Density Functional

A result computed with one density functional may be a property of the chemistry or a property of the functional. To separate the two, the electronic energies of the reference species and every available state were recomputed with the PBE0 functional using the same basis set, the same dispersion correction and the same relaxed geometries. Because only the electronic energy was recomputed, this is a test of the functional and not of the geometry.

Table 4.6 gives the comparison.

| Quantity | B3LYP-D3(BJ) | PBE0-D3(BJ) | Difference |
|---|---|---|---|
| Electronic adsorption energy of H₃VO₄, kJ mol⁻¹ | −93.01 | −93.07 | 0.06 |
| Electronic adsorption energy of H₂O, kJ mol⁻¹ | −78.32 | −78.62 | 0.30 |
| Advantage of vanadic acid over steam, kJ mol⁻¹ | 14.69 | 14.44 | 0.25 |

Table 4.6: Comparison of the two density functionals on identical geometries. Both functionals used the def2-TZVP basis set with D3 dispersion and Becke-Johnson damping.

The two functionals agree to within 0.3 kJ mol⁻¹ on the individual adsorption energies and to within 0.25 kJ mol⁻¹ on the difference between them. Agreement at this level between a functional containing empirical parameters and one containing none is a strong indication that the computed difference of about 14.5 kJ mol⁻¹ is a property of the chemical system rather than of the method used to describe it.

This is the single most important methodological result of the thesis. The absolute adsorption energies could still shift if the basis set were enlarged, if the cluster were enlarged, or if the counterpoise correction were applied, and each of those changes is a legitimate criticism of the present work. But a result that two independently parameterised functionals reproduce to within a quarter of a kilojoule per mole is unlikely to be an artefact, and it establishes the confidence with which the remaining results can be quoted.

## 4.6 Attempts at the Higher Steps of the Vanadium Route at the Density Functional Level

### 4.6.1 What was attempted

Following the semi-empirical profile, the density functional treatment was extended to the chemisorbed intermediate V-I1, the opened framework intermediate V-I2, the dealuminated product V-P, the steam product W-P, and the first aluminium oxygen cleavage saddle V-TS2. Each job was pre-registered with an acceptance gate before it was run, and the outcome of each is reported below regardless of whether it met the gate.

### 4.6.2 Results

Table 4.7 reports the electronic energies of every density functional structure, including the runs that did not converge.

| State | Log file | Optimisation cycles | Terminated normally | Converged | Imaginary modes | Electronic energy, Eh |
|---|---|---|---|---|---|---|
| Cluster reference | s1_03_cluster_optfreq.out | 1 after restart | yes | yes | one at −4.64 cm⁻¹ | −1709.39409388 |
| V-PRC | s1_04_vprc_optfreq.out | 40 | yes | yes | none | −2956.25453185 |
| V-I1 | s4_01_vi1_optfreq.out | 27 | yes | yes | none | −2956.26305203 |
| W-PRC | s1_05_wprc_optfreq.out | 63 | yes | yes | none | −1785.85055438 |
| W-P | s4_04_wp_optfreq.out | 75 | yes | yes | none | −1785.82987393 |
| V-I2, first pass | first_pass/s4_02_vi2_optfreq.out | 90 | yes | no | none | −2956.26562215 |
| V-I2, second pass | s4_02_vi2_optfreq.out | 60 | yes | no | none | −2956.26639173 |
| V-P, first pass | first_pass/s4_03_vp_optfreq.out | 90 | yes | no | none | −2956.05925722 |
| V-P, second pass | s4_03_vp_optfreq.out | 25 | no | no | none | −2956.05930432 |
| V-TS2 saddle | s4_05_vts2_optts.out | 200 | yes | no | fourteen | −2956.09584386 |

Table 4.7: Density functional stationary points at the B3LYP-D3(BJ)/def2-TZVP level, including those that did not meet the acceptance gate.

Four of the states met the full acceptance criteria: the cluster reference, V-PRC, V-I1 and W-P. Three did not.

The second intermediate V-I2 was optimised twice. The first attempt ran to the program's limit of ninety cycles and terminated normally without converging; the second attempt, started from a different displacement, ran sixty cycles and also failed to converge. Neither run produced a frequency analysis, so neither can be classified.

The dealuminated product V-P was also optimised twice. The first attempt ran ninety cycles and terminated normally without converging. The second attempt terminated abnormally after twenty five cycles. Neither produced a frequency analysis.

The saddle point attempt for the first aluminium oxygen cleavage was the most expensive single calculation performed in this work, running for one day and four hours and completing two hundred optimisation cycles without converging, and it returned fourteen imaginary modes. A structure with fourteen imaginary modes is a higher order saddle on a very flat region of the surface, not a first order transition state, and it is rejected outright. The same calculation performed at the semi-empirical level had returned a single imaginary mode, which shows how the shape of the surface changes between the two levels and is a reminder that a semi-empirical saddle point does not automatically translate into a density functional one.

### 4.6.3 What the converged part of the density functional ladder shows

The states that did converge still permit a partial ladder to be drawn, and it is reported in Table 4.8 and Figure 4.5.

| State | Relative to cluster + H₃VO₄, kJ mol⁻¹ | Status |
|---|---|---|
| V-PRC | −93.01 | Converged, frequency verified |
| V-I1 | −115.38 | Converged, frequency verified |
| V-I2 | −122.12 | Not converged, no frequency analysis |
| V-P | +419.69 | Not converged, no frequency analysis |
| V-TS2 | +323.63 | Rejected, fourteen imaginary modes |

Table 4.8: The density functional ladder for the vanadium route. Values for states that did not converge are arithmetic consequences of the computed electronic energies and are not established results.

![Figure 4.5: The level 2 ladder for the vanadium route. Dark columns are converged and frequency verified; light columns are states whose optimisation did not meet the acceptance criteria and whose energies are therefore brackets only.](figures/fig4_4_tier2_ladder.png)

Three observations follow.

First, the second step of the vanadium route is exothermic at the density functional level. The chemisorption of vanadic acid, V-PRC to V-I1, releases 22.37 kJ mol⁻¹. This is a modest stabilisation, not the deep trap that the semi-empirical calculation suggested, and it is reported here as a correction to the earlier estimate rather than as a confirmation of it. The physical interpretation is that vanadic acid, having adsorbed at the acid site, is able to draw a further 22 kJ mol⁻¹ of stabilisation by forming the additional aluminium oxygen contact seen in the geometry.

Second, the second chemisorption step, V-I1 to V-I2, releases only 6.75 kJ mol⁻¹ on the non-converged geometries. If that value survives a converged calculation it would mean that the opening of the framework by the first aluminium oxygen cleavage is close to thermoneutral, in which case the driving force for the second step would come from entropy and from the subsequent steps rather than from the step itself.

Third, and most importantly for the interpretation of this thesis, the aluminium extraction product computed at the density functional level lies far above the reactants. The value of +419.69 kJ mol⁻¹ belongs to a structure that did not converge and must not be quoted as a thermodynamic result. What can be said is weaker but still useful: the same comparison at the two different starting geometries, in two independent optimisations, gave values of +419.7 and +414.2 kJ mol⁻¹ respectively, so the qualitative conclusion is stable even though the number is not. The dealumination of the cluster model as computed here is strongly endothermic, and the density functional treatment does not reproduce the exothermic extraction that the semi-empirical calculation suggested.

### 4.6.4 Why the high energy product is not a numerical failure

It is tempting to dismiss the large positive energy of the product as evidence that the calculation is wrong. That reading would be a mistake, and the reason deserves explanation because it is central to the honest interpretation of this work.

The cluster model is a closed shell, neutral, hydrogen terminated fragment. When an aluminium atom is extracted from it and the framework bonds around the vacancy are closed, the product contains a new silanol group in place of a strong aluminium oxygen bond, and the extracted aluminium must be accommodated somewhere. In a real zeolite, four things stabilise the extracted aluminium species: the confinement of the cavity, which the cluster does not have; the surrounding water, which solvates the aluminium hydroxide; the subsequent repopulation of the vacancy by silicon, which the matrix supplies, and which the cluster cannot; and the entropy of distributing the extra framework species. The literature identifies all four of these as contributing to the driving force for dealumination, and the second and third in particular have been quantified by periodic calculations (Silaghi et al., 2016; Malola et al., 2012).

A gas phase cluster that lacks all four is therefore expected to give a much less favourable extraction energy than a periodic calculation, and that is exactly what the present work finds. The large positive value is a statement about the model and not about the chemistry. This is the principal limitation of this study and it is why the conclusion of Chapter Five rests on the adsorption comparison, which is a comparison between two adsorbates on an identical model, rather than on the extraction energies, which are comparisons between a model and a reality that the model does not reproduce.

### 4.6.5 The steam product at the density functional level

The steam product W-P did converge and pass its frequency analysis at the density functional level, and it is informative. Its energy relative to the separated reactants is −24.02 kJ mol⁻¹, while the water complex W-PRC lies at −78.32 kJ mol⁻¹. The hydrolysis step therefore costs 54.30 kJ mol⁻¹ on the cluster model, and the corresponding step at the PBE0 level costs 55.74 kJ mol⁻¹, so the two functionals agree that the steam hydrolysis of the cluster as modelled is uphill.

This appears at first to contradict the literature, which reports that the dealumination of zeolites by steam is a spontaneous process with a modest negative free energy of reaction over the complete sequence. The contradiction disappears when the same reasoning as in Section 4.6.4 is applied. The steam product computed here is a single hydrolysed aluminium oxygen bond in a gas phase cluster with no silanol nest, no fourth water molecule, no cavity confinement and no matrix silicon to heal the vacancy. The literature value of the overall free energy of reaction refers to the fully hydrolysed product Al(OH)₃(H₂O) after four water molecules and the healing of the vacancy. The present calculation stops after the first water molecule and therefore sits far uphill on a path whose later steps are downhill. The result is not a contradiction of the literature but a partial view along the same path.

## 4.7 Comparison with the Published Literature

### 4.7.1 Adsorption energies

The literature does not report a directly comparable water adsorption energy on a faujasite Brønsted acid site at the B3LYP-D3(BJ)/def2-TZVP level, so the comparison must be made against the range of values obtained from periodic calculations and from molecular dynamics. Silaghi et al. (2016) used Brønsted Evans Polanyi relationships linking the heat of water adsorption to the activation energy of hydrolysis and reported heats of adsorption of the order of tens of kilojoules per mole on faujasite. The present value of −93.01 kJ mol⁻¹ for water, or −81.75 kJ mol⁻¹ after zero point correction, is larger than those periodic values, which is the expected direction of the error for a finite cluster with hydrogen termination. The cluster has no lattice constraint resisting the deformation that adsorption causes, so the adsorbate is able to approach closer and to gain more energy than it would in the real framework.

The literature contains no comparable value for vanadic acid. No published calculation of the adsorption energy of H₃VO₄ on a zeolite Brønsted acid site was found in the course of this work, and the published DFT work on vanadium in zeolites concerns vanadium occupying framework positions (Tielens & Dzwigaj, 2010) rather than molecular vanadic acid arriving from the pore system. This is the gap that motivated the study, and the value of −93.01 kJ mol⁻¹, with a margin of 14.69 kJ mol⁻¹ over water, is offered as a first estimate against which later work can be compared.

### 4.7.2 Barriers

The steam barrier computed at the semi-empirical level in this work, 29.29 kJ mol⁻¹ relative to the adsorption complex, is much lower than the values reported in the literature. Malola et al. (2012) computed overall barriers for dealumination of chabazite of 190 to 260 kJ mol⁻¹ depending on whether the energy of water adsorption is counted, with the rate determining step being the inversion of a hydroxyl group. Silaghi et al. (2016) computed the energy barrier for hydrolysis of the first aluminium oxygen bond across mordenite, faujasite, MFI and chabazite, and found values that varied with framework type. Nielsen et al. (2019) reported intrinsic barriers near 100 kJ mol⁻¹ for the single water pathway from molecular dynamics, and lower values when additional water molecules participate.

The discrepancy between the present semi-empirical value and the literature is large, and it has two explanations, both of which are expected. The first is that the cluster model is small and unconstrained, which lowers barriers, as discussed in Section 4.2.3. The second is that GFN2-xTB systematically underestimates reaction barriers for bond rearrangement processes, which is a known feature of tight binding methods and is why they are used to generate structures rather than to report energies. The present work makes no claim that its semi-empirical barriers are accurate, and the steam barrier is quoted only for the purpose of comparing the two routes within the same method.

No published barrier exists for the vanadium route, so the provisional value of 160.70 kJ mol⁻¹ relative to V-I1 stands as an estimate only, and it is hedged by the failure of the two sided displacement test reported in Section 4.3.4.

### 4.7.3 Reaction energies

The literature value for the overall free energy of the acid catalysed dealumination of a zeolite, computed by periodic methods on the complete reaction, is of the order of a few tens of kilojoules per mole in the exothermic direction. The present work computes the fully extracted product of the vanadium route as strongly endothermic on the cluster model, and the first hydrolysis product of the steam route as 54.30 kJ mol⁻¹ endothermic relative to the water complex. Both of these differences from the literature arise from the same set of model deficiencies, discussed in Section 4.6.4, and the present results should not be read as a challenge to the published values. They define the boundary of what the model in this work can address.

## 4.8 What the Results Say about the Disputed Mechanism

The disagreement in the literature, set out in Section 2.6, is whether the entity that attacks the zeolite framework is vanadic acid derived from vanadium or hydroxide derived from sodium, and whether the bond broken is an aluminium oxygen bond or a silicon oxygen bond. The present calculations bear on the first half of that question directly and on the second half only indirectly.

### 4.8.1 The case for vanadic acid as an attacking agent

Three computed findings support the position that vanadic acid is capable of attacking the framework in its own right, without requiring sodium.

The first is the adsorption energy. Vanadic acid binds to the Brønsted acid site more strongly than water does, by 14.69 kJ mol⁻¹ at the B3LYP level and 14.44 kJ mol⁻¹ at the PBE0 level. The site therefore has a genuine thermodynamic preference for the vanadium-bearing species, and under conditions in which both are present the equilibrium coverage of the acid site favours vanadic acid.

The second is the geometry of the complex. The optimised structure shows the vanadic acid already forming a 1.925 Å contact between one of its oxygens and the framework aluminium, in addition to the four framework oxygen contacts. The incoming molecule is not hydrogen bonded to the proton in a purely non-reactive way; it has begun to share electron density with the aluminium. This is the structural precursor to the aluminium oxygen cleavage, and it appears at the first step.

The third is the chemisorption step. The conversion of the adsorption complex into the chemisorbed intermediate releases a further 22.37 kJ mol⁻¹ at the B3LYP level, and the resulting intermediate retains all four framework oxygen contacts to the aluminium, which means the framework is still intact but the adsorbate is now firmly attached and the aluminium environment has already changed. A species that can form such a structure with only 22 kJ mol⁻¹ of net stabilisation has removed the entropy penalty of adsorption and positioned itself for the bond breaking step.

Together these three findings support a reading in which vanadic acid is not a spectator. It is thermodynamically preferred at the site over water, it makes chemical contact with the aluminium at the first step, and it forms a stable intermediate that positions it for the cleavage. The industrial logic set out by Wormsbecher et al. (1986) and elaborated by Trujillo et al. (1997), in which a volatile vanadium-bearing acid migrates to the framework and attacks it, is consistent with everything computed here about the adsorption step.

### 4.8.2 The case that must be conceded to the opposing position

Two computed findings weaken the simple version of that argument, and they need to be stated.

The first is that the advantage of vanadic acid over water at the acid site is small in absolute terms. A difference of about 14.5 kJ mol⁻¹ in the electronic adsorption energy is roughly six times the thermal energy at 298 K, but it is well within the error bars that a cluster model and a finite basis set impose on an absolute binding energy. The counterpoise correction, which this work specified but did not obtain, would be expected to change both values by an amount of this order if the basis set incompleteness differs between the two adsorbates. It is a real effect, since two functionals agree on it to within 0.25 kJ mol⁻¹, but it is not a large effect.

The second is that the temperature dependence works against vanadic acid. The entropy penalty of adsorption is larger for the larger molecule, so much so that at 298 K water becomes the more favourable adsorbate once entropy is counted, and at 1003 K the gap widens to 66.4 kJ mol⁻¹. Any argument that vanadic acid outcompetes water for the site on thermodynamic grounds alone must address the fact that raising the temperature to the regenerator condition reverses the ordering found at the electronic level.

The honest position that follows is this. The present calculations demonstrate that vanadic acid is a chemically competent attacker of the faujasite framework and that it is preferred over water when only the electronic energy and the enthalpy are considered. They do not demonstrate that vanadium is the dominant destruction agent under operating conditions, and they cannot, because the model contains no sodium, no extra-framework aluminium, no rare earth cations and no pore confinement. Xu et al. (2002) confined their claim about vanadium having little effect to systems without sodium, and the present work is consistent with that narrow claim: it shows a modest, real but not overwhelming preference for vanadic acid at a site where no sodium is present.

### 4.8.3 The claim about the full mechanism

One claim that has circulated in earlier drafts of this work must be withdrawn on the evidence in this chapter. It is not correct to describe the present study as having validated the full mechanism of vanadium-promoted dealumination by density functional theory. Three of the five states on the vanadium route did not reach convergence at the density functional level, the saddle point for the first aluminium oxygen cleavage was rejected with fourteen imaginary modes, and the extraction product was computed as strongly endothermic on the model. What has been established by density functional theory in this work is the adsorption comparison and the second step of the vanadium route. The remainder of the route is established only at the semi-empirical level.

It is also necessary to place this work correctly against the published corpus, since the phrase first principle appears casually in the literature and can create a false impression of priority. The first complete first principles treatment of zeolite dealumination by steam was published by Malola et al. (2012), and the mechanism has since been established across four frameworks by Silaghi et al. (2016) and studied under realistic water loading by Nielsen et al. (2019). This work is not the first computational study of zeolite dealumination, and it is not the first computational study of vanadium in a zeolite, because Tielens and Dzwigaj (2010) computed the acid base properties of vanadium-containing zeolite sites by periodic DFT several years earlier. What appears to be new here, on the basis of the literature searches conducted for this thesis and subject to the possibility that relevant work was missed, is the comparison of a molecular vanadic acid attacking species against water on the same faujasite Brønsted acid site using identical methods at the density functional level, with the result stated as a binding energy margin. Priority claims of this kind should be made cautiously and can only be settled by a wider search.

## 4.9 Implications for the Design of Vanadium Traps

The practical purpose of quantifying the binding of vanadic acid on the zeolite is to give the designers of vanadium traps a number to beat.

The trap and the zeolite are in competition for the same mobile vanadium species. The trap wins if the free energy of vanadic acid bound to the trap is lower than the free energy of vanadic acid bound to the zeolite acid site. The present calculation gives the zeolite side of that competition as −81.75 kJ mol⁻¹ after zero point correction, and as −95.48 kJ mol⁻¹ for the enthalpy at 298 K.

The number has to be used with care for two reasons already discussed. The cluster model overestimates binding because it lacks lattice constraint, so the true value for a real faujasite framework is likely to be somewhat less negative. And the temperature dependence works in the trap's favour, because the entropy penalty of bringing the species out of the gas phase applies to the trap as much as to the zeolite, so the comparison at the electronic and enthalpy level is the meaningful one.

The experimental literature gives at least one confirmation that a trap with a sufficient affinity does exist. Etim et al. (2018) showed by X-ray diffraction that mobile vanadic acid reacts preferentially with yttrium oxide in a mixed magnesium yttrium oxide, forming crystalline yttrium vanadate, and that this preserves the framework. The formation of a crystalline ternary oxide implies a binding energy substantially larger than the 93 kJ mol⁻¹ computed here for the zeolite, which is consistent with the observation that the trap works. The present result therefore supplies the missing half of an argument that the experimental work had already made from the other end.

The design implication is specific. A candidate trap material should be screened first by computing the adsorption energy of H₃VO₄ on its surface at the same level of theory used here, and the material retained if that energy is more negative than about −95 kJ mol⁻¹. This converts the selection of a trap from a purely empirical screen into a computed screen followed by experimental confirmation.

## 4.10 Limitations of the Evidence Presented

The limitations already stated in Section 1.8 are restated here in the specific terms of the computed evidence, because a reader who has followed the chapter will now be able to judge their weight.

The most serious limitation is that the aluminium extraction step was not established at the density functional level, either for the vanadium route or for the steam route. The chapter reports the vanadium extraction as endothermic on the model and explains why that is a property of the model; but until a periodic calculation or a larger cluster is used, the thermodynamics of the extraction step remain open.

The second is the absence of the counterpoise correction. The comparison of two adsorbates is more robust to basis set superposition error than an absolute binding energy would be, because both complexes suffer the same deficiency, but the correction is not negligible at the level of a 14.5 kJ mol⁻¹ difference and the number should be treated as provisional for that reason.

The third is the size of the cluster. Four tetrahedral atoms is at the small end of what is used in the zeolite literature for reaction studies, and the faujasite supercage is much larger than the fragment used here. The confinement effect, which Silaghi et al. (2016) showed is itself a driving force for aluminium extraction, is entirely absent.

The fourth is that only one Brønsted acid site environment was modelled. Zeolite Y has acid sites in the supercage and in the sodalite cage, and the two differ in accessibility and in acid strength.

Fifth, the model contains no sodium, which is the species at the centre of the opposing mechanistic account. The present work cannot discriminate between the three positions reviewed in Section 2.6 on the basis of the sodium chemistry, because there is no sodium in the calculation.

Sixth, the temperature treatment assumes that the enthalpy and entropy of adsorption are constant between 298 K and 1003 K. Over a range of 705 K this assumption is an approximation, and while it is adequate for establishing the sign and rough magnitude of the temperature effect it is not adequate for precise free energies.

## 4.11 Summary of the Chapter

The density functional calculations produced one robust result and one partial ladder. The robust result is that vanadic acid binds more strongly than water to the Brønsted acid site of a faujasite cluster by 14.69 kJ mol⁻¹ at the B3LYP-D3(BJ)/def2-TZVP level and 14.44 kJ mol⁻¹ at the PBE0-D3(BJ)/def2-TZVP level, a margin of about 14.5 kJ mol⁻¹ that is reproduced by two independently parameterised functionals. The partial ladder shows that the chemisorption of vanadic acid releases a further 22.37 kJ mol⁻¹ and produces an intermediate in which the framework is still intact but the vanadium has made direct contact with the framework aluminium. The extraction of the aluminium and the saddle point for the first bond cleavage were not established at the density functional level and are reported as brackets only.

The semi-empirical calculations produced a complete profile for both routes. On that profile vanadic acid descends to a deep chemisorbed intermediate that water does not reach, the first aluminium oxygen cleavage on the vanadium route has a provisional barrier of 160.70 kJ mol⁻¹ against 29.29 kJ mol⁻¹ for the first hydrolysis on the steam route, and the two routes are not equivalent in mechanism at any point.

The comparison with the literature shows that the present steam adsorption energy is larger in magnitude than periodic values, as expected for a cluster model; that the present semi-empirical steam barrier is much smaller than the published values, as expected for a tight binding method on a small cluster; and that no published value exists for the vanadic acid adsorption energy against which to compare, which is the gap this work set out to fill.
