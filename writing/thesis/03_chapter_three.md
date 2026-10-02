# CHAPTER THREE: MATERIALS AND METHODS

## 3.1 Research Design and Conceptual Framework

This study employs a multi-tiered, first-principles computational chemistry research design to investigate the elementary reaction mechanisms and thermodynamics of vanadic acid-induced framework dealumination in zeolite Y.

Figure 3.1 depicts the conceptual framework guiding this research design. The investigation is structured as a comparative, two-pathway study evaluated across three escalating levels of electronic structure theory:
- **Pathway 1 (Vanadium Deactivation Route):** Gaseous orthovanadic acid ($H_3VO_4$) approaching, adsorbing upon, and sequentially hydrolyzing the aluminium–oxygen bonds of a representative active-site faujasite cluster ($AlSi_4O_4H_{13}$).
- **Pathway 2 (Steam Baseline Route):** A single gaseous water molecule ($H_2O$) interacting with the identical cluster model, establishing the intrinsic reference benchmark for pure hydrothermal dealumination under non-poisoned conditions.

```
       +-------------------------------------------------------------+
       |               CONCEPTUAL RESEARCH FRAMEWORK                 |
       +-------------------------------------------------------------+
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
   [PATHWAY 1: VANADIUM ROUTE]                               [PATHWAY 2: STEAM ROUTE]
   Reactants: Cluster + H3VO4                                Reactants: Cluster + H2O
         |                                                         |
         +----------------------------+----------------------------+
                                      |
                                      v
         +---------------------------------------------------------+
         |          TIER 1: SEMI-EMPIRICAL GFN2-xTB                |
         |  - Unconstrained geometry optimizations (11 states)     |
         |  - Relaxed potential energy surface coordinate scans    |
         |  - CI-NEB & OptTS transition state saddle searches      |
         |  - Harmonic frequency validation (zero vs. 1 imag mode) |
         +---------------------------------------------------------+
                                      |
                                      v
         +---------------------------------------------------------+
         |     TIER 2: HYBRID DENSITY FUNCTIONAL THEORY            |
         |  - B3LYP-D3(BJ) / def2-TZVP / RIJCOSX                   |
         |  - Geometry optimization of isolated reactants & active |
         |    site cluster (E = -1709.3941 Eh)                     |
         |  - Pre-reaction complexes (V-PRC, W-PRC)                |
         |  - Rigorous adsorption energy & competitive margin      |
         +---------------------------------------------------------+
                                      |
                                      v
         +---------------------------------------------------------+
         |       TIER 3: HIGH-LEVEL SINGLE-POINT BENCHMARK         |
         |  - PBE0-D3(BJ) / def2-TZVP / Grid5 / FinalGrid6         |
         |  - Methodological functional sensitivity analysis       |
         |  - External benchmark comparison vs. periodic DFT       |
         +---------------------------------------------------------+
                                      |
                                      v
         +---------------------------------------------------------+
         |           DATA PROVENANCE & RIGOROUS AUDITING           |
         |  - Formal 5-point transition state criteria (A1 - A5)   |
         |  - Automated, non-destructive calculation register      |
         |  - Industrial synthesis for Nigerian RFCC operation     |
         +---------------------------------------------------------+
```
**Figure 3.1**  
*Conceptual research framework and multi-tier computational strategy adopted for the investigation.*

The multi-tier strategy balances computational tractability with chemical accuracy:
1. **Tier 1 (Exploratory PES):** Semi-empirical tight-binding theory (GFN2-xTB) rapidly explores vast conformational degrees of freedom, identifying reaction intermediates, scanning breaking bonds, and generating initial guess trajectories for transition state algorithms.
2. **Tier 2 (Hybrid DFT Characterization):** Hybrid Density Functional Theory ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$) refines the geometries and electronic structures of the pristine active site, reference molecules, and pre-reaction adsorption complexes, delivering high-accuracy adsorption thermodynamics.
3. **Tier 3 (Functional Benchmarking):** The parameter-free hybrid functional ($PBE0\text{-}D3(BJ)/\text{def2-TZVP}$) validates electronic energies and reaction barriers, establishing methodological invariance and validating the steam baseline against published periodic DFT standards (Silaghi et al., 2015).

---

## 3.2 Molecular Model Systems

### 3.2.1 The Faujasite 22-Atom Active Site Cluster ($AlSi_4O_4H_{13}$)
The active catalytic site of zeolite Y is represented using a hydrogen-terminated cluster model excised from the experimental crystallographic coordinates of the faujasite (FAU) framework (Breck, 1974; Baerlocher & McCusker, n.d.).

```
                         H(13) [Brønsted Proton]
                           :
                         O(1)  [Bridging Oxygen]
                       /       \
       [SiH3]-O(2)---Al---------O(4)---[SiH3]
                      |
                     O(3)---[SiH3]
```
**Figure 3.2**  
*Schematic coordination architecture of the 22-atom $AlSi_4O_4H_{13}$ faujasite active site cluster model.*

The cluster model has the stoichiometric composition **$\text{AlSi}_4\text{O}_4\text{H}_{13}$** and comprises exactly **22 atoms**:
- **One aluminium atom ($Al$):** Occupies the central tetrahedral framework T-site.
- **Four bridging oxygen atoms ($O$):** Tetrahedrally coordinated to the central aluminium atom.
- **Four silicon atoms ($Si$):** Represent the next-nearest tetrahedral framework T-sites.
- **Twelve terminal hydrogen atoms ($H$):** Form terminal silane bonds ($Si-H$) along the original Si–O crystallographic bond vectors, neutralizing dangling covalent bonds with minimal steric perturbation (Sauer, 1989).
- **One acidic proton ($H^+$):** Coordinated to the bridging oxygen atom ($O_1$), forming the catalytically active bridging Brønsted acid hydroxyl group ($Si-O(H)-Al$) projecting into the supercage.

This 22-atom cluster captures the fundamental quantum electronic properties of the active site: local orbital hybridization, ionic-covalent bond polarization, and proton transfer thermodynamics. Because all atoms are unconstrained during geometry optimization, the cluster relaxes naturally upon adsorption and reaction, capturing local framework strain and lattice relaxation accompanying dealumination.

### 3.2.2 Mobile Reactants: Orthovanadic Acid ($H_3VO_4$) and Steam ($H_2O$)
The mobile gas-phase attacking species are modeled as isolated molecular entities:
1. **Orthovanadic Acid ($H_3VO_4$, 8 atoms):** Formulated as a monomeric, tetrahedral pentavalent vanadium complex ($V^{5+}$). The central vanadium atom is coordinated to three terminal hydroxyl groups ($-OH$) and one formal vanadyl double-bonded oxygen ($V=O$).
2. **Steam ($H_2O$, 3 atoms):** Formulated as an isolated, neutral gas-phase water molecule.

Table 3.1 specifies the atomic stoichiometry, composition, net molecular charge, and spin multiplicity for all chemical species and stationary points evaluated in this investigation.

**Table 3.1**  
*Stoichiometric specifications, atom counts, net charges, and multiplicities of all model stationary points*

| System Label | Chemical Identity / Stationary State Role | Stoichiometric Formula | Total Atoms | Net Charge | Multiplicity ($2S+1$) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Cluster** | Pristine FAU active-site Brønsted hydroxyl model | $AlSi_4O_4H_{13}$ | 22 | 0 | 1 (Singlet) |
| **H3VO4** | Isolated gas-phase orthovanadic acid reactant | $H_3VO_4$ | 8 | 0 | 1 (Singlet) |
| **H2O** | Isolated gas-phase steam molecule reactant | $H_2O$ | 3 | 0 | 1 (Singlet) |
| **V-PRC** | Vanadic acid pre-reaction adsorption complex | $AlSi_4O_8H_{16}V$ | 30 | 0 | 1 (Singlet) |
| **V-I1** | Chemisorbed vanadate reaction intermediate | $AlSi_4O_8H_{16}V$ | 30 | 0 | 1 (Singlet) |
| **V-TS2** | Transition state for 1st framework $Al-O$ bond cleavage | $AlSi_4O_8H_{16}V$ | 30 | 0 | 1 (Singlet) |
| **V-I2** | Partially hydrolysed dealumination intermediate | $AlSi_4O_8H_{16}V$ | 30 | 0 | 1 (Singlet) |
| **V-P** | Final extracted aluminium-vanadate product complex | $AlSi_4O_8H_{16}V$ | 30 | 0 | 1 (Singlet) |
| **W-PRC** | Steam pre-reaction adsorption complex | $AlSi_4O_5H_{15}$ | 25 | 0 | 1 (Singlet) |
| **W-TS** | Transition state for 1st steam $Al-O$ bond cleavage | $AlSi_4O_5H_{15}$ | 25 | 0 | 1 (Singlet) |
| **W-P** | Hydrolysed silanol/aluminol steam product complex | $AlSi_4O_5H_{15}$ | 25 | 0 | 1 (Singlet) |

*Source:* Formulated for this study. All species have closed-shell singlet ground states.

---

## 3.3 Computational Chemistry Software and Execution Platforms

All quantum chemical simulations were performed using the **ORCA quantum chemistry program package** (Version 6.1.1, release 2026; Neese, 2012; Neese et al., 2020). ORCA was selected for its exceptional efficiency in resolving electronic structures, advanced second-order SCF convergence algorithms, automated transition state search routines, and native integration of semi-empirical tight-binding methods.

Molecular visualization, cluster excision, initial reaction coordinate assembly, and vibrational normal mode animations were performed using:
- **Avogadro (Version 1.2.0; Hanwell et al., 2012):** Initial 3D molecular structure building, bond distance measurements, and Cartesian coordinate editing.
- **VESTA 3 (Momma & Izumi, 2011):** Crystallographic visualization of the bulk faujasite unit cell and verification of T-site coordination polyhedra.
- **Spartan '14 (Wavefunction, Inc., Irvine, CA):** Exploratory molecular mechanics force-field pre-optimizations.
- **Python 3.11:** Algorithmic automation, calculation register management, CSV parsing, and statistical data visualization.

High-level DFT calculations and intensive geometry optimizations were executed remotely on dedicated high-performance cloud virtual machine infrastructure (**Azure VM instance: `orca-bus`**, Ubuntu Linux 22.04 LTS, 4 dedicated vCPUs, Intel Xeon Platinum 8272CL @ 2.60 GHz, 8 GB RAM, high-speed NVMe storage). Parallel execution was achieved using OpenMPI 4.1.6, configured with custom memory-channel allocations (`rmaps_base_oversubscribe = 1`, `hwloc_base_use_hwthreads_as_cpus = 1`) to ensure full parallel utilization of all CPU hardware threads.

Table 3.2 details the software tools, versions, and execution environments deployed.

**Table 3.2**  
*Computational software environments, specifications, and hardware resource allocation*

| Software Package | Version / Release | Primary Analytical Function | Execution Environment |
| :--- | :---: | :--- | :--- |
| **ORCA** | 6.1.1 (64-bit Linux) | Ab initio DFT, GFN2-xTB, OptTS, analytical Hessians | Azure Cloud VM (`orca-bus`, 4 vCPUs) |
| **OpenMPI** | 4.1.6 | Message Passing Interface for parallel ORCA runs | Linux Ubuntu 22.04 LTS |
| **Avogadro** | 1.2.0 | Cartesian coordinate editing and visual inspection | Local Workstation (Windows 11) |
| **VESTA** | 3.5.8 | Crystallographic verification of FAU framework | Local Workstation (Windows 11) |
| **Python** | 3.11.9 | Automation pipelines, parsing, and manifest auditing | Local & Remote Environments |
| **tmux** | 3.2a | Persistent background session management | Remote Azure VM Terminal |

*Source:* Author's computational environment inventory.

---

## 3.4 Multi-Tier Computational Protocol

### 3.4.1 Tier 1: Semi-Empirical GFN2-xTB Exploratory Mapping
The first computational tier deployed the **GFN2-xTB** semi-empirical method developed by Bannwarth, Ehlert, and Grimme (2019), accessed natively through ORCA 6.1.1. GFN2-xTB is a self-consistent tight-binding quantum mechanical method parameterized across elements up to atomic number 86. It incorporates:
- Second-order density-dependent electrostatics via isotropic atomic charges and anisotropic atom-centered multipole moments (dipoles and quadrupoles).
- Dynamic, geometry-dependent D4 London dispersion energy corrections.
- Analytical first and second derivatives, enabling rapid geometry optimization and harmonic vibrational frequency calculations at 1/1000th the computational cost of hybrid DFT.

In Tier 1:
- Unconstrained geometry optimizations were performed on all 11 model systems using tight convergence criteria:
  ```orca
  ! XTB2 TightOpt
  ```
- Harmonic vibrational frequencies were calculated analytically (`! XTB2 FREQ`) at the converged geometries to confirm that each stationary point corresponded to a true local minimum (zero imaginary frequencies, $N_{\text{imag}} = 0$).
- Relaxed one-dimensional potential energy surface (PES) coordinate scans were performed by incrementally stretching targeted framework $Al-O$ and $Si-O$ bonds in steps of $0.05\text{ \AA}$ while allowing all remaining degrees of freedom to relax, identifying approximate barrier crests.
- Saddle searches were conducted using Climbing Image Nudged Elastic Band (CI-NEB) chains containing 8 to 16 geometric images, followed by Transition State Optimization (`! XTB2 OptTS NumFreq`) starting from the highest-energy band image.

### 3.4.2 Tier 2: Hybrid DFT ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$) Optimizations
In the second computational tier, stationary points of primary chemical interest were refined using high-level hybrid Density Functional Theory:
- **Exchange-Correlation Functional:** Becke’s three-parameter hybrid exchange functional paired with the Lee-Yang-Parr correlation functional (**B3LYP**; Becke, 1993; Lee et al., 1988), which incorporates 20% exact Hartree-Fock exchange.
- **Empirical Dispersion Correction:** Grimme’s third-generation empirical dispersion with Becke-Johnson rational damping (**D3(BJ)**; Grimme et al., 2010, 2011), essential for capturing non-covalent van der Waals forces between incoming adsorbates and the zeolitic cluster.
- **Basis Set:** Weigend and Ahlrichs’ balanced, split-valence triple-$\zeta$ basis set augmented with polarization functions (**def2-TZVP**; Weigend & Ahlrichs, 2005) for all atoms ($V, Al, Si, O, H$).
- **Coulomb & Exchange Acceleration:** The Resolution of Identity approximation for the Coulomb matrix paired with the Chain of Spheres algorithm for Hartree-Fock exchange (**RIJCOSX**; Neese et al., 2020), utilizing the matching **def2/J** auxiliary basis set. This accelerated two-electron integral evaluations by a factor of 10 to 30 without loss of chemical accuracy.
- **Integration Grids:** Standard DefGrid3 for geometry optimizations, ensuring high numerical precision in grid-based numerical quadrature.
- **SCF Convergence:** TightSCF criteria, enforcing convergence tolerances of $1.0 \times 10^{-8}\ E_h$ in energy change and $1.0 \times 10^{-5}$ in root-mean-square density matrix change, accelerated by Second-Order SCF (SOSCF) routines.

The typical ORCA input specification for Tier 2 optimizations was:
```orca
! B3LYP D3BJ def2-TZVP def2/J RIJCOSX TightSCF TightOpt
%pal nprocs 4 end
```

Analytical harmonic vibrational frequencies were computed at the converged geometries to confirm zero imaginary modes for minima and extract zero-point vibrational energies (ZPE).

### 3.4.3 Tier 3: High-Level Single-Point Energy Benchmarking
To eliminate functional-specific bias and evaluate methodological sensitivity, all stationary-point geometries were evaluated at **Tier 3** using the parameter-free hybrid functional **PBE0** (Adamo & Barone, 1999):
- **Functional:** PBE0-D3(BJ), incorporating 25% exact Hartree-Fock exchange.
- **Basis Set:** def2-TZVP with def2/J auxiliary fitting.
- **Quadrature Precision:** High-density numerical grids (**Grid5** angular grid with a pruned **FinalGrid6** quadrature at the final SCF cycle).
- **Execution:** Full 8-way parallel task allocation.

Table 3.3 summarizes the computational parameterization across all three tiers.

**Table 3.3**  
*Detailed parameterization of theoretical model chemistries across the three computational tiers*

| Computational Parameter | Tier 1 (Exploratory PES) | Tier 2 (Hybrid DFT Optimization) | Tier 3 (Functional Benchmark) |
| :--- | :--- | :--- | :--- |
| **Theoretical Method** | Semi-Empirical GFN2-xTB | Hybrid DFT: B3LYP-D3(BJ) | Hybrid DFT: PBE0-D3(BJ) |
| **Exact HF Exchange** | None | 20% | 25% |
| **Basis Set** | Atom-centered TB basis | Ahlrichs def2-TZVP | Ahlrichs def2-TZVP |
| **Auxiliary Fitting** | None | def2/J Coulomb fitting | def2/J Coulomb fitting |
| **Numerical Integration** | Tight coordinate tolerances | DefGrid3 (ORCA standard) | Grid5 / FinalGrid6 (Ultra-fine) |
| **SCF Tolerance** | $1.0 \times 10^{-6}\ E_h$ | $1.0 \times 10^{-8}\ E_h$ (TightSCF) | $1.0 \times 10^{-8}\ E_h$ (TightSCF) |
| **Geometry Optimization** | TightOpt (Full unconstrained) | TightOpt (Full unconstrained) | Single-Point Energy on T1/T2 Geoms |
| **Primary Output** | PES topologies, saddle guesses | Equilibrium geometries, $\Delta E_{\text{ads}}$ | Methodological sensitivity, barriers |

*Source:* Formulated for this investigation.

---

## 3.5 Stationary Point Search and Transition State Verification Protocol

To prevent the reporting of spurious mathematical artifacts or unconverged saddle points, this study enforced a strict **five-point formal verification protocol (A1–A5)** for every transition state candidate, summarized in Table 3.4.

**Table 3.4**  
*The five-point formal saddle-point verification criteria (A1–A5) enforced in this study*

| Rule Index | Verification Rule | Algorithmic Criterion & Mathematical Requirement | Action Upon Failure |
| :---: | :--- | :--- | :--- |
| **A1** | **Normal Termination** | ORCA process must exit with `****ORCA TERMINATED NORMALLY****`. | Execution discarded; re-run with modified SCF damping. |
| **A2** | **Gradient Convergence** | Max gradient $< 1.0 \times 10^{-4}\text{ a.u.}$; RMS gradient $< 3.0 \times 10^{-5}\text{ a.u.}$; Energy change $< 1.0 \times 10^{-6}\ E_h$. | Optimization continued; step size dampened. |
| **A3** | **Mode Count** | Diagonalized Cartesian Hessian must possess **exactly one** negative eigenvalue ($\nu_1 < 0\text{ cm}^{-1}$; $N_{\text{imag}} = 1$). All other normal modes must be strictly real ($\nu_i > 0$). | If $N_{\text{imag}} > 1$, structure is a higher-order saddle; re-optimize along unwanted modes. |
| **A4** | **Two-Sided Displacement** | Displace structure by $\pm 0.01–0.05\text{ \AA}$ along the single imaginary normal mode eigenvector; unconstrained local optimization from displaced geometries must connect forward to designated product and reverse to reactant minimum. | If both directions return to same minimum, saddle does not connect claimed states; labeled "not established". |
| **A5** | **Preceding Intermediate** | The putative preceding intermediate must be an authenticated local minimum possessing $N_{\text{imag}} = 0$. | Intermediate re-optimized until confirmed true minimum. |

*Source:* Formulated from best practices in computational reaction engineering (Jensen, 2017).

Transition state searches were executed via a two-stage algorithm:
1. **Double-Ended Chain Search (CI-NEB):** An initial chain of 8 to 16 geometric images interpolating between reactant minimum $\mathbf{R}$ and product minimum $\mathbf{P}$ was optimized using the Climbing Image Nudged Elastic Band algorithm. The highest-energy image was driven upward along the reaction path to locate the crest of the barrier.
2. **Eigenvector-Following Refinement (OptTS):** The coordinates of the climbing image were transferred to the quasi-Newton OptTS algorithm (`! OptTS`), which calculates or updates the exact Cartesian Hessian and steps uphill along the lowest Hessian eigenvector while minimizing gradients along all other $3N-7$ orthogonal degrees of freedom.

---

## 3.6 Energetic Formulations and Thermochemical Accounting

### 3.6.1 Adsorption Energy ($\Delta E_{\text{ads}}$) and Competitive Margin
The non-covalent adsorption energy ($\Delta E_{\text{ads}}$) of an incoming gas-phase molecule ($A = H_3VO_4\text{ or }H_2O$) at the zeolitic active site is defined as:

$$\Delta E_{\text{ads}}(A) = E_{\text{complex}}(A\text{-PRC}) - \left[ E_{\text{cluster}} + E_{\text{gas}}(A) \right]$$

where:
- $E_{\text{complex}}(A\text{-PRC})$ is the total electronic energy of the optimized pre-reaction complex.
- $E_{\text{cluster}}$ is the total electronic energy of the unperturbed 22-atom active site cluster.
- $E_{\text{gas}}(A)$ is the total electronic energy of the isolated, relaxed gas-phase molecule ($H_3VO_4$ or $H_2O$).

Under this thermodynamic sign convention, exothermic adsorption yields negative values ($\Delta E_{\text{ads}} < 0$).

The **competitive adsorption margin ($\Delta\Delta E_{\text{ads}}$)** quantifying the thermodynamic advantage of vanadic acid over steam for access to the Brønsted acid site is defined as:

$$\Delta\Delta E_{\text{ads}} = \Delta E_{\text{ads}}(H_3VO_4) - \Delta E_{\text{ads}}(H_2O)$$

A negative margin ($\Delta\Delta E_{\text{ads}} < 0$) demonstrates that vanadic acid binds more strongly than steam, driving selective adsorption even in dilute gas-phase concentrations.

### 3.6.2 Reaction Energy ($\Delta E_{\text{rxn}}$) and Activation Barriers ($\Delta E^{\ddagger}$)
Along the reaction coordinate, the relative electronic energy of any stationary state $i$ with respect to the separated initial reactants is defined as:

$$\Delta E_i = E_i - \left[ E_{\text{cluster}} + E_{\text{gas}}(A) \right]$$

For an elementary reaction step transforming intermediate $\mathbf{I}_j$ to intermediate $\mathbf{I}_{j+1}$ through transition state $\mathbf{TS}$, the **forward activation barrier ($\Delta E^{\ddagger}_{\text{fwd}}$)** and **reverse activation barrier ($\Delta E^{\ddagger}_{\text{rev}}$)** are defined as:

$$\Delta E^{\ddagger}_{\text{fwd}} = E(\mathbf{TS}) - E(\mathbf{I}_j)$$
$$\Delta E^{\ddagger}_{\text{rev}} = E(\mathbf{TS}) - E(\mathbf{I}_{j+1})$$

The overall elementary reaction energy for the step is given by:

$$\Delta E_{\text{step}} = E(\mathbf{I}_{j+1}) - E(\mathbf{I}_j) = \Delta E^{\ddagger}_{\text{fwd}} - \Delta E^{\ddagger}_{\text{rev}}$$

All energies were converted from atomic units (Hartrees, $E_h$) to standard chemical units (kilojoules per mole, $\text{kJ/mol}$) using the standard conversion factor:

$$1\ E_h = 2625.499638\text{ kJ/mol}$$

---

## 3.7 Calculation Register and Data Provenance Protocol

To ensure absolute scientific reproducibility and audit integrity, all computational runs were governed by a **strict data provenance protocol**:
1. **Unique Job Identifiers:** Every ORCA calculation was assigned an immutable alphanumeric identifier encoding its computational tier, sequential index, system label, and theoretical method (e.g., `s1_01_h2o_optfreq`, `s1_03_cluster_optfreq`).
2. **Versioned CSV Manifests:** Calculation outcomes were automatically appended to structured manifest files (`manifest_scope1.csv`, `manifest_scope2.csv`, `manifest_scope3.csv`, `manifest_scope4.csv`) tracking job name, theoretical level, convergence status (`PASS`/`FAIL`/`SKIP`), final electronic energy ($E_h$), execution wall clock time (seconds), and absolute output file paths.
3. **Non-Destructive File Policy:** If a calculation was repeated with modified parameters, previous output logs were preserved by appending version timestamps (`_V02.out`), guaranteeing that failed trials, SCF convergence difficulties, and saddle-search histories remain permanently auditable.
4. **Automated Auditing:** An independent Python audit script (`audit_tier2.py`) parsed completed outputs, verified normal termination strings, extracted final energies, and compiled summary registers without manual transcription.

---

## 3.8 Chapter Summary

This chapter detailed the complete computational materials and methods deployed in this study. The molecular model systems were defined, comprising the 22-atom $AlSi_4O_4H_{13}$ faujasite active site cluster and gas-phase $H_3VO_4$ and $H_2O$ reactants. The multi-tier theoretical framework was formulated across semi-empirical GFN2-xTB (Tier 1), hybrid DFT $B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$ (Tier 2), and high-level $PBE0\text{-}D3(BJ)/\text{def2-TZVP}$ single-point benchmarking (Tier 3), executed via ORCA 6.1.1 on high-performance cloud infrastructure. The five-point saddle verification criteria (A1–A5), thermodynamic formulations for adsorption and barrier heights, and automated calculation registers were formally established, providing the rigorous foundation for the results presented and discussed in Chapter Four.
