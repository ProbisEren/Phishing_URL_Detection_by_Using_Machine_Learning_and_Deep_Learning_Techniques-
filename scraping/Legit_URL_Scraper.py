import csv
import json
import random

INPUT_FILE = "data/raw/tranco_top_sites.csv"
SAMPLE_SIZE = 50000

print("[DEBUG] Reading local Tranco CSV...")

domains = []

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2 and row[1] != "domain":
            domains.append(row[1].strip())

print("[DEBUG] total domains loaded:", len(domains))

random.shuffle(domains)
domains = domains[:SAMPLE_SIZE]

legit_urls = [
    {
        "text": f"https://{domain}",
        "label": 0
    }
    for domain in domains
]

print("[DEBUG] legit samples selected:", len(legit_urls))

with open("data/raw/legit_urls.json", "w") as f:
    json.dump(legit_urls, f, indent=2)

with open("data/raw/legit_urls.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    for item in legit_urls:
        writer.writerow([item["text"], item["label"]])

print("[SUCCESS] legit_urls.json & legit_urls.csv saved")