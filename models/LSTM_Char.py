import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import csv
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, accuracy_score



MAX_CHARS = 200        # URL'ler kısa, yeterli
VOCAB_SIZE = 100       # karakter seti küçük
EMBED_DIM = 32
LSTM_UNITS = 64
BATCH_SIZE = 128
EPOCHS = 15


def load_csv(path):
    texts, labels = [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            texts.append(row[0])
            labels.append(int(row[1]))
    return texts, np.array(labels)


def run_lstm():
    print("[INFO] Loading train / test data...")

    X_train_texts, y_train = load_csv("data/processed/train.csv")
    X_test_texts, y_test = load_csv("data/processed/test.csv")

    print("[INFO] Character-level tokenization...")
    tokenizer = Tokenizer(char_level=True, lower=False)
    tokenizer.fit_on_texts(X_train_texts)

    X_train_seq = tokenizer.texts_to_sequences(X_train_texts)
    X_test_seq = tokenizer.texts_to_sequences(X_test_texts)

    X_train_pad = pad_sequences(X_train_seq, maxlen=MAX_CHARS)
    X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_CHARS)

    vocab_size = min(VOCAB_SIZE, len(tokenizer.word_index) + 1)

    print("[INFO] Building LSTM model...")
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=EMBED_DIM, input_length=MAX_CHARS),
        Dropout(0.3),
        LSTM(LSTM_UNITS),
        Dropout(0.3),
        Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    early_stop = EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    )

    print("[INFO] Training LSTM...")
    history = model.fit(
        X_train_pad, y_train,
        validation_split=0.15,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        callbacks=[early_stop],
        verbose=1
    )

    with open("data/processed/lstm_history.pkl", "wb") as f:
        pickle.dump(history.history, f)

    print("[SUCCESS] Training history saved to data/processed/lstm_history.pkl")

    print("[INFO] Evaluating model...")
    y_pred_prob = model.predict(X_test_pad)
    y_pred = (y_pred_prob > 0.5).astype(int)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    run_lstm()