from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils import extract_text
from app.classify import classify_text
from app.redact import hybrid_redact
from fastapi.responses import StreamingResponse
from app.utils import save_redacted_pdf_with_layout
import os
import io
app = FastAPI()

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
        "characters_extracted": len(text),
        "elapsed_time_sec": elapsed
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
        "characters_extracted": len(text),
        "elapsed_time_sec": elapsed
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
