# Vanadium-zeolite-y-dealumination

> **A Comparative Density Functional Theory Study of Vanadic Acid and Steam
> Adsorption on the Brønsted Acid Site of Zeolite Y: Evidence for the Mechanism
> of Vanadium-Promoted Dealumination in Residue Fluid Catalytic Cracking**

**Author:** Ahmad Usman Shehu (U19CE1068)
**Affiliation:** Department of Chemical Engineering, Faculty of Engineering,
Ahmadu Bello University, Zaria, Kaduna State, Nigeria

**New here? Read `GUIDE.md` first.** It says which file to open in which program
and what to export. The thesis is `deliverables/thesis_ABU.docx`, built from the
chapters in `writing/thesis_src/`. Earlier drafts are in `writing/_superseded/`
and must not be submitted; the reason is in `writing/_superseded/README.md`.

---

## Overview

This repository contains the computational chemistry calculations, structural
models, analysis scripts and thesis chapters for a study of the elementary
mechanism by which zeolite Y (faujasite) is destroyed in a residue fluid
catalytic cracking regenerator. The study compares the adsorption of volatile
vanadic acid (H3VO4) on the zeolite Bronsted acid site against the adsorption of
steam (H2O) on the same site, using semi-empirical (GFN2-xTB) and
dispersion-corrected hybrid density functional theory (DFT).

The principal finding is that vanadic acid binds to the acid site more strongly
than water by about 14.5 kJ/mol, a margin that two density functionals reproduce
to within 0.25 kJ/mol. The extraction of framework aluminium was not established
at the density functional level and is reported as such.

---

## Repository layout

```
deliverables/          the thesis document
figures/               original figures, plus figures taken from the literature
writing/thesis_src/    the chapters the thesis is built from
writing/Sources/       source PDFs, their extracted text, images and captions
writing/_superseded/   earlier drafts: do not submit
simulation/            the calculations
GUIDE.md               which file to open in which program
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

## Reproducing the results

```bash
python3 simulation/analysis/parse_orca.py     # read every ORCA log into a register
python3 simulation/analysis/build_tables.py   # rebuild the result tables
python3 figures/make_figures.py               # redraw the original figures
python3 build_thesis_abu.py                   # rebuild the thesis document
```

Every number in the thesis traces back to a log file named in
`simulation/analysis/RESULTS.md`.

## Citation

This work forms part of a B.Eng. research project submitted to the Department of
Chemical Engineering, Ahmadu Bello University, Zaria. Please reference the
repository and the author when citing the models or the dataset.
