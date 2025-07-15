from bs4 import BeautifulSoup
import requests
import re

def analyze_ctas(url: str) -> list:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return [{"error": str(e)}]

    soup = BeautifulSoup(response.content, "html.parser")

    cta_buttons = soup.find_all("a") + soup.find_all("button")
    results = []

    for tag in cta_buttons:
        label = tag.text.strip().lower()
        style = tag.get("style", "").lower()
        color = "red" if "red" in style else ("blue" if "blue" in style else "neutral")

        tone = "action" if any(kw in label for kw in ["buy", "get", "shop", "now"]) else (
               "exploratory" if any(kw in label for kw in ["learn", "discover", "see"]) else "neutral")

        results.append({
            "Text": label,
            "Color": color,
            "Tone": tone,
            "HTML Tag": tag.name
        })

    return results
