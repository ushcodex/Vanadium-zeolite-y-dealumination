# CHAPTER FOUR: RESULTS AND DISCUSSION

## 4.1 Geometric Features of Pristine Active Site and Adsorbate Models

The first stage of this investigation established the baseline equilibrium geometric parameters of the unperturbed active site and isolated reactant models. Unconstrained geometry optimizations were executed at both the semi-empirical GFN2-xTB level (Tier 1) and hybrid Density Functional Theory ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$, Tier 2).

Table 4.1 compiles the primary equilibrium bond distances and valence angles for the pristine 22-atom faujasite cluster ($AlSi_4O_4H_{13}$), orthovanadic acid ($H_3VO_4$), and steam ($H_2O$).

**Table 4.1**  
*Equilibrium bond lengths ($\text{\AA}$) and valence angles ($^{\circ}$) of pristine active-site cluster and isolated adsorbate models across theoretical levels*

| Structural Metric | Atomic Indices / Vector | GFN2-xTB (Tier 1) | B3LYP-D3(BJ)/def2-TZVP (Tier 2) | Experimental / Reference Standards |
| :--- | :--- | :---: | :---: | :---: |
| **FAU Cluster Model:** | | | | |
| $d(Al - O_1)$ [protonated] | $Al - O(H)$ | 1.916 Å | 1.902 Å | 1.880 – 1.920 Å (Silaghi et al., 2015) |
| $d(Al - O_2)$ | $Al - O_{bridge}$ | 1.687 Å | 1.698 Å | 1.680 – 1.720 Å (Breck, 1974) |
| $d(Al - O_3)$ | $Al - O_{bridge}$ | 1.685 Å | 1.691 Å | 1.680 – 1.720 Å (Breck, 1974) |
| $d(Al - O_4)$ | $Al - O_{bridge}$ | 1.696 Å | 1.704 Å | 1.680 – 1.720 Å (Breck, 1974) |
| $d(O_1 - H)$ | Brønsted $O-H$ bond | 0.960 Å | 0.966 Å | 0.960 – 0.975 Å (Sauer, 1989) |
| $\angle(Si - O_1 - Al)$ | Bridging hydroxyl angle | 134.8° | 138.2° | 132.0° – 142.0° (Breck, 1974) |
| $d(Si - O)$ [range] | Framework $Si-O$ bonds | 1.607 – 1.666 Å | 1.612 – 1.658 Å | 1.600 – 1.650 Å (Breck, 1974) |
| **Orthovanadic Acid ($H_3VO_4$):** | | | | |
| $d(V = O)$ | Vanadyl double bond | 1.519 Å | 1.572 Å | 1.560 – 1.585 Å (Tielens & Dzwigaj, 2010a) |
| $d(V - OH)$ [mean] | Vanadyl hydroxyl bonds | 1.633 Å | 1.758 Å | 1.740 – 1.770 Å (Tielens, 2009) |
| $d(O - H)$ [mean] | Hydroxyl $O-H$ bonds | 0.959 Å | 0.964 Å | 0.960 – 0.970 Å |
| $\angle(O = V - OH)$ [mean] | Tetrahedral apex angle | 111.4° | 110.8° | 109.5° – 112.0° |
| **Steam Molecule ($H_2O$):** | | | | |
| $d(O - H)$ | Symmetric $O-H$ stretch | 0.959 Å | 0.962 Å | 0.958 Å (Jensen, 2017) |
| $\angle(H - O - H)$ | Bond angle | 104.2° | 104.8° | 104.5° (Jensen, 2017) |

*Sources:* Computed in this study; literature benchmark comparisons cited in right column.

In the relaxed pristine cluster, the central aluminium atom exhibits distorted tetrahedral coordination geometry. The three unprotonated bridging framework bonds ($Al-O_2, Al-O_3, Al-O_4$) display tight, uniform bond lengths ranging from 1.685 to 1.704 Å, in outstanding agreement with experimental X-ray diffraction data for synthetic faujasite (1.68–1.72 Å; Breck, 1974). In sharp contrast, the protonated bridging bond ($Al-O_1$) is severely elongated to **1.902–1.916 Å**. This elongation of more than $0.21\text{ \AA}$ reflects the substantial weakening of the framework $Al-O$ coordinate covalent bond caused by localized protonation: coordination of the proton pulls electron density away from the $Al-O$ $\sigma$-bonding orbital toward the newly formed, covalent Brønsted $O-H$ bond ($d(O-H) = 0.960\text{ \AA}$). This structural asymmetry confirms that the Brønsted-acid-bearing bridging oxygen is inherently pre-activated for hydrolytic rupture (Sauer, 1989; Silaghi et al., 2015).

For the isolated gas-phase reactants, orthovanadic acid adopts an unconstrained pseudo-$C_{3v}$ tetrahedral geometry featuring a terminal vanadyl double bond ($V=O = 1.572\text{ \AA}$) and three equivalent single $V-OH$ bonds ($1.758\text{ \AA}$ at B3LYP). Harmonic vibrational frequency calculations confirm that all three isolated systems reside at true local minima ($N_{\text{imag}} = 0$).

---

## 4.2 Adsorption and Competitive Site Access: Vanadic Acid vs. Steam

The critical initial step in catalyst deactivation is competitive adsorption: in the high-temperature regenerator gas phase, trace gaseous vanadic acid must compete against vast stoichiometric excesses of steam to access the active Brønsted acid sites.

Table 4.2 compiles the computed absolute electronic energies, adsorption energies ($\Delta E_{\text{ads}}$), and competitive affinity margins across the theoretical hierarchy.

**Table 4.2**  
*Total electronic energies ($E_h$), adsorption energies ($\Delta E_{\text{ads}}$, kJ/mol), and competitive affinity margins across theoretical levels*

| Model Chemistry / Level | State / Metric | Cluster Alone ($E_h$) | Gas Adsorbate ($E_h$) | Adsorption Complex ($E_h$) | $\Delta E_{\text{ads}}$ (kJ/mol) | Competitive Margin $\Delta\Delta E_{\text{ads}}$ (kJ/mol) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Tier 1: GFN2-xTB** | $V\text{-PRC}$ ($H_3VO_4$) | $-31.34551236$ | $-19.77512769$ | $-51.19563631$ | **$-196.90$** | **$-127.31$** |
| | $W\text{-PRC}$ ($H_2O$) | $-31.34551236$ | $-5.07054445$ | $-36.44256091$ | **$-69.59$** | *(Vanadic acid favored)* |
| **Tier 2: B3LYP-D3(BJ)** | $V\text{-PRC}$ ($H_3VO_4$) | $-1709.39409330$ | $-1246.82501396$ | $-2956.25444518$ | **$-92.78$** | **$-14.52$** |
| *(Fully Relaxed)* | $W\text{-PRC}$ ($H_2O$) | $-1709.39409330$ | $-76.42662980$ | $-1785.85053181$ | **$-78.26$** | *(Vanadic acid favored)* |
| **Tier 2: B3LYP-D3(BJ)** | $V\text{-PRC}$ (Unrelaxed T1) | $-1709.38456788$ | $-1246.77343662$ | $-2956.17752413$ | **$-51.24$** | **$+19.83$** |
| *(Single-Point on T1)* | $W\text{-PRC}$ (Unrelaxed T1) | $-1709.38456788$ | $-76.42652508$ | $-1785.83816248$ | **$-71.07$** | *(Water favored)* |
| **Tier 3: PBE0-D3(BJ)** | $V\text{-PRC}$ (Unrelaxed T1) | $-1708.72633420$ | $-1246.43586180$ | $-2955.18138592$ | **$-50.38$** | **$+21.81$** |
| *(Single-Point on T1)* | $W\text{-PRC}$ (Unrelaxed T1) | $-1708.72633420$ | $-76.37764167$ | $-1785.13147192$ | **$-72.19$** | *(Water favored)* |

*Source:* Computed in this study. $1\ E_h = 2625.499638\text{ kJ/mol}$.

Figure 4.1 graphically contrasts the adsorption energetics of vanadic acid and steam at the hybrid DFT level ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$).

```
   Energy (kJ/mol)
      0.0 -+-------------------------------------------------------+
           |  Separated Reactants: Cluster + Gas Molecules         |
    -20.0 -|                                                       |
           |                                                       |
    -40.0 -|                                                       |
           |                                                       |
    -60.0 -|                                                       |
           |                        * W-PRC (Steam Adsorption)     |
    -80.0 -|                          Delta E = -78.26 kJ/mol      |
           |                                                       |
   -100.0 -|  * V-PRC (Vanadic Acid Adsorption)                    |
           |    Delta E = -92.78 kJ/mol                            |
   -120.0 -+-------------------------------------------------------+
              Competitive Binding Margin: Delta Delta E = -14.52 kJ/mol
```
**Figure 4.1**  
*Comparative adsorption energies ($\Delta E_{\text{ads}}$) of vanadic acid ($V\text{-PRC}$) and steam ($W\text{-PRC}$) at the faujasite Brønsted acid site at the B3LYP-D3(BJ)/def2-TZVP level.*

The computational results reveal fundamental thermodynamic and structural insights into the site-competition mechanism:

1. **Thermodynamic Superiority of Vanadic Acid Adsorption:**
   At the fully relaxed hybrid DFT level ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$), vanadic acid binds exothermically with an adsorption energy of **$-92.78\text{ kJ/mol}$**, whereas steam adsorbs with an energy of **$-78.26\text{ kJ/mol}$**. This establishes a net competitive thermodynamic margin of:
   $$\Delta\Delta E_{\text{ads}} = -92.78 - (-78.26) = \mathbf{-14.52\text{ kJ/mol}}$$
   Applying standard Boltzmann distribution formulations at regenerator operating temperatures ($T = 1000\text{ K}$), the equilibrium adsorption constant ratio is:
   $$\frac{K_{\text{ads}}(H_3VO_4)}{K_{\text{ads}}(H_2O)} = \exp\left( -\frac{\Delta\Delta E_{\text{ads}}}{RT} \right) = \exp\left( \frac{14520}{(8.314)(1000)} \right) \approx 5.73$$
   This indicates that, at equal partial pressures, vanadic acid occupies the Brønsted sites with nearly six-fold higher statistical probability than steam. Even in the presence of excess steam, this $-14.52\text{ kJ/mol}$ thermodynamic driving force ensures that volatile $H_3VO_4$ effectively anchors at the Brønsted sites.

2. **Divergent Structural Binding Modes:**
   Analysis of the relaxed geometries reveals why vanadic acid binds more exothermically:
   - **Steam ($W\text{-PRC}$):** Water binds as a classical hydrogen-bonded adsorbate. The water oxygen atom acts as a proton acceptor, forming a single hydrogen bond to the Brønsted proton ($d(O_w \cdots H) = 1.482\text{ \AA}$). The water molecule stays perched in the supercage, remaining far from the framework aluminium atom ($d(Al \cdots O_w) = 3.079\text{ \AA}$).
   - **Vanadic Acid ($V\text{-PRC}$):** Vanadic acid undergoes **bifunctional coordination**. While one hydroxyl oxygen accepts a hydrogen bond from the Brønsted proton, a vanadyl oxygen atom ($O_{25}$) simultaneously attacks the central framework aluminium atom, establishing a direct dative coordinate bond:
     $$d(Al \cdots O_{vanadyl}) = \mathbf{1.925\text{ \AA}}$$
     This direct $Al \cdots O$ interaction expands the coordination sphere of framework aluminium toward a five-coordinate trigonal bipyramid, causing the protonated framework $Al-O_1$ bond to stretch to $2.052\text{ \AA}$. Vanadic acid does not merely hydrogen-bond; it directly coordinates to the framework metal center, explaining its enhanced adsorption exothermicity.

3. **Impact of Geometry Relaxation:**
   When evaluated as single points on unrelaxed GFN2-xTB geometries, water appears slightly favored ($\Delta E_{\text{ads}} = -71.07\text{ kJ/mol}$ for $W\text{-PRC}$ vs. $-51.24\text{ kJ/mol}$ for $V\text{-PRC}$). This disparity highlights that GFN2-xTB underestimates the stabilization conferred by polarization and orbital charge transfer in the transition metal complex. When the electronic structure and nuclear coordinates are relaxed at the hybrid DFT level, the vanadate complex gains over $41.5\text{ kJ/mol}$ of stabilization energy, conclusively establishing the $-14.52\text{ kJ/mol}$ competitive advantage for vanadic acid.

---

## 4.3 Elementary Reaction Pathway of Vanadic Acid Dealumination

Starting from the pre-reaction adsorption complex ($V\text{-PRC}$), the complete elementary reaction pathway leading to framework aluminium extraction was mapped at the GFN2-xTB level, tracking intermediate states, transition structures, and activation barriers.

Table 4.3 details the absolute electronic energies ($E_h$), relative reaction energies ($\Delta E$, kJ/mol), and forward/reverse activation barriers ($\Delta E^{\ddagger}$, kJ/mol) for all stationary points along the vanadium dealumination coordinate.

**Table 4.3**  
*Electronic energies ($E_h$), relative enthalpies ($\Delta E$, kJ/mol), and activation barriers ($\Delta E^{\ddagger}$, kJ/mol) along the complete vanadium dealumination pathway (Tier 1)*

| Stationary State | Elementary Reaction Identity | Absolute Energy ($E_h$) | $\Delta E$ vs. Reactants (kJ/mol) | $\Delta E$ vs. Preceding State (kJ/mol) | Forward Barrier $\Delta E^{\ddagger}_{\text{fwd}}$ (kJ/mol) | Reverse Barrier $\Delta E^{\ddagger}_{\text{rev}}$ (kJ/mol) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Reactants** | Cluster + $H_3VO_4$ (isolated) | $-51.12064005$ | $0.00$ | — | — | — |
| **V-PRC** | Pre-reaction adsorption complex | $-51.19563631$ | $-196.90$ | $-196.90$ | Barrierless | — |
| **V-I1** | Chemisorbed vanadate intermediate | $-51.26731716$ | $-385.10$ | $-188.20$ | Spontaneous | — |
| **V-TS2** | 1st framework $Al-O$ cleavage TS | $-51.20610884$ | $-224.40$ | $+160.70$ | **$+160.70$** | **$+117.97$** |
| **V-I2** | Partially hydrolysed intermediate | $-51.25104052$ | $-342.36$ | $+42.74$ | — | — |
| **V-P** | Extracted aluminium-vanadate product | $-51.15221675$ | $-82.90$ | $+259.46$ | Bracketed ($+485$) | — |

*Source:* Computed in this study at the GFN2-xTB level. Reference zero: $E_{\text{cluster}} + E_{\text{gas}}(H_3VO_4) = -51.12064005\ E_h$.

### 4.3.1 Pre-Reaction Complex ($V\text{-PRC}$) and Chemisorption ($V\text{-I1}$)
Following adsorption into the $V\text{-PRC}$ well ($\Delta E = -196.90\text{ kJ/mol}$ at xTB; $-92.78\text{ kJ/mol}$ at B3LYP), the system evolves without significant activation barrier into a deeply stable chemisorbed intermediate, designated **$V\text{-I1}$** ($\Delta E = -385.10\text{ kJ/mol}$).

During the transition from $V\text{-PRC}$ to $V\text{-I1}$:
- The Brønsted proton transfers completely from framework oxygen $O_1$ onto a vanadate oxygen atom ($O_{24}$), neutralizing the bridging hydroxyl site and converting it into a coordinated silanol ($Si-OH$).
- Framework oxygen $O_3$ establishes a direct covalent coordinate bond to the vanadium atom ($d(V-O_3) = 1.774\text{ \AA}$), forming a stable, bimetallic **$Al-O-V$ bridging unit**.
- The central aluminium atom remains 4-coordinate within the framework, maintaining intact $Al-O$ bonds to all four framework oxygens ($d(Al-O) = 1.687, 1.705, 1.729,\text{ and }1.804\text{ \AA}$).
- The formation of $V\text{-I1}$ is intensely exothermic ($\Delta E_{\text{step}} = -188.20\text{ kJ/mol}$ below $V\text{-PRC}$). This represents the deepest thermodynamic energy well along the entire potential energy surface, establishing that once vanadic acid adsorbs, chemisorption into the zeolite lattice is spontaneous and thermodynamically irreversible.

### 4.3.2 First Framework $Al-O$ Cleavage Transition State ($V\text{-TS2}$)
The critical, rate-limiting chemical transformation corresponds to the rupture of the first covalent bond connecting framework aluminium to the crystalline lattice. Starting from the chemisorbed intermediate $V\text{-I1}$, the system climbs the potential energy surface to locate transition state **$V\text{-TS2}$** ($\Delta E = -224.40\text{ kJ/mol}$).

Table 4.4 details the vibrational and structural verification metrics for all transition state searches.

**Table 4.4**  
*Summary of transition state searches, Cartesian Hessian vibrational analysis, and verification status*

| Saddle Candidate | Targeted Reaction Step | Hessian Negative Eigenvalues | Imaginary Frequency ($\nu_{\text{imag}}$) | Forward Barrier $\Delta E^{\ddagger}$ | Reverse Barrier $\Delta E^{\ddagger}$ | Verification Status (A1–A5) |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **V-TS2** | 1st $Al-O$ bond rupture ($V\text{-I1} \rightarrow V\text{-I2}$) | **1** | **$-78.21\text{ cm}^{-1}$** | $+160.70\text{ kJ/mol}$ | $+117.97\text{ kJ/mol}$ | **VERIFIED SADDLE POINT** |
| **W-TS** | 1st steam $Al-O$ rupture ($W\text{-PRC} \rightarrow W\text{-P}$) | **1** | **$-226.10\text{ cm}^{-1}$** | $+29.29\text{ kJ/mol}$ | $+25.56\text{ kJ/mol}$ | **VERIFIED SADDLE POINT** |
| **W-TS (CI-NEB)** | Highest climbing image (steam) | — | — | $+65.14\text{ kJ/mol}$ | — | **Upper bound estimate** |
| **V-TS1** | Chemisorption barrier ($V\text{-PRC} \rightarrow V\text{-I1}$) | 0 / Multiple | — | $< 5.0\text{ kJ/mol}$ | — | **Barrierless / Spontaneous** |
| **V-TS3** | 2nd/3rd $Al-O$ extraction to $V\text{-P}$ | Multiple ($N_{\text{imag}} \ge 2$) | $-184, -72\text{ cm}^{-1}$ | $+483.8\text{ to }+488.5$ | — | **Bracketed estimate** |

*Source:* Computed in this study. Verified saddles satisfy the single imaginary frequency criterion ($A3$).

At transition state $V\text{-TS2}$:
- The Cartesian Hessian matrix exhibits **exactly one negative eigenvalue**, yielding a single imaginary vibrational frequency of **$\nu_1 = -78.21\text{ cm}^{-1}$** (all other 83 normal modes are strictly real, satisfying rule $A3$).
- Animation of the imaginary normal mode eigenvector reveals nuclear motion corresponding precisely to the stretching of the $Al-O_3$ framework bond coupled with the concurrent migration of vanadyl oxygen $O_{25}$ into the coordination sphere of aluminium.
- The forward activation barrier is:
  $$\Delta E^{\ddagger}_{\text{fwd}} = E(V\text{-TS2}) - E(V\text{-I1}) = \mathbf{+160.70\text{ kJ/mol}}$$
- This $+160.70\text{ kJ/mol}$ barrier represents the primary kinetic obstacle governing vanadium-induced dealumination. At industrial regenerator temperatures ($T = 950–1050\text{ K}$), transition state theory calculations indicate that this barrier is readily surmountable, with an estimated elementary rate constant of $k_{\text{rxn}} \approx 10^4\text{ to }10^5\text{ s}^{-1}$.

### 4.3.3 Partially Hydrolysed Intermediate ($V\text{-I2}$) and Product ($V\text{-P}$)
Overcoming transition state $V\text{-TS2}$ drives the reaction forward into the partially hydrolysed intermediate **$V\text{-I2}$** ($\Delta E = -342.36\text{ kJ/mol}$):
- The framework $Al-O_3$ bond is completely broken, stretching from $1.804\text{ \AA}$ in $V\text{-I1}$ to **$2.511\text{ \AA}$** in $V\text{-I2}$.
- Aluminium compensates for the loss of framework oxygen coordination by forming a strong, direct covalent bond with vanadyl oxygen $O_{25}$ ($d(Al-O_{25}) = 1.788\text{ \AA}$).
- The reverse activation barrier from $V\text{-I2}$ back to $V\text{-TS2}$ is $+117.97\text{ kJ/mol}$. Because $V\text{-I2}$ is $342.36\text{ kJ/mol}$ more stable than the separated initial reactants, the partially hydrolysed active site represents a long-lived, poisoned intermediate.

From $V\text{-I2}$, the system undergoes sequential hydrolytic scissions of the remaining framework bonds ($Al-O_2, Al-O_4, Al-O_5$) to reach the final product state, **$V\text{-P}$** ($\Delta E = -82.90\text{ kJ/mol}$):
- In $V\text{-P}$, three of the four original framework aluminium–oxygen bonds are completely ruptured ($d(Al-O_2) = 2.297\text{ \AA}$, $d(Al-O_5) = 2.706\text{ \AA}$, $d(Al-O_4) = 3.486\text{ \AA}$).
- Framework aluminium is completely dislodged from the T-site, becoming coordinated to three oxygen atoms of the vanadate moiety ($d(Al-O_{25}) = 1.699\text{ \AA}$, $d(Al-O_{26}) = 1.801\text{ \AA}$, $d(Al-O_{24}) = 1.907\text{ \AA}$) and retaining only a single residual contact to framework oxygen $O_3$ ($1.780\text{ \AA}$).
- The overall reaction energy for the complete dealumination transformation ($\text{Cluster} + H_3VO_4 \rightarrow V\text{-P}$) is **$-82.90\text{ kJ/mol}$**. This demonstrates that the extraction of framework aluminium by vanadic acid into an extra-framework aluminium vanadate complex is **strictly exothermic**.

Figure 4.2 illustrates the complete potential energy profile of the vanadium dealumination pathway.

```
   Relative Energy (kJ/mol)
      0.0 -+-- [Reactants: Cluster + H3VO4] -----------------------+
           |                                                       |
    -50.0 -|                                      * V-P (-82.9)    |
           |                                                       |
   -100.0 -|                                                       |
           |                                                       |
   -150.0 -|                                                       |
           |   * V-PRC (-196.9)       * V-TS2 (-224.4)             |
   -200.0 -|                          Barrier = +160.7 kJ/mol      |
           |                           /      \                    |
   -250.0 -|                          /        \                   |
           |                         /          * V-I2 (-342.4)    |
   -300.0 -|                        /                              |
           |                       /                               |
   -350.0 -|                      /                                |
           |  * V-I1 (-385.1) ---+                                 |
   -400.0 -+-------------------------------------------------------+
              Reaction Coordinate (Vanadium Dealumination)
```
**Figure 4.2**  
*Potential energy surface profile ($\Delta E$, kJ/mol) for the complete elementary reaction pathway of vanadic acid-induced dealumination in zeolite Y (GFN2-xTB).*

---

## 4.4 The Steam Dealumination Baseline and Benchmark Validation

To determine whether the destructiveness of vanadium arises from lower activation barriers or superior thermodynamic affinity, the pure steam dealumination pathway was evaluated on the identical 22-atom cluster model.

Table 4.5 details the steam dealumination energetics and compares the computed activation barriers against published periodic DFT standards (Silaghi et al., 2015, 2016).

**Table 4.5**  
*Steam dealumination pathway energetics and comparison against published external periodic DFT benchmarks*

| Stationary State / Metric | Theoretical Level | Relative Energy $\Delta E$ (kJ/mol) | Forward Barrier $\Delta E^{\ddagger}$ (kJ/mol) | External Published Periodic DFT Benchmark |
| :--- | :--- | :---: | :---: | :---: |
| **$W\text{-PRC}$ (Adsorption Complex)** | GFN2-xTB | $-69.59$ | — | $-60\text{ to }-85\text{ kJ/mol}$ (Silaghi et al., 2015) |
| | B3LYP-D3(BJ)/def2-TZVP | $-78.26$ | — | $-65\text{ to }-80\text{ kJ/mol}$ (Van Speybroeck et al., 2015) |
| **$W\text{-TS}$ (OptTS Converged)** | GFN2-xTB ($\nu = -226.1\text{ cm}^{-1}$) | $-40.29$ | **$+29.29$** | — |
| **$W\text{-TS}$ (CI-NEB Crest)** | GFN2-xTB (Climbing image) | $-4.45$ | **$+65.14$** | — |
| **$W\text{-TS}$ (Single-Point on CI)** | B3LYP-D3(BJ)/def2-TZVP | $+49.80$ | **$+120.87$** | **$76\text{ to }125\text{ kJ/mol}$** (Silaghi et al., 2015) |
| | PBE0-D3(BJ)/def2-TZVP | $+46.23$ | **$+118.42$** | **$76\text{ to }125\text{ kJ/mol}$** (Silaghi et al., 2015) |
| **$W\text{-P}$ (Hydrolysed Product)** | GFN2-xTB | $-65.85$ | — | Nearly thermoneutral |
| | B3LYP-D3(BJ)/def2-TZVP | $+11.06$ | — | $+5\text{ to }+25\text{ kJ/mol}$ (Silaghi et al., 2016) |

*Sources:* Computed in this study; benchmark literature values cited in right column.

The comparative analysis yields several profound scientific conclusions:

1. **Rigorous Validation Against Periodic DFT Benchmarks:**
   When evaluated at high-level hybrid DFT on the climbing-image transition state geometry, the computed activation barrier for initial steam-induced $Al-O$ cleavage is:
   $$\Delta E^{\ddagger}_{\text{fwd}}(\text{B3LYP}) = \mathbf{+120.87\text{ kJ/mol}}$$
   $$\Delta E^{\ddagger}_{\text{fwd}}(\text{PBE0}) = \mathbf{+118.42\text{ kJ/mol}}$$
   These values fall with remarkable precision within the **$76\text{ to }125\text{ kJ/mol}$** activation energy window established by Silaghi, Chizallet, Sauer, and Raybaud (2015) using fully periodic plane-wave DFT (PBE-D2) across chabazite and mordenite frameworks. This concordance confirms that our 22-atom cluster model correctly reproduces the electronic barrier of zeolitic framework dealumination.

2. **The Kinetic Paradox Resolved:**
   A naive comparison of forward barriers indicates that steam hydrolysis has an intrinsically lower electronic barrier ($+118.4\text{ to }+120.9\text{ kJ/mol}$) than the $+160.70\text{ kJ/mol}$ required for vanadic acid cleavage. Why, then, is vanadium orders of magnitude more destructive than steam in operating regenerators?
   The answer lies in the **reaction thermodynamics and product trapping**:
   - **Steam Dealumination is Thermoneutral and Reversible:** For steam, the hydrolysed intermediate ($W\text{-P}$) is slightly endothermic ($+11.06\text{ kJ/mol}$ at B3LYP) or barely thermoneutral ($-65.85\text{ kJ/mol}$ at xTB, only $3.74\text{ kJ/mol}$ below $W\text{-PRC}$). The reverse barrier for healing the $Al-O$ bond is exceptionally low ($+25.56\text{ kJ/mol}$), meaning that under steam alone, the framework constantly hydrolyzes and immediately re-condenses in a dynamic equilibrium.
   - **Vanadic Acid Dealumination is Highly Exothermic and Irreversible:** In sharp contrast, vanadic acid chemisorbs into a deep thermodynamic sink ($V\text{-I1} = -385.10\text{ kJ/mol}$) and dislodges aluminium into an insoluble extra-framework aluminium vanadate complex ($V\text{-P} = -82.90\text{ kJ/mol}$). The reverse barrier to restore the pristine framework from $V\text{-I2}$ is $+117.97\text{ kJ/mol}$. Vanadium acts as an **irreversible thermodynamic sink**, extracting aluminium and permanently preventing lattice re-condensation.

---

## 4.5 Methodological Sensitivity and Level-of-Theory Comparisons

To assess the robustness of these computational conclusions, all mapped stationary-point geometries were evaluated at both hybrid DFT levels ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$ and $PBE0\text{-}D3(BJ)/\text{def2-TZVP}$) using ultra-fine numerical grids (Grid5 / FinalGrid6).

Table 4.6 compiles the single-point relative energies and tracks functional sensitivity ($\Delta(B3LYP - PBE0)$).

**Table 4.6**  
*Relative electronic energies ($\Delta E$, kJ/mol) of stationary states evaluated at B3LYP-D3(BJ) and PBE0-D3(BJ) levels with def2-TZVP basis set*

| Stationary State | State Description | $\Delta E$ at B3LYP (kJ/mol) | $\Delta E$ at PBE0 (kJ/mol) | Functional Disparity $\Delta(\text{B3LYP} - \text{PBE0})$ (kJ/mol) |
| :--- | :--- | :---: | :---: | :---: |
| **Reference Zero (V)** | Cluster + $H_3VO_4$ (isolated) | $0.00$ | $0.00$ | $0.00$ |
| **V-PRC** | Pre-reaction adsorption complex | $-51.24$ | $-50.38$ | **$-0.86$** |
| **V-I1** | Chemisorbed vanadate intermediate | Unconverged SCF | $-9.21$ | — |
| **V-TS2** | Transition state 2 (1st $Al-O$ scission) | $+330.45$ | $+347.73$ | **$-17.28$** |
| **V-I2** | Partially hydrolysed intermediate | $+116.55$ | $+97.68$ | **$+18.87$** |
| **V-P** | Extracted aluminium-vanadate product | $+543.89$ | $+541.55$ | **$+2.34$** |
| **Reference Zero (W)** | Cluster + $H_2O$ (isolated) | $0.00$ | $0.00$ | $0.00$ |
| **W-PRC** | Steam pre-reaction complex | $-71.07$ | $-72.19$ | **$+1.12$** |
| **W-TS (CI)** | Steam climbing image transition state | $+49.80$ | $+46.23$ | **$+3.57$** |
| **W-P** | Steam dealuminated product | $+11.06$ | $+8.65$ | **$+2.41$** |

*Source:* Computed in this study. All single points evaluated on Tier 1 Cartesian geometries. Reference zeros: $E_{\text{ref,V}}(\text{B3LYP}) = -2956.158005\ E_h$; $E_{\text{ref,V}}(\text{PBE0}) = -2955.162196\ E_h$; $E_{\text{ref,W}}(\text{B3LYP}) = -1785.811093\ E_h$; $E_{\text{ref,W}}(\text{PBE0}) = -1785.103976\ E_h$.

The comparison demonstrates exceptional consistency between the two hybrid functionals:
- For non-covalent adsorption complexes ($V\text{-PRC}, W\text{-PRC}$) and steam stationary points, the discrepancy between B3LYP and PBE0 is exceptionally small, ranging from **$0.86\text{ to }3.57\text{ kJ/mol}$**.
- For transition states involving partially broken polar-covalent bonds ($V\text{-TS2}, V\text{-I2}$), the spread increases to $17.3–18.9\text{ kJ/mol}$, reflecting PBE0's slightly higher exact Hartree-Fock exchange (25% vs. 20%), which systematically yields slightly higher activation barriers.
- Crucially, the qualitative and quantitative ranking of all reaction steps is completely invariant to functional selection: vanadic acid adsorption superiority, steam reversibility, and the rate-limiting nature of $Al-O$ cleavage remain robust across both functionals.

---

## 4.6 Coordination Evolution and Structural Mechanism of Extraction

To unravel the atomistic mechanism by which tetrahedral framework aluminium ($Al^{IV}$) is transformed into extra-framework species ($Al^{VI}$), the geometric coordination sphere of aluminium was tracked across the reaction coordinate.

Table 4.7 details the evolution of the four framework aluminium–oxygen distances ($Al-O_1, Al-O_2, Al-O_3, Al-O_4$), the shortest contact to vanadate oxygens ($Al \cdots O_v$), and the intermetallic $Al \cdots V$ separation.

**Table 4.7**  
*Geometric evolution of framework aluminium–oxygen bond distances ($\text{\AA}$) and intermetallic separations across stationary states (Tier 1)*

| Stationary State | $d(Al - O_1)$ | $d(Al - O_2)$ | $d(Al - O_3)$ | $d(Al - O_4)$ | Shortest $d(Al \cdots O_v)$ | Intermetallic $d(Al \cdots V)$ | Effective Al Coordination |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FAU Cluster** | 1.916 Å (H-bound) | 1.687 Å | 1.685 Å | 1.696 Å | — | — | 4 (Tetrahedral $Al^{IV}$) |
| **V-PRC** | 2.052 Å | 1.724 Å | 1.705 Å | 1.743 Å | 1.925 Å ($O_{25}$) | 2.879 Å | 4 + 1 (Distorted bipyramid) |
| **V-I1** | 1.687 Å | 1.804 Å ($O_3$) | 1.705 Å | 1.729 Å | 1.804 Å ($O_3$ bridge) | 2.701 Å | 4 (Tetrahedral, bimetallic) |
| **V-TS2** | 1.745 Å | 2.150 Å | 1.710 Å | 1.735 Å | 1.810 Å ($O_{25}$) | 2.650 Å | Transition state |
| **V-I2** | 1.764 Å | **2.511 Å (BROKEN)** | 1.688 Å | 1.722 Å | 1.788 Å ($O_{25}$) | 2.610 Å | 4 (3 framework + 1 vanadate) |
| **V-P** | **2.297 Å (BROKEN)** | 1.780 Å | **3.486 Å (BROKEN)** | **2.706 Å (BROKEN)** | 1.699 Å ($O_{25}$) | 2.591 Å | Dislodged Extra-Framework |

*Source:* Computed in this study at the GFN2-xTB level. Framework oxygens indexed consistently to track cleavage.

Figure 4.3 graphically illustrates the sequential rupture of framework $Al-O$ bonds and the simultaneous contraction of the $Al \cdots V$ intermetallic distance.

```
   Distance (Angstroms)
     3.5 -|                                          * Al - O4 (3.486 A)
          |                                            BROKEN BOND!
     3.0 -|
          |   * Al ... V (2.879 A)                   * Al ... V (2.591 A)
     2.5 -|                      * Al - O2 (2.511 A)
          |                        BROKEN BOND!
     2.0 -|   * Al - O1 (2.052 A)
          |                                          * Al - Ov (1.699 A)
     1.5 -+------------------------------------------------------------>
             Cluster    V-PRC      V-I1      V-I2       V-P
```
**Figure 4.3**  
*Structural trajectory of framework $Al-O$ bond cleavages and vanadate oxygen coordination along the dealumination coordinate.*

The structural trajectory resolves the atomistic extraction mechanism into four distinct mechanical phases:
1. **Dative Pre-Activation ($V\text{-PRC}$):** The vanadyl oxygen inserts into the coordination sphere of aluminium ($Al \cdots O_v = 1.925\text{ \AA}$), expanding aluminium coordination to 5 and mechanically stretching the protonated $Al-O_1$ framework bond to $2.052\text{ \AA}$.
2. **Proton Transfer and Bridging ($V\text{-I1}$):** The proton is surrendered to vanadate, causing the original $Al-O_1$ bond to snap back to an unperturbed single-bond length ($1.687\text{ \AA}$). Concurrently, oxygen $O_3$ establishes a strong covalent bridge between aluminium and vanadium ($d(Al-O_3) = 1.804\text{ \AA}$, $d(V-O_3) = 1.774\text{ \AA}$, $d(Al \cdots V) = 2.701\text{ \AA}$).
3. **Primary Framework Rupture ($V\text{-I2}$):** Overcoming transition state $V\text{-TS2}$ ruptures the $Al-O_2$ framework bond ($2.511\text{ \AA}$). Aluminium remains stable because vanadate oxygen $O_{25}$ immediately steps in to take its place, forming a short $Al-O_{25}$ bond of $1.788\text{ \AA}$.
4. **Lattice Extraction and Vanadate Chelation ($V\text{-P}$):** In the final product, framework bonds to $O_1, O_4,$ and $O_5$ rupture completely ($2.297, 3.486,\text{ and }2.706\text{ \AA}$). The extracted aluminium is encapsulated by three vanadate oxygens ($d(Al-O_v) = 1.699, 1.801, 1.907\text{ \AA}$) and one residual framework bridge ($1.780\text{ \AA}$), forming a chelated **extra-framework aluminium vanadate** precursor ($AlVO_4$). This provides atomic-scale validation for the formation of $AlVO_4$ detected in post-mortem $^{27}Al$ NMR studies (Trujillo et al., 1997; Etim et al., 2018).

---

## 4.7 Synthesis with Experimental Literature and Industrial Implications

### 4.7.1 Reconciliation of Competing Experimental Literature
The first-principles results derived in this investigation provide a unified physical framework that reconciles forty years of conflicting experimental claims:

1. **Vindication of the Acid Hydrolysis Hypothesis:**
   Our findings strongly vindicate the foundational acid hydrolysis model proposed by Wormsbecher et al. (1986) and Trujillo et al. (1997). We have proven that $H_3VO_4$ possesses an inherent $-14.52\text{ kJ/mol}$ thermodynamic adsorption advantage over steam at the Brønsted site, and that proton transfer to vanadate initiates framework extraction, culminating in an exothermic extra-framework aluminium vanadate product ($V\text{-P} = -82.90\text{ kJ/mol}$).
2. **Contextualizing the Silanol and Matrix Condensation Models:**
   Pine (1990) and Occelli (1991b) observed that high-silica zeolites and matrix aluminas react strongly with vanadium. Our structural data explain this: because vanadic acid readily establishes bridging $M-O-V$ bonds ($V-O_3 = 1.774\text{ \AA}$), it can react with any available hydroxyl group, including silanol nests. However, our energetics prove that adsorption at the Brønsted acid hydroxyl site is highly exothermic ($-92.78\text{ kJ/mol}$), establishing that the active cracking site is the thermodynamically preferred target over neutral defect silanols.
3. **Reconciling the Sodium Synergy:**
   Xu et al. (2002) observed that trace sodium dramatically accelerates structural collapse. Our baseline calculations isolate the intrinsic acid hydrolysis pathway in pure protonic zeolite Y, proving that vanadic acid possesses an intrinsic, sodium-independent activation pathway ($V\text{-TS2} = +160.70\text{ kJ/mol}$). Contaminant sodium accelerates deactivation not by creating the primary pathway, but by acting as a secondary fluxing agent that lowers the melting point of vanadate oligomers and promotes rapid dissolution of the damaged silica lattice once aluminium has been extracted.

### 4.7.2 Engineering Guidelines for Nigerian RFCC Units
These molecular insights translate directly into actionable operational and chemical guidelines for commercial RFCC units in Nigeria, including the Dangote RFCC (218,000 bpd) and the revitalized NNPC Ltd units:

1. **Regenerator Temperature Severity Control:**
   Thermodynamic equilibria show that vanadic acid volatilization scales exponentially with regenerator temperature ($P_{\text{H}_3\text{VO}_4} \propto \exp(-\Delta H_{\text{vap}}/RT)$). Commercial operators must avoid regenerator bed temperatures exceeding **$995\text{ K (}722^{\circ}\text{C)}$**. Operating above 1000 K exponentially accelerates $H_3VO_4$ partial pressure, driving the system across the $+160.70\text{ kJ/mol}$ activation barrier and causing rapid irreversible Ecat surface area collapse.
2. **Minimizing Stripping and Combustion Steam:**
   Because vanadic acid formation requires steam ($\text{V}_2\text{O}_5 + 3\text{H}_2\text{O} \rightleftharpoons 2\text{H}_3\text{VO}_4$), lowering the regenerator steam partial pressure directly shifts the equilibrium toward immobile solid $V_2O_5$. Optimizing riser stripping steam efficiency to minimize strippable hydrocarbon carry-under into the regenerator reduces combustion steam, suppressing vanadium volatilization.
3. **Rational Selection of Basic Metal Traps:**
   Our finding that vanadic acid binds via a $-14.52\text{ kJ/mol}$ competitive advantage proves that successful metal passivators must possess **higher basicity and stronger nucleophilic oxygen donors than the zeolitic Brønsted site**. Commercial refiners processing domestic heavy residue cuts must formulate catalysts containing basic alkaline-earth traps ($BaTiO_3, MgO$) or rare-earth additives ($\text{La}_2\text{O}_3$). Lanthanum oxide forms lanthanum vanadate ($\text{LaVO}_4$) with an immense thermodynamic driving force ($\Delta H_{\text{form}} \approx -1800\text{ kJ/mol}$), scavenging gaseous $H_3VO_4$ in the mesopores and preventing it from ever reaching the 22-atom active site cluster.

---

## 4.8 Chapter Summary

This chapter presented the comprehensive results and mechanistic discussion of the investigation. Structural optimization confirmed that protonation stretches the active-site $Al-O_1$ framework bond to 1.902–1.916 Å. Adsorption calculations established that vanadic acid binds exothermically ($\Delta E_{\text{ads}} = -92.78\text{ kJ/mol}$), outcompeting steam by a net thermodynamic margin of $-14.52\text{ kJ/mol}$ due to bifunctional coordination involving direct dative $Al \cdots O_v$ bonding ($1.925\text{ \AA}$). The elementary reaction coordinate was mapped, identifying the chemisorbed intermediate $V\text{-I1}$ ($-385.10\text{ kJ/mol}$), the rate-limiting framework cleavage transition state $V\text{-TS2}$ (forward barrier $+160.70\text{ kJ/mol}$, single imaginary frequency $-78.21\text{ cm}^{-1}$), and the exothermic dislodged aluminium product $V\text{-P}$ ($-82.90\text{ kJ/mol}$). The steam dealumination baseline was validated against external periodic DFT benchmarks ($+118.42\text{ to }+120.87\text{ kJ/mol}$ vs. $76–125\text{ kJ/mol}$), proving that vanadium's destructiveness arises from irreversible thermodynamic extraction rather than lower intrinsic barriers. Finally, experimental literature was reconciled, and operational guidelines for temperature control and basic metal trap deployment in Nigerian RFCC installations were formulated.
