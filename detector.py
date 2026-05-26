import re
from urllib.parse import urlparse

suspicious_keywords = [
    "login", "verify", "update", "secure", "bank", "account", "free"
]

def analyze_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)

    # 1. HTTPS check
    if parsed.scheme != "https":
        score += 20
        reasons.append("No HTTPS used")

    # 2. IP address check
    if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
        score += 30
        reasons.append("URL uses IP address instead of domain")

    # 3. Keyword check
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            score += 15
            reasons.append(f"Suspicious keyword found: {keyword}")

    # 4. Long URL check
    if len(url) > 75:
        score += 10
        reasons.append("Unusually long URL")

    # 5. Special characters
    if "@" in url or "-" in url:
        score += 10
        reasons.append("Contains suspicious special characters")

    # Final risk level
    if score <= 30:
        level = "Safe"
    elif score <= 70:
        level = "Suspicious"
    else:
        level = "Dangerous"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }