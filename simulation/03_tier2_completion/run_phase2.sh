#!/usr/bin/env bash
# ============================================================================
#  run_phase2.sh - Complete Counterpoise, Minima Frequencies & Skipped Saddles
# ============================================================================
set -u
PKG="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PKG"
export ORCA="${ORCA:-/opt/orca/orca}"
mkdir -p "$PKG/results" "$PKG/results/geom"

echo "=============================================================="
echo " Starting Tier 2 Completion Phase 2 on $(hostname) at $(date -u '+%Y-%m-%d %H:%M:%SZ')"
echo " ORCA: $ORCA"
echo "=============================================================="

# 1. COUNTERPOISE BSSE FALLBACK (4 jobs, ~15-20 min total)
echo ""
echo ">>> [Phase 2.1] Counterpoise fallback calculations (ghost atoms)"
for f in jobs/scope2_fallback/*.inp; do
    [ -f "$f" ] || continue
    job=$(basename "$f" .inp)
    echo "  RUN   $job  ->  results/$job.out   ($(date -u '+%Y-%m-%d %H:%M UTC'))"
    $ORCA "$f" > "results/$job.out" 2>&1
    if grep -q "ORCA TERMINATED NORMALLY" "results/$job.out"; then
        E=$(grep "FINAL SINGLE POINT ENERGY" "results/$job.out" | tail -1 | awk '{print $5}')
        echo "        PASS  E=$E"
    else
        echo "        FAIL  see results/$job.out"
    fi
done

# 2. MINIMA RESTART & FREQUENCIES (4 jobs, ~6-8 h total)
echo ""
echo ">>> [Phase 2.2] Minima completion with frequencies (cluster, v-i1, v-i2, v-p)"
for f in jobs/minima_completion/*.inp; do
    [ -f "$f" ] || continue
    job=$(basename "$f" .inp)
    echo "  RUN   $job  ->  results/$job.out   ($(date -u '+%Y-%m-%d %H:%M UTC'))"
    $ORCA "$f" > "results/$job.out" 2>&1
    if grep -q "ORCA TERMINATED NORMALLY" "results/$job.out"; then
        E=$(grep "FINAL SINGLE POINT ENERGY" "results/$job.out" | tail -1 | awk '{print $5}')
        echo "        PASS  E=$E"
        xyz="jobs/minima_completion/${job}.xyz"
        state=$(echo "$job" | sed -E 's/^s[0-9]+_[0-9]+_//; s/_optfreq$//; s/vi1/v-i1/; s/vi2/v-i2/; s/vp/v-p/')
        [ -f "$xyz" ] && cp "$xyz" "results/geom/${state}.xyz" 2>/dev/null || true
    else
        echo "        FAIL  see results/$job.out"
    fi
done

# 3. SKIPPED SADDLES (Stage D: w-ts, v-ts1, v-ts3)
echo ""
echo ">>> [Phase 2.3] Skipped Transition States (w-ts, v-ts1, v-ts3)"
for job in s4_07_wts_optts s4_08_vts1_optfreq s4_06_vts3_optts; do
    f="jobs/scope4/${job}.inp"
    if [ -f "$f" ]; then
        echo "  RUN   $job  ->  results/$job.out   ($(date -u '+%Y-%m-%d %H:%M UTC'))"
        $ORCA "$f" > "results/$job.out" 2>&1
        if grep -q "ORCA TERMINATED NORMALLY" "results/$job.out"; then
            E=$(grep "FINAL SINGLE POINT ENERGY" "results/$job.out" | tail -1 | awk '{print $5}')
            echo "        PASS  E=$E"
        else
            echo "        FAIL  see results/$job.out"
        fi
    fi
done

# 4. FINAL CLOSEOUT & AUDIT
echo ""
echo ">>> [Phase 2.4] Final Audit & Table Generation"
python3 tools/audit_tier2.py results --table --cp --csv results/summary.csv || python3 tools/audit_tier2.py results --table --csv results/summary.csv || true

echo ""
echo "=============================================================="
echo " Phase 2 finished at $(date -u '+%Y-%m-%d %H:%M:%SZ')"
echo "=============================================================="
