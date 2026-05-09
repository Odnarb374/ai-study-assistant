
import re
import fitz

#extracts raw text from a pdf file using pymupdf.
def extract_text_from_pdf(file_path):
    text = ""

    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"

    return text


#cleans raw text
def clean_text(text):
    if text is None:
        return ""

    #remove page number lines
    text = re.sub(r"(?im)^\s*page\s+\d+(\s+of\s+\d+)?\s*$", "", text)
    text = re.sub(r"(?m)^\s*\d+\s*$", "", text)

    #remove extra spaces and too many blank lines
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    #fix spacing before punctuation
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    return text.strip()


#splits text into smaller chunks
def split_text_into_chunks(text, max_words=150):

    text = clean_text(text)

    if not text:
        return []

    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        if current_word_count + word_count > max_words and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_word_count = 0

        current_chunk.append(sentence)
        current_word_count += word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

#loads text from either a file path or pasted text
def load_text(file_path=None, text=None):

    if file_path is not None:
        if file_path.endswith(".pdf"):
            return extract_text_from_pdf(file_path)

        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        else:
            raise ValueError("Unsupported file type. Please use a PDF, TXT, or pasted text.")

    if text is not None:
        return text

    return ""


#main function
def process_text(file_path=None, text=None, max_words=150):

    raw_text = load_text(file_path=file_path, text=text)
    cleaned_text = clean_text(raw_text)
    chunks = split_text_into_chunks(cleaned_text, max_words=max_words)

    return chunks


if __name__ == "__main__":
    sample_text = """
    Page 1

    Machine learning is a field of artificial intelligence. It allows computers to learn from data.
    Supervised learning uses labeled examples. Unsupervised learning finds patterns without labels.

    2

    Neural networks are often used in NLP. They can process text, images, and other data.
    """

    chunks = process_text(text=sample_text)

    for i, chunk in enumerate(chunks, 1):
        print(f"\nChunk {i}:")
        print(chunk)