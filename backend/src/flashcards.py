from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(
    "google/flan-t5-base"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-base"
)

def generate_flashcards(keywords,sentences):
    flashcards = []


    for keyword in keywords:
        # find the keyword, and get surrounding sentences
        context = ""
        for i, s in enumerate(sentences):
            if keyword.lower() in s.lower():
                context = " ".join(sentences[max(0,i-1):i+2])
                break
        input_text = f"""
Create a definition for this keyword based on the context

Keyword: {keyword}
Context: {context}

Definition: 
"""
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(
            input_ids,
            max_new_tokens=100,
            num_beams=5,
            early_stopping=True
        )
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        flashcards.append([keyword,result])
    return flashcards