import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.title("🕵️‍♀️ Competitor Price Checker")

st.markdown("Enter a product URL from a competitor to extract potential price.")

url = st.text_input("🔗 Competitor Product URL")
price_regex = r"\$\d+(?:\.\d{2})?"

if st.button("Scrape Price"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        matches = re.findall(price_regex, text)
        if matches:
            st.success(f"Found Prices: {', '.join(matches[:5])}")
        else:
            st.warning("No obvious price found. Try another page.")
    except Exception as e:
        st.error(f"Error: {e}")
