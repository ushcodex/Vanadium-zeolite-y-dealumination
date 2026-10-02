#!/usr/bin/env bash
# ============================================================================
#  run_campaign.sh - Master runner for Tier 2/3 campaign (Stages A, B, C)
# ============================================================================
set -u

PKG="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PKG"

export ORCA="${ORCA:-/opt/orca/orca}"
mkdir -p "$PKG/results"

echo "=============================================================="
echo " Starting Tier 2/3 campaign on $(hostname) at $(date -u '+%Y-%m-%d %H:%M:%SZ')"
echo " ORCA: $ORCA"
echo "=============================================================="

# STAGE A: References & Clusters Opt+Freq (5 jobs)
echo ""
echo ">>> [Stage A.1] Scope 1: Frequency and Opt+Freq on reference molecules and clusters"
bash "$PKG/run_scope.sh" 1

# STAGE A: Counterpoise corrections (4 jobs)
echo ""
echo ">>> [Stage A.2] Scope 2: Counterpoise calculations on relaxed geometries"
bash "$PKG/run_scope.sh" 2

# STAGE A: PBE0 single points on initial relaxed geometries
echo ""
echo ">>> [Stage A.3] Scope 3: PBE0 single points on Stage A relaxed geometries"
bash "$PKG/run_scope.sh" 3

# STAGE B: The four key intermediates (minima)
echo ""
echo ">>> [Stage B] Scope 4 Minima: V-I1, V-I2, V-P, W-P"
ONLY='s4_0[1-4]*.inp' bash "$PKG/run_scope.sh" 4

# STAGE C: V-TS2 saddle refinement
echo ""
echo ">>> [Stage C] Scope 4 Transition State: V-TS2 OptTS + freq"
ONLY='s4_05*.inp' bash "$PKG/run_scope.sh" 4

# CLOSE OUT: PBE0 single points on newly relaxed geometries
echo ""
echo ">>> [Close Out] Scope 3: Updating PBE0 single points for new geometries"
bash "$PKG/run_scope.sh" 3

# Summary Audit
echo ""
echo ">>> [Audit] Generating Tier 2 summary and CSV table"
python3 "$PKG/tools/audit_tier2.py" "$PKG/results" --table --cp --csv "$PKG/results/summary.csv" || true

echo ""
echo "=============================================================="
echo " Campaign finished at $(date -u '+%Y-%m-%d %H:%M:%SZ')"
echo "=============================================================="
