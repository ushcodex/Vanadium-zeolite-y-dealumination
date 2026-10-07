#!/usr/bin/env python3
"""
extract_source_figures.py

Crops named figures out of the source PDFs in writing/Sources/ so that they can
be reused in the thesis with a proper "Source: ..." credit.

Why the page is cropped rather than the embedded bitmap:
  several of the most useful diagrams (notably Xu, Liu and Madon 2002, Figure 8)
  are stored as VECTOR drawing commands, so page.get_images() misses them
  entirely.  Rendering a clip of the page captures both raster and vector art.

Every crop below was located by reading the page's object rectangles and
checking them against the caption text; the caption recorded next to each crop
is the verbatim caption from the source, so any figure can be traced back.

Run:  python3 tools/extract_source_figures.py
"""

import csv
import os

import pymupdf
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "writing", "Sources")
OUT = os.path.join(ROOT, "figures", "from_sources")
MANIFEST = os.path.join(OUT, "_manifest.csv")

DPI = 300
MAX_EDGE = 1700  # keep the compiled thesis a sane size


def trim_and_cap(path):
    """Cut the white margin off a rendered crop and cap its longest edge."""
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = Image.new("L", im.size)
    diff.putdata([0 if a == b else 255
                  for a, b in zip(im.getdata(), bg.getdata())])
    bbox = diff.getbbox()
    if bbox:
        pad = 8
        w, h = im.size
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        im = im.crop(bbox)
    if max(im.size) > MAX_EDGE:
        s = MAX_EDGE / max(im.size)
        im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))),
                       Image.LANCZOS)
    im.save(path, optimize=True)
    return im.size

# slug, pdf, page (1-based), clip rect (x0, y0, x1, y1) in PDF points,
# verbatim caption, credit line
JOBS = [
    ("xu2002_fig8_pathways",
     "Pathways for Y Zeolite Destruction The Role of Sodium and Vanadium.pdf",
     7, (275, 500, 537, 684),
     "FIG. 8. Pathways to Y zeolite destruction.",
     "Xu, Liu and Madon (2002), Figure 8"),

    ("xu2002_fig6_na_v",
     "Pathways for Y Zeolite Destruction The Role of Sodium and Vanadium.pdf",
     6, (276, 62, 537, 642),
     "FIG. 6. ZSA retention after thermal (1060 K, 4 h) and hydrothermal treatments "
     "(1060 K, 1 atm, 90% steam/10% air, 4 h). High Si-USY impregnated with ammonium "
     "metavanadate, sodium nitrate, and sodium metavanadate.",
     "Xu, Liu and Madon (2002), Figure 6"),

    ("xu2002_fig1_na_stability",
     "Pathways for Y Zeolite Destruction The Role of Sodium and Vanadium.pdf",
     3, (52, 70, 538, 432),
     "FIG. 1. (A) Stability of USY decreases with increasing Na+ content under "
     "hydrothermal conditions but not under thermal conditions. (B) Unit cell sizes "
     "of steamed USY versus Na2O loading.",
     "Xu, Liu and Madon (2002), Figure 1"),

    ("trujillo1997_fig3_viv",
     "Carlos A. Trujillo (1997). The Mechanism of Zeolite Y Destruction by Steam in the Presence of Vanadium..pdf",
     6, (100, 37, 453, 262),
     "FIG. 3. Percentage of vanadium IV on the total vanadium in the sample as a "
     "function of temperature of calcination for impregnated zeolites.",
     "Trujillo et al. (1997), Figure 3"),

    ("etim2016_fig1_y_zeolite",
     "Etim(2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite..pdf",
     4, (208, 66, 405, 262),
     "Fig. 1. Structure of Y-zeolite showing average micropore width in the supercage "
     "formed by 12-membered oxygen rings.",
     "Etim, Xu, Ullah and Yan (2016), Figure 1"),

    ("etim2016_fig8_tem",
     "Etim(2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite..pdf",
     18, (70, 152, 534, 408),
     "Fig. 8. TEM micrographs of zeolite samples (a) parent-USY; (b) 0.3 wt.% V-USY; "
     "(c) 0.5 wt.% V-USY; (d) 10 wt.% Y/MgO-0.3 wt.% V-USY; (e) 10 wt.% Y/MgO-0.5 wt.% V-USY.",
     "Etim, Xu, Ullah and Yan (2016), Figure 8"),

    ("etim2016_fig12_fau_model",
     "Etim(2015). Effect of vanadium contamination on the framework and micropore structure of ultra stable Y-zeolite..pdf",
     24, (165, 368, 455, 516),
     "Fig. 12. 3D atomistic model of faujasite structure zeolite (a) with full "
     "framework aluminum atoms (b) without framework aluminum atoms.",
     "Etim, Xu, Ullah and Yan (2016), Figure 12"),

    ("etim2018_fig6_phases",
     "j.apcata.2018.02.011.pdf", 23, (68, 95, 544, 533),
     "Fig. 6. Phases of compounds formed in the presence of a passivator.",
     "Etim, Bai, Ullah, Subhan and Yan (2018), Figure 6"),

    ("etim2018_fig7_passivation",
     "j.apcata.2018.02.011.pdf", 24, (68, 178, 544, 539),
     "Fig. 7. Comparison of passivation at different treatment conditions. 10 wt.% "
     "passivator in catalyst.",
     "Etim, Bai, Ullah, Subhan and Yan (2018), Figure 7"),

    ("etim2018_fig8_surface_area",
     "j.apcata.2018.02.011.pdf", 25, (68, 95, 436, 376),
     "Fig. 8. Effect of passivation on the surface areas of vanadium contaminated catalyst.",
     "Etim, Bai, Ullah, Subhan and Yan (2018), Figure 8"),

    ("tielens2010_fig2_v_sites",
     "Probing acid–base sites in vanadium redox zeolites by DFT calculation.pdf",
     2, (129, 449, 476, 723),
     "Fig. 2. Protonation of zeolite sites A and B leading to the reorganization of "
     "both sites. Both sites have a V in oxidation state +5.",
     "Tielens and Dzwigaj (2010), Figure 2"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for slug, pdf, page_no, clip, caption, credit in JOBS:
        path = os.path.join(SRC, pdf)
        if not os.path.exists(path):
            rows.append([slug, "MISSING PDF", pdf, page_no, "", caption, credit])
            continue
        doc = pymupdf.open(path)
        page = doc[page_no - 1]
        rect = pymupdf.Rect(*clip)
        # clamp to the page so a wrong guess cannot produce a blank file
        rect = rect & page.rect
        pix = page.get_pixmap(dpi=DPI, clip=rect)
        out = os.path.join(OUT, slug + ".png")
        pix.save(out)
        final = trim_and_cap(out)
        rows.append([slug, "OK", os.path.basename(pdf), page_no,
                     "%dx%d px" % final, caption, credit])
        doc.close()

    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["slug", "status", "source_pdf", "page", "size",
                    "verbatim_caption", "credit"])
        w.writerows(rows)
    for r in rows:
        print("%-30s %-6s %-9s %5s  %s" % (r[0], r[1], r[4], r[3], r[6]))


if __name__ == "__main__":
    main()
