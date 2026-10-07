import os
import fitz  # PyMuPDF

sources_dir = r"c:\Users\PC\Documents\thesis\writing\Sources"
output_file = r"c:\Users\PC\Documents\thesis\writing\Sources\extracted_text.txt"

with open(output_file, "w", encoding="utf-8") as out_f:
    for filename in os.listdir(sources_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(sources_dir, filename)
            out_f.write(f"=== {filename} ===\n")
            try:
                doc = fitz.open(pdf_path)
                # Only extract first 5 pages to save space, but enough to get intro/claims
                for i, page in enumerate(doc):
                    if i > 5:
                        break
                    text = page.get_text()
                    # write out basic text, replacing newlines to compress
                    out_f.write(text.replace('\n', ' ') + "\n")
                doc.close()
            except Exception as e:
                out_f.write(f"Error reading {filename}: {e}\n")
            out_f.write("\n\n")

print("PDF text extraction complete.")
