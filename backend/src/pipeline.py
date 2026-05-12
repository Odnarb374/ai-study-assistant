from input_handler import load_text
from summarizer import summarize
from keywords import extract_keywords
from question_generator import generate_questions
from flashcards import generate_flashcards
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def chunk_text(text, max_tokens=200):
    tokens = tokenizer.encode(text)
    
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i+max_tokens]
        chunks.append(tokenizer.decode(chunk))
    
    return chunks


def run_pipeline(file_path=None, text=None):
    
    # Load text
    loaded_text = load_text(file_path, text)
    
    # Chunk
    chunks = chunk_text(loaded_text)
 
    # Generate outputs
    summary = summarize(chunks)
    keywords = extract_keywords(chunks)
    questions = generate_questions(chunks)
    flashcards = generate_flashcards(keywords)
    
    # Return outputs
    return {
        "summary": summary,
        "keywords": keywords,
        "questions": questions,
        "flashcards": flashcards
    }