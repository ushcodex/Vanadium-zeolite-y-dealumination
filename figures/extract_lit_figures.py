#!/usr/bin/env python3
"""Crop the figures cited in the thesis straight out of the source PDFs.

Rendering the page region (rather than saving the embedded bitmap) keeps the
vector text and line art sharp at 400 dpi, and lets the caption travel with the
figure so the attribution is never separated from the artwork.

Every entry below names the paper it comes from; the caption written to
figures/lit/<name>.txt is the caption that appears in the source, verbatim.
"""
import os, json
import pymupdf

SRC = "/home/user/Vanadium-zeolite-y-dealumination/writing/Sources"
OUT = "/home/user/Vanadium-zeolite-y-dealumination/figures/lit"
os.makedirs(OUT, exist_ok=True)
DPI = 400

# key: (output name, pdf file, page, xref of the embedded image,
#       caption as printed in the source, source line for the thesis)
FIG = [
    ("fig2_4_malola_paths",
     "anie.201104462.pdf", 2, 3,
     "Reaction paths for a) dealumination and b) desilication combined from five "
     "different NEB paths. Black lines: approach A, considering initially isolated "
     "water molecules; purple lines: approach B, considering initially adsorbed "
     "water molecules. Effective barriers for both approaches are labelled in the "
     "upper left corner.",
     "Malola, Svelle, Bleken and Swang (2012), Angewandte Chemie International "
     "Edition, 51, 652-655, Figure 2"),

    ("fig2_5_malola_steps",
     "anie.201104462.pdf", 2, 4,
     "Reaction steps with intermediate configurations shown for dealumination (left) "
     "and for desilication (right); c, covalent bonds; g, hydrogen bonds.",
     "Malola, Svelle, Bleken and Swang (2012), Angewandte Chemie International "
     "Edition, 51, 652-655, Figure 3"),

    ("fig2_2_faujasite_supercage",
     "Etim(2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite..pdf",
     4, 17,
     "Structure of Y-zeolite showing average micropore width in the supercage formed "
     "by 12-membered ring.",
     "Etim, Zhang, Ullah, Tao and Yan (2015), Journal of Colloid and Interface "
     "Science, 460, 139-149, Figure 1"),

    ("fig2_3_faujasite_atomistic",
     "Etim(2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite..pdf",
     24, 209,
     "3D atomistic model of faujasite structure zeolite: (a) with full framework "
     "aluminium atoms; (b) with partial framework aluminium atoms.",
     "Etim, Zhang, Ullah, Tao and Yan (2015), Journal of Colloid and Interface "
     "Science, 460, 139-149, Figure 12"),

    ("fig2_6_vanadium_mobility",
     "j.apcata.2018.02.011.pdf", 20, 438,
     "Effect of calcination temperature on the mobility of vanadium species.",
     "Etim, Xu, Zhang, Ullah, Hofmann, Yan and Ocone (2018), Applied Catalysis A: "
     "General, 556, 68-80, Figure 3"),

    ("fig2_7_vanadium_poisoning_scheme",
     "DAAEFinalReviewFUEL14December2022.pdf", 44, 195,
     "An illustration of the mechanisms of the vanadium poisoning of catalysts.",
     "Adanenche, Aliyu, Atta and El-Yakubu (2023), Fuel, 343, 127894, Figure 9"),

    ("fig2_8_xu_hydrothermal_stability",
     "Pathways for Y Zeolite Destruction The Role of Sodium and Vanadium.pdf", 5, 16,
     "Effect of vanadium on the hydrothermal stability of catalysts. Steaming "
     "conditions: 1060 K, 1 atm, 90% steam/10% air, 4 h.",
     "Xu, Bartholomew, Fahlstrom, Karanjikar and Woodruff (2002), Journal of "
     "Catalysis, 207, 237-246, Figure 4"),

    ("fig2_9_trujillo_scheme",
     "Carlos A. Trujillo (1997). The Mechanism of Zeolite Y Destruction by Steam in the Presence of Vanadium..pdf",
     14, 80,
     "Proposed scheme for the dealumination of zeolite Y by steam in the presence "
     "of vanadium.",
     "Trujillo, Uribe, Knops-Gerrits, Oviedo and Jacobs (1997), Journal of "
     "Catalysis, 168, 1-15, Scheme 1"),
]

CAP = ["# Figures taken from the source papers", ""]
for name, pdf, page, xref, caption, source in FIG:
    doc = pymupdf.open(os.path.join(SRC, pdf))
    pg = doc[page - 1]
    boxes = [i["bbox"] for i in pg.get_image_info(xrefs=True) if i.get("xref") == xref]
    if not boxes:
        print("MISSING", name, pdf, page, xref)
        doc.close()
        continue
    x0, y0, x1, y1 = boxes[0]
    # widen the crop so the caption and axis labels are included
    clip = pymupdf.Rect(max(0, x0 - 12), max(0, y0 - 10),
                        min(pg.rect.width, x1 + 12), min(pg.rect.height, y1 + 60))
    pix = pg.get_pixmap(dpi=DPI, clip=clip)
    out_png = os.path.join(OUT, name + ".png")
    pix.save(out_png)
    with open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8") as f:
        f.write(caption + "\n\nSOURCE: " + source + "\n")
    print("%-34s %5d x %-5d px  %s" % (name, pix.width, pix.height, source[:60]))
    doc.close()

print("\nwrote", len(FIG), "figure crops to", OUT)
