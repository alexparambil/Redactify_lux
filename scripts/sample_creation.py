from fpdf import FPDF

def create_nda_pdf(disclosing_party, receiving_party, date, filename="NDA_Agreement.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "NON-DISCLOSURE AGREEMENT (NDA)", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {date}", ln=True)
    pdf.ln(5)
    
    pdf.multi_cell(0, 10,
        f"This Non-Disclosure Agreement (\"Agreement\") is entered into as of {date} by and between:\n\n"
        f"Disclosing Party:\n{disclosing_party}\n\n"
        f"Receiving Party:\n{receiving_party}\n\n"
        "1. Purpose\n"
        "The Disclosing Party possesses confidential and proprietary information related to the training, "
        "development, and deployment of a machine learning model (\"Confidential Information\"). "
        "The Receiving Party agrees to receive and use this Confidential Information solely for the purpose "
        "of assisting with the training of the model.\n\n"
        "2. Definition of Confidential Information\n"
        "Confidential Information includes, but is not limited to training data sets, model architectures, "
        "algorithms, source code, business and technical information.\n\n"
        "3. Obligations of Receiving Party\n"
        "The Receiving Party agrees to maintain confidentiality, use information only for the stated purpose, "
        "not disclose to third parties without consent, and prevent unauthorized use.\n\n"
        "4. Term\n"
        "This Agreement shall remain in effect for a period of 2 years from the date above.\n\n"
        "5. Return or Destruction of Materials\n"
        "Upon termination or request, Receiving Party shall return or destroy all confidential information.\n\n"
        "6. Governing Law\n"
        "This Agreement shall be governed by the laws of [Your State/Country].\n\n"
        "IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.\n\n"
        "Disclosing Party Signature: ________________________\n\n"
        "Receiving Party Signature: ________________________\n"
    )
    
    pdf.output(filename)
    print(f"NDA PDF generated and saved as {filename}")

# Example usage
disclosing = "John Doe\n123 Business Rd.\nCityville, State, 12345\njohn.doe@example.com"
receiving = "Jane Smith\n456 Partner St.\nTownsville, State, 67890\njane.smith@example.com"
date_signed = "2025-05-21"

create_nda_pdf(disclosing, receiving, date_signed)
