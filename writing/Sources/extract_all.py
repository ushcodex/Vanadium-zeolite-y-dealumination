#!/usr/bin/env python3
"""Extract full text + embedded images from every source PDF.

Writes:
  writing/Sources/text/<slug>.txt               - full text, page marked
  writing/Sources/images/<slug>/pNNN_xref.png   - embedded raster figures
  writing/Sources/index.json                    - metadata index
"""
import json, os, re
import pymupdf

SRC = "/home/user/Vanadium-zeolite-y-dealumination/writing/Sources"
OUT_T = os.path.join(SRC, "text")
OUT_I = os.path.join(SRC, "images")
os.makedirs(OUT_T, exist_ok=True)
os.makedirs(OUT_I, exist_ok=True)


def slugify(name):
    s = os.path.splitext(name)[0]
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    s = re.sub(r"_+", "_", s)
    return s[:70]


index = []
for fn in sorted(os.listdir(SRC)):
    if not fn.lower().endswith(".pdf"):
        continue
    slug = slugify(fn)
    doc = pymupdf.open(os.path.join(SRC, fn))
    parts = []
    for i, page in enumerate(doc):
        parts.append("\n<<<PAGE %d>>>\n" % (i + 1) + page.get_text("text"))
    text = "".join(parts)
    with open(os.path.join(OUT_T, slug + ".txt"), "w", encoding="utf-8") as f:
        f.write(text)

    idir = os.path.join(OUT_I, slug)
    os.makedirs(idir, exist_ok=True)
    n = 0
    for i, page in enumerate(doc):
        for info in page.get_images(full=True):
            xref = info[0]
            try:
                pix = pymupdf.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                w, h = pix.width, pix.height
                if w < 150 or h < 150:
                    continue
                pix.save(os.path.join(idir, "p%03d_%05d_%dx%d.png" % (i + 1, xref, w, h)))
                n += 1
            except Exception as e:
                print("img fail", fn, xref, e)
    meta = doc.metadata or {}
    index.append(dict(
        file=fn, slug=slug, pages=doc.page_count,
        title=(meta.get("title") or "").strip(),
        author=(meta.get("author") or "").strip(),
        subject=(meta.get("subject") or "").strip(),
        creationDate=(meta.get("creationDate") or "").strip(),
        text_chars=len(text), images=n,
        first_lines=[l.strip() for l in text.split("\n")[:8] if l.strip()][:4],
    ))
    doc.close()
    print("%-70s %7d chars %3d img %3d pages" % (fn[:70], len(text), n, index[-1]["pages"]))

with open(os.path.join(SRC, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, indent=1)
print("\nWROTE", os.path.join(SRC, "index.json"))
