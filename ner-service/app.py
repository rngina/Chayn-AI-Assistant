from flask import Flask, request, jsonify
import spacy
import re

app = Flask(__name__)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Helper functions
def ner_pass(text):
    """
    Perform NER-based redaction for personal information (e.g., names, organizations).
    """
    doc = nlp(text)
    redacted_text = text
    entities = []

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]:  # Detect names, orgs, locations
            redacted_text = redacted_text.replace(ent.text, "[REDACTED]")
            entities.append({"entity": ent.text, "type": ent.label_})

    return redacted_text, entities

def regex_pass(text):
    """
    Perform regex-based redaction for email and phone numbers.
    """
    # Regex patterns
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_regex = r'\b\d{10,13}\b'

    # Detect emails and phone numbers
    emails = re.findall(email_regex, text)
    phones = re.findall(phone_regex, text)

    # Redact them
    redacted_text = text
    for email in emails:
        redacted_text = redacted_text.replace(email, "[REDACTED]")
    for phone in phones:
        redacted_text = redacted_text.replace(phone, "[REDACTED]")

    return redacted_text, emails, phones

@app.route("/ner", methods=["POST"])
def ner():
    """
    API endpoint for NER-based and regex-based redaction.
    """
    data = request.json
    text = data.get("text", "")

    # First pass: NER-based redaction (names, orgs, locations)
    ner_redacted_text, entities = ner_pass(text)

    # Second pass: Regex-based redaction (emails, phones)
    final_redacted_text, emails, phones = regex_pass(ner_redacted_text)

    response = {
        "original_text": text,
        "redacted_text": final_redacted_text,
        "entities": entities,
        "emails": emails,
        "phones": phones,
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
