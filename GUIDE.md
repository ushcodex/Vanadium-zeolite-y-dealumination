# Thesis build and editing guide

## 1. Main document and source files

| Task | File | Program |
|---|---|---|
| Read, edit, or print the thesis | `deliverables/thesis_ABU.docx` | Microsoft Word or LibreOffice Writer |
| Edit thesis wording | `00_prelims.md`, `01_chapter1.md`–`05_chapter5.md`, `06_references.md`, and `07_appendices.md` under `writing/markdown/` | VS Code or another text editor |
| Build the Word document | `build_thesis_abu.py` or `tools/build_thesis_docx.py` | Python 3 |
| Rebuild the author-produced figures | `tools/make_figures.py` | Python 3 with matplotlib and numpy |

`deliverables/Ahmad_Usman_Shehu_U19CE1068_Thesis.docx` is an identical compatibility copy of `deliverables/thesis_ABU.docx`. Edit the Markdown sources, not the generated Word files.

## 2. Build and update fields

Install the document dependencies and build the thesis:

```bash
python3 -m pip install python-docx Pillow
python3 build_thesis_abu.py
```

The builder applies A4 paper, Times New Roman 12 pt, double-spaced paragraphs, 3.5 cm left and 2.5 cm top, bottom, and right margins. Body paragraphs are justified and have no first-line indent. Chapter headings use the supervisor-requested, left-aligned `x.0 TITLE` format. The builder also creates a table of contents and lists of tables and figures with page-reference fields.

Before printing or exporting to PDF, update the Word fields: select the whole document with **Ctrl+A**, then press **F9**. This refreshes the table of contents, page numbers, and figure/table lists. Check the final pagination after updating fields.

If a figure changes, rebuild the figures before the document:

```bash
python3 -m pip install matplotlib numpy
python3 tools/make_figures.py
python3 build_thesis_abu.py
```

The figure script recreates the author-produced workflow, background, and molecular-structure illustrations. It reads the ORCA geometries under `simulation/03_tier2_completion/results/geom/`; the reported values remain traceable to the calculation logs and result registers under `simulation/`.

## 3. Chapters and structure

The active thesis source follows the five-chapter undergraduate project structure:

1. Introduction
2. Literature Review
3. Methodology
4. Results and Discussion
5. Conclusions and Recommendations

The references and appendices follow Chapter Five. Appendix A contains the calculation register, and Appendix B contains worked calculations.

Chapter-level headings are formatted as `1.0 INTRODUCTION`, `2.0 LITERATURE REVIEW`, and so on. Subheadings use decimal numbering. The Word builder applies left alignment to Heading 1, title case and bold to Heading 2, regular sentence case to Heading 3, and italic sentence case to Heading 4.

## 4. Figures and tables

Figure captions and table captions are written in the chapter Markdown using `[FIG: ...]` and `[TBL: ...]` directives. The builder uses these captions to create the document's lists and page references. Chapter Four presents geometries, adsorption energies, pathway assessment, harmonic Gibbs energies, and the competitive-site estimate in tables. Appendix A contains the calculation register; Appendix B contains worked numerical substitutions. The site-occupation result uses ideal-gas harmonic thermochemistry and a single-site model.

Figures generated from the ORCA coordinates are under `figures/`. Literature figures are under `figures/from_sources/`; their source is stated in each caption. Source papers and extracted text are under `writing/Sources/`.

## 5. Calculation records

The calculation inputs, output logs, geometries and registers are under `simulation/`. The ORCA logs provide the reported energies and vibrational frequencies. Appendix A summarises the selected job statuses and directs readers to the full calculation files.

For the calculation summary and formal site-occupation estimate, see `simulation/analysis/RESULTS.md` and `writing/markdown/_results_table.txt`. After changing calculation logs or registers, refresh the machine-readable results and the audit summary with:

```bash
python3 tools/build_results_table.py
python3 simulation/analysis/build_tables.py
```

To audit a Tier 1 result register, run:

```bash
python3 simulation/verify_tier1.py simulation/02_tier1
```
