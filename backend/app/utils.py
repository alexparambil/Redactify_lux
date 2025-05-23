 
import io
import pdfplumber
import time
from fpdf import FPDF
import os 
import fitz  # PyMuPDF

def extract_text(pdf_bytes: bytes):
    start_time = time.time()

    extracted_text = ""
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            cleaned_text = clean_text(page_text)  # clean here
            extracted_text += cleaned_text

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 3)

    return extracted_text, elapsed_time


def clean_text(text: str) -> str:
    replacements = {
        '\u201c': '"',  # left double quote
        '\u201d': '"',  # right double quote
        '\u2018': "'",  # left single quote
        '\u2019': "'",  # right single quote
        '\u2014': '-',  # em dash
        '\u2013': '-',  # en dash
        '\u2026': '...', # ellipsis
        '\u00a0': ' ',  # non-breaking space
        '\u2010': '-',  # hyphen
        '\u2011': '-',  # non-breaking hyphen
        '\u2012': '-',  # figure dash
        '\u2015': '-',  # horizontal bar
        '\u2032': "'",  # prime (minutes, feet)
        '\u2033': '"',  # double prime (seconds, inches)
        '\u00b7': '*',  # middle dot
        '\u2022': '*',  # bullet
        '\u201a': ',',  # single low-9 quotation mark
        '\u201e': '"',  # double low-9 quotation mark
        '\uf080': '',   # example: remove private use char causing error
        # Add any other problematic chars here
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text




def save_redacted_pdf_with_layout(pdf_bytes: bytes, entities_to_redact: list[str], original_filename: str) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in doc:
        words = page.get_text("words")  # list of (x0, y0, x1, y1, "word", block_no, line_no, word_no)
        for w in words:
            x0, y0, x1, y1, word = w[:5]
            if any(entity in word for entity in entities_to_redact):
                rect = fitz.Rect(x0, y0, x1, y1)
                page.add_redact_annot(rect, fill=(0, 0, 0))  # red box

        page.apply_redactions()

    output_path = os.path.join("output", f"redacted_{original_filename}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    return output_path
