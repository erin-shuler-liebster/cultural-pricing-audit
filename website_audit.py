
import requests
from bs4 import BeautifulSoup

PRICING_TAGS = {
    'uncertainty_avoidance': {
        'high': ['guarantee', 'no risk', 'money back'],
        'low': ['fast checkout', 'easy payment']
    },
    'individualism': {
        'high': ['your choice', 'customize', 'tailor'],
        'low': ['our customers', 'group deal']
    },
    'power_distance': {
        'high': ['premium plan', 'expert endorsed', 'VIP'],
        'low': ['simple pricing', 'flat rate']
    },
    'masculinity': {
        'high': ['performance', 'win', 'dominate'],
        'low': ['care', 'help', 'connect']
    },
    'long_term_orientation': {
        'high': ['future value', 'invest', 'lifetime'],
        'low': ['today only', 'instant access']
    },
    'indulgence': {
        'high': ['fun', 'joy', 'treat yourself'],
        'low': ['rational', 'budget', 'smart']
    }
}

def audit_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()

        results = {}
        for dim, keywords in PRICING_TAGS.items():
            found = []
            for level, words in keywords.items():
                for word in words:
                    if word in text:
                        found.append((level, word))
            if found:
                levels = [lvl for lvl, _ in found]
                dominant = max(set(levels), key=levels.count)
                results[dim] = f"{dominant} ({', '.join(w for _, w in found)})"
            else:
                results[dim] = "Not detected"
        return results
    except Exception as e:
        return {"error": str(e)}
