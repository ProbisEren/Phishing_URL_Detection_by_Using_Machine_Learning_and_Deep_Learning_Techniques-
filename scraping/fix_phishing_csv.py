import json
import csv

INPUT_JSON = "data/raw/phishing_urls.json"
OUTPUT_CSV = "data/raw/phishing_urls.csv"

print("[DEBUG] Loading phishing JSON...")

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

print("[DEBUG] total phishing records:", len(data))

rows = []

for item in data:
    text = item.get("text", "").strip()
    if text:
        rows.append([text, 1])

print("[DEBUG] valid phishing URLs:", len(rows))

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(rows)

print("[SUCCESS] phishing_urls.csv saved")