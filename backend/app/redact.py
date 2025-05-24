import re
import spacy
from typing import List, Tuple

# Load the SpaCy model once
nlp = spacy.load("en_core_web_trf")  # Consider switching to `en_core_web_sm` for faster speed with reduced accuracy

# Stopwords for cleaning entities
STOPWORDS = set(nlp.Defaults.stop_words)

# Precompiled regex patterns
REGEX_PATTERNS = {
    "email": re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\b"),
    "phone": re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}\b"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "canada_zip": re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\b"),
    "us_zip": re.compile(r"\b\d{5}(?:-\d{4})?\b"),
    "invoice": re.compile(r"\bInvoice:\s*[\w\-]+\b"),
}

def ml_redact_entities(text: str) -> Tuple[str, List[str]]:
    doc = nlp(text)
    redacted_text = text
    offset = 0
    entities = []

    for ent in doc.ents:
        start, end = ent.start_char + offset, ent.end_char + offset
        original = redacted_text[start:end]
        redacted_text = redacted_text[:start] + "[######]" + redacted_text[end:]
        offset += len("[######]") - len(original)
        entities.append(ent.text)

    return redacted_text, entities

def regex_redact(text: str) -> Tuple[str, List[str]]:
    matches = []
    redacted_text = text
    for name, pattern in REGEX_PATTERNS.items():
        for match in pattern.finditer(redacted_text):
            matches.append(match.group())
            redacted_text = redacted_text.replace(match.group(), "[######]")
    return redacted_text, matches

def hybrid_redact(text: str) -> Tuple[str, List[str]]:
    ml_redacted_text, ml_entities = ml_redact_entities(text)
    fully_redacted_text, regex_entities = regex_redact(ml_redacted_text)

    combined_entities = ml_entities + regex_entities

    # Split into words and remove stopwords + pure numbers
    clean_entities = {
        word for entity in combined_entities
        for word in entity.split()
        if word.lower() not in STOPWORDS and not word.isdigit()
    }

    return fully_redacted_text, list(clean_entities)
