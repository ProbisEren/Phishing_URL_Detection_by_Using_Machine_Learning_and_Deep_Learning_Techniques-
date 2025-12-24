import pickle
import matplotlib.pyplot as plt
import os

os.makedirs("figures/learning_curves", exist_ok=True)

with open("data/processed/lstm_history.pkl", "rb") as f:
    history = pickle.load(f)

epochs = range(1, len(history["loss"]) + 1)

# LOSS
plt.figure()
plt.plot(epochs, history["loss"], label="Training Loss")
plt.plot(epochs, history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("LSTM Learning Curve (Loss)")
plt.legend()
plt.savefig("figures/learning_curves/lstm_loss_curve.png", dpi=300)
plt.close()

# ACCURACY
plt.figure()
plt.plot(epochs, history["accuracy"], label="Training Accuracy")
plt.plot(epochs, history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("LSTM Learning Curve (Accuracy)")
plt.legend()
plt.savefig("figures/learning_curves/lstm_accuracy_curve.png", dpi=300)
plt.close()

print("[SUCCESS] Learning curve figures saved")