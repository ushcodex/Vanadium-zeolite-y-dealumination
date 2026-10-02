#!/bin/bash
# Run FROM YOUR LAPTOP (Git Bash/WSL): bash pull_results.sh DROPLET_IP
rsync -avz -e ssh root@$1:~/cloud_bus/results/ ./bus_results/
echo "Pulled results into ./bus_results/"
