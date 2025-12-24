import os
from PIL import Image
import matplotlib.pyplot as plt

folder = "figures/learning_curves"

loss_path = os.path.join(folder, "lstm_loss_curve.png")
acc_path = os.path.join(folder, "lstm_accuracy_curve.png")

loss_img = Image.open(loss_path)
acc_img = Image.open(acc_path)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].imshow(loss_img)
axes[0].axis("off")
axes[0].set_title("LSTM Learning Curve (Loss)")

axes[1].imshow(acc_img)
axes[1].axis("off")
axes[1].set_title("LSTM Learning Curve (Accuracy)")

plt.tight_layout()
plt.show()