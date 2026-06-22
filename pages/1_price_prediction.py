import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("🔮 Price Prediction")

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

# Property Type
property_type = st.selectbox(
    'Property Type',
    ['flat', 'house']
)

# Sector
sector = st.selectbox(
    'Sector',
    sorted(df['sector'].unique().tolist())
)

# Bedrooms
bedrooms = int(st.selectbox(
    'No. of Bedrooms',
    sorted(df['bedRoom'].unique().tolist())
))

# Bathrooms
bathroom = int(st.selectbox(
    'No. of Bathrooms',
    sorted(df['bathroom'].unique().tolist())
))

# Balcony
balcony = st.selectbox(
    'Balconies',
    sorted(df['balcony'].unique().tolist())
)

# Property Age
property_age = st.selectbox(
    'Property Age',
    sorted(df['agePossession'].unique().tolist())
)

# Built Up Area
built_up_area = st.number_input(
    'Built Up Area (sq ft)',
    min_value=0.0,
    value=1000.0
)

# Servant Room
servant_room = st.selectbox(
    'Servant Room',
    ['Yes', 'No']
)

# Store Room
store_room = st.selectbox(
    'Store Room',
    ['Yes', 'No']
)

# Furnishing Type
furnishing_type = st.selectbox(
    'Furnishing Type',
    sorted(df['furnishing_type'].unique().tolist())
)

# Facilities
facilities = st.selectbox(
    'Facilities',
    sorted(df['facilities'].unique().tolist())
)

# Floor Category
floor_category = st.selectbox(
    'Floor Category',
    sorted(df['floor_category'].unique().tolist())
)

if st.button('Predict'):

    # Validation 1
    if built_up_area < 300 or built_up_area > 12000:
        st.error("Please enter a realistic Built Up Area (100 - 12000 sq ft)")
        st.stop()

    # Validation 2
    if bathroom > bedrooms + 2:
        st.error("Number of bathrooms seems unrealistic")
        st.stop()

    # Validation 3
    if built_up_area < bedrooms * 150:
        st.error("Built Up Area is too small for the selected number of bedrooms")
        st.stop()

    data = [[
        property_type,
        sector,
        bedrooms,
        bathroom,
        balcony,
        property_age,
        built_up_area,
        servant_room,
        store_room,
        furnishing_type,
        facilities,
        floor_category
    ]]

    columns = [
        'property_type',
        'sector',
        'bedRoom',
        'bathroom',
        'balcony',
        'agePossession',
        'built_up_area',
        'servant room',
        'store room',
        'furnishing_type',
        'facilities',
        'floor_category'
    ]

    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]

    low = base_price - 0.22
    high = base_price + 0.22

    st.success(
        f"The price of the property is between ₹{low:.2f} Cr and ₹{high:.2f} Cr"
    )