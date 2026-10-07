#!/usr/bin/env python3
"""Pair every embedded raster image with the figure caption on the same page.

The image bounding boxes come from the PDF (page number + position). Figure
captions come from the text layer, collected per page. The two are matched on
page number and vertical order, which is enough to label the extracted files.
Scanned PDFs (no text layer) are reported as such.
"""
import json, os, re
import pymupdf

SRC = "/home/user/Vanadium-zeolite-y-dealumination/writing/Sources"
OUT_I = os.path.join(SRC, "images")

CAP = re.compile(r"^\s*(figs?\.?|figures?\.?|schemes?\.?|plates?\.?|tables?\.?)\s*\d+\s*[.:)]?", re.I)


def page_captions(doc):
    """Return {page_number: [caption, ...]} using the text layer."""
    out = {}
    for pno in range(1, doc.page_count + 1):
        blocks = doc[pno - 1].get_text("blocks")
        blocks.sort(key=lambda b: (round(b[1] / 4), b[0]))
        caps, buf = [], None
        for b in blocks:
            txt = " ".join(b[4].split())
            if not txt:
                continue
            if CAP.match(txt):
                if buf:
                    caps.append(buf)
                buf = txt
            elif buf is not None:
                if len(txt) < 300 and not txt.endswith("."):
                    buf += " " + txt
                else:
                    buf += " " + txt
                    caps.append(buf)
                    buf = None
        if buf:
            caps.append(buf)
        out[pno] = caps
    return out


report = []
for fn in sorted(os.listdir(SRC)):
    if not fn.lower().endswith(".pdf"):
        continue
    doc = pymupdf.open(os.path.join(SRC, fn))
    caps = page_captions(doc)
    idir = os.path.join(OUT_I, os.path.splitext(fn)[0].replace("(", "_").replace(")", "")
                        .replace(" ", "_").replace(".", "_")[:70])
    rows = []
    for pno in range(1, doc.page_count + 1):
        page = doc[pno - 1]
        try:
            infos = page.get_image_info(xrefs=True)
        except Exception:
            infos = []
        pr = page.rect
        # drop full-page scans and tiny icons
        imgs = []
        for inf in infos:
            x0, y0, x1, y1 = inf["bbox"]
            w, h = x1 - x0, y1 - y0
            if w < 0.75 * pr.width or h < 0.75 * pr.height:
                if w > 70 and h > 70:
                    imgs.append((round(y0), inf))
        imgs.sort(key=lambda t: t[0])
        pcaps = caps.get(pno, [])
        for k, (_, inf) in enumerate(imgs):
            cap = pcaps[k] if k < len(pcaps) else ""
            rows.append(dict(page=pno, xref=inf["xref"],
                             w=round(inf["bbox"][2] - inf["bbox"][0]),
                             h=round(inf["bbox"][3] - inf["bbox"][1]),
                             caption=cap))
    ntext = sum(len(v) for v in caps.values())
    report.append(dict(pdf=fn, textlayer_captions=ntext, images=rows))
    doc.close()

with open(os.path.join(SRC, "captions.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, indent=1)

md = ["# Figures embedded in the source PDFs (matched to captions)\n"]
for r in report:
    md.append("\n## %s   [%d captions found in text layer]" % (r["pdf"], r["textlayer_captions"]))
    for im in r["images"]:
        md.append("- p%02d xref%-5d %4dx%-4d :: %s" % (im["page"], im["xref"], im["w"], im["h"],
                                                       im["caption"][:250] or "(no caption on this page)"))
with open(os.path.join(SRC, "captions.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
print("wrote captions.md / captions.json")
