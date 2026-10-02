#!/bin/bash
# TIER 2 CLOUD BUS master queue. Run: nohup bash run_bus.sh > bus_status.log 2>&1 &
export PATH=/opt/orca:$PATH
mkdir -p ../results
echo "slot,functional,status,final_energy" > ../results/bus_manifest.csv
for f in jobs/*.inp; do
  n=$(basename "$f" .inp)
  echo "=== QUEUE $(date): $n ==="
  cp xyz/*.xyz . 2>/dev/null
  /opt/orca/orca "$f" > "results_tmp_$n.out" 2>&1
  if grep -q "ORCA TERMINATED NORMALLY" "results_tmp_$n.out"; then
    E=$(grep "FINAL SINGLE POINT ENERGY" "results_tmp_$n.out" | tail -1 | awk '{print $5}')
    slot=$(echo "$n" | sed 's/_[a-z0-9]*$//')
    func=$(echo "$n" | sed 's/.*_//')
    echo "$slot,$func,PASS,$E" >> ../results/bus_manifest.csv
    mv "results_tmp_$n.out" "../results/$n.out"
    echo "PASS $n E=$E"
  else
    echo "$n,,FAIL," >> ../results/bus_manifest.csv
    mv "results_tmp_$n.out" "../results/${n}_FAILED.out"
    echo "FAIL $n (see results/${n}_FAILED.out) - CONTINUING BUS"
  fi
done
echo "=== BUS COMPLETE $(date) ==="
