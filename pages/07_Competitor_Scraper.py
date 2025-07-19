import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🔎 Competitor Price Scraper")

url = st.text_input("Enter a product page URL (competitor):")

if url and st.button("Fetch Price"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(response.text, "html.parser")

        price_tags = soup.find_all(string=lambda t: "$" in t or "€" in t or "£" in t)
        if price_tags:
            st.write("Detected price-like strings:")
            for p in price_tags:
                st.markdown(f"- `{p.strip()}`")
        else:
            st.warning("No price-like strings detected.")
    except Exception as e:
        st.error(f"Error fetching or parsing the page: {e}")
