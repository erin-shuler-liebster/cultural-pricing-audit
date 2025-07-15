from bs4 import BeautifulSoup
import requests
from typing import Dict
import re

def extract_visual_pricing_elements(url: str) -> Dict[str, str]:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.content, "html.parser")

    # 1. Price color (red often used for urgency/discounts)
    price_tags = soup.find_all(string=re.compile(r"\$\d+|\d+€"))
    prices = {tag.parent.name: tag.parent for tag in price_tags if tag.parent}

    color_signals = []
    strikethroughs = 0
    for tag in prices.values():
        style = tag.get("style", "")
        if "red" in style:
            color_signals.append("red")
        if "line-through" in style:
            strikethroughs += 1

    # 2. Offer types
    html = soup.get_text().lower()
    offer_signals = {
        "coupon": "coupon" in html,
        "two_for_one": "2 for 1" in html or "two for one" in html,
        "free_shipping": "free shipping" in html,
        "limited_offer": "limited time" in html or "only today" in html,
    }

    result = {
        "Price Colors Used": ", ".join(set(color_signals)) or "None",
        "Strikethrough Prices": str(strikethroughs),
    }
    for offer, present in offer_signals.items():
        result[offer.replace("_", " ").title()] = "Detected" if present else "Not found"

    return result
