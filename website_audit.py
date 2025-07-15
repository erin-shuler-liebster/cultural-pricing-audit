import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import re

def audit_website(url: str) -> Dict[str, str]:
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

def extract_persuasive_quotes(text: str) -> dict:
    patterns = {
        "power_distance": [r"\bexclusive\b", r"\bpremium\b", r"\btrusted by experts\b"],
        "individualism": [r"\bpersonalized\b", r"\bjust for you\b", r"\byour\b"],
        "uncertainty_avoidance": [r"\bguarantee\b", r"\bno risk\b", r"\bsecure checkout\b"],
        "masculinity": [r"\bwin\b", r"\bbest in class\b", r"\bbeat the competition\b"],
        "long_term_orientation": [r"\binvestment\b", r"\bfuture value\b", r"\bsustainability\b"],
        "indulgence": [r"\btreat yourself\b", r"\bdeserve\b", r"\bluxury\b"]
    }

    quote_matches = {}
    for dim, pats in patterns.items():
        matches = []
        for pat in pats:
            found = re.findall(pat, text, flags=re.IGNORECASE)
            if found:
                matches.extend(found)
        if matches:
            quote_matches[dim] = list(set(matches))  # deduplicate
    return quote_matches
