from sklearn.feature_extraction.text import TfidfVectorizer

def extract_tfidf_features(texts, max_features=5000):
    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 4),
        max_features=max_features
    )
    X = vectorizer.fit_transform(texts)
    return X, vectorizer