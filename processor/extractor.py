# processor/extractor.py
import fitz  # PyMuPDF

def extract_sections(pdf_paths):
    sections = []

    for path in pdf_paths:
        doc = fitz.open(path)
        for i, page in enumerate(doc):
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                for line in block.get("lines", []):
                    text = " ".join([span["text"] for span in line["spans"]]).strip()
                    if 5 < len(text) < 300:  # filter garbage
                        sections.append({
                            "document": path,
                            "page": i + 1,
                            "text": text,
                            "title": text.split(".")[0]  # crude title guess
                        })
    return sections
