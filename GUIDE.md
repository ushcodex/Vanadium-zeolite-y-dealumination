# Which file to open in which program, and what to export

This guide answers one question: if you have to hand something in, or show
something to a supervisor, which file do you open and in what program.

---

## 1. The thesis itself

| What you want to do | Open this file | In this program |
|---|---|---|
| Read or print the thesis | `deliverables/thesis_ABU.docx` | Microsoft Word |
| Edit the thesis formatting | `deliverables/thesis_ABU.docx` | Microsoft Word |
| Change the wording, then rebuild | `writing/thesis_src/*.md` | Notepad++ or VS Code, then rerun `build_thesis_abu.py` |

The Word file is already formatted to the department's rules: Times New Roman
12 point, double spaced body text, 1.5 inch binding margin, tables and references
at 11 point, references with hanging indents, page numbers centred in the footer.
Open it in Word, check the page numbers on the List of Tables and List of Figures
against the real ones, and it is ready.

If you want a PDF, open the Word file and use **File > Save As > PDF**. Do not
export from anywhere else, because the pagination will change.

---

## 2. The figures

There are two kinds of figure in the thesis and they are kept in separate places.

### Figures you made yourself

| File | Where it appears | Open with |
|---|---|---|
| `figures/fig3_1_cluster_models.png` | Figure 4.1, the three cluster models | Any image viewer |
| `figures/fig3_2_workflow.png` | Figure 3.1, the workflow diagram | Any image viewer |
| `figures/fig4_1_tier1_profile.png` | Figure 4.2, the semi-empirical profiles | Any image viewer |
| `figures/fig4_2_adsorption.png` | Figure 4.3, the adsorption comparison | Any image viewer |
| `figures/fig4_3_gibbs_temperature.png` | Figure 4.4, Gibbs energy against temperature | Any image viewer |
| `figures/fig4_4_tier2_ladder.png` | Figure 4.5, the density functional ladder | Any image viewer |

These are produced by `figures/make_figures.py`. If you change a number in the
thesis, change it in the data block at the top of that script and run:

```
cd Vanadium-zeolite-y-dealumination
python3 figures/make_figures.py
python3 build_thesis_abu.py
```

### Figures taken from published papers

`figures/lit/` holds the figures that are reproduced from the literature, with
the original caption in a matching `.txt` file:

| File | Source paper | Where it appears |
|---|---|---|
| `fig2_2_faujasite_supercage.png` | Etim et al. (2016), Fig. 1 | Figure 2.1 |
| `fig2_3_faujasite_atomistic.png` | Etim et al. (2016), Fig. 12 | Figure 2.2 |
| `fig2_4_malola_paths.png` | Malola et al. (2012), Fig. 2 | Figure 2.3 |
| `fig2_5_malola_steps.png` | Malola et al. (2012), Fig. 3 | Figure 2.4 |
| `fig2_7_vanadium_poisoning_scheme.png` | Adanenche et al. (2023), Fig. 9 | Figure 2.5 |
| `fig2_6_vanadium_mobility.png` | Etim et al. (2018), Fig. 3 | Figure 2.6 |
| `fig2_9_trujillo_scheme.png` | Trujillo et al. (1997), p. 14 | Figure 2.7 |
| `fig2_8_xu_hydrothermal_stability.png` | Xu et al. (2002), Fig. 4 | Figure 2.8 |

Each of these was cropped at 400 dpi straight out of the source PDF by
`figures/extract_lit_figures.py`, so the resolution is the same as the printed
paper. **These are copyrighted.** For a thesis they are used as quotations with
the source cited in the caption, which is normal academic practice. If the thesis
is ever published, written permission from the publisher will be needed for each
one.

---

## 3. The source papers

| What you want | Where it is |
|---|---|
| The original PDFs | `writing/Sources/*.pdf` |
| The full text of every PDF, page marked | `writing/Sources/text/<paper>.txt` |
| Every picture embedded in every PDF, extracted | `writing/Sources/images/<paper>/` |
| A list of what is in each PDF | `writing/Sources/index.json` |
| A list of every figure in every PDF, with its caption | `writing/Sources/captions.md` |

Open the `.txt` files in Notepad++ or VS Code. Open the `.pdf` files in Adobe
Acrobat Reader or any browser. The `captions.md` file is the one to read first if
you are looking for a figure: it lists every image in every source with the
caption that belongs to it, so you can find the one you want without opening the
PDFs.

The extraction scripts are `writing/Sources/extract_all.py` (text and images) and
`writing/Sources/caption_images.py` (captions). Both are rerunnable.

---

## 4. The calculations

| What you want | Where it is | Open with |
|---|---|---|
| All raw ORCA output files | `simulation/**/*.out` | Notepad++ or VS Code, or ORCA itself |
| The machine-readable summary of all 163 jobs | `simulation/analysis/orca_register.csv` | Excel or LibreOffice Calc |
| The result tables used in Chapter 4 | `simulation/analysis/RESULTS.md` | Any text editor |
| The scripts that produced those tables | `simulation/analysis/parse_orca.py`, `build_tables.py` | VS Code |

**Important:** the ORCA files from the laptop runs are UTF-16 encoded and the
cloud runs are UTF-8. If you open them in a program and see only spaces between
the letters, or if a search finds nothing, the encoding is wrong. In VS Code use
the encoding selector at the bottom right and switch to UTF-16 LE.

---

## 5. Molecular structures

| What you want | Where it is | Open with |
|---|---|---|
| The optimised geometry of any state | `simulation/03_tier2_completion/results/geom/*.xyz` | Avogadro, GaussView, or VMD |
| The Tier 1 geometries | `simulation/02_tier1/<state>/*_canonical.xyz` | Avogadro |
| The structures with bonds defined | `simulation/molfiles/` | Avogadro |

If you open an `.xyz` file in Avogadro, it will guess the bonds. For a
transition state the guess is often wrong, because a bond that is halfway broken
looks like no bond at all. Use **Build > Add Hydrogens** and then **Auto
Optimise** only for the minima.

### To make a picture of a structure for a slide

1. Open the `.xyz` in Avogadro.
2. Set **Display Type** to Ball and Stick.
3. Rotate to the orientation you want.
4. **File > Export > Graphics** and save as PNG at 300 dpi.
5. Do not use the ray traced renderer unless you have time, because it is slow on
   a laptop.

---

## 6. What was deleted, and why

The previous draft figures were deleted. The old plotting script
(`generate_plots.py`, also deleted) drew the non-converged and rejected states of
the density functional ladder on the same axes as the converged ones and labelled
the result a reaction profile, which is misleading. Its replacement,
`figures/fig4_4_tier2_ladder.png`, draws the converged states in colour and the
non-converged ones in grey and says so in the caption.

The old chapters are in `writing/_superseded/`. Do not submit them. The reasons
are set out in `writing/_superseded/README.md`.

---

## 7. Rebuilding everything from scratch

```
cd Vanadium-zeolite-y-dealumination

# 1. re-read the source papers
python3 writing/Sources/extract_all.py
python3 writing/Sources/caption_images.py

# 2. re-read the ORCA logs and rebuild the result tables
python3 simulation/analysis/parse_orca.py
python3 simulation/analysis/build_tables.py

# 3. redraw the figures and rebuild the document
python3 figures/extract_lit_figures.py
python3 figures/make_figures.py
python3 build_thesis_abu.py
```

Step 2 takes about a minute because it reads every ORCA log in the archive.
