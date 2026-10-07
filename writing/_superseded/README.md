# Superseded drafts: do not cite or reuse

Everything in this folder is an earlier draft of the thesis, kept only so that the
history of the project is not lost. It must not be submitted, quoted, or used as a
source for anything.

## What is wrong with it

**The reference list is unreliable.** Several entries in
`markdown_drafts/references.md` and in `thesis_drafts/` were written from memory
rather than from the source documents. Some of them do not correspond to any
published work, and some attach real findings to the wrong authors, years or
journals. Every citation in those drafts must be treated as false until it is
checked against the original paper.

**Several claims are stronger than the evidence.** In particular:

- the drafts describe the work as having "validated the full mechanism" of
  vanadium dealumination by density functional theory. It did not. Three of the
  five states on the vanadium route did not converge at the density functional
  level, the first transition state was rejected with fourteen imaginary modes,
  and the extraction product was computed as strongly endothermic on the model.
  See Section 4.6 and Section 4.8.3 of the current thesis.

- the drafts describe the chemisorbed intermediate as a "deeply stabilised
  thermodynamic ratchet". The converged density functional value is 22.4 kJ/mol
  of stabilisation relative to the adsorption complex, which is a modest
  stabilisation rather than a deep trap.

- the drafts attribute the work to `U19CE1068` but state a submission date of
  November 2026 in one place and mislabel several tables and figures.

**The figures were plotted from partially unverified data.** The old
`generate_plots.py` script, now deleted, plotted the non-converged and rejected
states of the density functional ladder on the same axes as the converged ones
and labelled the result a reaction profile. The new `figures/fig4_4_tier2_ladder.png`
draws converged and non-converged states in different colours and states which is
which.

## What replaced it

- `writing/thesis_src/` contains the current chapters.
- `deliverables/thesis_ABU.docx` is the current document.
- `writing/Sources/` contains the source PDFs, their extracted text and their
  extracted figures.
- `simulation/analysis/orca_register.csv` and `RESULTS.md` contain the verified
  numbers.
