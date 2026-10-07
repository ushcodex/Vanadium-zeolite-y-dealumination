# CHAPTER FOUR

# RESULTS AND DISCUSSION

## 4.1 What the Calculations Actually Produced

The results are reported in the order in which they should be believed. Section 4.2 gives the quality gate that every structure had to pass, because several did not pass it and the chapter depends on the reader knowing which numbers are safe. Sections 4.3 to 4.6 report the adsorption result, which is the one finding that survives every test. Sections 4.7 to 4.10 report the rest of the pathway and say plainly what could not be established.

Table 4.1 lists every state that was carried into density functional theory, with the verdict of the acceptance rules from section 3.8.

[TBL: Table 4.1: Status of every state optimised at B3LYP D3(BJ)/def2 TZVP | State;Terminated;Converged;Imaginary modes;Energy (Eh);ΔE (kJ mol⁻¹);Verdict | Cluster reference;yes;yes;1, at 4.64 cm⁻¹;−1709.394094;n/a;accepted, flat minimum | H₃VO₄;yes;yes;0;−1246.825014;n/a;accepted | H₂O;yes;yes;0;−76.426630;n/a;accepted | V-PRC;yes;yes;0;−2956.254532;−93.0;accepted | V-I1;yes;yes;0;−2956.263052;−115.4;accepted | V-TS2;yes;no;14;−2956.095844;+323.6;rejected, not a saddle point | V-I2;yes;no, cycle limit;0;−2956.266392;−124.1;rejected, not a stationary point | V-P;no;no;not reached;−2956.059304;+419.6;rejected, job killed | W-PRC;yes;yes;0;−1785.850554;−78.3;accepted | W-P;yes;yes;0;−1785.829874;−24.0;accepted]

Five states are safe: the three reference species and the two pre reaction complexes, plus the chemisorbed intermediate V-I1 and the hydrolysed steam product W-P. Seven in total. Three states are not safe, for three different reasons, and the differences matter.

V-TS2 terminated normally but its optimisation did not converge, and its frequency calculation returned fourteen imaginary modes instead of exactly one. A structure with fourteen downhill directions is not the top of a single barrier; it is a point sitting on a ridge or in a basin rim, and no barrier can be read from it (see Figure 4.5). V-I2 terminated normally but used up its allowed optimisation cycles before the gradient fell to the convergence threshold, so its geometry is close to a minimum without being one. V-P did not terminate at all. The job was killed during a self consistent field cycle, and the energy listed for it is simply the last energy that happened to be written before the process died.

This is a smaller set of clean results than the study set out to produce, and it is reported as such. It is also enough to answer the question the study was designed to answer, because that question lives entirely in the adsorption step.

## 4.2 The Structures

The optimised reference species were shown in Figure 3.2. The two pre reaction complexes, which are the structures the whole comparison rests on, are shown in Figure 4.1.

[FIG: fig4_1_complexes.png | Figure 4.1: The two pre reaction complexes at B3LYP D3(BJ)/def2 TZVP. Left, V-PRC, vanadic acid on the acid site. Right, W-PRC, water on the acid site | Source: author, rendered from the optimised Cartesian coordinates]

Both adsorbates sit in the same place, hydrogen bonded to the Brønsted proton, and the difference between them is that vanadic acid brings three hydroxyl groups and a vanadyl oxygen to the site while water brings one oxygen and two hydrogens. Vanadic acid therefore has more to offer the framework: it can accept a hydrogen bond through its vanadyl oxygen and donate through any of its three hydroxyls. This is the structural reason the computed binding is stronger, and it is visible in Figure 4.1.

One qualification should be stated here because it will otherwise look like an omission later. The pre reaction complex is described as hydrogen bonded, and at the density functional level it is. In the Tier 1 geometry the same state already carried an aluminium to vanadyl oxygen contact of 0.193 nm, which is a bond and not a hydrogen bond. The density functional re optimisation relaxed this, but the reader should not imagine that the two states are separated by a clean, purely electrostatic step.

## 4.3 The Adsorption Result

Table 4.2 gives the adsorption energies of the two species at all three levels of theory, together with the difference between them. The difference is plotted in Figure 4.2.

[TBL: Table 4.2: Adsorption energy, ΔE, and the margin in favour of vanadic acid, at three levels of theory | Level of theory;H₃VO₄ (kJ mol⁻¹);H₂O (kJ mol⁻¹);ΔΔE, vanadic acid minus water (kJ mol⁻¹) | GFN2 xTB, Tier 1;−196.9;−69.6;−127.3 | B3LYP D3(BJ)/def2 TZVP;−93.0;−78.3;−14.7 | PBE0 D3(BJ)/def2 TZVP, single point;−93.1;−78.6;−14.4]

[FIG: fig4_2_adsorption.png | Figure 4.2: (a) Adsorption energy of vanadic acid and water at three levels of theory. (b) The margin by which vanadic acid outbinds water, against the thermal energy available at regenerator temperature | Source: author]

Three statements can be made about Table 4.2 with confidence.

First, vanadic acid does bind the site more strongly than water. The result holds at two independent density functionals, which differ by 0.1 kJ mol⁻¹ for vanadic acid and 0.3 kJ mol⁻¹ for water. That level of agreement is far better than the accuracy of either method, so the ranking is not an artefact of the functional.

Second, the margin is 14.7 kJ mol⁻¹ at B3LYP and 14.4 kJ mol⁻¹ at PBE0. As shown in section 3.9, this quantity can be written without the cluster reference energy at all, so it is immune to the one reference in the study that was imperfectly converged. It is the most defensible number in this thesis.

Third, the absolute binding energies are probably too large. No counterpoise correction was obtained, so both values carry an unquantified basis set superposition error. For a complex of this size the correction typically falls between 5 and 20 kJ mol⁻¹, which means the true binding energies are more likely to be near 75 to 88 kJ mol⁻¹ for vanadic acid and 60 to 73 kJ mol⁻¹ for water. The margin between them is affected much less, because the two complexes are of comparable size and the error largely cancels.

## 4.4 What 14.7 kJ mol⁻¹ Is Worth

A margin of 14.7 kJ mol⁻¹ sounds like a decisive preference. Under regenerator conditions it is not, and the arithmetic that shows this is the central result of the project.

At 1003 K the thermal energy kT is 8.34 kJ mol⁻¹. A free energy difference of 14.7 kJ mol⁻¹ therefore corresponds to a ratio of binding constants of

K_V / K_W = exp(14.7 / 8.34) ≈ 5.8

Vanadic acid holds a Brønsted site about six times more tightly than water does. Six times is not nothing, but it has to be set against how much more water there is. A regenerator at 2 atm with 20 per cent steam has a water partial pressure of 0.40 atm. Wormsbecher et al. (1986) put the vanadic acid concentration at 1 to 10 ppm; Trujillo et al. (1997) recalculated the equilibrium at 1.7 ppm and argued the bulk value must be below 1 ppm. Taking 10 ppm, which is the most generous figure in the literature, the partial pressure of vanadic acid is 2 × 10⁻⁵ atm. The ratio of partial pressures is therefore about 2 × 10⁴ in favour of water, and water is present at between four and five orders of magnitude the concentration of vanadic acid.

Figure 4.3 puts the two effects together in a two site Langmuir competition, using the computed binding constant ratio and taking the two species to compete for the same sites.

[FIG: fig4_3_competition.png | Figure 4.3: Estimated fraction of Brønsted sites held by vanadic acid under two site Langmuir competition at 1003 K, 20 volume per cent steam and 2 atm, using the binding constant ratio computed in this work | Source: author]

The estimate says that at 10 ppm of vanadic acid, about 0.03 per cent of the Brønsted sites are held by vanadic acid, roughly one site in three thousand four hundred. At Trujillo's 1.7 ppm it is about one site in twenty thousand. Water holds essentially all of the rest.

Three caveats attach to that number, and they are not small. The Langmuir picture assumes both species compete for one site and that neither dissociates, neither of which is strictly true. It uses a gas phase partial pressure for a species that Trujillo et al. (1997) argued concentrates locally inside the zeolite, and local concentration is precisely the escape route their hypothesis relies on. And it takes no account of the molten vanadium pentoxide phase, which is a liquid under regenerator conditions and can wet the catalyst directly. The calculation is not a proof. It is, however, a quantitative statement of the burden the vanadic acid hypothesis has to carry, and that burden is about four orders of magnitude. A hypothesis that needs a local concentration enhancement of 10⁴ to work has to explain where that enhancement comes from, and neither Wormsbecher et al. (1986) nor Trujillo et al. (1997) supplied a mechanism for it.

## 4.5 The Rest of the Vanadium Sequence

Beyond adsorption the sequence could not be completed, and the reasons are given here rather than left to the tables.

The chemisorbed intermediate V-I1 is a genuine minimum. It lies at −115.4 kJ mol⁻¹, about 22 kJ mol⁻¹ below the pre reaction complex, so the rearrangement in equation 3.3 is downhill. Its structure is informative: the aluminium retains all four of its framework oxygen contacts, and the vanadium sits about 0.27 nm away. No framework bond has broken at this stage. An earlier memo in the project described V-I1 as five coordinate aluminium; the coordinates do not support that description, and the corrected description is used here.

The next step is where the work stops. The candidate saddle point for the first framework aluminium oxygen hydrolysis, V-TS2, lies at +323.6 kJ mol⁻¹, which is why it appears high in Figure 4.4, but it is not a saddle point. Its fourteen imaginary modes are listed in Figure 4.5.

[FIG: fig4_4_energy_profile.png | Figure 4.4: Stationary points at B3LYP D3(BJ)/def2 TZVP relative to the separated reactants. Hollow markers and broken lines mark states that failed the acceptance tests | Source: author]

[FIG: fig4_5_imaginary.png | Figure 4.5: The fourteen imaginary frequencies returned for V-TS2. A true first order saddle point returns exactly one | Source: author]

The largest of those modes, at −566.6 cm⁻¹, is far too large to be the intended aluminium oxygen stretch, and the cluster of modes between −200 and −100 cm⁻¹ is characteristic of the capping hydrogens moving against the cluster rather than of framework chemistry. This is the frozen boundary showing up in the results, exactly as anticipated in section 3.10. Displacing along the modes and re optimising did not cleanly reach two distinct minima, so the two sided interval test was also failed.

Consequently no activation barrier is reported for any step of the vanadium route, and none should be inferred from Figure 4.4. The most that can be said from these numbers is that the region of the surface between V-I1 and V-I2 is high and flat, and that whatever path connects them does not run through the structure found here.

The same caution applies twice over further downstream. V-I2 did not converge, and V-P did not terminate. V-P, the state in which aluminium has been extracted from the framework, came out at +419.6 kJ mol⁻¹ relative to the separated reactants, which would make full extraction by a single vanadic acid molecule strongly endothermic. That number is reported for completeness and is then set aside, because it comes from a job that was killed. What can be said is that within this model, the sequence of steps mapped in equations 3.2 to 3.5 is not a downhill route to a dealuminated framework. That is consistent with Trujillo et al. (1997), who held that vanadium acts as a catalyst and is regenerated, rather than as a reagent that extracts aluminium stoichiometrically.

## 4.6 The Steam Control

The steam route behaved better than the vanadium route. Both W-PRC and W-P are converged minima with no imaginary frequencies. Water binds at −78.3 kJ mol⁻¹, and the hydrolysed product W-P lies at −24.0 kJ mol⁻¹, so the first hydrolysis of a framework aluminium oxygen bond costs about 54 kJ mol⁻¹ in electronic energy and stays below the separated reactants throughout.

This is a useful contrast with the vanadium route. On the steam side, the chemistry runs at energies that a thermal process at 1003 K can plausibly reach. On the vanadium side, the only clean statements are about adsorption, and everything past it either failed a test or sits at energies that the model cannot support. The steam baseline is also the only route in this study for which a barrier was obtained, and that barrier came from Tier 1 rather than from density functional theory: +29.3 kJ mol⁻¹ relative to W-PRC at GFN2 xTB, with one imaginary mode at −226 cm⁻¹.

## 4.7 Thermochemistry at Regenerator Temperature

Table 4.3 gives the Gibbs free energies of the accepted minima at the two temperatures, and Figure 4.6 shows the same values.

[TBL: Table 4.3: Gibbs free energy of the accepted minima relative to the separated reactants, at B3LYP D3(BJ)/def2 TZVP | State;ΔG at 298.15 K (kJ mol⁻¹);ΔG at 1003.15 K (kJ mol⁻¹) | V-PRC;−17.0;+133.4 | V-I1;−35.8;+108.3 | W-PRC;−28.9;+67.0 | W-P;+30.8;+132.7]

[FIG: fig4_6_gibbs.png | Figure 4.6: Gibbs free energy of the accepted minima at 298.15 K and 1003.15 K, relative to the separated reactants | Source: author]

At 298 K both adsorbates bind spontaneously and V-I1 is the most stable state in the study. At 1003 K every state is positive, which means that within this model nothing adsorbs at regenerator temperature at all.

That result should not be taken at face value, and the reason is worth stating carefully because it is the clearest limitation of the whole approach. The entropy penalty in equation 3.11 is the entropy of a gas molecule losing translational freedom, which is what happens when a gas phase molecule in an ideal gas model is pinned to a surface. In a real regenerator the water is already condensed in the pores, the zeolite does not lose much entropy on adsorption, and the relevant reference state is a physisorbed molecule rather than a free gas molecule. Silaghi et al. (2016) made exactly this point and recommended taking the physisorbed state as the reference for this reason. The gas phase harmonic treatment used here overstates the entropic penalty by a wide margin at 1003 K.

There is also a specific numerical caution. At 1003 K the harmonic oscillator approximation is stretched, low frequency modes dominate the entropy, and the low frequency modes in this cluster are partly artefacts of the frozen boundary. The ΔG values at 1003 K are therefore reported as an indication of direction and magnitude, not as numbers to be quoted to a decimal place. Their value is comparative: the ordering of the states at 1003 K is the same as at 298 K, and the gap between the two routes changes by only a few kilojoules per mole, so the conclusions drawn in section 4.4 from the electronic energies are not overturned by the thermochemistry.

## 4.8 What the Screening Method Got Wrong

The Tier 1 and Tier 2 results disagree, and the disagreement is instructive enough to be worth a figure. Figure 4.7 compares the margin between the two adsorbates at the two levels.

[FIG: fig4_7_method_gap.png | Figure 4.7: The margin between the two adsorbates as computed by the semi empirical screen and by density functional theory | Source: author]

GFN2 xTB put the margin at 127.3 kJ mol⁻¹, and density functional theory puts it at 14.7 kJ mol⁻¹. The cheap method overstated the difference between the two adsorbates by a factor of about nine. It was not wrong about the direction, and it was useful for geometry, but it was badly wrong about the size of the effect.

This has a practical consequence that is worth stating for anyone repeating this kind of work. A semi empirical screen is a way to find structures, not a way to measure energies. Had the Tier 1 numbers been reported as results, the conclusion would have been that vanadic acid outbinds water by more than 100 kJ mol⁻¹, which at 1003 K is a binding constant ratio of about 4 × 10⁶, and which would have overwhelmed the concentration disadvantage and appeared to confirm the vanadic acid hypothesis decisively. The confirmation would have been an artefact.

The Tier 1 barriers carry the same warning. The +160.7 kJ mol⁻¹ barrier obtained for the V-TS2 step at GFN2 xTB, and the +29.3 kJ mol⁻¹ barrier for the steam step, are values from a method that this section has just shown to be unreliable for energetics on this system. They are recorded because they were computed and because they guided the search, but no conclusion in this thesis rests on them.

## 4.9 Where This Leaves the Dispute

The dispute set out in section 2.6 can now be addressed directly, and the answer is not the one the project expected when it started.

The vanadic acid hypothesis requires that vanadic acid, at a few parts per million, wins the Brønsted acid site from steam at 20 per cent. This study measures the preference at 14.7 kJ mol⁻¹, which is a binding constant ratio of about 5.8 at regenerator temperature. Against a concentration disadvantage of four to five orders of magnitude, that preference is between three and four orders of magnitude too small. On the evidence of the adsorption step alone, the hypothesis as usually stated does not survive.

That conclusion has to be hedged in one specific way, and the hedge is the interesting part. Trujillo et al. (1997) anticipated the concentration problem and answered it with local concentration: vanadic acid accumulates inside the zeolite at levels far above its bulk gas concentration, because it is continuously generated there from vanadium pentoxide held at the acid site, as in equations 2.4 and 2.5. Nothing in this study tests that. A cluster with one acid site in the gas phase cannot say anything about accumulation in a pore. What this study does is put a number on how much accumulation would be needed, which is a factor of about 10⁴ over bulk. If that much accumulation happens, the hypothesis works; if it does not, it does not. The question is now sharp enough to be worth an experiment or a periodic calculation with an explicit pore.

The result does support the critics, though with a caveat of its own. Pine (1990) found that the activation energy of destruction is the same with and without vanadium, and concluded that the rate determining step does not involve vanadium. Xu et al. (2002) concluded that vanadium does not open a new pathway but merely releases sodium. Both positions are consistent with a small, real, but kinetically irrelevant binding preference for vanadic acid: vanadium does bind the site better than water does, so it is not a pure spectator, but the preference is nowhere near large enough to make it the agent that decides the rate. The finding therefore sits closer to Xu et al. (2002) and Pine (1990) than to Wormsbecher et al. (1986), while conceding to Trujillo et al. (1997) that vanadium is not chemically inert at the site.

Two further observations belong here. The absence of any validated barrier means this study provides no support for a catalytic rate enhancement by vanadium, and the positive ΔG values at 1003 K mean the model cannot represent the real driving force at regenerator temperature at all. Anyone quoting this thesis should quote the adsorption margin and the concentration argument, not the thermochemistry.

## 4.10 Implications for Practice

Two practical points follow, and both are modest.

The first concerns vanadium traps. Traps are chosen by screening because no one knows what binding strength they must beat. This study gives the number the zeolite sets: about 93 kJ mol⁻¹ uncorrected for vanadic acid at a Brønsted site, and probably nearer 75 to 88 kJ mol⁻¹ once basis set superposition error is removed. A trap that must protect the zeolite needs to bind vanadic acid more strongly than that, and it needs to do so at 1003 K in 20 per cent steam. That is a specification, and it is testable computationally before any trap is synthesised.

The second concerns where to look next. Because the adsorption step does not explain vanadium's effect, effort is better spent on the routes that do not depend on it: the sodium route of Xu et al. (2002), which this model cannot address because it contains no sodium, and the local concentration question raised by Trujillo et al. (1997). Both are natural extensions of the present work and both are described in section 5.4.
