import re
import numpy as np

def extract_custom_features(urls):
    features = []

    for url in urls:
        length = len(url)
        digit_count = sum(c.isdigit() for c in url)
        special_count = sum(c in "-_./@" for c in url)
        has_https = 1 if url.startswith("https") else 0
        has_ip = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0

        features.append([
            length,
            digit_count,
            special_count,
            has_https,
            has_ip
        ])

    return np.array(features)