class Document:
    def __init__(self, raw_text, chunks=None):
        self.raw_text = raw_text
        self.cleaned_text = None
        self.chunks = chunks or []
        self.ranked_chunks = []
        self.summary = None
        self.keywords = []
        self.questions = []
        self.flashcards = []