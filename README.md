# Redactify_lux 
This is the Redactify_lux project. 
# Redactify_lux

Redactify_lux is an intelligent document automation tool designed to streamline the classification and redaction of sensitive information in digital documents. Leveraging machine learning and OCR technologies, this backend API enables secure processing of various document types, enhancing privacy compliance and operational efficiency.

## Features

- **Document Classification**: Automatically categorizes documents based on their content.
- **Automated Redaction**: Identifies and redacts sensitive information such as personal identifiers, financial data, and confidential text.
- **OCR Integration**: Extracts text from scanned PDFs and images for processing.
- **RESTful API**: Provides an easy-to-use API endpoint for uploading documents and receiving processed outputs.
- **Extensible Architecture**: Modular design allowing easy integration of additional document types and redaction rules.

## Tech Stack

- **Backend**: Python, FastAPI
- **Machine Learning**: Scikit-learn / Custom models for classification and redaction


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alexparambil/Redactify_lux.git
   cd Redactify_lux/backend
## Backend (FastAPI)
- cd backend
- pip install -r requirements.txt
- uvicorn app.main:app --reload

APIs
### 🔹 POST /classify/
- Upload a PDF
- Returns: classification label, character count, etc.

### 🔹 POST /redact/
- Upload a PDF + optional `output_format` query ("text", "pdf", or "both")
- Returns: redacted text and/or redacted PDF (as download)

### 🔹 POST /process/
- Upload a PDF
- Returns: classification label,redacted text and redacted PDF  character count, etc.
