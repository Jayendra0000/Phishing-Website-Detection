import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "login", "verify", "update", "secure",
    "account", "bank", "confirm", "signin"
]

def extract_url_features(url: str):
    features = []

    # 1. URL length
    features.append(len(url))

    # 2. Has IP address
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    features.append(1 if re.search(ip_pattern, url) else 0)

    # 3. Count of dots
    features.append(url.count("."))

    # 4. Count of hyphens
    features.append(url.count("-"))

    # 5. Count of '@'
    features.append(url.count("@"))

    # 6. HTTPS usage
    features.append(1 if url.startswith("https") else 0)

    # 7. Number of digits
    features.append(sum(char.isdigit() for char in url))

    # 8. Suspicious keywords
    features.append(
        sum(1 for word in SUSPICIOUS_WORDS if word in url.lower())
    )

    return features
