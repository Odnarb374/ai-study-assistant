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
Create a short answer study question ONLY from the following passage.

Example 1
Passage:
Water boils at 100 degrees Celsius at sea level.

Question:
At what temperature does water boil at sea level?

Answer:
100 degrees Celsius

Example 2
Passage:
The mitochondria produces energy for the cell.

Question:
What is the function of the mitochondria?

Answer:
It produces energy for the cell.

Passage:
{chunk}

Question: 
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