
import streamlit as st
from website_audit import audit_website
from cultural_pricing_algorithm import CulturalPricingTranslator

# 🎯 Hofstede Profiles
profiles = {
    "USA": {
        "power_distance": 0.40, "individualism": 0.91, "uncertainty_avoidance": 0.46,
        "masculinity": 0.62, "long_term_orientation": 0.26, "indulgence": 0.68
    },
    "France": {
        "power_distance": 0.68, "individualism": 0.71, "uncertainty_avoidance": 0.86,
        "masculinity": 0.43, "long_term_orientation": 0.63, "indulgence": 0.48
    },
    "Germany": {
        "power_distance": 0.35, "individualism": 0.67, "uncertainty_avoidance": 0.65,
        "masculinity": 0.66, "long_term_orientation": 0.83, "indulgence": 0.40
    }
}

translator = CulturalPricingTranslator(profiles)

st.set_page_config(page_title="🌍 Cultural Pricing Advisor", layout="wide")
st.title("🌍 Cultural Pricing Communication Advisor")
st.markdown("Paste a sales page URL and select a target culture to receive communication feedback.")

url = st.text_input("🔗 Website URL")
country = st.selectbox("🌐 Target Market", list(profiles.keys()))

if st.button("Analyze Website"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        st.info(f"Auditing {url}...")
        tags = audit_website(url)
        if "error" in tags:
            st.error(tags["error"])
        else:
            st.subheader("🧠 Detected Website Signals")
            for k, v in tags.items():
                st.markdown(f"- **{k.title()}**: {v}")

            st.subheader(f"📊 Cultural Alignment for {country}")
            feedback = translator.assess_alignment(tags, country)
            for dim, result in feedback.items():
                st.markdown(f"- **{dim.title()}**: {result}")

            st.subheader("🔧 Recommendations")
            recs = translator.recommend_improvements(tags, country)
            for dim, rec in recs.items():
                st.markdown(f"- {dim.title()}: {rec}")
