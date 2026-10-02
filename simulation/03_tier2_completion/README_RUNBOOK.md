# TIER 2 / TIER 3 COMPLETION RUNBOOK

Everything needed to finish the cloud DFT work of this project: the input files,
the geometries, a resumable runner, the audit tools, and the order in which to
run them so that the remaining credit buys the thesis rather than a pile of
half-finished optimisations.

Package root: `simulation/03_tier2_completion/`

---

## 0. What this package is, and what it is not

**It is** the four scopes that were agreed as feasible: frequencies on the
already-optimised structures, a counterpoise correction, PBE0 single points on
relaxed geometries, and optimisations for the eight states the Tier 2 plan
called for but never ran.

**It is not**

* a new method, a new basis set, or a new model — every job keeps the level you
  already used, so the new numbers join the old ones without a caveat;
* an attempt to make the transition states appear. Three saddle refinements are
  included, each with a decision rule written down **before** the run, exactly
  so that a failure is reportable as a failure;
* a replacement for the missing chapter. The thesis work (methodology rewrite,
  research questions, Chapter Five, title page) happens on the laptop and is not
  affected by whether these jobs run.

**Nothing in this package deletes or overwrites any existing result.** A re-run
of a job that already has an output file is written alongside it.

---

## 1. Five things the repository audit found — read this before spending money

These were checked directly against the files in this repository, not against
the summaries.

**(1) The cluster minimum was never actually converged.**
`cloud_results/opt_results/results/opt03_cluster.out` ends with
`ORCA finished by error termination in SCF gradient` after **2 geometry cycles**
(RMS gradient 3.4e-3, no convergence string, `TOTAL RUN TIME` absent), yet
`opt_manifest.csv` and `opt_status.log` disagree about it (PASS vs FAIL) and the
manifest quotes an energy from that run. The cluster is **the reference zero of
every binding energy in the thesis** — the 106.69 and 92.20 kJ/mol numbers both
depend on it. Scope 1 job `s1_03` re-runs it. The failing run looks like an
MPI/IO failure at the gradient step (the output carries libmpi `epoll` warnings),
not a chemistry problem; if it dies the same way, set `%pal nprocs 2` and retry.

**(2) The headline margin does not depend on the cluster — the absolute
binding energies do.**
Reproduced from `cloud_results/opt_results` energies:
`E(V‑PRC) − E(cluster) − E(H3VO4) = −106.69 kJ/mol`,
`E(W‑PRC) − E(cluster) − E(H2O) = −92.20 kJ/mol`, margin **14.49 kJ/mol**. The
margin cancels the cluster exactly (it equals `E(V‑PRC) − E(W‑PRC) − E(H3VO4) +
E(H2O)`), so the headline survives an unconverged reference; the two individual
binding energies do not. Fix (1) before quoting 106.69 / 92.20.

**(3) The 24 single points are not a pathway, and one of them is missing
entirely.**
At B3LYP on the unrelaxed Tier 1 shapes, V‑P (the product) sits **+544 kJ/mol**
above the reference and W‑P **+82 kJ/mol**, i.e. dealumination appears strongly
endothermic, the opposite of the Tier 1 result. `slot06_vi1_b3lyp` failed
(empty energy), so the V‑I1 → V‑I2 barrier cannot even be formed from that set.
The report already treats this set as evidence about method sensitivity; this
package supersedes it with relaxed geometries.

**(4) The counterpoise template in `orca_templates/` uses a keyword that does
not exist.**
`t3_pbe0_counterpoise.inp` writes `! ... Counterpoise` with a `%geom Fragments`
block. ORCA has no `Counterpoise` keyword (ORCA 6.1.1 manual, section 2.11.1).
The supported route is
`%frag Definition 1 {...} end 2 {...} end end` plus `%geom GhostFrags {n} end`.
Scope 2 uses the supported route, and `tools/gen_inputs.py --ghost-xyz` writes a
second, more primitive fallback (ghost atoms written as `O :`) in case the
fragment route misbehaves on your build. Do not run the old template.

**(5) Two different integration grids are already mixed in the archive.**
The five optimisation jobs ran with `DefGrid3`; the 24 bus single points ran with
`Grid5 FinalGrid6`. Energies from the two sets are not strictly comparable at the
kJ/mol level. The completion package standardises on **`DefGrid3`** everywhere,
because that is what the four converged geometries and the 13 hours of
optimisation already spent were computed with. If you would rather move the whole
study to the finer grid, do it for *every* job at once
(`sed -i 's/DefGrid3/Grid5 FinalGrid6/' jobs/*/*.inp`) and re-run the references
as well — never mix.

---

## 2. Time and money, calibrated on your own logs

Measured from the outputs in this repository (4-core VM for the optimisations,
8 ranks for the bus):

| job | atoms | wall time |
|---|---|---|
| `opt01_h2o` (B3LYP opt) | 3 | 19 s |
| `opt02_h3vo4` (B3LYP opt) | 8 | 11 m 56 s |
| `opt03_cluster` (B3LYP opt) | 22 | crashed after 2 cycles (~11 min) |
| `opt04_vprc` (B3LYP opt) | 30 | **9 h 52 m** |
| `opt05_wprc` (B3LYP opt) | 25 | **3 h 34 m** |
| 24 bus single points | 3–30 | 3 s – 11 m each, ~2 h 10 m total |

So one 30-atom geometry optimisation costs about ten hours on the 4-core box,
one 30-atom single point 15–25 minutes, and a frequency job on the same system
should be budgeted at **1.5–3× its optimisation** (a Hessian is not free).

| scope | jobs | honest estimate | cost at $0.19–0.23/h |
|---|---|---|---|
| 1 — frequencies + cluster fix | 5 opt+freq | 12–30 h | $2–7 |
| 2 — counterpoise | 4 single points | 1–3 h | < $1 |
| 3 — PBE0 on relaxed geometries | 13 single points | 4–10 h | $1–2 |
| 4a — four missing minima | 4 opt+freq | 40–110 h | $8–25 |
| 4b — three saddles + one diagnostic | 3 OptTS+freq, 1 opt | 30–150 h | $6–35 |

**Stage it; do not launch everything.**

* **Stage A** = scope 1 → scope 2 → scope 3. 20–45 h, well under $10. It fixes
  the reference zero, adds ZPE and Gibbs corrections at 298.15 K **and 1003.15 K**
  (which the methodology chapter currently promises and does not deliver), adds
  the BSSE correction, and gives the second functional on relaxed geometries.
* **Stage B** = scope 4a (the four minima). 40–110 h. This is what turns the
  Tier 2 numbers from five structures into a pathway.
* **Stage C** = the V‑TS2 refinement only. 10–40 h. The one barrier that carries
  the mechanism.
* **Stage D** = W‑TS, V‑TS3, V‑TS1. Only with credit to spare and the calendar
  to match.

Where the earlier advice in the project notes needs correcting: resizing to more
cores does **not** keep the cost constant. Azure bills the larger machine at
roughly its core ratio, while ORCA's speed-up is sub-linear, so 16 cores buys
calendar time, not money. And the $24.66 of "compute" in the billing report
implies about 110–130 h of *machine uptime*, while the ORCA logs account for only
**~16 h of actual calculation** — most of that line was the VM billing while it
sat idle. Deallocate between sessions; that discipline is worth more than any
tuning of the inputs.

---

## 3. Before the first job: three checks, two minutes

**a) Is the machine deallocated?**
Portal → Virtual machines → *your VM* → Overview → Status must read
**"Stopped (deallocated)"**. "Stopped" alone still bills compute. From a shell
with `az` installed:

```bash
az vm get-instance-view -g <RESOURCE_GROUP> -n <VM_NAME> \
   --query "instanceView.statuses[?contains(code,'PowerState')].displayStatus" -o tsv
az vm deallocate -g <RESOURCE_GROUP> -n <VM_NAME>      # if it is only "Stopped"
```

**b) Is the student credit still alive?**
The Azure for Students window closes 12 months after activation regardless of the
remaining balance. Check Portal → Cost Management + Billing → Credits (or the
Education page). If it has lapsed, renew while your student verification is still
valid; nothing else in this package matters until that is settled.

**c) What is the public IP now?**
A deallocate/start cycle can change it (and a reserved address keeps billing while
the VM is off).

```bash
az vm show -d -g <RESOURCE_GROUP> -n <VM_NAME> --query publicIps -o tsv
```

Then a two-minute smoke test on the machine itself, before anything long:

```bash
export PATH=/opt/orca:$PATH
cd ~/03_tier2_completion
/opt/orca/orca jobs/scope1/s1_01_h2o_optfreq.inp > /tmp/smoke.out 2>&1
grep -E "ORCA TERMINATED NORMALLY|FINAL SINGLE POINT ENERGY" /tmp/smoke.out
```

Water takes seconds. If it prints a final energy, the queue is good to go.

---

## 4. Upload, run, pull back

From the laptop, inside `simulation/`:

```bash
# Linux / WSL / Git Bash
rsync -avz 03_tier2_completion <user>@<IP>:~/
```

The eight Tier 1 geometries are **already inside** `xyz/` (`v-i1.xyz`, `v-i2.xyz`,
`v-p.xyz`, `w-p.xyz`, `v-ts2.xyz`, `v-ts3.xyz`, `w-ts.xyz`, `v-ts1.xyz`), copied
from `02_tier1/`; there is no separate upload step for them.

On the machine:

```bash
cd ~/03_tier2_completion
export ORCA=/opt/orca/orca
bash run_scope.sh 1                 # Stage A, first part
bash run_scope.sh 2
bash run_scope.sh 3
bash run_scope.sh 4 40              # Stage B, stop after 40 h of this session
bash run_scope.sh 3                 # re-run: regenerates and adds the new states
```

`bash run_scope.sh all 60` chains 1 → 2 → 4 → 3 in one session if you would
rather not babysit it. Every job's output, energy and wall time land in
`results/manifest_scope<N>.csv`; every finished job is skipped on a re-run; a
failed job never stops the queue. To stop the queue cleanly after the job that is
running, `touch results/STOP`. To keep it alive across disconnections,
`nohup bash run_scope.sh 1 > results/run1.log 2>&1 &` and `tail -f` the log.

Pull the results back with:

```bash
bash tools/pull_results.sh <user>@<IP>
```

and then, on the laptop:

```bash
python3 tools/audit_tier2.py results --table --cp --csv results/summary.csv
```

which reproduces every number in this section from the outputs themselves — no
value is ever typed by hand into a table.

---

## 5. What each scope does, and the rules decided in advance

### Scope 1 — `jobs/scope1/` (5 jobs)
Re-optimises to `TightOpt` and runs `FREQ` with `%freq Temp 298.15, 1003.15` for
H2O, H3VO4, and the cluster, and takes the Hessian (with a short re-optimisation)
on V‑PRC and W‑PRC.

*Gate*: terminated + converged + **zero** imaginary modes.
*Cheap option*: for the two large complexes, `sed -i 's/ Opt Freq/ Freq/'` on the
input skips the re-optimisation and only computes the Hessian at the existing
geometry.
*Buys*: the reference zero at a converged cluster, ZPE-corrected and Gibbs-corrected
energies at both 298.15 K and 1003.15 K (closing the "no temperature effects" gap
at no extra cost — the two temperatures come from one Hessian), and the fixed
cluster that every binding energy needs.

### Scope 2 — `jobs/scope2/` (4 jobs)
Boys–Bernardi counterpoise at PBE0 for V‑PRC and W‑PRC via
`%frag Definition` + `%geom GhostFrags`, one job per fragment.

*Gate*: both jobs terminate normally.
*Buys*: the BSSE answer. Expect it to matter: the vanadium complex and the water
complex borrow different amounts of basis from the framework, so the correction
acts differently on the two sides of a 14.49 kJ/mol margin. **If the margin
inverts under counterpoise, report that** — it is a real result, and a thesis
that reports it is stronger than one that hides it.
*Fallback*: `python3 tools/gen_inputs.py --ghost-xyz`, then run the two inputs in
`jobs/scope2_fallback/` manually (same level, same geometry, ghost atoms written
as `O :`).

### Scope 3 — `jobs/scope3/` (13 jobs, generated at run time)
`python3 tools/gen_inputs.py --scope3` builds one PBE0 single point for every
geometry present in `results/geom/` and `bash run_scope.sh 3` runs them. Run it
again after Stage B to pick up the newly relaxed states.

*Gate*: terminates normally; no frequency needed.
*Buys*: the B3LYP/PBE0 cross-check on **relaxed** geometries — the check the old
24 single points could not provide, because they used unrelaxed shapes.

### Scope 4 — `jobs/scope4/` (8 jobs, cheapest first)
Four minima (V‑I1, V‑I2, V‑P, W‑P) with `Opt Freq`, then V‑TS2, V‑TS3, W‑TS with
`OptTS Freq` (`Calc_Hess true`), then the V‑TS1 diagnostic as a plain `Opt`.

*Pre-registered rules — write these in the register before looking at the number:*
* a minimum is accepted only if terminated + converged + **0** imaginary modes;
* a saddle is accepted only if terminated + converged + **exactly 1** imaginary
  mode **and** the two ±0.1 Å displacement jobs from
  `python3 tools/gen_inputs.py --displace ...` land within 5 kJ/mol of the two
  minima that step is supposed to connect;
* anything else is recorded as **"not established at this level"**, and the
  barrier goes into the limitations section rather than into a table;
* the V‑TS1 job is a plain `Opt` on purpose: at Tier 1 every candidate slid into
  one minimum and the "saddle" was reproduced from both displacement directions.
  If it slides at Tier 2 as well, the reportable statement is *"chemisorption of
  vanadic acid is barrierless in this model"* — which is a result, not a failure.

---

## 6. Where the results go in the thesis

| new evidence | replaces / closes |
|---|---|
| converged cluster + 5 frequencies (298.15 K, 1003.15 K) | the methodology chapter's promise of thermochemistry at 1003 K; the missing cluster convergence |
| counterpoise-corrected interaction energies | "no basis-set correction on the binding energies" |
| PBE0 on relaxed geometries | the retracted 24 single-point set; gives a clean two-functional table |
| DSF pathway for the four missing minima | "five of the thirteen structures" |
| V‑TS2 decision (accepted or not established) | the one barrier that currently rests on a failed A4 test |

Research question 2 (does vanadium lower the barriers relative to steam?) is still
not answerable step-for-step, because the two routes pass through different
intermediates; the honest framing is the one already in the report — vanadium's
route is *thermodynamically* far more favourable. Research question 3 (charge
transfer) needs a Mulliken/Hirshfeld analysis on the new wavefunctions
(.gbw files are kept in `results/`), which is a laptop job, not a cloud job.

---

## 7. Troubleshooting

| symptom | action |
|---|---|
| job dies in "SCF gradient" with libmpi/epoll warnings | infrastructure, not chemistry: lower `%pal nprocs` to 2 and re-run that job only |
| SCF does not converge | add `KDIIS SOSCF` to the keyword line (the cluster job already carries it) |
| "The optimization did not converge" at 200 cycles | the geometry is still descending: copy the last frame from `results/geom/`, raise `%geom MaxIter`, re-run as a new version |
| one imaginary mode in a minimum at −5 to −30 cm⁻¹ | a floppy mode, not a broken structure: check the mode animation, then re-run with `TightOpt` and a finer grid for that one state |
| `%frag`/`GhostFrags` input rejected | use `python3 tools/gen_inputs.py --ghost-xyz` and run the fallback inputs |
| queue stops early | check `results/STOP` and the budget argument; `results/manifest_scope*.csv` shows exactly what finished |

---

## 8. File map

```
03_tier2_completion/
├── README_RUNBOOK.md            this file
├── AUDIT_FINDINGS.md            what was verified in the repository, with the arithmetic
├── run_scope.sh                 resumable runner (scopes 1, 2, 3, 4, all)
├── plan/JOB_PLAN.csv            the 30 jobs, their purpose, cost bracket and gate
├── xyz/                         13 input geometries, atom order identical to Tier 1
│   ├── cluster-crashed-frame.xyz   the unconverged DFT frame, kept for the record
│   └── relaxed/                 counterpoise inputs read the geometries from here
├── jobs/scope1|scope2|scope3|scope4|diagnostics|scope2_fallback/
├── results/                     outputs, manifests, wall clock, final geometries
│   ├── geom/<state>.xyz         written automatically after every successful Opt
│   └── diagnostics/             ±0.1 Å displaced structures for the A4 test
└── tools/
    ├── gen_inputs.py            --scope3 | --ghost-xyz | --displace
    ├── audit_tier2.py           audit table, level tables, counterpoise analysis
    └── pull_results.sh          rsync the results back to the laptop
```
