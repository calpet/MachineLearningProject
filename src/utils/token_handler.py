import nltk

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    return " ".join([token.lower() for token in tokens])

def tokenize(text):
    return nltk.word_tokenize(text)