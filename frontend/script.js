
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

    document.getElementById("flashcardsBox").innerText =
        "Q: What is AI?\nA: Artificial Intelligence";

});