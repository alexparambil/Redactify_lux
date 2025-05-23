 
import io
import pdfplumber
import time
from fpdf import FPDF
import os 
def extract_text(pdf_bytes: bytes):
    start_time = time.time()

    extracted_text = ""
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() or ""

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 3)

    return extracted_text, elapsed_time



def save_redacted_pdf(text: str, original_filename: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    lines = text.split("\n")
    for line in lines:
        pdf.multi_cell(0, 10, line)

    output_path = f"redacted_pdfs/redacted_{original_filename}.pdf"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)

    return output_path
