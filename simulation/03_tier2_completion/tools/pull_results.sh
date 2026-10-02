#!/usr/bin/env bash
# ============================================================================
#  pull_results.sh - copy the completion results back from the cloud machine
# ============================================================================
#  usage:  bash tools/pull_results.sh user@IP [remote_dir] [--with-scratch]
#
#    remote_dir defaults to ~/03_tier2_completion
#
#  The first rsync brings back results/ : every .out, the per-scope manifests,
#  the wall-clock log, the final geometries (results/geom/) and the A4
#  displacement structures (results/diagnostics/).
#
#  --with-scratch additionally brings back jobs/ : the .gbw wavefunction files
#  (needed for the charge analysis in the thesis) and the .hess files (needed to
#  redo the thermochemistry at other temperatures without recomputing a Hessian).
#  Those files are large; pull them only if you want the charge analysis.
#
#  Nothing is deleted on either side.
# ============================================================================
set -eu

host="${1:-}"
[ -z "$host" ] && { sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
remote_dir="${2:-~/03_tier2_completion}"
with_scratch="${3:-}"

here="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$here/results"

echo "pulling results/ from $host:$remote_dir"
rsync -avz -e ssh "$host:$remote_dir/results/" "$here/results/"

if [ "$with_scratch" = "--with-scratch" ]; then
  echo "pulling jobs/ (wavefunctions and Hessians) from $host:$remote_dir"
  mkdir -p "$here/results/scratch_remote"
  rsync -avz --include '*/' --include '*.gbw' --include '*.hess' --include '*.zip' \
        --exclude '*' -e ssh "$host:$remote_dir/jobs/" "$here/results/scratch_remote/"
fi

echo
echo "done. now audit locally:"
echo "  python3 tools/audit_tier2.py results --table --cp --csv results/summary.csv"
