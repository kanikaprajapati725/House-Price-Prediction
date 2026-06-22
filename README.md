# Gurgaon Property Price Predictor

This project predicts residential property prices in Gurgaon using cleaned real-estate listing data and a machine learning regression pipeline. It includes the full notebook workflow from raw flat/house datasets through cleaning, feature engineering, EDA, feature selection, model selection, final model export, and a Streamlit app for price prediction.

## Project Overview

The app estimates property prices in crores based on inputs such as:

- Property type: flat or house
- Sector/location
- Bedrooms, bathrooms, balconies
- Property age/possession status
- Built-up area
- Servant room and store room availability
- Furnishing type
- Facilities category
- Floor category

The deployed prediction flow uses:

- `df.pkl`: feature reference data used to populate Streamlit input options
- `pipeline.pkl`: trained preprocessing and regression pipeline
- `app.py`: Streamlit landing page
- `pages/1_price_prediction.py`: prediction form and inference logic
- `pages/2_analytics.py`: analytics page placeholder

## Repository Structure

```text
.
|-- app.py
|-- df.pkl
|-- pipeline.pkl
|-- output_report1.html
|-- CSV Files/
|   |-- appartments.csv
|   |-- flats - flats.csv
|   |-- houses.csv
|   |-- flats_cleaned.csv
|   |-- house_cleaned.csv
|   |-- Gurgaon_properties.csv
|   |-- Gurgaon_properties_cleaned.csv
|   |-- Gurgaon_properties_missing_value_imputation.csv
|   |-- Gurgaon_properties_outlier_treated.csv
|   `-- Gurgaon_properties_post_feature_selection_3.csv
|-- Notebooks/
|   |-- Flat_dataset_cleaning.ipynb
|   |-- House_dataset_cleaning.ipynb
|   |-- merge_houses_ans_flats.ipynb
|   |-- Feature-engineering.ipynb
|   |-- EDA _Pandas _Profilling.ipynb
|   |-- EDA _univariate _analysis.ipynb
|   |-- EDA_multivariate_analysis.ipynb
|   |-- outlier_detection.ipynb
|   |-- missing_value_imputation.ipynb
|   |-- feature_selection.ipynb
|   |-- Model_Selection.ipynb
|   `-- final_model.ipynb
`-- pages/
    |-- 1_price_prediction.py
    `-- 2_analytics.py
```

## Data Pipeline

The project follows this data preparation and modeling flow:

1. Raw data collection
   - `flats - flats.csv`
   - `houses.csv`
   - `appartments.csv`

2. Cleaning
   - `Flat_dataset_cleaning.ipynb` creates `flats_cleaned.csv`
   - `House_dataset_cleaning.ipynb` creates `house_cleaned.csv`

3. Merging
   - `merge_houses_ans_flats.ipynb` combines cleaned flats and houses into `Gurgaon_properties.csv`

4. Feature engineering
   - `Feature-engineering.ipynb` extracts structured features from fields such as `areaWithType`, `additionalRoom`, `agePossession`, `furnishDetails`, and `features`

5. Exploratory analysis
   - `EDA _Pandas _Profilling.ipynb` generates the profiling report saved as `output_report1.html`
   - `EDA _univariate _analysis.ipynb` studies individual columns such as property type, society, sector, price, price per square foot, bedrooms, and bathrooms
   - `EDA_multivariate_analysis.ipynb` studies relationships such as property type vs price, area, price per square foot, and correlation

6. Outlier treatment and missing value handling
   - `outlier_detection.ipynb` produces `Gurgaon_properties_outlier_treated.csv`
   - `missing_value_imputation.ipynb` produces `Gurgaon_properties_missing_value_imputation.csv`

7. Feature selection and model building
   - `feature_selection.ipynb` uses correlation analysis, Random Forest, Gradient Boosting, LASSO, and baseline modeling
   - `Model_Selection.ipynb` compares encoding strategies and tunes models
   - `final_model.ipynb` exports `df.pkl` and `pipeline.pkl`

## Modeling Details

The final prediction artifact is an sklearn `Pipeline` with:

- `ColumnTransformer` preprocessing
- `StandardScaler` for numeric features: `bedRoom`, `bathroom`, `built_up_area`
- `OrdinalEncoder` for categorical features such as property type, balcony, furnishing type, facilities, floor category, servant room, and store room
- `OneHotEncoder` for `agePossession`
- `category_encoders.TargetEncoder` for `sector`
- `xgboost.XGBRegressor` as the final regression model

The target price is predicted on a log scale in the app and converted back with `np.expm1`.

## Key Datasets

| File | Rows | Purpose |
| --- | ---: | --- |
| `CSV Files/flats - flats.csv` | 3026 | Raw flat listings |
| `CSV Files/houses.csv` | 1044 | Raw house listings |
| `CSV Files/flats_cleaned.csv` | 2801 | Cleaned flat data |
| `CSV Files/house_cleaned.csv` | 818 | Cleaned house data |
| `CSV Files/Gurgaon_properties.csv` | 3619 | Merged flat and house data |
| `CSV Files/Gurgaon_properties_cleaned.csv` | 3615 | Cleaned merged data |
| `CSV Files/Gurgaon_properties_missing_value_imputation.csv` | 3493 | Data after missing value imputation |
| `CSV Files/Gurgaon_properties_outlier_treated.csv` | 3494 | Data after outlier treatment |
| `CSV Files/Gurgaon_properties_post_feature_selection_3.csv` | 3492 | Final modeling dataset |

The final modeling dataset contains these columns:

```text
property_type, sector, price, bedRoom, bathroom, balcony, agePossession,
built_up_area, servant room, store room, furnishing_type, facilities,
floor_category
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the main dependencies:

```bash
pip install streamlit pandas numpy scikit-learn xgboost category-encoders
```

For running the notebooks, also install:

```bash
pip install jupyter matplotlib seaborn ydata-profiling
```

## Run the Streamlit App

From the project root, run:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Important Notes

- `pipeline.pkl` was created with scikit-learn `1.9.0`. Loading it with a different scikit-learn version can raise compatibility warnings or errors. For best results, use the same scikit-learn version used during export, or regenerate the model from `Notebooks/final_model.ipynb`.
- The app expects `df.pkl` and `pipeline.pkl` to be present in the project root.
- Price output is shown as an estimated range in crores.
- `pages/2_analytics.py` currently contains a placeholder analytics page.

## Future Improvements

- Add a `requirements.txt` or `environment.yml` with pinned package versions.
- Build out the Streamlit analytics page using the EDA outputs.
- Add model evaluation metrics and validation plots to the README.
- Add input examples and screenshots of the app.
- Re-export the model with a pinned, reproducible environment.
