from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re

tokenizer = AutoTokenizer.from_pretrained(
    "google/flan-t5-base"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-base"
)

def generate_flashcards(keywords,sentences):
    flashcards = []


    for keyword in keywords:

        # Find sentence containing keyword
        context = ""

        for i, s in enumerate(sentences):

            # whole-word matching
            if re.search(rf"\b{re.escape(keyword)}\b", s, re.IGNORECASE):

                # surrounding sentences
                context = " ".join(
                    sentences[max(0, i-1): min(len(sentences), i+2)]
                )
                break

        # fallback
        if not context:
            context = "No context available."

        prompt = f"""
You are creating study flashcards.

Using ONLY the context below:
- Write a short student-friendly definition
- Focus on the keyword
- Keep the answer concise
- Do not add outside information

Example 1
Keyword: Photosynthesis

Context:
Photosynthesis is the process plants use to convert sunlight into energy.

Definition:
The process plants use to convert sunlight into energy.

Example 3
Keyword: Mitochondria

Context:
Mitochondria are organelles that generate energy for the cell.

Definition:
Organelles that generate energy for the cell.


Now create a new flashcard definition.

Keyword: {keyword}

Context:
{context}

Definition:
"""

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            num_beams=4,
            temperature=0.7,
            repetition_penalty=1.5
        )

        definition = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        ).strip()

        flashcards.append([keyword, definition])

    return flashcards