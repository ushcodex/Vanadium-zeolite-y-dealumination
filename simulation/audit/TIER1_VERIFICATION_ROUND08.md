# TIER 1 VERIFICATION MEMO: ROUND 8

**Project**: DFT Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in RFCC Units (Final-Year Thesis, ABU Zaria)
**Date**: 2026-07-29
**Auditor**: Verification desk (Arena)
**Scope of this round**: Band D A4 two-sided fall-in test; Band D A2 mode-animation evidence; Band A CI-displacement diagnostic; Band B OptTS continuation 2; Band C OptTS continuation 2 (protocol stop); audit of the three uploaded tracking documents.
**Documents audited**: `calculation_register.csv` (35 data rows), `tier1_summary.md`, `provenance_map.md` (all uploaded 2026-07-29).
**Conversion used throughout**: 1 Eh = 2625.50 kJ/mol. All energies in Eh, all relative energies in kJ/mol.

---

## 1. Executive Verdict

| Band | Claim under audit | Arithmetic | A-chain verdict | Status after this memo |
|---|---|---|---|---|
| D (W-TS) | A4 two-sided test executed | MATCH (16 of 16 figures re-derived) | **A4 FAIL**: both displacements fall into the W-PRC well | Saddle **rejected for PRC to P connectivity**; retained as degenerate proton-shuttle diagnostic |
| D (W-TS) | A2 animation: mode 6 reactive | Vector table verified in part | Animation claim **over-reported by sub-agent**: mode is water-proton dominated, not Al-O cleavage | Correction recorded in Section 3(c) |
| A (V-TS1) | Both CI displacements land in same +300 basin | MATCH | **Non-elementarity SEALED** | Band A closed as bundled; microstepping or bracket required |
| B (V-TS2) | Converged, exactly 1 imaginary mode (-78.21 cm-1) | MATCH | **A1, A2, A3 PASS**; first converged single-mode saddle candidate | **A4 PENDING** (Round 9 task 9.1); raw log tail still owed |
| C (V-TS3) | Continuation 2 hit MaxIter, 1 imaginary mode at step 0 | MATCH | Unconverged; protocol stop | **BRACKETED** at +483.80 to +488.54 vs V-I2 |

Summary: one genuine single-mode saddle now stands on the vanadium route (Band B, +160.70 vs V-I1), subject to the two-sided fall-in test. The steam route saddle exists but does not connect reactant to product; the steam hydrolysis barrier remains an apparent, bundled estimate at Tier 1.

---

## 2. Independent Arithmetic Re-Derivation

Recomputed from register energies at 2625.50 kJ/mol per Eh. All register column entries passed (35 rows, 0 mismatches vs route zeros).

| # | Quantity | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 | Band B TS vs V-I1 (-51.26731716) | +160.70 | +160.70 | MATCH |
| 2 | Band B TS vs V-I2 (-51.25104052) | +117.96 (body text) | +117.97 | MATCH (0.01 truncation remainder, non-blocking) |
| 3 | Band B TS rel zero (-51.12064005) | -224.40 | -224.40 | MATCH |
| 4 | Band B continuation 1 rel zero | -224.01 | -224.01 | MATCH |
| 5 | Band C continuation 2 vs V-I2 | +488.54 | +488.54 | MATCH |
| 6 | Band C continuation 2 rel zero | +146.17 | +146.17 | MATCH |
| 7 | Band A +displacement vs V-PRC | +299.93 | +299.93 | MATCH |
| 8 | Band A -displacement vs V-PRC | +299.97 | +299.97 | MATCH |
| 9 | W-TS +displacement vs W-PRC | +1.35 | +1.35 | MATCH |
| 10 | W-TS -displacement vs W-PRC | +1.34 | +1.34 | MATCH |
| 11 | W-TS saddle vs W-PRC | +29.29 | +29.29 | MATCH |
| 12 | W-TS saddle vs W-P | +25.56 | +25.56 | MATCH |

Cross-checks that matter for adjudication:

| Check | Value | Meaning |
|---|---|---|
| W-P vs W-PRC well gap | +3.74 | Wells closer than A4 tolerance (5): energy alone cannot assign wells |
| W-TS +displacement vs W-P | -2.39 | Displaced minimum sits 2.39 BELOW W-P energy; ambiguous by energy, decisive by geometry |
| Saddle to each displaced well drop | -27.95 / -27.95 | Both sides descend about 28 kJ/mol into the same basin |
| Band A displaced minima vs earlier slid-to-minimum frame (-51.08133370) | -0.17 / -0.13 | Same basin, small refinement; basin identity confirmed |
| Band B continuation 1 to 2 energy change | -0.39 | Settled endgame; consistent with genuine convergence in 12 steps |
| Band C continuation 1 to 2 energy change | +4.74 | Energy rose while unconverged; consistent with ridge walk, not a minimum |
| V-I1 vs V-I2 well gap | +42.73 | For Band B, A4 well assignment is decidable by energy alone; geometry still required on record |

---

## 3. Band D Adjudication (W-TS-T1-V04)

### (a) A4 two-sided fall-in test: FAIL for PRC to P connectivity

Rule: a first-order saddle connecting W-PRC to W-P must fall into two different minima along its single imaginary mode; where wells lie within 5 kJ/mol, geometry discriminators decide.

| Metric | Saddle W-TS-T1-V04 | +0.01 nm displacement | -0.01 nm displacement | Canonical W-PRC |
|---|---|---|---|---|
| Energy (Eh) | -36.43140308 | -36.44204682 | -36.44204971 | -36.44256091 |
| vs W-PRC (kJ/mol) | +29.29 | +1.35 | +1.34 | 0.00 |
| Imaginary modes | 1 (-226.10 cm-1) | 0 | 0 | 0 |
| Al-O2 (A) | 1.7185 | 1.7198 | 1.7194 | 1.7195 |
| Al-O3 (A) | 1.7042 | 1.7037 | 1.7041 | 1.7040 |
| Al-O4 (A) | 1.7210 | 1.7204 | 1.7201 | 1.7202 |
| Al-O22 (water, A) | 2.0650 | 2.0695 | 2.0699 | 2.0701 |
| Well assigned | saddle | **W-PRC** | **W-PRC** | W-PRC |

Both sides land in the W-PRC well: energies within +1.35 kJ/mol of the canonical PRC minimum, four framework Al-O bonds intact at PRC values, water molecularly adsorbed at PRC distance. Neither side approaches the hydrolysed product geometry (W-P requires a cleaved Al-O and a consumed water). **A4 fails.** W-TS-T1-V04 is a converged first-order saddle, but it is a **degenerate intrawell saddle**: it connects the pre-reaction complex to a PRC-type configuration, not reactant to product. It cannot be used as the steam hydrolysis barrier.

### (b) What this saddle actually is

A water-mediated proton-relay (proton-shuttle) saddle inside the hydrated complex well, about +29.29 kJ/mol above W-PRC. Physically this quantity remains meaningful: proton shuttling through the adsorbed water is cheap, so the hydrolysis bottleneck is not proton transfer but the organization of Al-O cleavage. Retain as a diagnostic entry, not as W-TS.

### (c) Correction to the sub-agent A2 animation claim

The report stated mode 6 "breaks the framework Al-O bond". The pasted vector does not support that phrasing. Per-atom displacement magnitudes from `optts2_bandD_ci.out`:

| Atom (index) | Role | \|dr\| (A) |
|---|---|---|
| H (24) | water hydrogen | **0.8992** |
| H (23) | water hydrogen | **0.4271** |
| O (22) | water oxygen | 0.0577 |
| O (4) | framework oxygen | 0.0389 |
| O (3) | framework oxygen | 0.0354 |
| O (2) | framework oxygen | 0.0337 |
| Al (0) | active site | 0.0253 |
| H (21) | Bronsted proton | 0.0087 |
| Si (5 to 8), caps (9 to 20) | framework | 0.0070 or less |

Water hydrogens carry 11 to 35 times the framework displacement. The mode is a water-dominated proton relay. The framework participates only at second order. The correct A2 wording: "mode 6 animates a water-mediated proton-relay coordinate; it is reactive, but the reacting-bond reorganization is the proton shuffle, not Al-O cleavage." Corrected on the record.

### (d) Consequence for the steam barrier

The band D CI estimate (+65.14 apparent vs W-PRC, rel -4.44) remains the Tier 1 best available apparent estimate for the bundled hydrolysis event. No verified elementary steam barrier exists at Tier 1 after this round. Thesis Table 4.3 W-TS row is unchanged.

---

## 4. Band A Adjudication (V-TS1): Non-Elementarity SEALED

| Probe | Result |
|---|---|
| OptTS continuation from CI seed (V04) | Converged to 0-imag basin, E = -51.08133370 (+300.10 vs V-PRC) |
| +0.01 nm displacement along -188.09 cm-1 from CI image (V05) | 0 imag, E = -51.08139865 (+299.93 vs V-PRC); 0.17 kJ/mol below the V04 frame |
| -0.01 nm displacement (V06) | 0 imag, E = -51.08138390 (+299.97 vs V-PRC); 0.13 kJ/mol below the V04 frame |

Two independent probes land in the same shallow +300 kJ/mol basin. Opposite displacement directions from a ridge point that fall into one basin, plus a 0-imag first-order critical point there, seal the diagnosis: **no first-order saddle exists near the Band A ridge for the bundled V-PRC to V-I1 step at GFN2-xTB.** The step bundles several bond events (adsorption cascade plus chemisorption reorganization). Band A is closed as elementary. Resolution options are microstepping (subdivide the step) or bracketed closure (Section 11 decision).

---

## 5. Band B Adjudication (V-TS2-T1-V05): A1, A2, A3 PASS; A4 Pending

| Criterion | Evidence | Verdict |
|---|---|---|
| A1 converged refinement | "THE OPTIMIZATION HAS CONVERGED", normal termination, 12 iterations, end-of-job FREQ block printed | PASS (register record; raw tail owed, below) |
| A2 one credible reactive mode | Exactly 1 imaginary mode at -78.21 cm-1; outside sub-20 noise band and outside the 20 to 50 judgment band | PASS on the letter; reactive animation evidence to be harvested for the record (task 9.2) |
| A3 above both wells | E = -51.20610884 = +160.70 vs V-I1, +117.97 vs V-I2; both far above +1 kJ/mol | PASS |
| A4 two-sided fall-in | Not yet run | PENDING (task 9.1) |
| A5 provenance | Register row V-TS2-T1-V05 maps one structure, one log, one energy | PASS |

This is the first converged single-mode saddle candidate of the campaign. If A4 passes, the verified V-TS2 barrier becomes **+160.70 kJ/mol above V-I1** (rel -224.40), replacing the +413.25 CI estimate; the ratio 413.25/160.70 = 2.6 documents why climbing-image estimates must be refined before tabulation.

Documents-not-statements caveat: the register numbers are arithmetically self-consistent, but primary log evidence has not been shown. Required verbatim paste in the next report: from `optts3_bandB_ci.out`, the convergence block, the FINAL SINGLE POINT ENERGY line, and the lowest lines of the end-of-job VIBRATIONAL FREQUENCIES block (task 9.3). Until then Band B stays at "Candidate (pending A4)".

---

## 6. Band C Adjudication (V-TS3-T1-V05): Protocol Stop, Bracketed

Continuation 2 terminated normally at MaxIter 301, E = -51.06496560 (+488.54 vs V-I2, rel +146.17). The step-0 Hessian of continuation 2 showed 1 imaginary mode (-40.33 cm-1), down from 3. Energy rose +4.74 kJ/mol between continuations, typical for an unconverged ridge walk. Per the pre-agreed protocol ("one more continuation; if it does not converge, stop and report as bracketed"), Band C is closed at Tier 1 as a bracket:

**V-TS3 (I2 to P) bracket: +483.80 to +488.54 kJ/mol above V-I2 (unverified, unconverged).**

Had it converged, the -40.33 cm-1 mode would have fallen in the 20 to 50 judgment band and required recorded animation evidence; moot now.

---

## 7. Document Audit

| Check | Result |
|---|---|
| Register data rows | 35 (was 29; six added: V-TS1 V05/V06, V-TS2 V05, V-TS3 V05, W-TS V06/V07) |
| Duplicate Job IDs | NONE |
| Rel Energy column vs route zeros | 0 mismatches beyond rounding |
| No-silent-deletion rule | Honored: artifacts, superseded, slid, frozen-cap, and displacement rows all retained with honest statuses |
| A2 rule text in tier1_summary.md | Verbatim correct: "sub-20 cm-1 presumptive flat-mode noise; modes between 20 and 50 decided by recorded mode-animation evidence". No silent relaxation this round |
| Provenance map | 35 rows, one input, one log, one xyz per row; V-I1 and V-P input names remain historical carryover previously verified |
| tier1_summary energy tables | Mirror register; statuses match |

Findings requiring correction (hygiene, non-blocking):

1. Editorial slip in the sub-agent report body: Band B section printed "E = -36.43140308 Eh" before the correct value -51.20610884 Eh. The first figure is the W-TS energy pasted by mistake. Register and summary carry the correct value. Recorded so the walkthrough can be fixed; task 9.3 raw paste closes the issue at primary-evidence level.
2. Stale statuses after this memo's verdicts; relabels prescribed in Section 8 (relabel, never delete).

---

## 8. Prescribed Register Relabels (Apply Verbatim, Keep All Rows)

| Job ID | New Status | Notes action |
|---|---|---|
| W-TS-T1-V04 | Rejected for PRC to P connectivity (A4 fail) | Append: "same-well fall-in to W-PRC on both sides; retained as degenerate proton-shuttle diagnostic saddle (+29.29 kJ/mol vs W-PRC)" |
| V-TS1-T1-V02 | Superseded (non-elementarity sealed by V04 to V06) | Keep note text |
| V-TS1-T1-V03 | Superseded (non-elementarity sealed by V04 to V06) | Keep note text |
| V-TS3-T1-V05 | Bracketed closure | Append: "protocol stop after continuation 2; band C bracket +483.80 to +488.54 kJ/mol vs V-I2" |
| V-TS2-T1-V05 | (unchanged) Candidate (pending A4) | Awaits task 9.1 |

Update `tier1_summary.md` Section 2 rows to match, and add a short subsection "Round 8 outcomes" stating: Band D saddle degenerate (A4 fail), Band A sealed non-elementary, Band B single-mode candidate pending A4, Band C bracketed.

---

## 9. Thesis Impact Assessment

No thesis number changes this round:

- The prepared Table 4.3 / Figure 4.1 / Section 4.4 rewrite was gated on Band D A4 PASS. A4 failed. The W-TS row stands at the apparent CI estimate (-4.44 rel, +65.14 apparent), labeled provisional.
- Table 4.4 and Section 4.6 carry audit statuses that are now stale ("pending A4" for W-TS; "under refinement" for sealed and bracketed bands), and V-TS2-T1-V05 (pending A4) is not yet shown. These refresh in one rebuild at Round 9 closeout, together with the Band B A4 verdict, to avoid two consecutive rebuilds.
- If Band B A4 passes next round, prepared diffs activate: Table 4.3 V-TS2 barrier +413.25 becomes +160.70 (rel -224.40); Figure 4.1 V-TS2 bar moves from +28.15 to -224.40; Section 4.6 gains the verified single-mode saddle paragraph and the "CI estimates run about 2.6 times refined values" observation; Section 4.8 limitations gain the degenerate steam saddle and sealed non-elementarity statements.
- If Band B A4 fails, the thesis records zero verified Tier 1 saddles; all four barriers remain apparent or bracketed, and Chapter 4 reframes Tier 1 as a minima-level thermodynamic mapping (adsorption preference 127.31 kJ/mol, chemisorption exothermicity, pathway exothermicity all stand) with saddle resolution deferred to Tier 2.

The headline results verified in earlier rounds are untouched: adsorption preference of vanadic acid over water 127.31 kJ/mol, chemisorption into V-I1 (-385.10 rel), exothermic path to V-P (-82.90 rel).

---

## 10. Round 9 Execution List (for the compute agent)

Constraints as always: one job at a time; launch only with `cmd /c "D:\ORCA_6.1.0\orca.exe job.inp > job.out"`; `%pal nprocs 1 end`.

**9.1 Band B A4 two-sided test.**
From the converged saddle geometry `02_tier1/V-TS2/optts3_bandB_ci.xyz`, build two displaced structures along mode 6 (-78.21 cm-1) at +0.01 nm and -0.01 nm, using the same script and convention used for the W-TS_A4 jobs. Run two Opt Freq jobs from template `t1_xTb_opt_freq.inp` with `%geom Calc_Hess true end`, named `V-TS2_ts_pos_disp.inp/.out` and `V-TS2_ts_neg_disp.inp/.out`, in `02_tier1/V-TS2/`. A4 verdict: the two wells V-I1 (-385.10 rel) and V-I2 (-342.36 rel) sit 42.73 kJ/mol apart, so each displaced minimum must land within 5 kJ/mol of one well each; geometry discriminators corroborate.

**9.2 Band B mode-6 vector harvest.**
From `optts3_bandB_ci.out` NORMAL MODES, produce the per-atom \|dr\| table (same parser used for Band D). Identify which bonds animate; expected content is the first Al-O cleavage coordinate. Paste the top movers.

**9.3 Primary-evidence pastes.**
Paste verbatim, no paraphrase: (i) from `optts3_bandB_ci.out`: the "THE OPTIMIZATION HAS CONVERGED" block, the FINAL SINGLE POINT ENERGY line, and the lowest lines of the end-of-job VIBRATIONAL FREQUENCIES block; (ii) the convergence and energy tails of both 9.1 displacement logs; (iii) the final FREQ blocks of the 9.1 logs (expect 0 imaginary each if they are minima).

**9.4 Well discriminators for the record.**
From stored canonical xyz files, tabulate for V-I1: Al coordination count within 2.3 A (expected 5, chemisorbed), listing the contacting atoms; for V-I2: Al coordination count (expected 4) plus the new hydrolysis bonds (list O-H pairs below 1.05 A on formerly bridging oxygens). This pre-declares the geometry test used to adjudicate 9.1.

**9.5 Bookkeeping.**
Apply Section 8 relabels; add register rows V-TS2-T1-V06 and V-TS2-T1-V07 for the 9.1 runs once executed (Status "Diagnostic run (A4)"); update tier1_summary.md and provenance_map.md; append walkthrough; rebuild the zip archive; re-upload `calculation_register.csv`, `tier1_summary.md`, `provenance_map.md`.

---

## 11. Decision Gate (User Input Required)

Four decisions gate the final Tier 1 closure and Chapter 4 finalization. They are also posed in the chat interface.

1. Thesis submission window (asked twice before; still unanswered). This decides microstepping feasibility.
2. Bands A and D path: subdivide each bundled step into elementary microsteps (several weeks of single-core laptop time, uncertain payoff at GFN2-xTB), or close them now as honest brackets and apparent estimates with Tier 2 named as the arbiter.
3. Band C: accept the protocol stop and bracket, or authorize one final continuation (expected cost roughly 300 more iterations with no convergence guarantee).
4. Thesis rebuild timing: single rebuild at Round 9 closeout (recommended), or an immediate bookkeeping rebuild now.

---

*Verification desk note: every verdict above derives from documents and re-derived arithmetic, not from narrative claims. Where primary log evidence is still owed (Band B convergence tail), the record says so and the row stays below acceptance until the paste arrives.*
