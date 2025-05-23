# scripts/prepare_dataset.py
import os
import json
from app.utils import extract_text
data = []

BASE_DIR = r"D:\Projects\Redactify_lux\training_data"
for category in os.listdir(BASE_DIR):
    category_path = os.path.join(BASE_DIR, category)
    for file in os.listdir(category_path):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(category_path, file)
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()
                text, _ = extract_text(pdf_bytes)
                data.append({"text": text, "label": category})


output_dir = r"D:\Projects\Redactify_lux\scripts"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "classifier_dataset.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
