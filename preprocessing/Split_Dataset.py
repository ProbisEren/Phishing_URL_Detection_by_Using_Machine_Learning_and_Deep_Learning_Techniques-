import csv
import random

INPUT_CSV = "data/processed/final_dataset.csv"
TRAIN_CSV = "data/processed/train.csv"
VAL_CSV = "data/processed/val.csv"
TEST_CSV = "data/processed/test.csv"

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

print("[DEBUG] Loading final dataset...")

with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

print("[DEBUG] total samples:", len(data))

random.shuffle(data)

n_total = len(data)
n_train = int(n_total * TRAIN_RATIO)
n_val = int(n_total * VAL_RATIO)

train_data = data[:n_train]
val_data = data[n_train:n_train + n_val]
test_data = data[n_train + n_val:]

print("[DEBUG] train size:", len(train_data))
print("[DEBUG] val size:", len(val_data))
print("[DEBUG] test size:", len(test_data))


def save_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        writer.writerows(rows)


save_csv(TRAIN_CSV, train_data)
save_csv(VAL_CSV, val_data)
save_csv(TEST_CSV, test_data)

print("[SUCCESS] train / val / test split completed")