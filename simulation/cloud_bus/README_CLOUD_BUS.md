# CLOUD BUS READ ME: The One-Chance Single-Point Package

**What this is**: 24 single-point jobs (12 structures x 2 hybrid DFT levels, B3LYP-D3(BJ) and PBE0-D3(BJ) with def2-TZVP) that re-rank every verified Tier 1 number at hybrid DFT quality. No optimization, no saddle hunting, nothing that failed all campaign is in this package.

**Total cost**: under 2 hours of an 8-core node, about USD 1 of DigitalOcean credit. You hold USD 200. The "one chance" is your calendar, not the money: even several failed re-runs cost pocket change.

---

## Step 1: Create the node (10 minutes)

1. Claim the GitHub Student Developer Pack DigitalOcean credit (USD 200, one year) at education.github.com, then sign in at cloud.digitalocean.com with the GitHub link.
2. Create a Droplet: **Ubuntu 24.04 LTS**, **Shared CPU Basic, 8 vCPU / 16 GB** (regular tier, about USD 48 per month billed per hour, so one afternoon costs about USD 0.40).
3. From Windows, connect: `ssh root@DROPLET_IP` in PowerShell or Git Bash.

## Step 2: Install ORCA 6.1 Linux (10 minutes)

1. Download `orca_6_1_0_linux_x86-64_shared_openmpi416.tar.xz` (or the 6.1 Linux build you already have forum access to) onto your laptop from the ORCA site, then copy up:
   `scp orca_6_1*.tar.xz root@DROPLET_IP:/opt/`
2. On the droplet:
   ```
   apt update && apt install -y xz-utils libgomp1 rsync
   cd /opt && tar -xf orca_6_1*.tar.xz && mv orca_6_1* orca
   /opt/orca/orca 2>&1 | head -3   # prints the ORCA banner error for missing input = binary alive
   ```

## Step 3: Upload the package

From your laptop, inside `thesis/simulation/`:
```
scp -r cloud_bus root@DROPLET_IP:~/
scp: copy your xyz files into cloud_bus/xyz/ FIRST (see Step 4 note)
```

## Step 4: Provide geometries (before running)

Copy these 12 files from your offline project into `cloud_bus/xyz/` before upload:
`h2o-T1-V01.xyz, h3vo4-T1-V01.xyz, cluster-T1-V02.xyz, V-PRC_canonical.xyz, W-PRC-T1-V02.xyz, V-I1_canonical.xyz, optts3_bandB_ci.xyz, V-I2_canonical.xyz, V-P_canonical.xyz, W-P-T1-V01.xyz, neb_ts_bandD_NEB-CI_converged.xyz, V-R-T1-V02.xyz`
(paths inside your project: `01_models/...` and `02_tier1/...`, exact locations are in `provenance_map.md`).

## Step 5: Smoke test (2 minutes)

```
cd ~/cloud_bus
export PATH=/opt/orca:$PATH
/opt/orca/orca jobs/slot01_h2o_b3lyp.inp > results_smoke.out
grep -E "TERMINATED NORMALLY|FINAL SINGLE" results_smoke.out
```
If the energy line prints, the full bus is GO. If SCF stalls, add `KDIIS SOSCF` to the keyword line of that input and retry (this is the only failure mode this package can plausibly have).

## Step 6: Run the bus (about 1 to 2 hours, unattended)

```
cd ~/cloud_bus
nohup bash run_bus.sh > bus_status.log 2>&1 &
```
Jobs run in slot order; every finished job lands in `~/cloud_bus/results/` immediately; `bus_manifest.csv` marks PASS/FAIL per job so a bad job can never poison the queue. Slot 07 saddle-region structure is labelled by its Round 10 status; its numbers are used with the verification outcome.

You may disconnect; `nohup` keeps the bus alive. Check anytime: `tail -5 bus_status.log`.

## Step 7: Pull results and destroy

From your laptop:
```
bash pull_results.sh DROPLET_IP
```
Upload `bus_results/` contents here (or paste `bus_manifest.csv`). I audit every energy at 2625.50 kJ/mol per Eh and build the three-level robustness table (xTB / B3LYP / PBE0) for the thesis in the same turn.

Then **destroy the droplet** (billing is hourly; also the credit clock is one year).

---

## Why DigitalOcean and not the others (student pack options)

| Option | Verdict for THIS job |
|---|---|
| **DigitalOcean (USD 200 credit, 1 year)** | **Pick this.** Full root Linux, zero quota surprises, your own wall clock, cheapest to learn in one afternoon. |
| Azure for Students (USD 100, no card) | Fine backup. Portal is heavy and VM size quotas sometimes need approval tickets that can eat the only afternoon you have. |
| GitHub Codespaces (free with pack) | Not for this: 30 minute idle timeout kills unattended runs; reinstall each codespace; 4 cores max. |
| Google Colab | Not for this: no persistent ORCA install, session caps, CPU tier tiny. |
| AWS / GCP free tiers | Work, but card verification and quota flows add risk you do not need. |

## Hard rules (from the census memo, Section 2.1)

- **Never** submit OptTS, NEB, or IRC on this bus. Saddle culture on this cluster is documented failure territory; the bus is single points only (plus optional minima `Opt` as a follow-up only after all 24 pass).
- One bus, one table: do not change methods mid-run. If a job FAILs, the queue continues; diagnose after the bus.
- `%pal nprocs 8 end` is set for the 8 vCPU droplet. If you take 16 vCPU instead, edit all inputs once: `sed -i 's/nprocs 8/nprocs 16/' jobs/*.inp` and raise `%maxcore` no higher than 3000.
