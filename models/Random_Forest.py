import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from features.Custom_Features import extract_custom_features


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


def run_random_forest():
    print("[INFO] Loading train / test data...")

    X_train_texts, y_train = load_csv("data/processed/train.csv")
    X_test_texts, y_test = load_csv("data/processed/test.csv")

    print("[INFO] Extracting custom URL features...")
    X_train = extract_custom_features(X_train_texts)
    X_test = extract_custom_features(X_test_texts)

    print("[INFO] Training Random Forest...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    print("[INFO] Evaluating model...")
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    run_random_forest()