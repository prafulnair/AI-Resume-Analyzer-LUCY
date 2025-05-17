import fitz

def extract_text_from_pdf(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()

    except Exception as e:
        print(f"[ERROR] Failed to parse {path}: {e}")
        return ""