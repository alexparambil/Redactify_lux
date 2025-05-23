import re
from typing import List, Tuple
import spacy
# Sample regex patterns
REGEX_PATTERNS = {
    "email": r"\b[\w.-]+?@\w+?\.\w+?\b",
    "phone": r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
}



# Load a pre-trained spaCy English model
nlp = spacy.load("en_core_web_sm")

def ml_redact_entities(text: str):
    doc = nlp(text)  # Apply NLP pipeline to the text

    # Extract recognized named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    redacted_text = text
    for ent in doc.ents:
        # Replace each entity text with '[REDACTED]'
        redacted_text = redacted_text.replace(ent.text, "[REDACTED]")

    return redacted_text, [ent.text for ent in doc.ents]

def regex_redact(text: str) -> Tuple[str, List[str]]:
    redacted = text
    matches = []
    for label, pattern in REGEX_PATTERNS.items():
        found = re.findall(pattern, text)
        matches.extend(found)
        redacted = re.sub(pattern, "[REDACTED]", redacted)
    return redacted, matches

def hybrid_redact(text: str) -> Tuple[str, List[str]]:
    # Step 1: ML-based redaction
    ml_redacted_text, ml_entities = ml_redact_entities(text)

    # Step 2: Regex-based redaction on ML output
    fully_redacted_text, regex_entities = regex_redact(ml_redacted_text)

    all_entities = ml_entities + regex_entities
    return fully_redacted_text, all_entities
