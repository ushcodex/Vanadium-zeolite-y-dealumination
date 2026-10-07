# CHAPTER TWO

# LITERATURE REVIEW

## 2.1 Residue Fluid Catalytic Cracking and Contaminant Metals

Fluid catalytic cracking (FCC) is historically the most important conversion process in the petroleum refining industry. However, global crude oil supplies have progressively shifted towards heavier and dirtier fractions. The necessity for refiners to process these cheaper, heavy feedstocks—such as atmospheric residue and vacuum gas oil—to increase refinery margins has driven the development of the residue fluid catalytic cracking (RFCC) process (Adanenche et al., 2022). 

Processing these heavy, carbonaceous feedstocks introduces severe operational challenges. Residue feeds contain high levels of Conradson carbon residue and significant concentrations of heteroatoms and metal poisons, most notably vanadium, nickel, sodium, and iron (Adanenche et al., 2022). These metal contaminants deposit on the RFCC catalyst during the cracking process, permanently or temporarily deactivating the catalyst and promoting undesirable side reactions. Nickel and vanadium are identified as the most detrimental poisons; they promote severe dehydrogenation reactions leading to excessive coke and hydrogen gas production, which upsets the heat balance of the regenerator and overloads the wet gas compressors (Adanenche et al., 2022). Furthermore, vanadium severely compromises the structural integrity of the zeolite active component.

## 2.2 Zeolite Y and Steam-Induced Dealumination

The active component of RFCC catalysts is zeolite Y, a microporous crystalline aluminosilicate with a faujasite (FAU) structure. The catalytic cracking activity is derived from its Bronsted acid sites, which are formed by the substitution of silicon atoms by aluminum/proton pairs within the framework (Malola et al., 2011).

During the regeneration cycle of the FCC process, carbon deposits (coke) are burned off the catalyst in an oxidizing atmosphere, generating significant amounts of steam at high temperatures. Exposure to steam causes a slow degradation process known as hydrothermal dealumination or irreversible deactivation. Both silicon and aluminum atoms can be hydrolyzed by steam, but aluminum is substantially less stable in a steam atmosphere than silicon (Malola et al., 2011). 

Density functional theory (DFT) investigations by Malola et al. (2011) revealed that the dealumination process proceeds via a series of hydration reactions. Their calculations demonstrated that the complete extraction of a framework aluminum atom by steam requires at least three water molecules and leaves behind a "silanol nest" defect, where four hydroxy groups occupy the void left by the extracted tetrahedral atom. The computed effective energy barrier for steam dealumination ranges from 190 to 260 kJ/mol, which is 40-50 kJ/mol lower than the barrier for desilication (Malola et al., 2011). These findings underscore that while steam alone is capable of extracting framework aluminum and causing catalyst deactivation, it is a highly activated process requiring significant thermal energy.

## 2.3 The Mechanism of Vanadium Poisoning

When vanadium is present in the feedstock, the destruction of the zeolite framework is dramatically accelerated. The mechanism of vanadium-induced destruction has been a subject of extensive investigation.

Trujillo et al. (1997) utilized electron spin resonance (ESR), UV-VIS diffuse reflectance, and sorption measurements to elucidate the dynamics of vanadium on zeolite Y. They observed that vanadium initially deposits on the external surface of the zeolite but migrates into the internal channels upon heating in an oxidizing atmosphere. While water assists in transporting vanadium to the acid sites, it is not strictly required for the migration itself (Trujillo et al., 1997).

Crucially, Trujillo et al. (1997) established that although the strongest acid sites can stabilize vanadium in the V(IV) oxidation state (as VO²⁺ cations), experimental evidence indicates that V(IV) does not play a direct role in the destruction of the zeolite framework. Instead, under the steam-rich conditions of the regenerator, vanadium in the V(V) oxidation state forms volatile vanadic acid. The governing reaction within the zeolite is described as:

VO²⁺-Y + 2 H₂O ⇌ H⁺-Y + H₃VO₄         (2.1)

Because vanadic acid (H₃VO₄) is a strong acid formed in the presence of steam, it attacks the SiO₂/Al₂O₃ framework, accelerating the hydrolysis of the framework bonds. In this manner, vanadium effectively acts as a catalyst for the steam-induced destruction of the zeolite (Trujillo et al., 1997).

## 2.4 Structural Damage and Mesopore Evolution

The macroscopic consequence of this vanadic acid attack is severe structural degradation. Etim et al. (2015) investigated the specific effects of vanadium contamination on the framework and micropore structure of ultra-stable Y (USY) zeolite. Using a combination of X-ray diffraction, nitrogen adsorption, transmittance electron microscopy (TEM), and solid-state NMR, they demonstrated that in the presence of steam, vanadium causes massive structural damage to the zeolite framework.

A key finding by Etim et al. (2015) was the excessive evolution of non-inter-crystalline mesopores driven by vanadium contamination. At a vanadium loading of just 0.5 wt.%, the evolved mesopore size averaged approximately 25.0 nm. This is significantly larger than the standard mesopore sizes found in hydrothermally stable zeolitic materials optimized for FCC performance. The formation of these massive mesopores is a direct result of the accelerated, unregulated dealumination catalyzed by the mobile vanadic acid species penetrating the inner cavities of the zeolite (Etim et al., 2015).

## 2.5 Mitigation Strategies and Metal Passivators

To combat the deleterious effects of vanadium and other metals, refineries employ metal passivators and trapping agents. Adanenche et al. (2022) reviewed recent advances in the passivation of RFCC catalysts. While antimony and bismuth have historically been used to mitigate the dehydrogenating effects of nickel, controlling vanadium requires different strategies. 

Compounds based on tin, rare earth metals (such as cerium and lanthanum), and basic alkaline earth metals (such as magnesium) have attracted significant attention for their ability to trap and passivate vanadium (Adanenche et al., 2022). Etim et al. (2015) noted that the interaction of vanadium with a passivator limits its mobility and decreases its effective acidity, thereby preventing the vanadic acid from reaching the inner cavities of the zeolite where it causes massive structural breakdown. However, as the industry shifts towards processing increasingly heavy feeds, there remains a pressing need to develop RFCC catalysts with improved, environmentally friendly metal tolerance while maintaining intrinsic cracking properties (Adanenche et al., 2022).

## 2.6 Computational Investigation of Reaction Mechanisms

As demonstrated by Malola et al. (2011), computational modeling using density functional theory is highly effective for elucidating the reaction paths and activation barriers of zeolite dealumination. While their work provided crucial insights into baseline steam hydrolysis, understanding the specific energetic differences introduced by the catalytic action of vanadic acid (Trujillo et al., 1997) requires a comparative computational approach. 

To manage computational cost while exploring complex reaction coordinates, modern studies often employ a tiered approach. Semi-empirical tight-binding methods, such as GFN2-xTB, offer robust initial geometry optimization and pathway screening. Subsequently, higher-level hybrid DFT methods, incorporating dispersion corrections (e.g., B3LYP-D3(BJ)), are utilized to refine the geometries and provide accurate thermodynamic and kinetic energies for the proposed stationary points. This computational strategy is adopted in the present study to quantify the thermodynamic driving forces of vanadic acid attack versus baseline steam hydrolysis.
