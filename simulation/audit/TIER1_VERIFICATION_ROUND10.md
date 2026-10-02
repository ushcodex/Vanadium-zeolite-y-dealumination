# TIER 1 VERIFICATION MEMO: ROUND 10

**Project**: DFT Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in RFCC Units (Final-Year Thesis, ABU Zaria)
**Date**: 2026-07-30
**Auditor**: Verification desk (Arena)
**Scope of this round**: Audit of the Round 10 execution report (note amendments, walkthrough fixes, full geometry discriminator tables, V-system atom index map). **No tracking documents were attached this round**; the only machine-checkable item is the register CSV text embedded in the report.

---

## 1. Compliance Finding: The Prescribed Amendments Were Not Applied

The Round 9 memo Section 4 prescribed verbatim note texts and relabels. The register content embedded in the Round 10 report is **byte-for-byte identical to the Round 9 register in every audited cell**. Verifiable from the report itself:

| Row | Required (Round 9 memo, Section 4) | Found in Round 10 CSV | Status |
|---|---|---|---|
| V-TS2-T1-V05 note | "...A1-A3 and A5 passed; A4 chemistry-passed via pre-declared discriminators with recorded tolerance breach (endpoints +15.64 vs V-I2, +107.08 vs V-I1)" | "...A1-A5 passed" | **NOT APPLIED** |
| V-TS2-T1-V06 note | "...converged to an I2-family minimum ... A4 tolerance 5 not met, identity by geometry" | "converged to V-I2 well (+15.64 kJ/mol vs V-I2, 0 imag)" | **NOT APPLIED** |
| V-TS2-T1-V07 note | "...converged to a chemisorbed-family minimum ... A4 tolerance 5 not met, identity by geometry" | "converged to V-I1 well (+107.08 kJ/mol vs V-I1, 0 imag)" | **NOT APPLIED** |
| W-TS-T1-V04 status | "Rejected for PRC to P connectivity (A4 fail)" + appended note | "Candidate (pending A4)" | **NOT APPLIED** |
| V-TS1-T1-V02, V-TS1-T1-V03 status | "Superseded (non-elementarity sealed by V04 to V06)" | "Candidate, under refinement" | **NOT APPLIED** |
| V-TS3-T1-V05 status | "Bracketed closure" + bracket note | "Candidate, under refinement" | **NOT APPLIED** |

The report's own "Step 2" summary restated the OLD values inside its bullet list as though they were the required targets. These become mandatory Round 11 task 1, prescribed a third time. The walkthrough fixes (H27 dy = +0.237215, +15.64 sign, norm line 1.000000) are reported applied to `walkthrough.md`, which is outside the three auditable documents this turn.

---

## 2. Full-Geometry Audit: Three Findings That Change the Record

The Round 10 tables (Al-O to 3.0 A; O-H to 1.05 A; 30-atom index map) are the first complete geometry evidence. Atom indexing confirmed: 0 Al; 1-4 framework O; 5-8 Si; 9-20 capping H; 21 Bronsted proton; 22 V; 23-26 vanadate O; 27-29 vanadate protons.

### Finding 1: Canonical V-I1 is tetrahedral with an intact framework, not five-coordinate

Canonical V-I1 Al-O contacts to 3.0 A: **exactly four** (O1 1.6869, O3 1.7047, O4 1.7294, O2 1.8045 A). No vanadate oxygen lies within 3.0 A of aluminium. The report's own caption repeated "5-coordinated Al" while its table showed four contacts; the caption is stale, the table is data.

Consequences:
- The long-carried description "V-I1 contains a five-coordinate aluminium centre" (thesis Section 4.3; earlier memos) is **not supported by the canonical geometry on record**. The elongated framework bond Al-O2 = 1.8045 A matches the "Al-O = 0.180 nm" quoted in Section 4.3, which strongly suggests the original claim described this strained, vanadate-anchored framework bond and miscounted aluminium as five-coordinate. A V-O distance table (Round 11, required) will test whether the vanadate anchors through V-O2 (the "V-O = 0.177 nm" figure would then describe the V end of the same bridge).
- The proton inventory explains the -188.20 kJ/mol chemisorption sink without any five-coordinate centre: the Bronsted proton has transferred onto the vanadate (O23-H21 = 0.9592 A), giving the complex ion-pair character. Additionally O26 carries two bonded protons (H29 = 0.9712 and H19 = 0.9622, H19 being a nominal edge cap), indicating a second proton drawn from the cluster edge, an artifact-prone feature of the small cluster model to be acknowledged.

### Finding 2: Both A4 displacement arms broke Al-O2

- Positive arm: Al-O2 = 2.9853 A (broken), Al bonded to vanadate O24 (1.6676), framework silanol O3-H21 = 0.9575, four-coordinate Al. Hydrolysed (I2-family) character, consistent with Round 9.
- Negative arm: Al-O2 lies **beyond 3.00 A** (absent from the table), Al five-coordinate through O1, O3, O4, O24, O25 (two vanadate contacts), silanol O3-H21 = 0.9572 present, vanadate hydroxyl O24-H27 retained (0.9557).

Against Finding 1, the negative-side minimum cannot be assigned to the reactant family: canonical V-I1 has Al-O2 intact at 1.8045 A and zero vanadate-Al bonds. Both displacement directions landed in structures with Al-O2 cleaved. A first-order saddle connecting reactant to product must return the reactant on one side. **That return is not on the record.**

### Finding 3: The saddle's own mode does not look like a clean Al-O2 stretch

Mode 6 (-78.21 cm-1) amplitudes from the Round 9 table: Al 0.141, V 0.122, vanadate O23/O25/O26 0.164 to 0.195, relay protons H27 0.315 and H21 0.168, but framework O2 only 0.075. The displacement content is dominated by vanadate reorganization and proton shuttling with aluminium participation, not by O2 motion. Combined with Findings 1 and 2, the credible identifications of this saddle are: (i) a vanadate-rebinding or proton-shuttle saddle within the cleaved family (between canonical-I2-like and bidentate arrangements), or (ii) a saddle reached from an early-cleavage region whose displacement test jumped, in both directions, past narrower basins, including possibly past a thinner reactant-side well that a 0.01 nm step overshot.

---

## 3. Adjudication Update: V-TS2 Acceptance SUSPENDED

- Round 9 accepted V-TS2-T1-V05 as "the I1 to I2 first-cleavage saddle" with a recorded tolerance qualification. That acceptance rested on the negative arm being classifiable as chemisorbed-family, which rested on the inherited description of canonical V-I1 as five-coordinate.
- The full canonical geometry (Finding 1) removes that basis, and Finding 2 shows the reactant side of A4 was never reached.
- Effective now: V-TS2-T1-V05 status moves from "Accepted" to **"First-order saddle, converged and mode-verified, connectivity to V-I1 unproven; under re-adjudication"**. A1, A2, A3, A5 remain passed. A4 moves to FAILED AS EXECUTED (reactant-side basin not reached on either arm), with a documented means of appeal below.
- What does not change: all minima energetics (adsorption preference 127.31, chemisorption -188.20, pathway exothermicity -82.90), the degeneracy verdict on band D, the band A seal, the band C bracket.
- What is held in abeyance: the thesis claim that +160.70 kJ/mol is THE verified I1-to-I2 barrier. No thesis edit is made this round: the resolution test is cheap (below) and the current thesis text already carries the qualification language; if the test fails, the reverted wording is a prepared, contained edit (Table 4.3 row, Table 4.4 row, Figure 4.2 annotation, Sections 4.6 and 4.8). If it passes, the thesis stands exactly as built.

---

## 4. Round 11 Execution List (re-adjudication protocol; all jobs are hours-class, none are 10-hour)

Constraints unchanged: one job at a time; `cmd /c "D:\ORCA_6.1.0\orca.exe job.inp > job.out"`; `%pal nprocs 1 end`.

1. **Register compliance (paperwork, third prescription)**: apply the Round 9 memo Section 4 note texts verbatim; apply the pending relabels: W-TS-T1-V04 to "Rejected for PRC to P connectivity (A4 fail)" (append degenerate-shuttle note); V-TS1-T1-V02 and V03 to "Superseded (non-elementarity sealed by V04 to V06)"; V-TS3-T1-V05 to "Bracketed closure" (append bracket +483.80 to +488.54). Additionally set V-TS2-T1-V05 Status to "Under re-adjudication (connectivity to V-I1 unproven)" and its Verified field to "no" until the micro-A4 result.
2. **Attach the three documents** (`calculation_register.csv`, `tier1_summary.md`, `provenance_map.md`) to the next message. Claims without attachments are unverifiable by rule.
3. **Saddle geometry table**: from `optts3_bandB_ci.xyz`, print Al-O to 3.5 A, ALL V-O to 3.0 A, O-H to 1.05 A, Al coordination count at 2.3 A. The key question: is Al-O2 intact or broken AT the saddle, and where do H21 and H27 sit?
4. **Canonical V-I1 V-O table**: ALL V-O distances to 3.0 A for `V-I1_canonical.xyz`. Tests the V-O2 anchor hypothesis behind the "0.177 nm" figure in thesis Section 4.3 and settles what V-I1 actually is.
5. **Micro-A4 re-test**: repeat the two-sided displacement from the saddle along mode 6 at HALF the previous step, +/-0.005 nm (0.05 A), filenames `V-TS2_ts_posB_disp.inp/out` and `V-TS2_ts_negB_disp.inp/out`, Opt Freq, `%geom Calc_Hess true end`. On a staircase surface the 0.10 A step can clear narrow wells; 0.05 A is the standard re-test before declaring an A4 failure final. Parse both endpoints with the full table format of Round 10 task 2.
6. Report: verbatim tails (convergence, FINAL SINGLE POINT ENERGY, frequency blocks) for both micro-A4 jobs plus the full geometry tables of items 3, 4, 5.

Decision rule I will apply on receipt:
- If either micro-A4 arm lands in the reactant family (Al-O2 intact at 1.7 to 1.9 A, Al tetrahedral, no vanadate-Al bond, H21 on the vanadate or framework consistent with canonical V-I1), A4 passes with the tolerance note and the Round 9 acceptance is reinstated unchanged.
- If both arms again land in cleaved structures, A4 fails finally: the saddle is relabelled "first-order saddle within the cleavage region (family-internal)", +160.70 is withdrawn as the I1-to-I2 barrier, and the prepared thesis revert fires. Tier 1 then closes with zero verified barriers and a fully documented audit trail, which remains a defensible undergraduate result because the verified minima and the adsorption-preference core are untouched.

---

## 5. Cloud Track (answered in chat this round)

The cloud single-point package design from the census memo stands and is INDEPENDENT of this re-adjudication: single-point energies of the saddle geometry remain meaningful and are quoted with the outcome of the micro-A4. Slot 7 in the bus manifest is relabelled "saddle-region structure SP" in the manifest.

---

*Verification desk note: this is the verification system working as designed. A fuller document (the complete geometry tables) outranks an earlier summary ("5-coordinate Al"), and the record corrects itself against documents, never against wishes. The hypotheses about what V-I1 and the saddle really are remain exactly that, hypotheses, until the Round 11 tables land.*
