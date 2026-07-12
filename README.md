# Gurgaon Property Price Predictor

A deployed Streamlit machine-learning application that estimates residential property prices in Gurgaon, India. Enter a property's location and characteristics to receive an estimated price range in crores (₹).

The prediction is an indicative estimate based on historical real-estate listing data; it is not a property valuation or financial advice.

## Features

- Predicts prices for flats and houses in Gurgaon
- Uses sector, bedrooms, bathrooms, balconies, property age, built-up area, furnishing, facilities, and floor category
- Includes input validation for unrealistic area and bathroom/bedroom combinations
- Returns a price range in crores
- Runs through a simple, single-page Streamlit interface

## Application inputs

| Input | Description |
| --- | --- |
| Property type | Flat or house |
| Sector | Gurgaon locality/sector |
| Bedrooms and bathrooms | Number of bedrooms and bathrooms |
| Balconies and property age | Listing characteristics |
| Built-up area | Area in square feet |
| Servant room and store room | Availability of additional rooms |
| Furnishing type, facilities, floor category | Property configuration details |

## How it works

1. The app loads `df.pkl` to populate the available input choices.
2. It creates a one-row data set from the submitted property details.
3. `pipeline.pkl` preprocesses the features and uses the trained regression model to predict the log-transformed price.
4. The prediction is converted back to crores and displayed with a ±₹0.22 Cr estimate range.

## Project structure

```text
.
├── app.py                         # Streamlit application and prediction logic
├── df.pkl                         # Feature reference data for form options
├── pipeline.pkl                   # Trained preprocessing and regression pipeline
├── requirements.txt               # Pinned deployment dependencies
├── CSV Files/                     # Raw, cleaned, and modeling datasets
├── Notebooks/                     # Data cleaning, EDA, feature engineering, and modeling notebooks
└── output_report1.html            # Exploratory data analysis report
```

## Run locally

**Prerequisite:** Python 3.10 or later is recommended.

```bash
git clone https://github.com/kanikaprajapati725/House-Price-Prediction.git
cd House-Price-Prediction
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Data and modeling workflow

The notebooks document the full workflow:

1. Clean raw flat and house listings.
2. Merge the cleaned data into a Gurgaon property dataset.
3. Engineer features from listing details, possession status, rooms, furnishing, and amenities.
4. Perform exploratory analysis, treat outliers, and impute missing values.
5. Select features, compare models, and export the final artifacts used by the app.

The final modeling dataset is `CSV Files/Gurgaon_properties_post_feature_selection_3.csv` and contains:

```text
property_type, sector, price, bedRoom, bathroom, balcony, agePossession,
built_up_area, servant room, store room, furnishing_type, facilities,
floor_category
```

## Deployment notes

The repository includes the files required to deploy the app on Streamlit Community Cloud or a comparable Python hosting service:

- `app.py` is the application entry point.
- `requirements.txt` pins the runtime dependencies.
- `df.pkl` and `pipeline.pkl` must remain in the repository root because the app loads them at runtime.

## Tech stack

- Streamlit
- Pandas and NumPy
- scikit-learn
- XGBoost
- category-encoders

## Repository

[View the source code on GitHub](https://github.com/kanikaprajapati725/House-Price-Prediction)
