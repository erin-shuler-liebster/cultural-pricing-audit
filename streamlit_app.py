import streamlit as st
import pandas as pd
import datetime
from website_audit import audit_website, extract_persuasive_quotes
from cultural_pricing_algorithm import CulturalPricingTranslator

# ---- Page Configuration ----
st.set_page_config(
    page_title="Cultural Pricing Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Style ----
st.markdown("""
    <style>
        .main { background-color: #F7F9FA; }
        h1, h2, h3 { color: #003366; }
        .stButton>button { background-color: #006699; color: white; }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---- Cultural Profiles ----
cultural_profiles = {
    "USA": {"power_distance": 0.40, "individualism": 0.91, "uncertainty_avoidance": 0.46, "masculinity": 0.62, "long_term_orientation": 0.26, "indulgence": 0.68},
    "France": {"power_distance": 0.68, "individualism": 0.71, "uncertainty_avoidance": 0.86, "masculinity": 0.43, "long_term_orientation": 0.63, "indulgence": 0.48},
    "Germany": {"power_distance": 0.35, "individualism": 0.67, "uncertainty_avoidance": 0.65, "masculinity": 0.66, "long_term_orientation": 0.83, "indulgence": 0.40},
    "Sweden": {"power_distance": 0.31, "individualism": 0.71, "uncertainty_avoidance": 0.29, "masculinity": 0.05, "long_term_orientation": 0.53, "indulgence": 0.78}
}

translator = CulturalPricingTranslator(cultural_profiles)

# ---- Tabs ----
tabs = st.tabs(["Welcome", "Pricing Analyzer"])

# ---- Welcome Page ----
with tabs[0]:
    st.title("Welcome to the Cultural Pricing Communication Analyzer")
    st.markdown("""
    This tool helps you understand whether your pricing strategy communicates the **right signals** to **the right markets**.

    **Use Cases**
    - Market-entry preparation
    - Cultural adaptation for localization
    - Communication optimization
    - Conversion improvement

    👉 Head to the **Pricing Analyzer** tab to begin.
    """)

# ---- Analyzer Tab ----
with tabs[1]:
    st.title("Cultural Pricing Analyzer")
    url = st.text_input("Enter the URL of your pricing or product page")
    country = st.selectbox("Select your target market", list(cultural_profiles.keys()))

    if st.button("Run Analysis"):
        if not url:
            st.warning("Please enter a URL.")
        else:
            st.info("Auditing website content and comparing to cultural expectations...")
            tags = audit_website(url)

            if "error" in tags:
                st.error(f"Analysis failed: {tags['error']}")
            else:
                st.success("Website scanned and interpreted.")

                # Section 1
                st.header("1. What You're Communicating")
                for dim, signal in tags.items():
                    st.markdown(f"- **{dim.title()}**: {signal}")

                # Section 2
                st.header("2. What Your Audience Perceives")
                alignment = translator.assess_alignment(tags, country)
                for dim, feedback in alignment.items():
                    st.markdown(f"- **{dim.title()}**: {feedback}")

                # Section 3
                st.header("3. Likely Audience Reactions")
                perception = translator.explain_trace(country)
                for line in perception.values():
                    st.markdown(f"- {line}")

                # Section 4
                st.header("4. Cultural Adaptation Recommendations")
                improvements = translator.recommend_improvements(tags, country)
                if not improvements:
                    st.success("✔️ Your pricing communication is well-aligned!")
                else:
                    for dim, advice in improvements.items():
                        st.markdown(f"- **{dim.title()}**: {advice}")

                # Section 5
                st.header("5. Detected Persuasive Messaging")
                full_text = " ".join(tags.values())
                quotes = extract_persuasive_quotes(full_text)
                if not quotes:
                    st.info("No persuasive quotes detected.")
                else:
                    for dim, lines in quotes.items():
                        st.markdown(f"**{dim.title()}**: {', '.join(lines)}")

                # Download CSV
                st.subheader("📥 Download Your Cultural Pricing Report")
                df = pd.DataFrame({
                    "Cultural Dimension": list(tags.keys()),
                    "Website Signal": list(tags.values()),
                    "Perception Feedback": list(alignment.values()),
                    "Suggested Fix": [improvements.get(d, "Aligned") for d in tags.keys()],
                    "Detected Quotes": [", ".join(quotes.get(d, [])) for d in tags.keys()]
                })
                now = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download CSV Report",
                    data=csv,
                    file_name=f"cultural_pricing_{country}_{now}.csv",
                    mime="text/csv"
                )
