import streamlit as st

st.set_page_config(
    page_title="Gurgaon Property Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Gurgaon Property Price Predictor")

st.markdown("""
Predict residential property prices in Gurgaon using Machine Learning.

Use the sidebar to:

- 🔮 Predict Property Price
- 📊 Explore Analytics
""")

st.divider()

st.subheader("About the Project")

st.write("""
This project estimates property prices based on features such as
location, property type, area, bedrooms, bathrooms, furnishing status,
amenities and floor category.

The model has been trained on Gurgaon real estate data.
""")