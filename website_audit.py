# ✅ FILE: website_audit.py
import requests
from bs4 import BeautifulSoup
from typing import Dict

def audit_website(url: str) -> Dict[str, str]:
    """
    Takes a URL and returns detected pricing communication signals.
    Attempts to map content to Hofstede's six cultural dimensions.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.content, "html.parser")
    texts = soup.stripped_strings
    all_text = " ".join(texts).lower()

    dimension_keywords = {
        "power_distance": ["premium", "vip", "executive", "recommended by experts", "status"],
        "individualism": ["personal", "tailored", "your", "customized", "individual"],
        "uncertainty_avoidance": ["guarantee", "clear terms", "secure", "fixed price", "detailed"],
        "masculinity": ["win", "beat competitors", "top performance", "achievement", "best in class"],
        "long_term_orientation": ["investment", "long term", "future value", "durability", "plan ahead"],
        "indulgence": ["treat yourself", "pleasure", "enjoy", "premium experience", "luxury"]
    }

    results = {}
    for dim, keywords in dimension_keywords.items():
        found = [kw for kw in keywords if kw in all_text]
        results[dim] = ", ".join(found) if found else "None detected"

    return results
