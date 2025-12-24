import json
import csv
import random

PHISHING_JSON = "data/raw/phishing_urls.json"
LEGIT_CSV = "data/raw/legit_urls.csv"
OUTPUT_CSV = "data/processed/final_dataset.csv"

PHISHING_LIMIT = 50000
LEGIT_LIMIT = 50000

print("[DEBUG] Loading phishing URLs...")
with open(PHISHING_JSON, "r", encoding="utf-8") as f:
    phishing_data = json.load(f)

phishing_samples = [
    [item["text"], 1]
    for item in phishing_data
    if item.get("text")
]

print("[DEBUG] total phishing available:", len(phishing_samples))

random.shuffle(phishing_samples)

phishing_samples = phishing_samples[:min(PHISHING_LIMIT, len(phishing_samples))]

print("[DEBUG] phishing selected:", len(phishing_samples))


print("[DEBUG] Loading legit URLs...")
legit_samples = []

with open(LEGIT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        legit_samples.append([row[0], 0])

print("[DEBUG] total legit available:", len(legit_samples))

random.shuffle(legit_samples)

legit_samples = legit_samples[:len(phishing_samples)]

print("[DEBUG] legit selected:", len(legit_samples))


dataset = phishing_samples + legit_samples
random.shuffle(dataset)

print("[DEBUG] total merged samples:", len(dataset))


with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(dataset)

print("[SUCCESS] final_dataset.csv created")