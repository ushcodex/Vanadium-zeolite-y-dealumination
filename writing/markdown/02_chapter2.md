# 2.0 LITERATURE REVIEW

## 2.1 Zeolite Y in Residue Fluid Catalytic Cracking

Residue fluid catalytic cracking processes heavy refinery feeds that contain metals and other contaminants. The catalyst circulates between a reactor and a regenerator, where coke is burned in air and steam. Zeolite Y supplies many of the catalyst's cracking sites, and vanadium carried in the feed can accumulate on the catalyst during operation (Adanenche et al., 2023; Mitchell, 1980).

Zeolite Y has the faujasite framework, a crystalline network of silicon, aluminium, and oxygen atoms. A framework aluminium atom introduces a negative charge balanced by a proton on a neighbouring oxygen, forming a Brønsted acid site. Figure 2.1 shows the supercage and its twelve-membered-ring opening. Removal of framework aluminium removes the associated acid site and can leave silanol groups on neighbouring framework oxygens (Malola et al., 2012).

[FIG: from_sources/etim2016_fig1_y_zeolite.png | Figure 2.1: Structure of Zeolite Y showing the supercage and its twelve-membered-ring opening | Source: Etim, Xu, Ullah and Yan (2016), Figure 1]

## 2.2 Dealumination by Steam

Steam hydrolyses framework Al–O–Si bonds during catalyst regeneration. Density functional theory (DFT) calculations by Malola et al. (2012) described dealumination as a sequence of water-assisted bond-cleavage steps. Their calculated effective barriers depended on the reference state for incoming water, demonstrating the role of adsorption thermochemistry in reaction energetics. Figure 2.2 presents their calculated reaction paths for dealumination and desilication.

[FIG: from_sources/malola2012_fig2_paths.png | Figure 2.2: Calculated reaction paths for dealumination and desilication using gas-phase and adsorbed water references | Source: Malola, Svelle, Lønstad Bleken and Swang (2012), Figure 2]

Silaghi et al. (2016) examined dealumination in several zeolite frameworks and discussed how extra-framework aluminium could remain confined within the pores. Their work supported a stepwise description of hydrolysis. Steam hydrolysis therefore provides the baseline reaction for assessing additional effects associated with vanadium.

## 2.3 Vanadium under Regenerator Conditions

Vanadium in a regenerated catalyst is commonly associated with oxidised species, including vanadium pentoxide. Wormsbecher et al. (1986) proposed that vanadium pentoxide reacts with steam to form volatile vanadic acid:

V₂O₅(s) + 3 H₂O(g) ⇌ 2 H₃VO₄(g)
(2.1)

Equation (2.1) represents the gas-phase vanadic-acid source in the proposed route. Wormsbecher et al. (1986) discussed regenerator conditions near 730 °C, with about 20% steam at a total pressure of 2 atm, and estimated vanadic-acid concentrations in the low-parts-per-million range. Trujillo et al. (1997) considered the same high-steam environment and calculated an H₃VO₄ partial pressure of about 3.37 × 10⁻⁶ atm, corresponding to approximately 1.7 ppm at 2 atm. Appendix B.1 shows the pressure conversion used for the reported gas composition.

Occelli (1991) reviewed interactions of vanadium species with cracking catalysts and described changes in vanadium speciation during steaming and hydrolysis. Trujillo et al. (1997) proposed that vanadium could reach acid sites and form vanadic acid in the presence of water. Their local-enrichment proposal provides a pore-scale context for the acid-site comparison in this study.

## 2.4 Proposed Explanations for Vanadium-Related Damage

Three explanations are central to vanadium-related damage. The vanadic-acid route assigns H₃VO₄ a direct role in framework hydrolysis. The steam-dominated route assigns the principal attack to water and a catalytic or secondary role to vanadium. The sodium-mediated route proposes that vanadium mobilises sodium, after which sodium hydroxide attacks the framework. Table 2.1 compares the mechanisms and their supporting studies; Figure 2.3 shows their proposed sequence alongside the adsorption comparison examined here.

[TBL: Table 2.1: Proposed explanations for vanadium-related damage to Zeolite Y | Proposed mechanism;Proposed role of vanadium;Evidence discussed in the literature | Vanadic-acid route;H₃VO₄ directly promotes framework hydrolysis;Vanadium species in steamed catalysts and proposed acid-site chemistry, Wormsbecher et al. (1986) and Trujillo et al. (1997) | Steam-dominated route;Steam hydrolyses the framework and vanadium is secondary or catalytic;Similar apparent activation energies for vanadium-loaded and control catalysts, and damage to silicalite, Pine (1990) | Sodium-mediated route;Vanadium helps mobilise sodium and steam enables NaOH attack;Dependence of destruction on sodium availability and experiments with sodium vanadate, Xu et al. (2002)]

Pine (1990) reported similar apparent activation energies for destruction of ultra-stable Y zeolite under vanadium-loaded and control conditions. He also reported damage to silicalite, which contains little framework aluminium. These observations support a steam-led contribution and place vanadium's role within the broader catalyst environment.

Xu et al. (2002) proposed that vanadium and sodium act together. In their mechanism, vanadium-containing species mobilise sodium, and steam enables sodium hydroxide formation and framework attack. This pathway makes sodium availability a relevant variable alongside the vanadic-acid and steam routes in Table 2.1.

[FIG: fig2_1_dispute.png | Figure 2.3: Proposed explanations for vanadium-related damage to Zeolite Y and the adsorption comparison examined in this study | Source: author, based on Malola et al. (2012), Silaghi et al. (2016), Wormsbecher et al. (1986), Trujillo et al. (1997), Pine (1990), and Xu et al. (2002)]

Steam, vanadium speciation, sodium content, and conditions within the catalyst can contribute together to framework damage. The adsorption comparison addresses the molecular interaction component of the mechanisms illustrated in Figure 2.3, while the reaction-path calculations assess the first model Al–O cleavage step. The combined view connects molecular adsorption to the wider catalyst environment.

## 2.5 Evidence of Damage and Mitigation

Etim et al. (2016) examined vanadium-contaminated ultra-stable Y zeolite after steaming and reported changes in the framework and micropore structure. Figure 2.4 presents transmission electron micrographs from their study. These structural observations establish damage under the combined treatment and motivate molecular studies of the elementary steps.

[FIG: from_sources/etim2016_fig8_tem.png | Figure 2.4: Transmission electron micrographs of ultra-stable Y zeolite before and after vanadium contamination and steaming | Source: Etim, Xu, Ullah and Yan (2016), Figure 8]

Wormsbecher et al. (1986) reported catalyst protection by basic oxides under their test conditions. Etim et al. (2018) evaluated a magnesium–yttrium oxide trap and linked vanadium capture to formation of immobile yttrium vanadate. These studies demonstrate the practical importance of vanadium control and connect molecular speciation with catalyst performance.

## 2.6 Computational Studies and Research Context

Periodic DFT studies have calculated water-driven dealumination pathways in zeolites (Malola et al., 2012; Silaghi et al., 2016). Tielens and Dzwigaj (2010) studied acid-base sites in vanadium redox zeolites, focusing on vanadium incorporated within the framework. The present comparison complements these studies by evaluating an external vanadic-acid molecule and water at the same Zeolite Y Brønsted acid site.

Together, the literature describes steam-assisted hydrolysis, vanadium–zeolite interactions, and sodium-mediated damage as relevant parts of RFCC catalyst chemistry. Table 2.1 and Figure 2.3 organise these mechanisms for comparison with the adsorption, pathway, and thermochemical results in Chapter Four. The comparison distinguishes adsorbate preference from the broader explanations of catalyst damage.
