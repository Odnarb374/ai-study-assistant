def generate_flashcards(summary, terms):
    flashcards = []

    for term in terms:
        if term.lower() in summary.lower():
            flashcards.append({
                "term": term,
                "definition": f"Definition of {term} based on context."
            })

    return flashcards