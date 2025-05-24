import os
import io
import base64
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils import extract_text
from app.classify import classify_text
from app.redact import hybrid_redact
from fastapi.responses import StreamingResponse
from app.utils import save_redacted_pdf_with_layout
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    extracted_text, elapsed_time = extract_text(contents)

    return JSONResponse(content={
        "filename": file.filename,
        "content_type": file.content_type,
        "characters_extracted": len(extracted_text),
        "elapsed_time_sec": elapsed_time,
        "extracted_data":extracted_text
    })


@app.post("/classify/")
async def classify_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text, elapsed = extract_text(content)
    label = classify_text(text)
    return {
        "filename": file.filename,
        "category": label,
    }



@app.post("/redact/")
async def redact_pdf(file: UploadFile = File(...), output_format: str = "text"):
    content = await file.read()
    text, elapsed = extract_text(content)
    redacted_text, entities = hybrid_redact(text)

    if output_format == "pdf":
        from app.utils import save_redacted_pdf_with_layout
        pdf_path = save_redacted_pdf_with_layout(content, entities, file.filename)
        pdf_file = open(pdf_path, "rb")
        return StreamingResponse(pdf_file, media_type="application/pdf", headers={
            "Content-Disposition": f"attachment; filename=redacted_{file.filename}"
        })

    # For text or both, return JSON
    result = {
        "filename": file.filename,
        "redacted_entities": entities,
    }
    if output_format in ["text", "both"]:
        result["redacted_text"] = redacted_text
    if output_format == "both":
        from app.utils import save_redacted_pdf_with_layout
        pdf_path = save_redacted_pdf_with_layout(content, entities, file.filename)
        pdf_file = open(pdf_path, "rb")
        return StreamingResponse(pdf_file, media_type="application/pdf", headers={
            "Content-Disposition": f"attachment; filename=redacted_{file.filename}"
        })
    return result

@app.post("/process/")
async def process_pdf(file: UploadFile = File(...), output_format: str = "text"):
    content = await file.read()
    text, elapsed = extract_text(content)
    label = classify_text(text)
    redacted_text, entities = hybrid_redact(text)

    result = {
        "filename": file.filename,
        "classification": label,
        "redacted_entities": entities,
        "characters_extracted": len(text),
        "elapsed_time_sec": elapsed,
        "extracted_text": text,
    }

    result["redacted_text"] = redacted_text

    # Save and encode redacted PDF
    pdf_path = save_redacted_pdf_with_layout(content, entities, file.filename)
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
        result["redacted_pdf_base64"] = base64.b64encode(pdf_bytes).decode("utf-8")

    # Optional: return original file as base64 (for original download)
    result["original_pdf_base64"] = base64.b64encode(content).decode("utf-8")

    return JSONResponse(content=result)
