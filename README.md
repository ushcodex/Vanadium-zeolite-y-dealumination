# Vanadium and Zeolite Y

> **Density Functional Theory Evaluation of Vanadic Acid Zeolite Y Dealumination in Residue Fluid Catalytic Cracking Regenerator**

**Author:** Ahmad Usman Shehu (U19CE1068)

**Department:** Chemical Engineering, Ahmadu Bello University, Zaria

## Start here

- **Thesis:** `deliverables/thesis_ABU.docx` (the compatibility copy is `deliverables/Ahmad_Usman_Shehu_U19CE1068_Thesis.docx`). Both are generated from the same source and contain the same document.
- **Editable thesis source:** `writing/markdown/00_prelims.md`, `writing/markdown/01_chapter1.md`–`05_chapter5.md`, `writing/markdown/06_references.md`, and `writing/markdown/07_appendices.md`.
- **Build and formatting guide:** `GUIDE.md`.

## Study summary

The project compared vanadic acid and water adsorption at a local model of a Zeolite Y Brønsted acid site. B3LYP-D3(BJ)/def2-TZVP gave electronic adsorption energies of −93.01 kJ mol⁻¹ for vanadic acid and −78.32 kJ mol⁻¹ for water; the PBE0 single-point comparison gave a similar relative preference. Harmonic Gibbs energies favoured water at 298.15 K and 1003.15 K. A conditional single-site estimate using reported regenerator partial pressures gave a water-to-vanadic-acid occupation ratio of about 5.7 × 10⁷ to 5.7 × 10⁸.

GFN2-xTB produced a screening-level candidate for the first Al–O cleavage step, with a barrier of 160.70 kJ mol⁻¹ above V-I1. Appendix A records the DFT frequency and water-path displacement assessments; Appendix B gives the numerical substitutions for the reported energies and site fractions.

## Repository layout

```
deliverables/          generated thesis documents
writing/markdown/      active chapter and front-matter sources
writing/Sources/       source papers and extracted text
figures/               figures used by the thesis
simulation/             ORCA inputs, outputs, geometries and audit registers
tools/                  document, figure and results builders
GUIDE.md                how to edit, build and check the thesis
```

## Rebuild the thesis

Install the document dependencies, then run:

```bash
python3 -m pip install python-docx Pillow
python3 build_thesis_abu.py
```

The script writes both thesis filenames in `deliverables/`. It applies A4 paper, Times New Roman 12 pt, double-spaced body text, 3.5 cm left and 2.5 cm remaining margins, left-aligned `x.0 TITLE` chapter headings, and unindented body paragraphs. The table of contents and figure/table lists use Word fields. In Microsoft Word, update all fields before printing by selecting the document with **Ctrl+A** and pressing **F9**.

The figure script requires `matplotlib` and `numpy`; it regenerates author-produced structure, workflow, and background illustrations from the ORCA geometries and project sources:

```bash
python3 -m pip install matplotlib numpy
python3 tools/make_figures.py
python3 build_thesis_abu.py
```

The ORCA output files and calculation registers are retained under `simulation/`; Appendix A summarises the selected job outcomes.
