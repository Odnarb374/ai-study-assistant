from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(
    "mrm8488/t5-base-finetuned-question-generation-ap"
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "mrm8488/t5-base-finetuned-question-generation-ap"
)


def generate_question(chunk: str) -> str:
    """Generate an open-ended question from a passage."""
    # Format expected by this fine-tuned model
    input_text = f"answer: context: {chunk}"
    input_ids = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).input_ids

    outputs = model.generate(
        input_ids,
        max_new_tokens=64,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def generate_answer(chunk: str, question: str) -> str:
    """Answer a question using the passage as context."""
    prompt = (
        f"Answer based only on the passage.\n\n"
        f"Passage: {chunk}\n\n"
        f"Question: {question}\n\n"
        f"Answer:"
    )
    input_ids = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).input_ids

    outputs = model.generate(
        input_ids,
        max_new_tokens=60,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def generate_questions(chunks: list[str]) -> list[dict]:
    """Return a list of {question, answer} dicts for each chunk."""
    qa_pairs = []

    for chunk in chunks:
        question = generate_question(chunk)
        answer = generate_answer(chunk, question)

        print(f"Q: {question}")
        print(f"A: {answer}\n")

        qa_pairs.append({"question": question, "answer": answer})

    return qa_pairs