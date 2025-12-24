import requests
import json

print("[DEBUG] PhishTank request starting...")

url = "http://data.phishtank.com/data/online-valid.json"

response = requests.get(url)

print("[DEBUG] status_code =", response.status_code)

data = response.json()

print("[DEBUG] total records:", len(data))

emails = []

for item in data:
    if "details" in item:
        emails.append({
            "text": item["url"],
            "label": 1
        })

print("[DEBUG] phishing samples collected:", len(emails))

with open("data/raw/phishing_urls.json", "w") as f:
    json.dump(emails, f, indent=2)

print("[SUCCESS] phishing_urls.json saved")