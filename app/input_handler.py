import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text("text")

    return text


def load_text(input_data, is_file=True):
    if is_file:
        if input_data.endswith(".pdf"):
            return extract_text_from_pdf(input_data)
        elif input_data.endswith(".txt"):
            with open(input_data, "r", encoding="utf-8") as f:
                return f.read()
    else:
        return input_data