import os
import pandas as pd

os.makedirs("results", exist_ok=True)

data = [
    {
        "Model": "Logistic Regression (BoW)",
        "Accuracy": 0.9964768883878241,
        "Precision_avg": 1.00,
        "Recall_avg": 1.00,
        "F1_avg": 1.00
    },
    {
        "Model": "Logistic Regression (TF-IDF)",
        "Accuracy": 0.9915445321307779,
        "Precision_avg": 0.99,
        "Recall_avg": 0.99,
        "F1_avg": 0.99
    },
    {
        "Model": "Linear SVM (BoW)",
        "Accuracy": 0.9968996617812852,
        "Precision_avg": 1.00,
        "Recall_avg": 1.00,
        "F1_avg": 1.00
    },
    {
        "Model": "Random Forest (Custom Features)",
        "Accuracy": 0.9634301014656145,
        "Precision_avg": 0.96,
        "Recall_avg": 0.96,
        "F1_avg": 0.96
    },
    {
        "Model": "LSTM (Char-based)",
        "Accuracy": 0.9959836527621195,
        "Precision_avg": 1.00,
        "Recall_avg": 1.00,
        "F1_avg": 1.00
    }
]

df = pd.DataFrame(data)

df.to_csv("results/model_comparison.csv", index=False)

print("\n=== Model Comparison Table ===\n")
print(df.to_string(index=False))
print("\n[SUCCESS] model_comparison.csv saved to results/")