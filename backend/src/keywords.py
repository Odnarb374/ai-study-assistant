from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk

# Download required NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def extract_keywords(chunks):
    """
    Extract keywords from text chunks using NLTK.
    
    Args:
        chunks: List of text strings
        
    Returns:
        List of keywords sorted by frequency
    """
    # Combine all chunks
    text = " ".join(chunks)
    
    # Tokenize and convert to lowercase
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [
        token for token in tokens 
        if token.isalpha() and token not in stop_words
    ]
    
    # Calculate frequency distribution
    freq_dist = FreqDist(filtered_tokens)
    
    # Return top 10 keywords
    keywords = [word for word, freq in freq_dist.most_common(10)]
    
    return keywords
