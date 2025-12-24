from sklearn.feature_extraction.text import CountVectorizer

def extract_bow_features(texts, max_features=5000):
    vectorizer = CountVectorizer(
        analyzer="char",
        ngram_range=(2, 4),
        max_features=max_features
    )
    X = vectorizer.fit_transform(texts)
    return X, vectorizer