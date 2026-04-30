def generate_questions(summary):
    sentences = summary.split(".")
    questions = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:
            questions.append({
                "question": f"What does this mean: '{sentence}'?",
                "answer": sentence
            })

    return questions[:5]  