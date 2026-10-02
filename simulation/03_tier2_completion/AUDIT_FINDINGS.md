# AUDIT FINDINGS — what the repository actually contains

A file-by-file check of the Tier 1 and cloud Tier 2 work, done against the
outputs themselves on 2 October 2026, ahead of the completion runs. Everything
below is arithmetic that can be repeated from the files; the numbers quoted in
the project's own summaries are reproduced or corrected here, one by one.

Use this as the evidence base for the methodology and limitations sections.

---

## 1. Counts — confirmed

| claim | check | result |
|---|---|---|
| 37 Tier 1 jobs | rows in `analysis/calculation_register.csv` | 37 ✔ |
| 29 higher-level jobs | 5 optimisation outputs + 24 bus outputs | 29 ✔ |
| 24 single points = 12 structures × 2 functionals | `cloud_results/bus_results/bus_manifest.csv` | ✔ (of which **23 succeeded**; `slot06_vi1_b3lyp` failed with an empty energy) |
| every Tier 1 job logged with input, output, energy, verdict | register + `provenance_map.md` | ✔, including the superseded and excluded runs |
| 9 audit rounds | `audit/TIER1_VERIFICATION_ROUND02…10.md` (+ census, cleanup, way-forward) | ✔ |

## 2. The unconverged cluster reference

`cloud_results/opt_results/results/opt03_cluster.out`:

```
GEOMETRY OPTIMIZATION CYCLE   1 ... FINAL SINGLE POINT ENERGY  -1709.384567260244
GEOMETRY OPTIMIZATION CYCLE   2 ... FINAL SINGLE POINT ENERGY  -1709.388796011604
Norm of the Cartesian gradient ... 0.0277460998
RMS gradient                     ... 0.0034153088
ORCA finished by error termination in SCF gradient
```

* no `THE OPTIMIZATION HAS CONVERGED`, no `TOTAL RUN TIME` line;
* `opt_status.log` records `FAIL opt03_cluster`, while
  `opt_manifest.csv` records `opt03_cluster,PASS,−1709.388796011604,YES`;
* the two files disagree, and no second cluster output exists in the repository.
* the final DFT frame differs from the Tier 1 cluster minimum by max 0.055 Å /
  rms 0.029 Å, i.e. it is the same basin, slightly relaxed.

**Consequence**: the cluster reference for every binding energy is provisional.
`E(cluster)` appears in both reference zeros, so both absolute binding energies
change if this number moves. The margin between them does not (see §3).

The failure mode is an error termination in the *SCF gradient* step accompanied by
libmpi `epoll` warnings — that is the MPI transport, not the chemistry, so a plain
re-run (or one with fewer ranks) is expected to finish.

## 3. Binding energies — reproduced, with one caveat

From `cloud_results/opt_results` (B3LYP‑D3(BJ)/def2‑TZVP, `DefGrid3`,
kT = 2625.499638 kJ/mol per Eh):

```
E(V-PRC) - E(cluster) - E(H3VO4) = -2956.254445175078 +1709.388796011604 +1246.825013958827
                                 = -0.040635204647 Eh = -106.69 kJ/mol
E(W-PRC) - E(cluster) - E(H2O)   = -1785.850531808839 +1709.388796011604  +76.426623125197
                                 = -0.035113066933 Eh =  -92.20 kJ/mol
margin (V over W)                =  -0.005522137714 Eh =  -14.49 kJ/mol
```

The margin can be written without the cluster at all:

```
E(V-PRC) - E(W-PRC) - E(H3VO4) + E(H2O) = -14.49 kJ/mol
```

so it survives any error in `E(cluster)`; the two individual binding energies do
not. Tier 1 gave −196.90 and −69.59 kJ/mol (margin −127.31). The Tier 2 margin is
therefore **11 % of the Tier 1 margin**, not 90 % — worth stating exactly.

## 4. The single-point set is not a pathway

B3LYP‑D3(BJ)/def2‑TZVP single points on the **unrelaxed** Tier 1 geometries,
relative to `E(cluster) + E(H3VO4)` (kJ/mol):

| state | B3LYP (bus) | Tier 1 (xTB) |
|---|---|---|
| V‑PRC | −51.2 | −196.9 |
| V‑I1 | **job failed** | −385.1 |
| V‑TS2 | +330.5 | −224.4 |
| V‑I2 | +116.6 | −342.4 |
| V‑P | **+543.9** | −82.9 |

and on the steam side, relative to `E(cluster) + E(H2O)`: W‑PRC −71.1, W‑TS +49.8,
W‑P **+11.1** (Tier 1: −69.6, −4.4, −65.9).

The product of an irreversible dealumination sitting 544 kJ/mol *above* the
reactant is the clearest possible statement that these are method-sensitivity
probes, not a reaction profile. The report already says so; this table is the
evidence.

Two further numbers from the same set: the steam hydrolysis barrier is +65.14
kJ/mol at Tier 1 and **+120.87 kJ/mol** as a B3LYP single point on the same
unrelaxed shape (+118.4 with PBE0). Those are the two figures the report quotes as
"carrying caveats" — the caveat is that the upper figure is a single point on a
Tier 1 geometry, not a saddle at its own level.

## 5. The "213 kJ/mol" statement needs its sign checked

The report says the transition state in the single-point set "sits 213 kJ/mol
below one of the states it is supposed to connect". What the numbers support:

* at the same level (B3LYP), the V‑TS2 single point sits **+213.9 kJ/mol above**
  V‑I2, and +213.4 kJ/mol **below** V‑P — but V‑P is not one of its endpoints;
* at PBE0 the same saddle sits +356.9 above V‑I1 and +249.9 above V‑I2;
* V‑I1 has no B3LYP energy at all, so at B3LYP the lower endpoint of that step
  does not exist in this set.

There is no same-level comparison in which the saddle lies below either of its own
endpoints. Quote the +213.9 (above V‑I2) if the sentence is kept, or drop the
claim; as written it will not survive an examiner recomputing it.

## 6. Aluminium coordination at the chemisorbed state — the self-correction is right

Distances measured in the Tier 1 accepted structures:

| state | Al–O distances within 2.1 Å | count |
|---|---|---|
| V‑PRC (`V-PRC_canonical.xyz`) | 1.705, 1.724, 1.743, 1.925 (V‑O), 2.052 | 5 contacts, one of them the vanadic oxygen |
| V‑I1 (`V-I1_canonical.xyz`) | 1.687, 1.705, 1.729, 1.804 | **4** — framework intact, V at 2.701 Å |

So the correction recorded in the project memos is confirmed by the coordinates:
at the chemisorbed intermediate the aluminium still has its four framework oxygens
and nothing is broken. Two associated items:

* `analysis/tier1_summary.md` describes V‑I1 as "5‑coord Al". The geometry does
  not support that label; the register should be corrected.
* the Tier 1 V‑PRC is **not** purely hydrogen-bonded — it already carries an
  Al···O(V) contact of 1.925 Å. The narrative step "loose attachment first, it
  digs in later" is a reasonable description of the energy, but the PRC geometry
  is already past a pure H‑bond picture. Say that explicitly rather than letting
  a reader discover it.

## 7. Integration grids are mixed

`cloud_opt/jobs/*.inp` use `DefGrid3`; `cloud_bus/jobs/*.inp` use
`Grid5 FinalGrid6`. Energies from the two families differ at a level that matters
when the margin being quoted is 14.49 kJ/mol. The completion package uses
`DefGrid3` throughout (matching the converged geometries and the 13.5 h of
optimisation already paid for); if the finer grid is preferred, change every job
at once and re-run the references too.

## 8. The counterpoise template is wrong

`orca_templates/t3_pbe0_counterpoise.inp` requests `! … Counterpoise` and defines
fragments in `%geom`. ORCA has no `Counterpoise` keyword. The ORCA 6.1.1 manual
(§2.11.1) gives the supported construction:

```
%frag
  Definition
    1 {0 1 2 … 21} end
    2 {22 23 … 29} end
  end
end
%geom
  GhostFrags {1} end
end
```

with a second job ghosting fragment 2. The completion package uses this, plus a
fallback that writes the ghost atoms explicitly (`O :`) for builds on which the
fragment route is unhappy. CP-corrected *geometry optimisation* would need the
`BSSEOptimization.cmp` compound script and is deliberately out of scope.

## 9. Run times, and what the compute line implies

Measured `TOTAL RUN TIME` values: 3‑atom opt 19 s; 8‑atom opt 11 m 56 s; 30‑atom
opt **9 h 52 m**; 25‑atom opt **3 h 34 m**; the 24 single points 3 s – 11 m each
(~2 h 10 m in total). Total logged calculation time ≈ 16 h.

A "compute" charge of about $25 at the published per-hour rate for that machine
size therefore implies roughly 110–130 h of **uptime**, i.e. around five days of a
machine that was mostly idle between runs. That is the number to act on: allocate
between sessions rather than resizing, since a bigger machine is billed at
roughly its core ratio while the speed-up is less than proportional.

*(The billing reconstruction itself cannot be checked from this repository — it
contains no billing data — so it is quoted here only as a planning assumption.)*

## 10. Practical note for anyone auditing this archive with command-line tools

The ORCA outputs produced on the Windows laptop (`01_models/`, `02_tier1/`) are
**UTF‑16 encoded**, so `grep` silently finds nothing in them and a naive parser
appears to work on empty text. The cloud outputs are ordinary UTF‑8. Both
`tools/audit_tier2.py` in this package and the existing `verify_tier1.py` read
both encodings; any new script must too.

---

## What could not be verified from here

* VM power state, the student-credit clock, and the current public IP — no billing
  or portal data in the repository (§3 of the runbook lists the three checks);
* the identity of the machine used for the bus (the bus jobs request 8 ranks and
  `cloud_bus/README_CLOUD_BUS.md` still describes a DigitalOcean droplet, while the
  optimisation jobs ran with 4 ranks), which is why every time estimate above is
  given as a bracket rather than a number;
* Chapter Three, Four and Five prose — they are not in this repository, so the
  claim that "the archive stops at Chapter Four" could not be checked here.
