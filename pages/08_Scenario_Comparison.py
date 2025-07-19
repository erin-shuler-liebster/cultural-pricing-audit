import streamlit as st
import pandas as pd

st.title("📊 Market Scenario Comparison")

st.markdown("""
Compare predicted success across multiple cultural markets.

Useful for:
- Go-to-market strategy
- Creative localization planning
- Risk forecasting
""")

# Example inputs (can be dynamically linked later)
scenarios = {
    "Product A - Premium Focus": {"PDI": "High", "IDV": "High", "UAI": "Low"},
    "Product B - Safe Budget Option": {"PDI": "Low", "IDV": "Medium", "UAI": "High"},
}

countries = {
    "USA": {"PDI": 40, "IDV": 91, "UAI": 46},
    "Germany": {"PDI": 35, "IDV": 67, "UAI": 65},
    "France": {"PDI": 68, "IDV": 71, "UAI": 86},
}

# Table comparison
data = []
for scenario, dims in scenarios.items():
    for country, scores in countries.items():
        match = 0
        for dim, val in dims.items():
            if (val == "High" and scores[dim] >= 60) or \
               (val == "Low" and scores[dim] <= 40) or \
               (val == "Medium" and 40 < scores[dim] < 60):
                match += 1
        data.append({"Scenario": scenario, "Country": country, "Dimension Match": match})

df = pd.DataFrame(data).sort_values(by="Dimension Match", ascending=False)
st.dataframe(df)
