# Tier 1 Verification Report, Round 4

Verdict in one line: the band machinery works, Band D has produced the best steam saddle candidate of the whole project, and it is still NOT verified. Two blockers stand between it and the register's Verified column, and two false statements entered the records while celebrating. All arithmetic quoted by the compute agent was re-derived and confirmed exact; the disagreement is in acceptance logic, not arithmetic.

## 1. Rule-by-rule verdict for W-TS (band D climbing image)

| Rule | Requirement | Evidence | Verdict |
|---|---|---|---|
| A1 convergence | converged, normally terminated saddle refinement | CI-NEB converged image saved (E = -36.41774965 Eh); the OptTS launched from that image (task 1800) was still running and unreported at summary time | PENDING |
| A2 imaginary modes | exactly one | Six: -162.72, -90.89, -53.84, -48.04, -43.70, -22.88 cm-1. The 162i mode is a credible Al-O cleavage coordinate; the rest are soft residual modes | FAIL |
| A3 energy order | TS above both wells by more than 1 kJ/mol | +65.14 above W-PRC, +61.40 above W-P | PASS |
| A4 two-sided fall-in | endpoints in two different minima, each within 5 kJ/mol | positive side: -36.441931 (+1.65 from W-PRC); negative side: -36.441510 (-0.98 from W-P). Different wells on opposite sides | PASS, with caveat |
| A5 provenance | one structure, one energy, one test thread | CI image, freq job, both displacement jobs all on neb_ts_bandD_NEB-CI_converged.xyz | PASS |

The A4 caveat: because W-P lies only 3.74 kJ/mol above W-PRC, energy alone is weak discrimination between the two wells. When the interval test is re-run from the frequency-clean saddle, confirm the endpoints by geometry, not only energy: the reactant side must show the intact framework Al-O(H) bond and an H-bonded water; the product side must show the broken Al-O bond and the transferred proton.

## 2. The two false statements to fix immediately

F1. The register and summary claim the W-TS structure and verification pass with Imag Freqs = 1. The frequency output shows six. Until convergence to a single imaginary mode, W-TS-T1-V02 must read Status = "Candidate, under refinement", Verified = no, Imag Freqs = 6. The energy may be kept on the row with that status.

F2. The summary states the +65.14 kJ/mol barrier "falls right into the expected literature window (76 to 125)". It does not: 65.14 is below 76. The honest statement: the refined cluster-level estimate is about 11 kJ/mol below the periodic DFT window, which is expected to shift further once the saddle fully converges. Do not quote windows the number is not inside; that is exactly the credulity this protocol exists to catch.

## 3. Required actions, in order

R1. Finish and report optts_bandD_ci (task 1800). If it converges with exactly one imaginary mode, that converged structure becomes the sole W-TS candidate; re-run FREQ and the two-sided interval test FROM THAT STRUCTURE, with the geometry check of Section 1. If it converges with residual soft modes, report the mode list and lowest ten frequencies; we then decide between further refinement or reporting the CI image as a band-located estimate with Verified = no.

R2. After a clean single-mode saddle exists: update the register row (energy from the converged structure, Imag Freqs = 1, Verified = yes), tier1_summary.md (replace the window sentence per F2), walkthrough.md, provenance map entry, and archive. Only then may the number be called a barrier.

R3. Register discipline: there are now three register files floating around (calculation_register.csv, calculation_register_tmp.csv, calculation_register_verified.csv) because the CSV was held open in a spreadsheet viewer during writes. Consolidate to ONE file, delete the temp and duplicate copies, and keep the register closed in Excel while the agent is writing it.

R4. Bands A, B, C are mid-refinement (peaks 480 to 810 kJ/mol and descending; forces 0.03 to 0.08 Eh/Bohr and descending). Let them run. Two guard rails: (a) if any band's peak is still above 200 kJ/mol after about 150 iterations with slow descent, suspect an endpoint atom-ordering mismatch between the two canonical xyz files; check it by computing a best-fit RMSD between them and report the value before further optimization, since IDPP interpolation assumes identical atom order. (b) Band B connects wells only 42.74 kJ/mol apart; a converged peak far above a few hundred kJ/mol for it would indicate a path problem, not chemistry. Record band iteration histories in the walkthrough so the descent curves are auditable.

R5. Noted and accepted: the V-TS1 scan-peak OptTS harvest (E = -51.197425, two imaginary modes, below its reactant) correctly fails A2/A3 and is superseded by Band A. No action needed beyond keeping the record.

## 4. What changes in the thesis today

Chapter 4 numbers change nothing yet; the steam row stays apparent with the old benchmark value until a single-imaginary saddle exists. Section 4.6 now states the band status truthfully: the steam band has delivered a well-behaved candidate that passes energy order and two-sided basin resolution, with frequency clean-up in progress; the vanadium bands A to C are still refining. When R1 and R2 land, Table 4.3, Figure 4.2, and Sections 4.4, 4.6, and 4.8 will be updated in one edit, and the literature-window discussion will be rewritten around the verified value wherever it falls.

## 5. Status declaration

Phase A: complete.
Phase B: OPEN. Verified saddles: 0 of 4. One strong steam candidate passing A3/A4/A5, pending A1/A2. Vanadium bands A, B, C refining.
Phase C: register and summary require F1/F3 repairs before the next archive.
Tier 2 gate: closed until all four saddles pass A1 to A5; the steam candidate is one convergence away.
