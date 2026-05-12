from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

tokenizer = AutoTokenizer.from_pretrained(
    "google/flan-t5-base"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-base"
)


def generate_questions(chunks):
    questions = []


    for chunk in chunks:
        input_text = f"""
Read the passage and create one factual quiz question.

Passage:
{chunk}

Quiz Question: 
"""
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(
            input_ids,
            max_new_tokens=100,
            num_beams=5,
            early_stopping=True
        )
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(result)
        questions.append(result)

        input_text = f"""
Read the passage and answer the quiz question.

Passage:
{chunk}

Quiz Question: 
{result}

Answer:
"""
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(
            input_ids,
            max_new_tokens=100,
            num_beams=5,
            early_stopping=True
        )
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(result)
        questions.append(result)

    return questions