let flashcards = [];
let currentIndex = 0;
let showingAnswer = false;

// Button to submit files or text
document.getElementById("submitButton").addEventListener("click", async () => {

    // Get text
    const text = document.getElementById("textInput").value;

    // Get file
    const file = document.getElementById("fileInput").files[0];

    // Temporary fake outputs for testing frontend

    document.getElementById("summaryBox").innerText =
        "This is a sample summary.";

    document.getElementById("keywordsBox").innerText =
        "AI, Study, Learning, Notes";

    document.getElementById("questionsBox").innerText =
        "1. What is AI?\n2. What is machine learning?";

    // Fake backend data for now
    flashcards = [
        { q: "What is AI?", a: "Artificial Intelligence" },
        { q: "What is ML?", a: "Machine Learning" }
    ];

    currentIndex = 0;
    showingAnswer = false;

    showFlashcard();
});

function showFlashcard() {
    const card = document.getElementById("flashcard");

    if (flashcards.length === 0) {
        card.innerText = "No flashcards available";
        return;
    }

    const current = flashcards[currentIndex];

    card.innerText = showingAnswer ? current.a : current.q;
}

// Switch between questions and answers when clicked
document.getElementById("flashcard").addEventListener("click", () => {
    if (flashcards.length === 0) return;

    showingAnswer = !showingAnswer;
    showFlashcard();
});

// Next button
document.getElementById("nextCard").addEventListener("click", () => {
    if (flashcards.length === 0) return;

    currentIndex = (currentIndex + 1) % flashcards.length;
    showingAnswer = false;
    showFlashcard();
});

// Previous button
document.getElementById("prevCard").addEventListener("click", () => {
    if (flashcards.length === 0) return;

    currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;

    showingAnswer = false;
    showFlashcard();
});