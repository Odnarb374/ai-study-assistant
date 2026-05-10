from transformers import pipeline

def summarize(chunks):
    """
    Summarize text chunks using a transformer model.
    
    Args:
        chunks: List of text strings
        
    Returns:
        String containing the summary
    """
    # Combine all chunks
    text = " ".join(chunks)
    
    # Limit text length for the model (max ~1024 tokens for most summarization models)
    # Approximate: 1 token ≈ 4 characters
    max_chars = 4096
    if len(text) > max_chars:
        text = text[:max_chars]
    
    # Initialize summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Generate summary
    summary_result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    summary = summary_result[0]['summary_text']
    
    return summary
