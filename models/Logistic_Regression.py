import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from features.BoW_Features import extract_bow_features

def load_csv(path):
    texts = []
    labels = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            texts.append(row[0])
            labels.append(int(row[1]))
    return texts, labels


def run_logistic_regression():
    print("[INFO] Loading train / test data...")

    X_train_texts, y_train = load_csv("data/processed/train.csv")
    X_test_texts, y_test = load_csv("data/processed/test.csv")

    print("[INFO] Extracting BoW features...")
    X_train, vectorizer = extract_bow_features(X_train_texts)
    X_test = vectorizer.transform(X_test_texts)

    print("[INFO] Training Logistic Regression...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    print("[INFO] Evaluating model...")
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    run_logistic_regression()