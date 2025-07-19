import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🌍 Hofstede Global Map & Pricing Insights")

# Load Hofstede values (limited sample, expand as needed)
hofstede_data = pd.DataFrame([
    {"Country": "USA", "PDI": 40, "IDV": 91, "UAI": 46, "MAS": 62, "LTO": 26, "IVR": 68},
    {"Country": "France", "PDI": 68, "IDV": 71, "UAI": 86, "MAS": 43, "LTO": 63, "IVR": 48},
    {"Country": "Germany", "PDI": 35, "IDV": 67, "UAI": 65, "MAS": 66, "LTO": 83, "IVR": 40},
    {"Country": "Sweden", "PDI": 31, "IDV": 71, "UAI": 29, "MAS": 5, "LTO": 53, "IVR": 78},
])

# Visualization
fig = px.choropleth(
    hofstede_data,
    locations="Country",
    locationmode="country names",
    color="IDV",  # Default color by individualism
    hover_data=["PDI", "UAI", "MAS", "LTO", "IVR"],
    color_continuous_scale="Blues",
    title="Individualism Score by Country"
)

st.plotly_chart(fig)

selected = st.selectbox("🔍 Choose a country for full 6D insights", hofstede_data["Country"])

row = hofstede_data[hofstede_data["Country"] == selected].iloc[0]
st.markdown(f"""
### {selected} Cultural Profile:
- **Power Distance** (PDI): {row['PDI']}
- **Individualism** (IDV): {row['IDV']}
- **Uncertainty Avoidance** (UAI): {row['UAI']}
- **Masculinity** (MAS): {row['MAS']}
- **Long-Term Orientation** (LTO): {row['LTO']}
- **Indulgence** (IVR): {row['IVR']}

**Implication:** Tailor your pricing communication to align with high/low scores using the analyzer tool.
""")
