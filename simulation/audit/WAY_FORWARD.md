# SIMULATION WAY FORWARD

**Two-Tier Computational Protocol for the DFT Investigation of Zeolite Y Deactivation by Vanadium**

Project working document, Department of Chemical Engineering, Ahmadu Bello University, Zaria. July 2026.

## 1. What this document is

This document is the execution plan for the computational work defined in Chapter Three of the project report. It fixes the models, the software stack, the exact input files, the order of jobs, the quality gates between stages, and the way results must be recorded so that Chapter Four can be written directly from the calculation register. Where Chapter Three states what is computed, this document states how, command by command.

## 2. The research approach in one paragraph

The study computes two reaction pathways on one small faujasite cluster: (a) the eight-state vanadic acid dealumination pathway V-R, V-PRC, V-TS1, V-I1, V-TS2, V-I2, V-TS3, V-P, and (b) the four-state steam baseline W-R, W-PRC, W-TS, W-P. Everything is first mapped completely at the GFN2-xTB semi-empirical level on the local laptop, where each job takes seconds to tens of minutes and survives the electricity situation. Only then is the confirmed stationary-point set transferred to a rented cloud instance, where all geometries are re-optimized and analysed at dispersion-corrected hybrid DFT in ORCA 6.1. Mechanistic conclusions are drawn only from Tier 2 numbers; Tier 1 provides the geometry and pathway map. The published steam-dealumination barrier range of Silaghi et al. (2015), 76 to 125 kJ/mol, is the fixed external benchmark for the baseline pathway.

## 3. Assets already in hand

The following files exist in the project archive.

**Table 1**

*Starting structures and their state assignments*

| File (simulation/molfiles/) | Assigned state | Role |
|---|---|---|
| V-R_01_Reactants_Isolated.mol | V-R | Non-interacting cluster plus H3VO4 reference |
| V-PRC_02_Pre_Reaction_Complex_PRC.mol | V-PRC | Hydrogen-bonded pre-reaction complex |
| V-TS1_03_Transition_State_1_TS1.mol | V-TS1 | Chemisorption saddle-point guess |
| (to be generated, see Section 6.2) | V-I1 | Chemisorbed intermediate |
| V-TS2_05_Transition_State_2_TS2.mol | V-TS2 | First Al-O cleavage saddle-point guess |
| (to be generated, see Section 6.2) | V-I2 | Hydrolysed intermediate |
| V-TS3_07_Transition_State_3_TS3.mol | V-TS3 | Final Al-O cleavage saddle-point guess |
| V-P_08_Product_Dealuminated_EFAL.mol | V-P | Dealuminated product |

The old numbering skips 04 and 06; those two slots are exactly where the intermediates V-I1 and V-I2 belong. They are obtained by optimization, not by hand drawing (Section 6.2). Ready XYZ seeds for the bare cluster, H3VO4, H2O, and every state above are in simulation/xyz_seeds/. The numbers of the files and folders in this document refer to that simulation directory.

## 4. Computing environment

### 4.1 Local laptop

The local machine is a quad-core 64-bit laptop (Intel i7-3740QM, 16 GB RAM). It runs all structure building and the complete Tier 1 programme. No GPU is needed or used at any point of the study. Software to install and verify:

1. Avogadro 2 and VESTA: structure editing and crystal reference display.
2. ORCA 6.1 (free for academic users after registration at the ORCA forum): all quantum chemistry. Confirm the xTB interface by running a one-line test job on water with keyword XTB2; if the interface is missing, install xtb separately with conda (conda install -c conda-forge xtb) and repeat.
3. Multiwfn: Hirshfeld charge analysis in Stage 6.
4. Python 3 with NumPy and matplotlib: tables and charts.
5. tmux (or equivalent persistent terminal) and rsync for cloud sessions.

Verification test before any project job: optimize H2O at XTB2, then at B3LYP-D3(BJ)/def2-SVP, confirm convergence strings appear, and confirm the O-H bond length is about 0.096 nm.

### 4.2 Cloud instance

A rented Linux instance of 8 to 16 virtual CPU cores, 32 to 64 GB RAM, and about 200 GB storage is sufficient. Prepare it as follows:

1. Install Ubuntu 24.04 LTS, create a working directory /work, and transfer the ORCA 6.1 Linux archive to it.
2. Extract to /opt/orca and add /opt/orca to PATH and LD_LIBRARY_PATH in .bashrc.
3. Test with the water verification job in a tmux session, then detach; tmux keeps jobs alive through disconnections.
4. Synchronize results with rsync -avz remote:/work/results/ local:results/ after every batch, and confirm files open locally before deleting anything remotely.

Keep the instance rented only for Tier 2 weeks; the total Tier 2 programme is estimated at 40 to 60 hours of uptime on a 12 to 16 core instance, so a single active week is enough. Never leave the instance running unattended and billed.

### 4.3 Electricity and data-loss discipline

1. All local jobs are short (under one hour); queue them in power windows.
2. After every converged local job, copy the output into results/ immediately.
3. Every Friday, compress the whole project directory with 7-Zip and copy the archive to an external drive and to cloud storage. Two copies, two different media, every week.
4. Keep a notebook with the date, power availability, and jobs attempted; the calculation register (Section 8) lives in the archive, not in the notebook.

## 5. Naming convention and directories

Use directories 01_models, 02_tier1, 03_tier2, 04_tier3, 05_analysis, 06_archive. Every calculation is named STATE-Tn-Vnn, for example V-TS2-T1-V03, meaning state V-TS2, Tier 1, third version. A versioned retry never overwrites its predecessor. The register spreadsheet logs every name with its input file, software version, convergence status, final electronic energy, and accepted or rejected status with reason.

## 6. Stage-by-stage runbook

### 6.1 Stage 1: models (local)

1. Open the FAU reference in VESTA for orientation only; the working cluster is the idealized tetrahedral AlSi4O4H13 model of seed file cluster_AlSi4O4H13.xyz.
2. Optimize cluster_AlSi4O4H13.xyz, H3VO4.xyz, and H2O.xyz at XTB2 with template t1_xTb_opt_freq.inp. Rename the input file reference accordingly.
3. Quality gate: ORCA prints THE OPTIMIZATION HAS CONVERGED; frequency block shows no imaginary modes; cluster Si-O bonds fall near 0.162 nm and Al-O bonds near 0.174 to 0.20 nm (the Al-O(H) bond carrying the Brønsted proton is the longest). If the cluster rearranges or tears, rebuild the caps at 0.148 nm and repeat.

### 6.2 Stage 2: complexes, intermediates, products (local)

1. V-PRC: optimize the seed V-PRC_start.xyz at XTB2. Prepare a second orientation by rotating H3VO4 about the hydrogen-bond axis in Avogadro and optimize that too; keep the lower-energy converged structure and record the spread.
2. W-PRC: dock H2O at the Brønsted proton in Avogadro (place the water oxygen about 0.25 nm from the proton) and optimize; prepare one alternative orientation as above.
3. V-P and W-P: optimize the seeds V-P_start.xyz and a hand-built W-P (break one Al-O bond, place the water oxygen bound to Al, place both transferred protons as silanols).
4. V-I1: take the V-TS1 guess, displace the forming Al-O(V) bond about 0.02 nm shorter and the transferred proton fully onto the vanadic oxygen, and optimize at XTB2. It must converge to a stable minimum with the vanadic acid chemisorbed on aluminium (five-coordinate Al) and zero imaginary frequencies. Do not hand-craft the connectivity blindly beyond this displacement.
5. V-I2: take the V-TS2 guess, complete the first cleavage in the drawn direction (the breaking Al-O bond 0.02 nm longer, transferred protons settled as two silanols), and optimize at XTB2.
6. Quality gate: every one of these seven structures optimizes to a clean minimum (zero imaginary frequencies) and retains the intended coordination pattern, checked visually in Avogadro.

### 6.3 Stage 3: saddle points (local)

For each of the four steps (V-PRC to V-I1, V-I1 to V-I2, V-I2 to V-P, W-PRC to W-P):

1. Run the relaxed scan t1_xTb_relaxed_scan.inp along the bond being broken or formed, using the atom numbers of the converged endpoint XYZ files.
2. From the scan maximum, first try NEB-TS (template t1_xTb_nebts.inp) between the confirmed endpoint states; use the seeded guesses V-TS1, V-TS2, V-TS3 as checkpoints, because those geometries already carry the correct proton transfers and save many cycles.
3. Confirm each saddle point with a FREQ job: exactly one imaginary frequency, and the animated imaginary mode (open the output in Avogadro) moves along the reacting bonds.
4. Verify by displacing the saddle geometry plus and minus 0.01 nm along the imaginary mode and optimizing both; the two directions must relax into the intended reactant and product of Table 1/Chapter 3.
5. Quality gate: all four saddle points pass steps 3 and 4 before Tier 2 starts. Record Tier 1 relative energies of all states in the register as the first pathway map.

### 6.4 Stage 4: Tier 2 refinement (cloud)

1. Transfer all converged Tier 1 structures to the instance under tmux.
2. Minima (cluster, H3VO4, H2O, V-PRC, V-I1, V-I2, V-P, W-PRC, W-P): run t2_b3lyp_opt_freq.inp.
3. Saddle points (V-TS1, V-TS2, V-TS3, W-TS): run t2_b3lyp_optts_freq.inp starting from each Tier 1 saddle geometry.
4. Quality gate: minima have zero imaginary frequencies and saddle points exactly one at the DFT level; the DFT geometry must remain recognizably the Tier 1 structure. If a saddle point disappears or drifts to a different mechanism at DFT, return to Stage 3 with the DFT picture and note the change in the register; report the DFT result, never the Tier 1 one.

### 6.5 Stage 5: final energies and thermochemistry (cloud)

1. Run t3_pbe0_singlepoint.inp on every Tier 2 geometry.
2. Run t3_pbe0_counterpoise.inp for V-PRC and W-PRC; record the counterpoise-corrected interaction energy lines.
3. Run t2_freq_1003K.inp on every Tier 2 geometry to obtain the Gibbs corrections at 1003 K; the 298.15 K corrections come from the Stage 4 frequency runs.
4. Quality gate: every used energy reads from a line containing FINAL SINGLE POINT ENERGY, and every Gibbs value traces to a frequency file with the correct imaginary-mode count.

### 6.6 Stage 6: analysis (local)

1. Convert each Tier 2 wavefunction file with orca_2mkl NAME -molden and open the molden file in Multiwfn; run option 7 (population analysis) then 5 (Hirshfeld) then print atomic charges. Record the net charge on the adsorbate fragment and on the Al atom for V-PRC, V-I1, V-TS2, V-P, and W-PRC.
2. Tabulate Al-O and Si-O bond lengths at the attacked sites for every state.
3. Compute every energy difference of Table 3.4 of the report in a Python notebook directly from the register energies; no numbers typed by hand into the final tables.
4. Apply the validation anchors of report Table 3.5 and record pass or fail for each, with the numbers.

## 7. Estimated effort

**Table 2**

*Job inventory and time estimate*

| Tier | Jobs | Count | Per-job estimate | Platform |
|---|---|---|---|---|
| Tier 1 XTB | opts, scans, NEB-TS, freqs | about 40 | seconds to tens of minutes | local laptop |
| Tier 2 DFT | re-opts with frequencies | 13 | 1 to 3 h each at 12 to 16 cores | cloud instance |
| Tier 2 DFT | saddle-point refinements | included above | 2 to 6 h each | cloud instance |
| Tier 3 DFT | single points | 13 | under 1 h each | cloud instance |
| Tier 3 DFT | counterpoise | 2 | about 1 h each | cloud instance |

On the local laptop a single Tier 2 job would take one to three days; thirteen such jobs through an intermittent power supply is the schedule risk that the cloud week removes. The cloud budget is one working week of one modest instance.

## 8. Calculation register and Chapter Four feed-stock

The register spreadsheet has these columns: Job ID; state; tier; input file; software and version; cores and wall time; convergence result; imaginary frequency count; final electronic energy (Hartree); Gibbs correction at 298.15 K; Gibbs correction at 1003 K; accepted or rejected with reason. Chapter Four needs exactly five tables and four figures, all filled from the register:

1. Table: optimized structures and state assignments, with key bond lengths.
2. Table: adsorption energies of H3VO4 and H2O, electronic, counterpoise-corrected, and Gibbs at both temperatures, with orientation spread.
3. Table: relative electronic and Gibbs energies of all twelve states against their pathway references, at both temperatures, with the Tier 1 versus Tier 2 deviation column.
4. Table: four step barriers with the same corrections.
5. Table: Hirshfeld net charges and geometry fingerprints per state.
6. Figures: pathway energy diagram for the vanadic route; overlay of the two routes at process temperature; bond-length evolution along the vanadic route; charge-transfer bar chart.

## 9. Failure playbook

1. SCF will not converge: add KDIIS or SOSCF to the keyword line and rerun; for the vanadium jobs all species are closed-shell, so spin is never the cause.
2. Optimization wanders into a different structure: restart from the best intermediate geometry in the NAME_trj.xyz trajectory, never from the ruined final frame.
3. Frequency run shows more than one imaginary mode in a supposed minimum: displace along the largest imaginary mode by 0.05 nm and re-optimize.
4. Scan energy jumps erratically: shorten the scan range around the suspected barrier to 0.01 nm steps and rely on NEB-TS between clean endpoints.
5. ORCA interface for XTB not found on the laptop: install xtb through conda-forge and rerun the XTB2 verification job.
6. Power cut mid-job: ORCA does not resume an optimization; restart the same input from the last frame of NAME_trj.xyz and log it as a new version.
7. Cloud money runs out before Tier 2 finishes: pause at the nearest quality gate, archive everything, and complete the remaining jobs locally overnight in order of importance: W pathway first (it validates the method against the Silaghi benchmark), then V-PRC, V-TS2, V-P, then the rest.

## 10. Definition of done

The computational work is finished when every quantity of report Table 3.4 has a Tier 2 value, every validation anchor of report Table 3.5 is recorded as pass or fail with numbers, the register is complete, and every accepted XYZ, input, and output file exists in the archive in two copies. At that point Chapter Four writes itself from the five tables and four figures of Section 8.
