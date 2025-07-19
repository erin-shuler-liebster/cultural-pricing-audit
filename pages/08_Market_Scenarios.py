import streamlit as st
import pandas as pd
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator

st.title("Market Scenario Comparison")

url = st.text_input("Enter sales page URL to evaluate")
countries = st.multiselect("Select countries to compare", ["USA", "France", "Germany", "Sweden"])

translator = CulturalPricingTranslator()

if st.button("Run Market Analysis"):
    result = audit_website(url)
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Cultural Match Scores")
        rows = []
        for country in countries:
            feedback = translator.assess_alignment(result, country)
            match_score = sum("Strong" in v or "Good" in v for v in feedback.values())
            rows.append({"Country": country, "Matching Dimensions": match_score, "Total Possible": 6})
        df = pd.DataFrame(rows).set_index("Country")
        st.dataframe(df)
