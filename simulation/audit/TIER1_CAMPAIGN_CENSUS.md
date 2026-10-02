# TIER 1 CAMPAIGN CENSUS AND CLOUD TIER 2 FEASIBILITY ASSESSMENT

**Project**: DFT Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in RFCC Units (Final-Year Thesis, ABU Zaria)
**Date**: 2026-07-29
**Author**: Verification desk (Arena), from the 37-row calculation register audited over Rounds 1 to 9
**Context**: User constraint received 2026-07-29: submission window under 3 weeks; cloud submission possible exactly once ("one chance bus"); non-convergence or failed jobs are not affordable.

---

## 1. Exact Tier 1 Census (37 registered jobs)

Every job is in `calculation_register.csv`; deleted nothing throughout (no-silent-deletion rule). Final adjudicated status per job:

| Final status | Count | Job IDs |
|---|---|---|
| ACCEPTED, verified minimum (number quoted in thesis) | 10 | cluster-T1-V02; h3vo4-T1-V01; h2o-T1-V01; V-R-T1-V02; V-PRC_canonical; V-I1-T1-V01; V-I2-T1-V04; V-P-T1-V01; W-PRC-T1-V02; W-P-T1-V01 |
| ACCEPTED, verified saddle (number quoted in thesis, with A4 qualification) | 1 | V-TS2-T1-V05 |
| APPARENT estimate retained and quoted as such | 1 | W-TS-T1-V02 (climbing image; W-TS row of Table 4.3) |
| DIAGNOSTIC test that answered its question | 7 | V-TS1-T1-V05; V-TS1-T1-V06 (band A sealing); V-TS2-T1-V06; V-TS2-T1-V07 (band B A4); W-TS-T1-V05 (frozen caps); W-TS-T1-V06; W-TS-T1-V07 (band D A4) |
| BRACKETED closure (quoted as bracket) | 1 | V-TS3-T1-V05 |
| FAILED, interpolation artifact, excluded | 3 | V-TS1-T1-V01; V-TS2-T1-V01; V-TS3-T1-V01 |
| FAILED, slid off ridge into minimum (method outcome) | 1 | V-TS1-T1-V04 |
| REJECTED for connectivity after full testing | 1 | W-TS-T1-V04 (degenerate proton-shuttle saddle) |
| SEALED non-elementary: trail rows closing band A | 2 | V-TS1-T1-V02; V-TS1-T1-V03 |
| TRAIL rows inside the band B refinement that produced the verified saddle | 3 | V-TS2-T1-V02; V-TS2-T1-V03; V-TS2-T1-V04 |
| TRAIL rows inside the band C refinement that produced the bracket | 3 | V-TS3-T1-V02; V-TS3-T1-V03; V-TS3-T1-V04 |
| TRAIL row superseded by the rejected refined saddle | 1 | W-TS-T1-V03 |
| SUPERSEDED by a better run, kept on record | 3 | V-PRC-T1-V01; V-I2-T1-V03; W-TS-T1-V01 |
| **Total** | **37** | |

### 1.1 The numbers that answer your question directly

- **Jobs you ran in Tier 1 (registered)**: 37.
- **Accepted (verified, quoted in the thesis)**: 11 of 37 (ten minima and one saddle). One further job supplies the apparent steam estimate, and one supplies the band C bracket, so 13 of 37 jobs (35 percent) carry numbers that appear in the thesis; all 37 appear in the audit trail that makes those numbers defensible (register, Chapters 3 and 4, memos Rounds 1 to 9).
- **Failed or rejected, clearly separated**: 3 interpolation artifacts excluded up front; 1 refinement that slid into a minimum; 1 converged saddle rejected for connectivity (band D). That is 5 of 37 (14 percent) that produced no usable state, and each produced a documented diagnosis instead.
- **Saddle campaign scoreboard**: 4 steps attacked; 1 verified, 1 bracketed, 1 sealed non-elementary, 1 degenerate. Zero steps left unresolved.

### 1.2 What the 14 percent failure rate means

Every failure occurred in the same place: forcing a first-order saddle out of an ultra-flat, multi-event step on a floppy 30-atom semi-empirical surface. Nothing failed in minima optimization, frequency confirmation, or single-point evaluation. This pattern is the single most important fact for cloud design (Section 2).

---

## 2. Objective Cloud Forecast ("One Chance Bus")

### 2.1 What the Tier 1 evidence says about each job type

| Job type | Tier 1 evidence of behavior on this cluster | Failure risk on cloud (objective) | Allowed on the bus? |
|---|---|---|---|
| Single-point (SP) energies at hybrid DFT on EXISTING optimized geometries | All 37 jobs produced final energies without exception; SCF never failed at xTB | Near zero. SCF at hybrid level on a closed-shell 30-atom cluster with V(V) d0 is routine with standard settings; worst case needs damping, which the prepared inputs pre-empt | **YES, this is the bus** |
| Minima geometry optimizations at hybrid DFT starting from verified xTB minima | Every minimum converged at xTB, often far from its start | Low to moderate: will converge, but on this flat surface may settle into a near-energy conformer tens of kJ/mol off; still useful | Yes, but only AFTER all SP jobs, and never blocking them |
| Frequency calculations at hybrid DFT on minima | xTB frequencies completed every time | Low risk mechanically; real cost is wall-time (numerical Hessian is 180 finite displacements for 30 atoms) | Optional last item in the window |
| Transition-state optimizations (OptTS) of bands A, C, D at hybrid DFT | Documented ride-off, degenerate, non-elementary behavior at xTB; converged only 2 of 4 bands after 3 continuation rounds each | High (objectively above 50 percent per step, based on this campaign's own record). A failed OptTS produces nothing quotable | **NO. Never put these on the one-chance bus** |
| OptTS re-verification of the verified V-TS2 at hybrid DFT | The saddle exists and the A4 mode direction is known | Moderate: better odds than bands A/C/D because an exact-mode start is available, but a slide would still leave you empty-handed | Not on the first bus |

### 2.2 The recommended bus manifest (SP re-ranking package)

Purpose: upgrade every headline number of the thesis to hybrid-DFT-quality statements ("re-confirmed at two hybrid levels"), with zero optimization risk. Each job is fully independent; any partial completion still yields an interpretable result, because the queue is ordered by thesis priority.

Queue order (reverse dependencies impossible; references first because every relative energy needs them):

| Slot | Job | Structure source (existing file) | Why this slot |
|---|---|---|---|
| 1 | cluster SP (B3LYP and PBE0) | 01_models/cluster/cluster-T1-V02.xyz | Reference zero of both routes; tiny job, validates settings end to end |
| 2 | H3VO4 SP (both levels) | 01_models/h3vo4/h3vo4-T1-V01.xyz | Vanadium reference zero |
| 3 | H2O SP (both levels) | 01_models/h2o/h2o-T1-V01.xyz | Water reference zero |
| 4 | V-PRC SP (both levels) | 02_tier1/V-PRC/V-PRC_canonical.xyz | Headline: the 127.31 kJ/mol adsorption preference |
| 5 | W-PRC SP (both levels) | 02_tier1/W-PRC/W-PRC-T1-V02.xyz | Same headline, water side |
| 6 | V-I1 SP (both levels) | 02_tier1/V-I1/V-I1_canonical.xyz | Chemisorption sink |
| 7 | V-TS2 SP (both levels) | 02_tier1/V-TS2/optts3_bandB_ci.xyz | Hybrid single-point on the verified saddle: upgrades the +160.70 barrier statement |
| 8 | V-I2 SP (both levels) | 02_tier1/V-I2/V-I2_canonical.xyz | Barrier needs both wells |
| 9 | V-P SP (both levels) | 02_tier1/V-P/V-P_canonical.xyz | Exothermicity claim |
| 10 | W-P SP (both levels) | 02_tier1/W-P/W-P-T1-V01.xyz | Steam step reaction energy |
| 11 | W-TS CI SP (both levels) | 02_tier1/W-TS/neb_ts_bandD_NEB-CI_converged.xyz | Apparent steam estimate at hybrid level (interpreted as apparent, geometry is not a DFT saddle) |
| 12 | V-R SP (both levels) | optional; equals slot 1+2 in the supermolecular sense | Consistency check only |

Method settings (to be locked into the generated inputs): B3LYP-D3(BJ)/def2-TZVP and PBE0-D3(BJ)/def2-TZVP single points; `TightSCF`, `SlowConv` fallback pre-armed with `KDIIS` and `SOSCF` fallback; `Grid5`/`FinalGrid6`; charge 0, multiplicity 1 everywhere (all species are closed-shell singlets at V(V) d0); the def2 ECP on vanadium is applied automatically by ORCA. Expected cost per structure per level: minutes on a modern cloud node; the whole package, both functionals, comfortably inside one submission window including queue time.

If, and only if, slots 1 to 12 finish inside the window: add minima optimizations (`Opt`) at B3LYP-D3(BJ)/def2-SVP for the 10 minima in the same priority order, then frequencies on those optima. Never queue OptTS on this bus.

### 2.3 What the SP package will and will not do

Will:
- Replace "at a second level of theory, we trust this ordering" with measured hybrid-DFT re-ranking for: adsorption preference (127.31), chemisorption sink (188.20), pathway exothermicity (82.90), the verified first-cleavage barrier (160.70 at the saddle geometry), and the steam estimate (65.14, still apparent).
- Feed Chapter 5 a clean "robustness across levels" table (xTB vs B3LYP vs PBE0), the strongest defensible claim this thesis can carry without new optimizations.

Will not:
- Produce verified hybrid-DFT barriers (that needs DFT gradient optimization and frequencies, the next bus, not this one).
- Resolve bands A, C, D (documented as requiring microstepping or higher-tier sampling; assigned to future work).

Expected direction of changes (stated honestly so nothing surprises you): cluster-model xTB adsorption values commonly soften at hybrid level, so the adsorption preference is likely to shrink from 127.31; with a margin that size the ORDER (vanadic acid wins the acid site) is safe. Barriers on this class of surface commonly move by tens of kJ/mol with level; the thesis already states this uncertainty range, and the robustness table quantifies it rather than hiding it.

### 2.4 What I need from you to build the package

1. Cloud provider and instance shape: ORCA version available (must be 6.x for matching keywords), cores per node, walltime limit, and whether jobs are submitted as one batch or separate runs.
2. Your xyz folder as it stands (the paths in the table, from your offline project), so the generated inputs reference geometry files you actually hold.
3. One line confirming target: "build the 12-slot SP package" (default unless you object).

On receipt I generate: 24 ready inputs (12 structures x 2 levels, or combined-functionals per structure if preferred), a batch script, a checksum manifest tying every output to a register row, and an ingestion template so the moment you paste results here, audit and Chapter 5 table production happen in one turn.

---

*This document is the canonical campaign census for the thesis audit trail and may be cited in Chapter Five as the Tier 1 execution record.*
