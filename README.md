# 🔐 Redactify Lux — Smart Document Classification & Redaction

**Illuminate your privacy. Automate your compliance.**

Redactify Lux is an AI-powered document automation tool that classifies PDF documents and redacts sensitive information using a hybrid approach of machine learning and regex. Designed with modularity and privacy-first principles, it enables secure document processing for legal, financial, and enterprise workflows.

---

## ✨ Key Features

- 📄 **Document Classification** — Automatically detects type (e.g., NDA, Invoice, Shipping Order)  
- 🛡️ **Hybrid Redaction** — Redacts sensitive data using ML-based NER + regex  
- 🧠 **ML & OCR Powered** — Uses NLP and OCR to extract and understand content  
- 🔄 **Text & PDF Output** — Returns redacted data as plain text or downloadable PDF  
- ⚡ **Modern Frontend** — Drag & drop UI with real-time feedback and dual-view preview

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Scikit-learn, spaCy, PyMuPDF
- **Frontend**: React, Material UI (MUI)
- **PDF Redaction**: Layout-aware with PyMuPDF & FPDF
- **Classification**: Trained on real-world-like documents with high accuracy

---

## 🚀 Getting Started

### ✅ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### ✅ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 API Endpoints

### 🔹 `POST /classify/`
- Upload a PDF  
- Returns: Classification label, character count, etc.

### 🔹 `POST /redact/`
- Upload a PDF  
- Query param: `output_format=text|pdf|both`  
- Returns: Redacted text and/or redacted PDF

### 🔹 `POST /process/`
- Upload a PDF  
- Performs both classification & redaction  
- Returns: classification label, redacted text, redacted entities, and optional PDF download

---

## 💻 Sample `curl` Requests

```bash
curl -X POST "http://localhost:8000/classify/" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_docs/sample_invoice.pdf"

curl -X POST "http://localhost:8000/redact/?output_format=pdf" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_docs/sample_invoice.pdf" \
  --output redacted_output.pdf

curl -X POST "http://localhost:8000/process/?output_format=both" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_docs/sample_invoice.pdf"
```

---

## 📸 Demo UI Highlights

- 🔄 Drag & drop interface
- 📑 Extracted and redacted text shown side-by-side
- 📥 Download redacted PDF instantly
- 🎨 Responsive and modern React design

---

## 🙋‍♂️ About

Created as a demo-ready AI-powered tool to showcase intelligent document automation. Ideal for integration or pilot use in firms focused on compliance, legal tech, or enterprise automation.

> Redactify Lux is not here to replace your enterprise tools — it’s the agile sandbox to empower innovation teams, support lean client pilots, and seed future-ready IP.