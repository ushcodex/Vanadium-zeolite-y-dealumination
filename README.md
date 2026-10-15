# Vanadium and Zeolite Y

> **Density Functional Theory Evaluation of Vanadic Acid Zeolite Y Dealumination in Residue Fluid Catalytic Cracking Regenerator**

**Author:** Ahmad Usman Shehu (U19CE1068)

**Department:** Chemical Engineering, Ahmadu Bello University, Zaria

## Start here

- **Thesis:** `deliverables/thesis_ABU.docx` (the compatibility copy is `deliverables/Ahmad_Usman_Shehu_U19CE1068_Thesis.docx`). Both are generated from the same source and contain the same document.
- **Editable thesis source:** `writing/markdown/00_prelims.md` and `writing/markdown/01_chapter1.md` through `06_references.md`.
- **Build and formatting guide:** `GUIDE.md`.

## Study summary

The project compared vanadic acid and water adsorption at a local model of a Zeolite Y Brønsted acid site. B3LYP-D3(BJ)/def2-TZVP gave electronic adsorption energies of −93.0 kJ mol⁻¹ for vanadic acid and −78.3 kJ mol⁻¹ for water. PBE0 single-point calculations gave −93.1 and −78.6 kJ mol⁻¹, respectively. These are uncorrected electronic energies; the harmonic gas-phase calculations did not support a reliable site-occupancy estimate at regenerator temperature.

The proposed density-functional transition state for framework Al–O cleavage had fourteen imaginary frequencies. The study therefore reports no validated activation barrier and does not claim to establish the full dealumination mechanism.

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

The ORCA output files and calculation registers are retained under `simulation/`. The thesis does not treat unconverged structures as validated results.
