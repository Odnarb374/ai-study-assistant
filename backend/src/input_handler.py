import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text("text")

    return text


def load_text(file_path, text):
    if file_path != None:
        if file_path.endswith(".pdf"):
            return extract_text_from_pdf(file_path)
    else:
        return text
    
