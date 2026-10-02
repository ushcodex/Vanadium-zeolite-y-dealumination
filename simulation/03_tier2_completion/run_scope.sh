#!/usr/bin/env bash
# ============================================================================
#  run_scope.sh - resumable runner for the Tier 2 / Tier 3 completion package
# ============================================================================
#  USAGE
#     bash run_scope.sh 1                 # scope 1 (frequencies + cluster fix)
#     bash run_scope.sh 2                 # scope 2 (counterpoise)
#     bash run_scope.sh 3                 # scope 3 (PBE0 single points; generated first)
#     bash run_scope.sh 4                 # scope 4 (the eight missing states)
#     bash run_scope.sh all               # 1 -> 2 -> 4 -> 3, in that order
#     bash run_scope.sh 4 40              # stop cleanly once 40 h of THIS session have run
#
#  ENVIRONMENT
#     ORCA=/opt/orca/orca   path to the binary (default /opt/orca/orca)
#     BUDGET_HOURS=40       same as the second argument
#     DRYRUN=1              print what would run, execute nothing
#
#  BEHAVIOUR (deliberate, read once)
#     * Resumable   - a job whose results/<job>.out already shows
#                     "ORCA TERMINATED NORMALLY" is skipped, so you can stop and
#                     restart at any time without losing or repeating work.
#     * No deletion - a rerun of a job that already has an output file is written
#                     as results/<job>_V<timestamp>.out instead of overwriting.
#     * Budget      - the wall clock of the whole session is accumulated in
#                     results/wallclock.log; the runner stops BEFORE starting a
#                     new job once the budget is spent (a running job always
#                     finishes, so you never corrupt a calculation).
#     * Stop switch - create the file results/STOP and the runner stops after the
#                     current job.  Remove it to continue.
#     * One manifest per scope: results/manifest_scope<N>.csv
#     * Final geometries of Opt/OptTS jobs are copied to results/geom/<state>.xyz
#
#  Nothing here deletes or overwrites a previous result.
# ============================================================================
set -u

PKG="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PKG"

ORCA="${ORCA:-/opt/orca/orca}"
DRYRUN="${DRYRUN:-0}"
SCOPE="${1:-}"
BUDGET_HOURS="${2:-${BUDGET_HOURS:-0}}"

RES="$PKG/results"
GEOM="$RES/geom"
mkdir -p "$RES" "$GEOM" "$PKG/xyz/relaxed"

# job-base -> state name used for results/geom/<state>.xyz
declare -A STATE=(
  [s1_01_h2o_optfreq]=h2o          [s1_02_h3vo4_optfreq]=h3vo4
  [s1_03_cluster_optfreq]=cluster  [s1_04_vprc_optfreq]=v-prc
  [s1_05_wprc_optfreq]=w-prc
  [s2_01_vprc_cp_ghost_frag1]=v-prc-ghost-h3vo4
  [s2_01_vprc_cp_ghost_frag2]=v-prc-ghost-cluster
  [s2_02_wprc_cp_ghost_frag1]=w-prc-ghost-h2o
  [s2_02_wprc_cp_ghost_frag2]=w-prc-ghost-cluster
  [s4_01_vi1_optfreq]=v-i1   [s4_02_vi2_optfreq]=v-i2
  [s4_03_vp_optfreq]=v-p     [s4_04_wp_optfreq]=w-p
  [s4_05_vts2_optts]=v-ts2   [s4_06_vts3_optts]=v-ts3
  [s4_07_wts_optts]=w-ts     [s4_08_vts1_optfreq]=v-ts1
)

usage() {
  sed -n '2,33p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 1
}
[ -z "$SCOPE" ] && usage

case "$SCOPE" in 1|2|3|4|all) ;; *) echo "scope must be 1, 2, 3, 4 or all"; exit 1 ;; esac

if [ "$DRYRUN" != "1" ]; then
  if [ ! -x "$ORCA" ]; then
    echo "ERROR: ORCA binary not found or not executable: $ORCA"
    echo "       export ORCA=/opt/orca/orca   (or fix the path in .bashrc)"
    exit 1
  fi
  echo "ORCA binary : $ORCA"
  "$ORCA" 2>&1 | head -3 || true
fi

SESSION_SECONDS=0
BUDGET_SECONDS="$(awk "BEGIN{printf \"%d\", ($BUDGET_HOURS+0)*3600}")"
BUDGET_SECONDS="${BUDGET_SECONDS:-0}"
declare -i JOB_OK=0 JOB_FAIL=0 JOB_SKIP=0

manifest_header() {
  local f="$RES/manifest_scope$1.csv"
  [ -f "$f" ] || echo "job,scope,status,final_energy_Eh,runtime_s,output_file" > "$f"
}

record() {  # scope base status energy seconds outfile
  printf '%s,%s,%s,%s,%s,%s\n' "$2" "$1" "$3" "$4" "$5" "$6" \
    >> "$RES/manifest_scope$1.csv"
}

unique_out() {  # base -> a path that does not exist yet
  local b="$1" f="$RES/$1.out" i=2
  while [ -e "$f" ]; do f="$RES/${b}_V$(printf '%02d' $i).out"; i=$((i+1)); done
  printf '%s' "$f"
}

run_job() {  # scope, input-file
  local scope="$1" inp="$2"
  local base; base="$(basename "$inp" .inp)"
  local dir;  dir="$(dirname "$inp")"
  local existing="$RES/$base.out"

  manifest_header "$scope"

  if [ -f "$existing" ] && grep -aq "ORCA TERMINATED NORMALLY" "$existing"; then
    echo "  SKIP  $base   (already finished: results/$base.out)"
    record "$scope" "$base" SKIP "" 0 "results/$base.out"
    JOB_SKIP=$((JOB_SKIP+1)); return 0
  fi

  if [ -f "$RES/STOP" ]; then
    echo "  STOP file present - stopping before $base"; return 9
  fi
  if [ "$BUDGET_SECONDS" -gt 0 ] && [ "$SESSION_SECONDS" -ge "$BUDGET_SECONDS" ]; then
    echo "  BUDGET SPENT ($((SESSION_SECONDS/3600))h of ${BUDGET_HOURS}h) - stopping before $base"
    return 9
  fi

  local out; out="$(unique_out "$base")"
  local scratch="$RES/scratch_${base}.out"
  echo "  RUN   $base  ->  ${out#$PKG/}   ($(date -u '+%Y-%m-%d %H:%M UTC'))"
  if [ "$DRYRUN" = "1" ]; then
    echo "        [dry-run] $ORCA $inp > $scratch"
    SESSION_SECONDS=$((SESSION_SECONDS+600)); return 0
  fi

  local t0=$SECONDS
  ( cd "$PKG" && "$ORCA" "$inp" > "$scratch" 2>&1 )
  local dt=$((SECONDS-t0))
  SESSION_SECONDS=$((SESSION_SECONDS+dt))
  printf '%s,%s,%s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$base" "$dt" >> "$RES/wallclock.log"

  local energy="" status="FAIL"
  if grep -aq "ORCA TERMINATED NORMALLY" "$scratch"; then
    status="PASS"
    energy="$(grep -a "FINAL SINGLE POINT ENERGY" "$scratch" | tail -1 | awk '{print $NF}')"
  fi

  mv "$scratch" "$out"
  record "$scope" "$base" "$status" "$energy" "$dt" "${out#$PKG/}"

  if [ "$status" = "PASS" ]; then
    JOB_OK=$((JOB_OK+1))
    echo "        PASS  E=$energy  wall=$((dt/3600))h$(( (dt%3600)/60 ))m"
    # keep the final geometry of an Opt/OptTS run (single points have none)
    local g=""
    if grep -qE '(^|[[:space:]])(Opt|OptTS|TightOpt)([[:space:]]|$)' "$inp"; then
      for cand in "$dir/$base.xyz" "$dir/${base}_optimized.xyz"; do
        [ -f "$cand" ] && g="$cand" && break
      done
    fi
    if [ -n "$g" ]; then
      local st="${STATE[$base]:-$base}"
      cp "$g" "$GEOM/$st.xyz"
      echo "        geometry -> results/geom/$st.xyz"
    fi
  else
    JOB_FAIL=$((JOB_FAIL+1))
    echo "        FAIL  see ${out#$PKG/}  (last 5 lines:)"
    tail -5 "$out" | sed 's/^/          /'
    echo "        queue continues; nothing is deleted"
  fi
  return 0
}

run_dir() {  # scope, directory
  local scope="$1" d="$2" rc=0
  local files=()
  while IFS= read -r f; do files+=("$f"); done < <(find "$d" -maxdepth 1 -name '*.inp' | sort)
  if [ ${#files[@]} -eq 0 ]; then
    echo "  (no inputs in ${d#$PKG/})"; return 0
  fi
  for f in "${files[@]}"; do
    run_job "$scope" "$f" || { rc=$?; break; }
  done
  return $rc
}

prepare_relaxed() {
  echo "scope 2: geometry check"
  for s in v-prc w-prc; do
    if [ -f "$GEOM/$s.xyz" ]; then
      cp "$GEOM/$s.xyz" "$PKG/xyz/relaxed/$s.xyz"
      echo "  xyz/relaxed/$s.xyz  <-  results/geom/$s.xyz (scope 1 output)"
    else
      echo "  WARNING: results/geom/$s.xyz not found; using the pre-existing"
      echo "           xyz/relaxed/$s.xyz.  The counterpoise energy is only valid if"
      echo "           this geometry is the SAME one whose supermolecule energy you quote."
    fi
  done
}

generate_scope3() {
  echo "scope 3: generating PBE0 single points from the relaxed geometries found"
  if ! command -v python3 >/dev/null 2>&1; then
    echo "  ERROR: python3 not found; cannot generate scope 3 inputs."; return 1
  fi
  python3 tools/gen_inputs.py --scope3 || return 1
}

echo "=============================================================="
echo " Tier 2/3 completion run - scope $SCOPE - $(date -u '+%Y-%m-%d %H:%M UTC')"
echo " budget: ${BUDGET_HOURS}h of this session (0 = unlimited)"
echo "=============================================================="

rc=0
case "$SCOPE" in
  1) run_dir 1 "$PKG/jobs/scope1" || rc=$? ;;
  2) prepare_relaxed; run_dir 2 "$PKG/jobs/scope2" || rc=$? ;;
  3) generate_scope3; run_dir 3 "$PKG/jobs/scope3" || rc=$? ;;
  4) run_dir 4 "$PKG/jobs/scope4" || rc=$? ;;
  all)
     run_dir 1 "$PKG/jobs/scope1" || rc=$?
     [ $rc -eq 0 ] && { prepare_relaxed; run_dir 2 "$PKG/jobs/scope2" || rc=$?; }
     [ $rc -eq 0 ] && { run_dir 4 "$PKG/jobs/scope4" || rc=$?; }
     [ $rc -eq 0 ] && { generate_scope3 && run_dir 3 "$PKG/jobs/scope3" || rc=$?; }
     ;;
esac

echo "--------------------------------------------------------------"
echo " scope $SCOPE finished: $JOB_OK passed, $JOB_FAIL failed, $JOB_SKIP skipped"
echo " session wall clock: $((SESSION_SECONDS/3600))h $(( (SESSION_SECONDS%3600)/60 ))m"
echo " manifest: results/manifest_scope$SCOPE.csv"
echo " next: python3 tools/audit_tier2.py results"
[ $rc -eq 9 ] && echo " (stopped early by budget or STOP file - rerun the same command to continue)"
echo "--------------------------------------------------------------"
