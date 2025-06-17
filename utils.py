import fitz  # PyMuPDF
import json
import pandas as pd

def read_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    return ""

def export_flashcards(flashcards, format):
    if format == 'json':
        return json.dumps(flashcards, indent=2).encode('utf-8')
    elif format == 'csv':
        df = pd.DataFrame(flashcards)
        return df.to_csv(index=False).encode('utf-8')
    return b""

def export_anki(flashcards):
    output = ""
    for card in flashcards:
        output += f"{card['question']}\t{card['answer']}\n"
    return output.encode('utf-8')
