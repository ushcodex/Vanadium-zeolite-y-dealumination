# CHAPTER TWO

# LITERATURE REVIEW

## 2.1 Arrangement of This Chapter

The review is arranged as a funnel. It begins with the refinery process that creates the problem, narrows to the catalyst, then to the chemistry of the framework bond that breaks, then to the three competing explanations for why vanadium makes it break faster, and finishes with the computational tools that let the question be tested and with the specific gap this project fills. Every source is used once, for the point it establishes best.

## 2.2 The Refinery Context: Why Residue Is Cracked at All

A refinery makes money on the spread between the crude it buys and the products it sells, so it has a standing incentive to buy cheaper, heavier crude. Heavier crude means more atmospheric and vacuum residue, and residue is where the contaminants live. Residue fluid catalytic cracking exists to convert that residue. The trade is explicit: cheaper feed in exchange for higher catalyst consumption, more coke, more hydrogen, and faster permanent deactivation (Adanenche et al., 2023).

The contaminants arrive as heteroatoms and metals. Sulfur and nitrogen raise emissions and poison acid sites; nickel promotes dehydrogenation; sodium neutralises acid sites and, as will be seen, does structural damage of its own; vanadium attacks the zeolite. Adanenche et al. (2023) reviewed the mitigation of these poisons and concluded that antimony, bismuth, boron, magnesium, tin and the rare earths have all been pressed into service as traps or passivators, and that the central design target is a catalyst with better metal tolerance that still cracks well. That target cannot be reached by trial alone, because the poisons act at a scale no refinery instrument observes.

## 2.3 The Catalyst: Zeolite Y and the Acid Site

A cracking catalyst particle is a composite. Zeolite Y crystals are dispersed in an active or inert matrix and held together with a binder, and the whole is spray dried into a microsphere that can circulate. The zeolite is the rate controlling constituent, and its unit cell size, measured by X ray diffraction, is used throughout the industry as a working measure of how much framework aluminium survives (Xu, Liu, & Madon, 2002).

Zeolite Y has the faujasite topology. Its structure, built from silica and alumina tetrahedra sharing oxygen atoms, is shown in Figure 2.1, and the same framework drawn as an atomistic model with and without framework aluminium is shown in Figure 2.2. Two cavities matter: the sodalite cage and the larger supercage, which is entered through a twelve membered oxygen ring about 0.74 nm across and is where most of the cracking happens.

[FIG: from_sources/etim2016_fig1_y_zeolite.png | Figure 2.1: Structure of Y-zeolite showing the average micropore width in the supercage formed by the twelve membered ring | Source: Etim, Xu, Ullah and Yan (2016), Figure 1]

[FIG: from_sources/etim2016_fig12_fau_model.png | Figure 2.2: Three dimensional atomistic model of the faujasite structure, (a) with full framework aluminium atoms and (b) with partial framework aluminium atoms | Source: Etim, Xu, Ullah and Yan (2016), Figure 12]

Substituting a trivalent aluminium for a tetravalent silicon leaves the framework one negative charge short. A proton on a nearby bridging oxygen restores neutrality and creates the Brønsted acid site, written here as Al(OH)Si. That proton is the whole point of the catalyst: it is what a hydrocarbon molecule takes when it cracks. It follows that any chemistry which removes aluminium from the framework, or which covers that proton, removes activity, and that the number of acid sites and the number of framework aluminium atoms are the same number.

## 2.4 How the Framework Breaks: Steam Dealumination

The catalyst circulates continuously between a riser, where it cracks feed and collects coke, and a regenerator, where air burns the coke off. Burning hydrocarbon coke produces water, and the stripping steam adds more, so a regenerator atmosphere is typically about 20 per cent steam at roughly 730 °C and 2 atm. Steam attacks the framework whether or not any metal is present.

The attack is a hydrolysis. Each of the four aluminium oxygen bonds is broken in turn by a water molecule, and the pieces are capped: the oxygen left behind on the silicon becomes a silanol, and the hydroxyl goes to the aluminium. Writing the intact framework site as Al(OSi)₄H, where H is the single Brønsted proton, the sequence ends as

Al(OSi)₄H + 3 H₂O ⇌ Al(OH)₃ + 4 ≡Si–OH
(2.1)

Al(OH)₃ + H₂O ⇌ Al(OH)₃(H₂O)
(2.2)

Equation 2.1 is the dealumination step proper. It costs one Brønsted acid site and leaves behind the four silanol groups known as a silanol nest. Equation 2.2 hydrates the detached aluminium hydroxide into the extra framework species that then sits in the pores.

The first computation of this whole sequence came from Malola et al. (2012), who ran periodic density functional theory with the PBE functional on chabazite and traced the path with the nudged elastic band method. They reported that at least three water molecules are needed to detach aluminium as Al(OH)₃, that a fourth water gives the more stable Al(OH)₃(H₂O), and that the effective barrier is 190 kJ mol⁻¹ when each incoming water is counted from the gas phase and 260 kJ mol⁻¹ when it is counted from an adsorbed state. Desilication costs 40 to 50 kJ mol⁻¹ more, so aluminium is the easier atom to remove, which is the experimental observation. The rate determining step is not a hydrolysis at all but the inversion of a hydroxyl group.

The computed reaction paths are reproduced as Figure 2.3, and the individual reaction steps as Figure 2.4. Together they show why the mechanism is described as a sequence: each step is a hydrolysis in which a water molecule is consumed, an aluminium oxygen bond is replaced by a hydroxyl on the silicon and a hydroxyl on the aluminium, and the aluminium is progressively loosened until it leaves.

[FIG: from_sources/malola2012_fig2_paths.png | Figure 2.3: Reaction paths for (a) dealumination and (b) desilication, combined from five nudged elastic band paths. Black lines, approach A, counting each incoming water from the gas phase; purple lines, approach B, counting it from an adsorbed state. The effective barriers for both approaches are labelled | Source: Malola, Svelle, Lønstad Bleken and Swang (2012), Figure 2]

[FIG: from_sources/malola2012_fig3_steps.png | Figure 2.4: Reaction steps with the intermediate configurations for dealumination, left, and for desilication, right. c denotes a covalent bond and g a hydrogen bond | Source: Malola, Svelle, Lønstad Bleken and Swang (2012), Figure 3]

Silaghi, Chizallet, Sauer, and Raybaud (2016) extended this to four frameworks including faujasite, using periodic density functional theory with dispersion corrections and free energy estimates. They found a broadly common mechanism: water adsorbs on the aluminium atom in the position anti to the Brønsted proton, then the aluminium oxygen bonds hydrolyse one after another until the aluminium is dislodged as Al(OH)₃(H₂O), and they were able to fit Brønsted Evans Polanyi relationships across the whole path.

Two things follow for the present work. First, steam dealumination is a well understood, quantified baseline, with a barrier in the region of 190 to 260 kJ mol⁻¹. Second, the mechanism is stepwise hydrolysis of aluminium oxygen bonds by water molecules that adsorb on the aluminium itself. Any claim that vanadic acid accelerates this must explain how an acid, arriving with far fewer molecules, competes with that.

## 2.5 Vanadium: From Porphyrin to Volatile Acid

Vanadium enters the unit inside porphyrin and porphyrin like complexes in the residue. Mitchell (1980) showed that these molecules are too large to enter the zeolite pores, so the metal is deposited on the outside of the catalyst particle together with the coke, and that synthetic deposition reproduces the effects seen on equilibrium catalyst. Once in the regenerator the organic ligands burn away and the vanadium oxidises. Under regenerator conditions vanadium pentoxide is molten, with a melting point near 690 °C, and this mobility is part of how it spreads.

Wormsbecher et al. (1986) identified the mobile species as volatile vanadic acid, produced by

V₂O₅ + 3 H₂O(g) ⇌ 2 H₃VO₄(g)
(2.3)

and estimated its regenerator concentration at 1 to 10 ppm for 730 °C, 20 per cent steam and 2 atm total pressure. Because vanadic acid is a strong acid comparable with phosphoric acid, they argued it hydrolyses the silica alumina framework, and on the strength of that reasoning they proposed and demonstrated basic alkaline earth oxides, especially magnesia, as scavengers.

Trujillo et al. (1997) tested the vanadium speciation directly with electron spin resonance and diffuse reflectance spectroscopy on two USY zeolites. Their results refine the picture in three ways. Vanadium deposited on the external surface migrates inward, and water assists but is not essential for that migration. Under the strongly reducing conditions of the riser, vanadium cannot persist as V(V), so the damage must occur in the regenerator and not during stripping. Most importantly, V(IV) does not carry the destruction. A zeolite exchanged so that its vanadium sat at the acid sites was steamed in a reducing atmosphere of steam with carbon monoxide in nitrogen and lost no more structure than a vanadium free sample steamed the same way, whereas the same material steamed in steam and air collapsed completely. Trujillo et al. (1997) called this a real proof that vanadium must be present as V(V) to catalyse the destruction. Figure 2.5 shows why the two regimes differ: the fraction of the total vanadium present as V(IV) falls away as the calcination temperature rises, so the destructive oxidising regime is also the regime in which V(V) dominates.

[FIG: from_sources/trujillo1997_fig3_viv.png | Figure 2.5: Percentage of the total vanadium present as V(IV) as a function of calcination temperature for impregnated zeolites | Source: Trujillo et al. (1997), Figure 3]

Trujillo et al. (1997) also reported that extra framework aluminium competes with the zeolite for vanadium and delays its arrival at the acid sites, which is one reason a zeolite that already contains extra framework aluminium survives longer. Instead, they proposed the two step sequence

V₂O₅ + 2 H⁺–Y ⇌ 2 VO₂⁺–Y + H₂O
(2.4)

VO₂⁺–Y + 2 H₂O ⇌ H⁺–Y + H₃VO₄
(2.5)

in which vanadium(V) is first trapped at the acid site as a cationic species, poisoning the site reversibly, and is then mobilised again by steam as vanadic acid. They offered this as an explanation of how a small amount of vanadium can do large damage, and they noted that vanadic acid has a pK of 0.05, so it is genuinely a strong acid.

They also raised the objection that has never been fully answered. A typical feed carries about 1 per cent sulfur, of which 5 to 10 per cent reaches the regenerator in the coke and is oxidised, giving a minimum sulfur trioxide or sulfuric acid concentration near 60 ppm. Sulfuric acid is stronger than vanadic acid and at least an order of magnitude more abundant. If acid catalysed hydrolysis of framework aluminium were the mechanism, the sulfur acid should dominate, and it does not destroy zeolite. Trujillo et al. (1997) answered their own objection by proposing that vanadic acid reaches a much higher local concentration inside the zeolite than in the bulk gas, and by recomputing the bulk equilibrium at 1.7 ppm, arguing that the true bulk value must be below 1 ppm, since otherwise all the vanadium would leave with the flue gas instead of accumulating on the catalyst.

## 2.6 The Dispute: Three Explanations, and What Each Has to Explain

The literature has settled on three accounts of vanadium induced destruction. They are set out side by side in Figure 2.6, together with the source that states each one most clearly.

[FIG: fig2_1_dispute.png | Figure 2.6: The three competing explanations for vanadium induced destruction of zeolite Y, and the question this project tests | Source: compiled by the author from Malola et al. (2012), Silaghi et al. (2016), Wormsbecher et al. (1986), Trujillo et al. (1997), Pine (1990) and Xu et al. (2002)]

The first account is that steam alone does it and vanadium is a spectator or a minor accelerant. This is the position implied by the computational work of Malola et al. (2012) and Silaghi et al. (2016), which obtains a full dealumination mechanism without any metal at all, and it is supported by the fact that zeolite Y is deliberately steamed during manufacture.

The second account is the vanadic acid hypothesis of Wormsbecher et al. (1986) as refined by Trujillo et al. (1997): volatile H₃VO₄ is a strong acid that catalyses the hydrolysis of framework aluminium and is regenerated rather than consumed, which is how a little vanadium destroys a lot of zeolite. This is the most widely quoted mechanism and the one assumed in most reviews of metal passivation, including the recent one by Adanenche et al. (2023).


Trujillo et al. (1997) also set out how the hydrolysis itself proceeds, in Figure 2.7, which places Kerr's scheme for dealumination above a more detailed picture in which the hydronium ion attacks the negatively charged oxygen of the acid site and a water molecule is inserted into the structure. On this picture, the reason a sodium counter ion accelerates the loss is that it raises the negative charge density on that oxygen, so the attack is faster.

[FIG: from_sources/trujillo1997_scheme.png | Figure 2.7: Kerr's scheme for zeolite dealumination, above, together with the electrophilic attack of the hydronium ion on the negatively charged oxygen of the acid site, below | Source: Trujillo et al. (1997), page 14]

The third account denies that vanadium opens a new pathway. Pine (1990) measured the kinetics of USY destruction between 740 and 800 °C at 1 atm of steam with 0 to 4000 ppm of vanadium. He found first order kinetics with no induction period, an activation energy of 79.0 kcal mol⁻¹ (about 331 kJ mol⁻¹), and rate constants directly proportional to vanadium loading. Because the data taken with vanadium extrapolate cleanly to the data taken without it, he concluded that the reaction under study is ordinary steam destruction and that vanadium and sodium are both catalysts of that same reaction, nearly equal in activity and synergistic. Two of his observations are hard to reconcile with the vanadic acid hypothesis. Vanadium attacks silicalite, a zeolite that is essentially aluminium free, so the attack cannot be confined to aluminium sites. And the activation energy is the same whether vanadium is present or not, which means the kinetically significant step does not involve vanadium.

Xu et al. (2002) took the third account further and gave it a mechanism. Working with USY of high and low unit cell size and with two commercial catalysts, they showed that the effect of vanadium depends almost entirely on how much exchangeable sodium is present. Cutting sodium oxide from 1.19 to 0.03 weight per cent on the zeolite reduced the vanadium effect by a factor of about five, and a catalyst whose sodium was locked up in an amorphous matrix was barely affected by 4200 ppm of vanadium at all. They then tested model compounds on a highly siliceous USY that is stable to steam, with the result shown in Figure 2.8. Sodium metavanadate destroys the zeolite only when steam is present; ammonium metavanadate, which gives metavanadic acid but no sodium, destroys very little even at 8000 ppm of vanadium; and sodium nitrate, which gives sodium but no vanadium, destroys a great deal once steam is available. From this they argued that metavanadic acid acts as a catalyst that strips sodium off its exchange site, and that the sodium hydroxide so formed does the damage:

HVO₃ + Na⁺–Y ⇌ NaVO₃ + H⁺–Y
(2.6)

NaVO₃ + H₂O ⇌ HVO₃ + NaOH
(2.7)

NaOH ⇌ Naᵟ⁺OHᵟ⁻ (in steam)
(2.8)

followed by attack of the polarised hydroxide on a framework silicon oxygen bond. Their full scheme is reproduced as Figure 2.9. On this reading, vanadium matters because it makes sodium available, the destructive agent is the same with or without vanadium, and the activation energy is therefore unchanged, exactly as Pine (1990) observed. They also addressed the sulfur puzzle that had troubled Trujillo et al. (1997): sulfur oxides cannot do what vanadium does, because only vanadium forms a mobile acid that can pull a cation off an exchange site and then release it again.

[FIG: from_sources/xu2002_fig6_na_v.png | Figure 2.8: Retention of zeolite surface area after thermal and hydrothermal treatment of a highly siliceous USY carrying ammonium metavanadate, sodium nitrate and sodium metavanadate | Source: Xu, Liu and Madon (2002), Figure 6]

[FIG: from_sources/xu2002_fig8_pathways.png | Figure 2.9: Pathways to zeolite Y destruction as proposed by Xu, Liu and Madon, in which steam hydrolysis of framework aluminium and attack by sodium hydroxide are the only two destructive routes and vanadium acts only to release sodium | Source: Xu, Liu and Madon (2002), Figure 8]


Trujillo et al. (1997) themselves conceded the weakness in their own account. They wrote that an acid hydrolysis mechanism does not explain why two chemically different species, sodium and vanadium, produce similar effects and act synergistically, and they sketched an electrophilic attack by the hydronium ion on the negatively charged framework oxygen, arguing that a sodium counter ion raises the negative charge density on that oxygen and therefore speeds the hydrolysis. This is an admission that the vanadic acid hypothesis, as stated, is incomplete rather than a demonstration that it is wrong.


What separates the accounts is therefore a single measurable quantity. If vanadic acid is to be the destructive agent, it must win the acid site against steam, which is present at a partial pressure roughly 10⁴ to 10⁵ times larger. Steam does not have to be chemically superior to win; it only has to be numerous. The sodium route requires no such win, because it does not rely on vanadic acid holding the site at all. This project computes the missing number.

## 2.7 What the Damage Looks Like

Whatever the route, the result is visible. Etim, Xu, Ullah, and Yan (2016) contaminated ultra stable Y zeolite with 0.3 and 0.5 weight per cent vanadium, steamed it, and characterised it with X ray diffraction, nitrogen adsorption, transmission electron microscopy and solid state nuclear magnetic resonance. In the presence of steam, vanadium produced excessive evolution of non intercrystalline mesopores averaging about 25.0 nm at 0.5 weight per cent vanadium, far larger than the mesopores in hydrothermally optimised FCC zeolites, together with about 80 per cent loss of BET surface area. The micrographs in Figure 2.10 show the corresponding destruction of the crystal. Their vanadate immobilisation experiments also showed that vanadium is mobile under reaction conditions, and that a passivator which immobilises it limits both its mobility and its acidity, which is why crystallinity survives.

[FIG: from_sources/etim2016_fig8_tem.png | Figure 2.10: Transmission electron micrographs of ultra stable Y zeolite before and after vanadium contamination and steaming | Source: Etim, Xu, Ullah and Yan (2016), Figure 8]

## 2.8 Holding the Poison Back

Because vanadium cannot be removed from the feed economically, it is managed on the catalyst. The principle was established by Wormsbecher et al. (1986), who argued on acid base grounds that a basic solid with a suitable pore structure should out compete the zeolite for vanadic acid, and showed that 20 per cent magnesia blended into the catalyst preserved activity at vanadium loadings of 0.67 and 1.34 weight per cent. They also identified the complication that regenerator sulfur dioxide can sulfate the oxide and compete with vanadate formation.

Progress since then has been in the choice of trap. Etim, Bai, Ullah, Subhan, and Yan (2018) prepared a mixed magnesium yttrium oxide and showed by X ray diffraction that vanadium is preferentially captured as crystalline yttrium vanadate, YVO₄, and that the protection follows the amount of trap added (Figure 2.11). Their passivation mechanism is again acid base chemistry: mobile vanadic acid meets a more basic oxide, forms an immobile vanadate, and so never reaches the zeolite. Faghani, Mohammadipour, Tarighi, Naderifar, and Habibzadeh (2024) took the same idea to barium titanate and reported that 10 weight per cent of it preserved 18.7 per cent more crystalline structure and 12 per cent more surface retention at 6000 ppm of vanadium. Adanenche et al. (2023) surveyed the field and concluded that alkaline earths, rare earths, tin, boron, antimony and bismuth are all in use, and that the persistent problem with alkaline earths is that they also form silicates and lose capacity.

[FIG: from_sources/etim2018_fig8_surface_area.png | Figure 2.11: Effect of a magnesium yttrium oxide passivator on the surface areas of vanadium contaminated catalyst | Source: Etim, Bai, Ullah, Subhan and Yan (2018), Figure 8]

The engineering question behind all of this is quantitative and still open. A trap has to bind vanadic acid more strongly than the zeolite does. Nobody knows how strongly the zeolite binds it, so trap selection proceeds by screening. The number this project computes is exactly the number a trap has to beat.

## 2.9 Computational Chemistry as a Way In

The reason the dispute has lasted forty years is that the decisive events are small, fast and buried inside a hot, opaque solid. Quantum chemistry offers a way to compute the energies of species that cannot be isolated.

Density functional theory obtains the ground state energy and electron distribution of a system from its electron density rather than from a many electron wavefunction, which makes it affordable for systems of tens to hundreds of atoms. In practice a calculation is specified by a functional, which approximates the exchange and correlation energy, and a basis set, which is the set of functions used to represent the orbitals. This work uses two hybrid functionals, B3LYP (Becke, 1993; Lee, Yang, & Parr, 1988) and PBE0 (Adamo & Barone, 1999), with the def2 TZVP basis set of Weigend and Ahlrichs (2005), and adds Grimme's D3 dispersion correction with Becke Johnson damping (Grimme, Ehrlich, & Goerigk, 2011) because plain functionals describe weak long range attraction poorly, and adsorption is dominated by it. Doing the work twice with two different functionals is a cheap way to find out whether a conclusion belongs to the chemistry or to the approximation.

The alternative for screening is a semi empirical method, in which parts of the quantum mechanical problem are replaced by parameters fitted to reference data. GFN2 xTB, the method used in the first tier here, is a self consistent tight binding scheme with multipole electrostatics and density dependent dispersion, parametrised across the periodic table to Z = 86 (Bannwarth, Ehlert, & Grimme, 2019). It is orders of magnitude cheaper than density functional theory and is designed to give good geometries and reasonable non covalent interactions, which makes it well suited to searching a potential energy surface for candidate structures that are then refined properly. All calculations in this project were run with the ORCA package (Neese, 2025).

Computational work on zeolites is mature. Dealumination has been mapped as described in section 2.4. Vanadium in zeolites has also been studied, though for a different purpose: Tielens and Dzwigaj (2010) used periodic density functional theory with pyridine adsorption infrared spectroscopy to characterise the acid base character of framework vanadium sites, and showed that the V–OH groups of framework V(V) and V(IV) are more acidic than the Si–OH groups of a siliceous zeolite (Figure 2.12). That is vanadium as a deliberate catalytic centre, not vanadium as a poison, but it establishes that vanadium in a zeolite framework is computationally tractable and that its acidity can be quantified.

[FIG: from_sources/tielens2010_fig2_v_sites.png | Figure 2.12: Framework vanadium sites in a sodalite model, showing protonation of sites A and B in the V(V) state | Source: Tielens and Dzwigaj (2010), Figure 2]

The same approach is established in this department. Uzochukwu et al. (2023) modelled the formation of a choline chloride and glycerol deep eutectic solvent with semi empirical, Hartree Fock and density functional methods on a mobile workstation, computed binding energies with and without correction for basis set superposition error, and used the results to rank formation pathways by thermodynamic feasibility. The present work applies the same logic to a different problem: rank two competing adsorbates by how strongly they hold a site, and ask whether the ranking is large enough to matter.

## 2.10 The Gap This Study Fills

Three things are missing from the literature as reviewed. First, no published value exists for the binding energy of vanadic acid at a faujasite Brønsted acid site computed at a modern hybrid density functional level and compared, within the same model and at the same level of theory, with water. Reviews of vanadium poisoning continue to assert that vanadic acid attacks the framework, but the assertion has not been tested against the obvious competitor. Second, the strongest experimental case against the vanadic acid hypothesis, that of Pine (1990) and Xu et al. (2002), rests on kinetic arguments and on the behaviour of model compounds; it has not been examined from the adsorption side. Third, the local computational literature has applied these methods to solvent design but not to catalyst deactivation.

This study fills the first gap, speaks to the second, and begins the third. It does not attempt to simulate a full catalytic cycle, and it does not claim to have validated the whole mechanism. It computes the one number that decides whether the vanadic acid hypothesis is even viable, and then asks what that number means under regenerator conditions.

A note on novelty, stated plainly. This is not the first density functional study of zeolite dealumination, which is due to Malola et al. (2012) and was extended by Silaghi et al. (2016), and it is not the first density functional study of vanadium in a zeolite, which includes Tielens and Dzwigaj (2010). To the best of the author's knowledge after searching the literature, no previous study has placed vanadic acid and water on the same faujasite Brønsted acid site at the same level of theory and reported the difference in their binding energies, which is the comparison the vanadic acid hypothesis requires and which is reported in Chapter Four.
