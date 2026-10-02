---
lang: en
---

\newpage

# CHAPTER THREE

# 3.0 MATERIALS AND METHODS

## 3.1 Research Design

The study is designed as a two-tier quantum chemical investigation of two competing reaction pathways on a single molecular model of the active region of zeolite Y, followed by a final-level refinement of the energetics of the complete stationary-point set.

The design rests on four decisions.

**One model, two pathways.** Vanadic-acid-assisted dealumination and steam-only hydrolysis are computed on the same cluster, with the same atom ordering, the same reference species, and the same energy bookkeeping. Because the two routes differ only in the attacking molecule, every comparison between them is a comparison of chemistry rather than of model construction.

**A cheap tier for the landscape, an accurate tier for the numbers.** The complete pathway is first mapped at the GFN2-xTB semi-empirical level (Tier 1), where a stationary-point search costs seconds to minutes and the whole landscape can be explored without consuming the project's computing budget. The confirmed stationary points are then re-optimised at dispersion-corrected hybrid DFT (Tier 2), and the final energetics are evaluated at a second hybrid functional and with a basis-set superposition correction (Tier 3). Mechanistic conclusions are drawn from the hybrid DFT numbers; the semi-empirical tier supplies the geometry map, the candidate saddle points, and an independent cross-check on every energetic trend.

**Verification before interpretation.** Each calculation passes a stated acceptance gate before its energy is allowed into a table: minima must show a converged optimisation with no imaginary vibrational modes, and saddle-point candidates must show exactly one imaginary mode whose displacement vector moves the reacting bonds and must connect the claimed reactant and product minima when displaced along that mode in both directions. Jobs that do not pass a gate are recorded with their verdict and excluded from the reported energetics.

**Reproducibility as a design requirement.** Every job is stored, named, and indexed in a calculation register that links the reported energy to its input file, output log, final geometry, software version, and acceptance verdict. This register is the direct source of the tables in Chapter Four; no number is transcribed by hand from a log into a table.

## 3.2 The Model System

### 3.2.1 The faujasite cluster

The active site of zeolite Y is represented by a hydrogen-terminated cluster of the faujasite framework, cut around one framework aluminium atom and its four neighbouring silicon T-sites. The cluster has the composition AlSi4O4H13 and 22 atoms: one aluminium, four bridging oxygens, four silicon atoms, and thirteen hydrogen atoms.

The connectivity reproduces the two features that constitute the catalytically active site. First, the aluminium is tetrahedrally coordinated by four bridging oxygens, each of which is bonded to one silicon atom, so that the local Al-O-Si framework topology of faujasite is preserved. Second, one of the four bridging oxygens additionally carries a proton, giving the bridging hydroxyl group Si-O(H)-Al that is the Brønsted acid site of the zeolite. In the optimised cluster this protonated oxygen is the most weakly bound to aluminium (Al-O = 0.192 nm against 0.169-0.170 nm for the three unprotonated bridges) and the O-H distance is 0.096 nm, the geometric signature of a Brønsted acid site.

The cluster is terminated at the four silicon atoms by three hydrogen atoms each, placed along the directions of the framework bonds that were cut, at a silicon-hydrogen distance chosen so that the capping groups reproduce the electronic effect of the continuation of the lattice without introducing artificial strain. All peripheral silicon-hydrogen and aluminium-oxygen distances are monitored after every optimisation; a rearrangement of the capping groups, rather than of the reacting site, is treated as a model fault and corrected before the structure is accepted.

### 3.2.2 The attacking species

The mobile vanadium species is represented by vanadic acid, H3VO4, the V(V) molecule formed from vanadium pentoxide in the steam-rich regenerator and identified experimentally as the volatile poison of FCC catalysts (Wormsbecher et al., 1986). Vanadic acid is a strong acid of the phosphoric acid family and carries both a Lewis-basic V=O oxygen and acidic hydroxyl groups, which is what allows it to interact simultaneously with the Brønsted proton and with the framework aluminium during attack. Water, H2O, is computed as the reference attacking molecule of the steam-only baseline.

Both species are optimised as isolated molecules in the gas phase before any complex is built, and their energies define, together with the bare cluster, the reference zeros of the two pathways (Section 3.6).

### 3.2.3 The stationary-point set

Eleven states are computed, listed in Table 3.1. The vanadium route comprises the isolated reference state, the pre-reaction complex, the chemisorbed intermediate, two successive aluminium-oxygen cleavage transition structures, the hydrolysed intermediate in which the framework has opened, the third cleavage transition structure, and the dealuminated product in which the aluminium has been extracted as extra-framework material. The steam route comprises the water pre-reaction complex, its hydrolysis transition structure, and the corresponding product.

Every state keeps the same atom ordering: the 22 cluster atoms first, in an invariant order, followed by the atoms of the adsorbate. This convention is what makes the states directly comparable, it allows a rigid-body approach trajectory to be computed between the same two atoms in every file, and it permits the framework and the adsorbate to be addressed as two fragments in the counterpoise calculations of Section 3.4.4.

**Table 3.1**

*Stationary-point set defining the two reaction pathways of this study*

| State | Role in the pathway | Composition | How the structure was obtained |
|---|---|---|---|
| cluster | Reference: bare Brønsted acid site | AlSi4O4H13 (22 atoms) | Optimised from the idealised faujasite cut |
| H3VO4 | Reference: isolated vanadic acid | H3VO4 (8 atoms) | Optimised isolated molecule |
| H2O | Reference: isolated water | H2O (3 atoms) | Optimised isolated molecule |
| V-R | Isolated reference state, vanadium route | cluster + H3VO4 (30 atoms) | H3VO4 placed at non-interacting distance |
| V-PRC | Pre-reaction complex | cluster + H3VO4 (30 atoms) | Hydrogen-bonded docking at the Brønsted proton |
| V-I1 | Chemisorbed intermediate | cluster + H3VO4 (30 atoms) | Optimisation from the chemisorption saddle guess |
| V-TS1 | Chemisorption transition structure | cluster + H3VO4 (30 atoms) | Relaxed scan, NEB and eigenvalue-following search |
| V-TS2 | First Al-O cleavage transition structure | cluster + H3VO4 (30 atoms) | NEB and OptTS refinement from the curated seed |
| V-I2 | Hydrolysed intermediate (framework opened) | cluster + H3VO4 (30 atoms) | Optimisation from the first-cleavage product side |
| V-TS3 | Final Al-O cleavage transition structure | cluster + H3VO4 (30 atoms) | NEB and OptTS refinement from the curated seed |
| V-P | Dealuminated product (EFAL) | cluster + H3VO4 (30 atoms) | Optimisation from the final-cleavage product side |
| W-PRC | Steam pre-reaction complex | cluster + H2O (25 atoms) | Water docked at the Brønsted proton |
| W-TS | Steam hydrolysis transition structure | cluster + H2O (25 atoms) | NEB and OptTS refinement |
| W-P | Steam dealuminated product | cluster + H2O (25 atoms) | Optimisation from the cleavage product side |

*Source:* Author.

## 3.3 Software Tools

All electronic-structure calculations were performed with ORCA 6.1, a freely licensed academic quantum chemistry package that provides, within one input format, the semi-empirical tight-binding method used for Tier 1, the hybrid DFT methods used for Tier 2 and Tier 3, nudged elastic band and eigenvalue-following transition-state searches, and analytic or numerical vibrational analysis. Using one program for every tier guarantees that the geometry conventions, the atom ordering, and the energy definitions are identical across levels, which is what makes the cross-level comparison of Section 3.7 possible.

Molecular structures were assembled, inspected, and corrected in Avogadro 2 and Spartan, and the crystal reference for the faujasite framework was displayed in VESTA. Energy processing, pathway tables, and figures were produced with Python 3 scripts that read the ORCA outputs directly, so that every value plotted or tabulated is derived from the calculation log rather than re-entered by hand. Cloud sessions were managed with tmux and rsync, which keep long jobs alive through disconnections and synchronise results back to the project archive immediately after each batch.

**Table 3.2**

*Software tools, versions, and their role in the workflow*

| Tool | Role in this study |
|---|---|
| ORCA 6.1 | All semi-empirical and DFT calculations: geometry optimisation, nudged elastic band and transition-state searches, vibrational analysis, single-point energies, counterpoise corrections |
| Avogadro 2 | Assembly, editing, and visual inspection of the cluster and the adsorbate complexes |
| Spartan | Independent structure building and visual checking of connectivity |
| VESTA | Display and orientation of the faujasite (FAU) framework reference |
| Python 3 (standard library, NumPy, matplotlib) | Register maintenance, energy bookkeeping, validation scripts, tables, and figures |
| tmux, rsync | Persistent cloud sessions and synchronisation of results to the project archive |

*Source:* Author.

## 3.4 Computational Levels and Settings

### 3.4.1 Tier 1: semi-empirical mapping (GFN2-xTB)

The complete reaction landscape is explored with the GFN2-xTB tight-binding Hamiltonian through the ORCA interface. The method reproduces geometries and reaction energies of organic and main-group systems at a small fraction of the cost of DFT, which allows the full stationary-point sequence — optimisations, relaxed scans along the reacting bonds, nudged elastic band searches, and frequency checks — to be carried out on the local workstation. Tier 1 establishes the connectivity of every state, the identity of the intermediates, the candidate transition structures, and a first, internally consistent set of relative energies.

### 3.4.2 Tier 2: hybrid DFT geometries and frequencies

Every Tier 1 minimum is re-optimised at the B3LYP level with the D3(BJ) dispersion correction and the def2-TZVP basis set, using the resolution-of-identity chain-of-spheres approximation for the Coulomb and exchange terms (RIJCOSX) with the matching def2/J auxiliary basis. Saddle-point candidates are refined with an eigenvalue-following optimiser from the Tier 1 geometry, with an exact initial Hessian, and each stationary point is submitted to a vibrational analysis in the same job. Tight self-consistent-field convergence and a production-grade integration grid are used throughout, and every state is computed as a closed-shell singlet.

The B3LYP-D3(BJ)/def2-TZVP combination is a standard, widely benchmarked choice for zeolite cluster chemistry: the hybrid functional captures the localised electronic reorganization of bond breaking and forming, the dispersion correction is essential for the hydrogen-bonded pre-reaction complexes, and the triple-zeta basis describes the aluminium, silicon, and vanadium centres consistently.

### 3.4.3 Tier 3: final-level single points and second functional

The final electronic energies of the refined geometries are evaluated at the PBE0-D3(BJ)/def2-TZVP level. PBE0 contains 25 per cent exact exchange, which makes it a genuinely independent check on the B3LYP description rather than a variation of it; agreement between the two functionals on the ranking of the states and on the sign of every step is the study's principal defence against functional-dependent conclusions.

### 3.4.4 Basis-set superposition correction

For the two adsorption complexes, V-PRC and W-PRC, the interaction energy is also computed with the Boys-Bernardi counterpoise correction. The framework and the adsorbate are defined as two fragments, and the calculation is repeated with each fragment in turn represented by its basis functions only, at the geometry of the complex, so that the energy of each fragment is evaluated in the presence of the basis set of its partner. The counterpoise-corrected interaction energy removes the basis-set superposition error that otherwise inflates the computed binding of the adsorbate, an effect that is proportionally most important in exactly the comparison this study makes, since vanadic acid and water draw on the framework basis to different extents.

### 3.4.5 Thermodochemistry at process temperature

Vibrational analysis of the refined structures supplies, in addition to the imaginary-mode audit, the thermochemical functions of each state. Each frequency calculation reports the zero-point energy and the Gibbs free energy correction at 298.15 K and at 1003.15 K, the latter being the working temperature of the FCC regenerator (730 °C). The high-temperature correction is what allows the computed stability ordering of the states to be discussed in terms of the operating process rather than at standard conditions, and the low-temperature correction provides the standard-state values used for comparison with published work.

**Table 3.3**

*Computational levels, settings, and the reason for each choice*

| Tier | Method and settings | Purpose and reason for the choice |
|---|---|---|
| 1 | GFN2-xTB (GFN2 tight binding) | Complete pathway mapping, relaxed scans, NEB searches, and frequency checks at negligible cost; establishes connectivity and candidate saddles before DFT is attempted |
| 2 | B3LYP-D3(BJ)/def2-TZVP, RIJCOSX with def2/J, tight SCF, production grid | Geometry and vibrational level of the study; hybrid functional for bond reorganization, dispersion correction for hydrogen bonding, triple-zeta basis for Al, Si and V |
| 2 | OptTS with exact initial Hessian, frequency analysis in the same job | Localisation of first-order saddle points and immediate verification of the imaginary mode count |
| 3 | PBE0-D3(BJ)/def2-TZVP single points on Tier 2 geometries | Independent second functional for the final ranking of states without dependence on a single exchange-correlation functional |
| 3 | Boys-Bernardi counterpoise with framework and adsorbate as fragments | Removal of basis-set superposition error from the competitive adsorption comparison |
| 2-3 | Frequency analysis with thermochemistry at 298.15 K and 1003.15 K | Zero-point and Gibbs corrections at standard and at regenerator temperature |
| All | Closed-shell singlet, neutral charge; identical atom ordering in every file | Physical consistency of the model and comparability of every state on one energy scale |

*Source:* Author.

## 3.5 Step-by-Step Procedure

**Step 1 — Reference species.** The bare cluster, vanadic acid, and water were optimised and submitted to vibrational analysis, and the resulting geometries were checked against the expected bond-length ranges (silicon-oxygen about 0.162 nm, aluminium-oxygen 0.170-0.192 nm, with the longest aluminium-oxygen bond at the protonated bridge). The three reference energies define the zeros of the two pathways.

**Step 2 — Pre-reaction complexes.** Vanadic acid was docked at the Brønsted proton through its V=O oxygen to form the hydrogen-bonded pre-reaction complex V-PRC, and a second orientation was prepared by rotating the molecule about the hydrogen-bond axis; the lower-energy converged structure was retained and the energy spread between the two orientations recorded. The water complex W-PRC was prepared in the same way. A separate non-interacting reference state, V-R, was built with the adsorbate at a distance from the framework; after optimisation it converged into the same basin as V-PRC, which is itself a result: it establishes that the approach of vanadic acid to the Brønsted site carries no barrier, and that the two files describe one physical state.

**Step 3 — Chemisorbed intermediate.** Starting from the chemisorption saddle guess, with the forming aluminium-oxygen bond shortened and the acidic proton of vanadic acid fully transferred to the framework, V-I1 was optimised to a stable minimum. In the converged structure the aluminium retains four framework oxygen neighbours at 0.169-0.180 nm, with the vanadium centre held at 0.270 nm from the aluminium: the adsorbate is bound at the site, and no framework bond has yet been broken.

**Step 4 — First cleavage (V-TS2, V-I2).** The first aluminium-oxygen cleavage was mapped by a relaxed scan along the breaking bond, followed by a nudged elastic band search between the confirmed endpoints and an eigenvalue-following refinement of the saddle. The converged transition structure carries exactly one imaginary mode, whose displacement vector describes the breaking aluminium-oxygen bond and the concerted proton transfer. The product of this step, V-I2, is the hydrolysed intermediate in which the framework has opened and two silanol groups have been formed; its geometry was obtained by completing the cleavage in the direction indicated by the saddle and re-optimising.

**Step 5 — Final cleavage and product (V-TS3, V-P).** The same three-stage protocol — scan, band search, saddle refinement — was applied to the second cleavage, in which the aluminium is released from its remaining framework bonds. The product state V-P contains the extracted aluminium as extra-framework material together with the silanol-terminated framework, and is the end point against which the overall thermodynamic feasibility of the vanadium route is judged.

**Step 6 — Steam baseline (W-PRC, W-TS, W-P).** The corresponding hydrolysis sequence was computed for water on the same cluster, giving the steam pre-reaction complex, its transition structure, and its product. This is the route against which the published periodic DFT barrier range for steam dealumination is used as an external benchmark.

**Step 7 — Tier 2 refinement.** Every Tier 1 minimum was re-optimised at B3LYP-D3(BJ)/def2-TZVP, and every Tier 1 saddle candidate was refined with the eigenvalue-following optimiser from its own geometry. Each refined structure was checked for retention of the intended connectivity, its imaginary-mode count was recorded, and its final energy and geometry were written to the register.

**Step 8 — Tier 3 evaluation.** PBE0-D3(BJ)/def2-TZVP single points were evaluated on the refined Tier 2 geometries, and the counterpoise correction was applied to the two adsorption complexes. The thermochemical analysis at 298.15 K and 1003.15 K was carried out from the Tier 2 vibrational data.

**Step 9 — Analysis.** The pathways were assembled into energy tables and profile figures directly from the register by Python scripts, the two functional levels were compared state by state, the adsorption competition was evaluated with and without the counterpoise correction, and the steam barrier was compared with the published benchmark range.

## 3.6 Computed Quantities and Energy Bookkeeping

Two reference zeros are used, one per pathway. The vanadium route is referenced to the separated framework cluster and vanadic acid molecule,

E_ref,V = E(cluster) + E(H3VO4)

and the steam route to the separated cluster and water molecule,

E_ref,W = E(cluster) + E(H2O).

For each stationary point the following quantities are reported:

1. **Relative electronic energy**, ΔE = E(state) - E_ref, in kJ mol-1.
2. **Zero-point-corrected relative energy**, ΔE + ΔZPE, using the zero-point energy obtained from the vibrational analysis.
3. **Relative Gibbs free energy**, ΔG = ΔE + Δ(G - E), using the Gibbs correction reported at 298.15 K and at 1003.15 K.
4. **Interaction (adsorption) energy** of the pre-reaction and chemisorbed complexes, E(state) - E(cluster) - E(adsorbate), reported both uncorrected and with the Boys-Bernardi counterpoise correction.
5. **Activation barriers**, expressed as the energy of the transition structure relative to the state that precedes it in the pathway, and reported together with the reverse barrier where the step is reversible in principle.
6. **Structural descriptors** for every state: the aluminium-oxygen distances, the vanadium-oxygen distances, the aluminium-vanadium separation, and the number and position of the protons transferred, which together define what has and has not changed at each step.

Energies are converted from Hartree to kJ mol-1 with 1 Eh = 2625.499638 kJ mol-1 and reported to 0.01 kJ mol-1, which is the precision of the printed quantities; the discussion in Chapter Four rounds differences to the accuracy justified by the method. Negative values denote stabilisation relative to the reference zero throughout.

**Table 3.4**

*Energy quantities computed for each stationary point and pathway*

| Quantity | Definition | Reported for |
|---|---|---|
| ΔE | E(state) - E_ref (electronic) | Every state, both pathways |
| ΔE + ΔZPE | Electronic energy with zero-point correction | Every state with a frequency calculation |
| ΔG (298.15 K), ΔG (1003.15 K) | Electronic energy with the Gibbs correction at standard and regenerator temperature | Every state with a frequency calculation |
| Adsorption energy, uncorrected | E(complex) - E(cluster) - E(molecule) | Pre-reaction and chemisorbed complexes |
| Interaction energy, counterpoise-corrected | Same quantity with the Boys-Bernardi correction from the two ghost-fragment calculations | V-PRC and W-PRC |
| Activation barrier | E(transition structure) - E(preceding state) | Every localised transition structure |
| Structural descriptors | Al-O, V-O, Al...V distances; proton inventory | Every state |

*Source:* Author.

## 3.7 Validation Plan

Six validation anchors were applied before any computed number was interpreted. They are listed in Table 3.5.

**Geometry gate.** Each minimum must show a converged geometry optimisation and, on vibrational analysis, no imaginary frequency. Bond lengths are checked against the ranges expected for faujasite: silicon-oxygen about 0.162 nm, aluminium-oxygen 0.170-0.192 nm, and the longest aluminium-oxygen bond at the bridging hydroxyl that carries the Brønsted proton.

**Model identity check.** The non-interacting reference state V-R and the pre-reaction complex V-PRC are compared both energetically and geometrically, by measuring the shortest contact between the framework and the adsorbate in each structure. A contact in the hydrogen-bonding range confirms that the two files describe one physical state — the complex formed without a barrier — and prevents a spurious interaction energy being attributed to two different structures.

**Saddle-point acceptance chain.** A transition structure is admitted only if it satisfies, in order: convergence of the saddle optimisation with normal termination; exactly one imaginary mode, of a magnitude that indicates a genuine reaction coordinate rather than numerical noise, with the displacement vector animating the reacting bonds; an energy ordering in which the transition structure lies above both states it connects; a two-sided test in which the structure displaced along its imaginary mode in both directions relaxes to the claimed reactant and product minima, within 5 kJ mol-1 of their accepted energies; and a complete provenance record linking energy, log, structure, and verdict to a single register row. A candidate that fails any of these tests is recorded with its verdict and is not used to support a mechanistic conclusion.

**Cross-level agreement.** The ranking of the states and the sign of every step are compared between the semi-empirical tier and the two hybrid functional levels. Agreement in ranked order and in sign is treated as confirmation; a disagreement is investigated before it is reported, because it identifies the quantity whose value depends on the method.

**External benchmark.** The computed steam hydrolysis barrier is compared with the published periodic DFT range for steam dealumination of zeolites, 76-125 kJ mol-1 (Silaghi et al., 2015), which was obtained on a periodic model rather than on a cluster. Agreement within that range validates the cluster model quantitatively for the reaction step that both approaches compute.

**Provenance audit.** Every energy appearing in a Chapter Four table is traced back to a register row, and each register row to an input file, an output log, and a final geometry file. The audit is performed with a script that reads the outputs directly and reports, for each job, the termination status, the optimisation convergence status, the imaginary-mode count, the final energy, and the wall-clock time, so that a mis-typed or mis-attributed number cannot survive into the report.

**Table 3.5**

*Validation anchors for checking the computed results*

| Anchor | Criterion | Action if the criterion is not met |
|---|---|---|
| Geometry gate | Converged optimisation, bond lengths within the faujasite ranges | Rebuild the capped periphery and re-optimise before continuing |
| Minimum gate | No imaginary vibrational mode | Re-optimise with a tighter convergence threshold; a residual floppy mode is identified by animating it before the structure is accepted |
| Model identity | V-R and V-PRC identical in energy and geometry to within the hydrogen-bond contact range | Re-examine the starting geometry and re-optimise |
| Saddle acceptance chain | Convergence, exactly one imaginary mode, correct energy ordering, two-sided displacement test, provenance | Record the candidate with its verdict; a barrier that fails the chain supports no conclusion and the electronic bracket is reported instead |
| Cross-level agreement | Same ranked order and same sign of each step at every level of theory | Investigate the quantity that disagrees and report its method dependence explicitly |
| External benchmark | Steam barrier within the published range 76-125 kJ mol-1 | Re-examine the model and the level of theory for that step before drawing comparisons |
| Provenance audit | Every tabulated energy maps to a register row, input, log, and geometry | Correct the register; an untraceable number is removed from the report |

*Source:* Author.

## 3.8 Statistical Treatment and Uncertainty

The results of this study are deterministic: each quantity is the solution of a defined electronic-structure problem, so there is no sampling distribution and no statistical significance to report. Uncertainty is handled instead by identifying and quantifying the three sources that matter for a computed energy difference, and by reporting them alongside the numbers:

1. **Method dependence.** Every thermodynamic and mechanistic conclusion is presented at more than one electronic-structure level, and the spread between levels is stated. Where the two hybrid functionals agree, the conclusion is a property of the chemistry; where they differ, the difference is reported as the method sensitivity of that quantity.
2. **Basis-set incompleteness.** The counterpoise correction quantifies the part of the interaction energy that arises from basis-set superposition at the def2-TZVP level, and the corrected value is reported alongside the uncorrected one for both adsorption complexes.
3. **Numerical thresholds.** Geometry optimisation, self-consistent-field convergence, and integration-grid settings are fixed and documented; residual numerical differences are small compared with the chemical energy differences discussed, and the same settings are used for every state so that the differences between states, which are the quantities interpreted, are free of systematic offsets.

Because the quantities interpreted in Chapter Four are differences between states computed with identical model, basis set, and settings — for example the competition between vanadic acid and water for the same site, or the barrier of one step relative to the state that precedes it — the systematic error of the method largely cancels, which is what makes relative comparisons of a few tens of kJ mol-1 meaningful even when the absolute accuracy of a hybrid DFT reaction energy is larger than that.

## 3.9 Computing Resources and Schedule

Tier 1 was executed on a quad-core workstation and, being inexpensive per job, was run in single-job batches that suited the local power supply and allowed every result to be inspected before the next job was launched. Tiers 2 and 3 were executed on a rented Linux cloud instance with four virtual processors and ORCA 6.1.1, used in short campaigns with results synchronised back to the project archive immediately after each batch. Cloud jobs were queued so that a completed job was never lost to a disconnection: each batch was launched in a persistent session, every finished output was copied out of the working directory at once, and the instance was released between campaigns.

**Table 3.6**

*Work schedule for the project*

| Stage | Work item | Platform |
|---|---|---|
| 1 | Literature review, model design, and cluster assembly | Local |
| 2 | Tier 1 mapping: references, complexes, intermediates, products | Local workstation |
| 3 | Tier 1 saddle searches, frequency checks, and the pathway audit | Local workstation |
| 4 | Tier 2 refinement of the stationary-point set at hybrid DFT | Cloud instance |
| 5 | Tier 3 single points, counterpoise, and thermochemistry at 298.15 K and 1003.15 K | Cloud instance |
| 6 | Energy tables, validation audit, figures, and writing | Local |

*Source:* Author.

## 3.10 Data Management and Reproducibility

Every calculation is named STATE-Tn-Vnn (state, tier, version) so that a repeated calculation never overwrites its predecessor: a revised or repeated job becomes the next version and the earlier version remains in the archive with its verdict. The calculation register records, for each row, the job identifier, the state, the tier, the input file, the output log, the final geometry file, the software and version, the convergence status, the number of imaginary frequencies, the final electronic energy, and the accept or reject verdict with its reason. A companion provenance map links each register row to the exact files from which its energy was read.

Input files, output logs, final geometries, and the register are stored together in the project archive, which is synchronised after every session and backed up to two independent media each week. Analysis scripts read the outputs directly rather than restating their values, so that the tables in Chapter Four regenerate from the archive. This structure is what allows any number in this report to be traced, checked, and recomputed, and it is the reason that superseded and rejected calculations are retained rather than deleted: they document the path by which the accepted results were reached.

## 3.11 Risk Register

The risks that attach to a computational project of this kind, and the measures adopted against each, are set out in Table 3.7.

**Table 3.7**

*Risk register and mitigation plan*

| Risk | Effect if unmanaged | Mitigation adopted |
|---|---|---|
| Self-consistent-field convergence stalls on a metal-containing cluster | Job aborts without an energy | Damped and second-order SCF convergence options reserved for such cases; tighter iteration limits set in the inputs of the affected jobs |
| Geometry optimisation reaches its iteration limit while still descending | Job ends without convergence | The last geometry is retained, the optimisation is continued from it with a rebuilt Hessian, and the continuation is recorded as a new version |
| A saddle-point search relaxes to a minimum | No barrier available for that step | The outcome is recorded as such; the step is then described by its thermodynamic end states and the barrier is reported only if it survives the two-sided displacement test |
| Low-frequency floppy modes appear as spurious imaginary frequencies | A minimum is misclassified | Mode animation is used to identify the motion before the structure is judged; peripheral capping groups are checked first, since they are the usual source of such modes |
| Cloud instance interrupted or released prematurely | Loss of computing time | Each batch runs in a persistent session, outputs are synchronised immediately after they are written, and every job is restartable from its own geometry |
| Loss of the local archive | Loss of the calculation record | Weekly backups to two independent media, plus the project repository that carries the inputs, geometries, register, and analysis scripts |

*Source:* Author.

## 3.12 Health, Safety, Environmental, and Ethical Considerations

The study is entirely computational and literature-based. It involves no chemical synthesis, no hazardous reagents, no pressurised or high-temperature equipment, and no biological or human subjects, so the usual laboratory hazards are not present. The health and safety considerations that apply are those of prolonged workstation and screen use, which are managed by structuring the work into scheduled sessions with the calculation batches running unattended.

The environmental footprint of the work is the electricity consumed by the local workstation and the cloud instance; it is minimised by mapping the pathway at the inexpensive semi-empirical level first and reserving hybrid DFT for the stationary points that carry the conclusions, and by releasing the cloud instance between campaigns.

Ethically, the study observes the standard requirements of computational research: all data reported are the outputs of the calculations described, no result is adjusted or selected to support a preferred mechanism, superseded and rejected calculations are retained in the register with their verdicts, and all experimental findings, methods, and data taken from the literature are cited at the point of use. No confidential or proprietary plant data are used; the Nigerian refinery context is drawn entirely from published sources and public information.

## 3.13 Chapter Summary

This chapter has defined the model — a hydrogen-terminated faujasite cluster carrying one Brønsted acid site, its two adsorbates vanadic acid and water, and the fourteen stationary points of the two pathways — and the computational protocol applied to it: semi-empirical mapping of the landscape, hybrid DFT refinement of every stationary point with B3LYP-D3(BJ)/def2-TZVP, final-level PBE0-D3(BJ)/def2-TZVP single points with a counterpoise correction for the adsorption complexes, thermochemical analysis at both 298.15 K and the 1003.15 K regenerator temperature, and a six-part validation plan that every number must pass before it is interpreted. The energy bookkeeping, the resource plan, the data-management scheme, and the risk and ethical framework that govern the execution of the work have been stated. Chapter Four presents the results obtained with this protocol.
