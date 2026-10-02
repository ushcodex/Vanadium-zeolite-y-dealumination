# Vanadium-zeolite-y-dealumination

> **A Density Functional Theory (DFT) Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in Residue Fluid Catalytic Cracking (RFCC) Units of Nigerian Refineries**

**Author:** Ahmad Usman Shehu  
**Affiliation:** Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, Kaduna State, Nigeria  

---

## Overview

This repository contains the computational chemistry calculations, structural models, analysis scripts, and dissertation chapters investigating the elementary mechanisms of Zeolite Y (faujasite) hydrothermal deactivation and dealumination under the influence of volatile vanadium species (vanadic acid, $\text{H}_3\text{VO}_4$) compared to a hydrothermal steam-only ($\text{H}_2\text{O}$) baseline.

The primary goal of this research is to resolve the atomistic pathway through which regenerator-borne vanadium accelerates framework breakdown, identifying transition states, activation barriers, and reaction energetics using semi-empirical (GFN2-xTB) and dispersion-corrected hybrid Density Functional Theory (DFT).

---

## Repository Structure

```
├── .gitignore               # Excludes archives and calculation temporary scratch files
├── README.md                # Project documentation and guide
├── figures/                 # Rendered figures, reaction profiles, and schematics
├── simulation/              # Quantum chemical calculation input decks, coordinates, and outputs
│   ├── 01_models/           # Zeolite Y cluster models and reference structures
│   ├── 02_tier1/            # Tier 1 stationary points, transition states (V-TS1, V-TS2, V-TS3, W-TS)
│   ├── analysis/            # Scripts for energy profiling and geometric property analysis
│   ├── audit/               # Saddle point validation and audit reports
│   ├── cloud_bus/           # Cloud calculation submission and transfer scripts
│   ├── cloud_opt/           # Optimization calculation configurations
│   ├── cloud_results/       # Completed optimization outputs
│   ├── local_results/       # Local workstation calculations
│   ├── molfiles/            # Curated molecular structures with explicit covalent connectivity
│   ├── orca_templates/      # Calculation input templates for ORCA
│   ├── xyz_seeds/           # Coordinate seeds for ORCA and xTB calculations
│   ├── README.txt           # Detailed file and protocol guide for simulations
│   └── verify_tier1.py      # Standard-library audit script for verifying ORCA outputs
└── writing/                 # Thesis documentation and writeups
    └── markdown/            # Markdown source chapters (Introduction, Literature Review, References)
```

---

## Key Reaction Pathways

1. **Vanadic Acid Attack Pathway:**
   - Adsorption complex ($\text{V-PRC}$) & Reactant state ($\text{V-R}$)
   - First $\text{Al}-\text{O}$ bond cleavage transition state ($\text{V-TS1}$) & intermediate ($\text{V-I1}$)
   - Second $\text{Al}-\text{O}$ bond cleavage transition state ($\text{V-TS2}$) & intermediate ($\text{V-I2}$)
   - Third $\text{Al}-\text{O}$ bond cleavage transition state ($\text{V-TS3}$) leading to framework dealuminated product ($\text{V-P}$)
2. **Steam Hydrolysis Baseline:**
   - Comparison with water-mediated hydrolytic bond cleavage ($\text{W-PRC} \rightarrow \text{W-TS} \rightarrow \text{W-P}$)

---

## Simulation Verification

To verify the convergence, imaginary frequency mode count, and electronic energies across all Tier 1 stationary points and transition state candidates, run:

```bash
python simulation/verify_tier1.py simulation/02_tier1
```

For supermolecular distance and fragment separation auditing:
```bash
python simulation/verify_tier1.py simulation/02_tier1 --dist
```

---

## Citation & License

This work forms part of a B.Eng. research project submitted to Ahmadu Bello University, Zaria. Please reference this repository and author when citing or utilizing the models and dataset.
