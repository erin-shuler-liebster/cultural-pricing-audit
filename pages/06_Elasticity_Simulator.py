import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📉 Price Elasticity Simulator")

st.markdown("""
Simulate how a price change might affect demand based on cultural expectations.

- **Price-sensitive markets** (e.g. high UAI) show sharp drops in demand when price increases.
- **Luxury-seeking markets** (e.g. high PDI/IVR) may be less elastic.

Adjust assumptions to visualize outcomes.
""")

# Inputs
base_price = st.slider("Base Price (USD)", 10, 200, 50)
base_demand = st.slider("Expected Demand at Base Price", 100, 10000, 1000)
elasticity = st.slider("Price Elasticity Coefficient", -3.0, 0.0, -1.2)

prices = np.linspace(base_price * 0.5, base_price * 1.5, 50)
demands = base_demand * (prices / base_price) ** elasticity
revenues = prices * demands

# Plot
fig, ax = plt.subplots()
ax.plot(prices, demands, label="Demand", color="blue")
ax.plot(prices, revenues, label="Revenue", color="green")
ax.set_xlabel("Price")
ax.set_ylabel("Units / Revenue")
ax.legend()
st.pyplot(fig)

# Optional export
st.download_button("📥 Download Table", pd.DataFrame({
    "Price": prices,
    "Demand": demands,
    "Revenue": revenues
}).to_csv(index=False).encode("utf-8"), file_name="price_elasticity_sim.csv", mime="text/csv")
