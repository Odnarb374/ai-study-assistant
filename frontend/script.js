let flashcards = [];
let currentIndex = 0;
let showingAnswer = false;

// Button to submit files or text
document.getElementById("submitButton").addEventListener("click", async () => {

    // Get text
    const text = document.getElementById("textInput").value;

    // Get file
    const file = document.getElementById("fileInput").files[0];

    const formData = new FormData();
    if (file) {
        formData.append("file", file);
    }
    formData.append("text", text);

    try {
        const response = await fetch("http://localhost:3000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // Fill other sections
        document.getElementById("summaryBox").innerText = data.summary;
        document.getElementById("keywordsBox").innerText = data.keywords;
        document.getElementById("questionsBox").innerText = data.questions;

        // Convert tuple array -> object array
        flashcards = data.flashcards.map(([q, a]) => ({
            q,
            a
        }));

        currentIndex = 0;
        showingAnswer = false;

        showFlashcard();

    } catch (err) {
        console.error(err);
        alert("Backend error or server not running");
    }
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