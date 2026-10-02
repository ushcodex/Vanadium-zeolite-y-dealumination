# UPLOAD AND RUN — one-page checklist (Stage A + B + C)

Everything below is copy-paste. The reasons behind each step are in
`README_RUNBOOK.md`; this file is only the order of operations.

Placeholders: `<user>` = cloud account, `<IP>` = current public IP of the VM.

---

## 0. Before you upload (2 minutes, on the cloud portal)

- [ ] VM status reads **"Stopped (deallocated)"** — "Stopped" alone still bills compute.
- [ ] Azure for Students credit is still inside its 12-month window.
- [ ] Note the **current** public IP (`az vm show -d -g <RG> -n <VM> --query publicIps -o tsv`). A deallocate/start cycle can change it.

## 1. Upload

From the laptop, inside `simulation/`:

```bash
rsync -avz 03_tier2_completion <user>@<IP>:~/
```

Nothing else needs uploading: the eight Tier 1 geometries are already inside
`xyz/` (`v-i1.xyz`, `v-i2.xyz`, `v-p.xyz`, `w-p.xyz`, `v-ts2.xyz`, `v-ts3.xyz`,
`w-ts.xyz`, `v-ts1.xyz`) and the counterpoise inputs read `xyz/relaxed/`, which
Stage A refreshes from its own output.

## 2. Smoke test (a few seconds — do not skip)

```bash
cd ~/03_tier2_completion
export ORCA=/opt/orca/orca
/opt/orca/orca jobs/scope1/s1_01_h2o_optfreq.inp > /tmp/smoke.out 2>&1
grep -E "ORCA TERMINATED NORMALLY|FINAL SINGLE POINT ENERGY" /tmp/smoke.out
```

A final energy means the binary, the environment and the input format all work.

## 3. Stage A — references, counterpoise, first single-point pass (~12–25 h)

```bash
tmux new -s run            # survive a dropped ssh connection
cd ~/03_tier2_completion
export ORCA=/opt/orca/orca

bash run_scope.sh 1        # 5 opt+freq jobs   (~10-20 h)
bash run_scope.sh 2        # 4 counterpoise    (~2-4 h)
bash run_scope.sh 3        # PBE0 single points on the relaxed geometries
```

Add a wall-clock ceiling per session if you want one: `bash run_scope.sh 1 40`
stops cleanly before the next job once 40 h of that session have elapsed.

## 4. Stage B — the four missing minima (~40–110 h)

```bash
ONLY='s4_0[1-4]*.inp' bash run_scope.sh 4     # V-I1, V-I2, V-P, W-P
```

## 5. Stage C — the V-TS2 saddle refinement (~10–40 h)

```bash
ONLY='s4_05*.inp' bash run_scope.sh 4         # V-TS2 OptTS + freq
```

## 6. Close out

```bash
bash run_scope.sh 3                            # adds PBE0 single points for the new geometries
python3 tools/audit_tier2.py results --table --cp --csv results/summary.csv
```

Then, back on the laptop, inside `simulation/`:

```bash
bash 03_tier2_completion/tools/pull_results.sh <user>@<IP>
python3 03_tier2_completion/tools/audit_tier2.py 03_tier2_completion/results \
        --table --cp --csv 03_tier2_completion/results/summary.csv
```

Deallocate the VM the moment the last job is pulled back.

---

## If something goes wrong

| Symptom | Action |
|---|---|
| A job ends without `ORCA TERMINATED NORMALLY` | Nothing is lost: the queue continues, the output stays as `results/<job>.out` and the row in the manifest reads FAIL. Read the tail of that file; re-run the same command to retry the failed job only. |
| You must stop now | `touch results/STOP` — the runner stops after the running job. Delete the file to continue. |
| Connection drops | Reconnect, `tmux attach -t run`. If tmux is gone, just re-run the same command: finished jobs are skipped. |
| You want to redo a job deliberately | Delete nothing. Re-run it; the new output is written as `results/<job>_V02.out` and a new manifest row, so the previous result is preserved. |
| Out of budget mid-Stage-B | Stop there. Stage A alone already supports the adsorption/competition chapter; Stage B answers the aluminium-extraction question. |

Stage D (`s4_06` V-TS3, `s4_07` W-TS, `s4_08` V-TS1) is **not** part of this
campaign. The inputs stay in `jobs/scope4/`; run them only if you later decide
to extend the study.
