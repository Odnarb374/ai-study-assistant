from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# Initialize summarization pipeline
model_name="facebook/bart-large-cnn"
    
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize(chunks):
    summaries = []

    for chunk in chunks:
        inputs = tokenizer(
            chunk,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=80,
            min_length=20,
            num_beams=4
        )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        summaries.append(summary)

    return " ".join(summaries)