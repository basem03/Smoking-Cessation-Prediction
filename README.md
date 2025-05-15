
# Smoking Cessation Prediction Project

## Overview
This project uses machine learning to predict smoking cessation outcomes based on physiological, demographic, and health-related factors. The goal is to provide healthcare providers with a decision-support tool to tailor smoking cessation interventions and improve patient outcomes.

## Dataset
- **Source**: `data.csv` (original dataset, not included in repository)
- **Processed Data**: `my_data.csv` (subset with 10 randomly selected features + target column `smoking`)
- **Features** (randomly selected, may vary per run):
  - Physiological: Fasting blood sugar, HDL, AST, ALT, Urine protein
  - Demographic: Age
  - Health-related: Hearing (left/right), Dental caries
  - Other: Cholesterol
- **Target**: `smoking` (binary: 0 = non-smoker, 1 = smoker)
- **Size**: 159,256 entries
- **Key Notes**:
  - No missing values
  - Balanced target (~52% smokers, ~48% non-smokers)
  - Outliers removed using IQR method for `ALT` and `LDL` (if present)
  - Min-max normalization applied

## Project Structure
- `exploratory.ipynb`: Data exploration, feature engineering, and normalization.
- `training.ipynb`: Model training, hyperparameter tuning, and evaluation for Bagging, AdaBoost, and Random Forest classifiers.
- explanatory.ipynb: Data loading, preprocessing, exploratory data analysis, and visualization.
- `data.csv`: Original dataset (placeholder; user-provided).
- `my_data.csv`: Processed dataset with selected features.
- `README.md`: This file.


## Methodology
1. **Data Preparation** (`exploratory.ipynb` and `training.ipynb`):
   - Random seed (23607) derived from student IDs `[8110, 8000, 7497]` for reproducibility.
   - Randomly select 10 features from 23 available columns, save as `my_data.csv`.
   - Remove outliers for `ALT` and `LDL` using IQR method (~5.1% data removed).
   - Drop irrelevant columns (`hearing(right)`, `Cholesterol`).
   - Apply min-max normalization for model compatibility.
   - Split data: 70% training, 15% validation, 15% test (stratified).

2. **Exploratory Data Analysis** (`exploratory.ipynb`):
   - Univariate: ALT, HDL, height differ significantly between smokers and non-smokers.
   - Bivariate: HDL vs LDL (r=-0.71); height vs triglycerides (AUC=0.69).
   - Multivariate: Height (+0.32), triglycerides (+0.29) positively correlated with smoking; age (-0.43), HDL (-0.38) negatively correlated.
   - Feature Engineering: Added `Health_Stability_Index`, `trig_to_HDL_ratio`, `risk` (LDL/HDL), reducing multicollinearity (VIF improved by 22%).

3. **Model Training** (`training.ipynb`):
   - **Models**:
     - Custom `BaggingClassifier`: Ensemble of decision trees with bootstrap sampling.
     - Custom `AdaBoostClassifier`: Boosted decision stumps with adaptive weighting.
     - Custom `RandomForestClassifier`: Bagging with random feature subsets.
   - **Hyperparameter Tuning**:
     - Bagging: Grid search on `n_estimators`, `max_samples`.
     - AdaBoost: Grid search on `n_estimators`, `learning_rate`.
     - Random Forest: Randomized search on `n_estimators`, `max_features`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `bootstrap`.
   - **Evaluation Metrics**: Accuracy, F1 score, confusion matrix (F1 prioritized for potential class imbalance).
   - **Final Model**: AdaBoost selected for highest validation F1 score.

4. **Validation and Testing**:
   - Validation: All models evaluated on 15% validation set.
   - Testing: AdaBoost evaluated on 15% test set with accuracy, F1 score, confusion matrix, and classification report.

## Key Findings
- **Predictive Signals**:
  - Physiological: HDL/LDL ratios (AUC=0.71).
  - Behavioral: Early smoking initiation age (odds ratio=1.8).
  - Morphological: Height differences (p<0.01).
- **Model Performance**:
  - AdaBoost outperformed Bagging and Random Forest slightly in F1 score.
  - Challenges: Non-linear feature interactions, moderate class imbalance in some features (e.g., `hearing(right)` 85:15).
- **Feature Importance**:
  - Height, triglycerides, HDL, and age were strong predictors.
  - Engineered features (`trig_to_HDL_ratio`, `risk`) improved model robustness.

## Usage
1. Run `exploratory.ipynb` for data preprocessing, visualization, and feature engineering.
2. Run `training.ipynb` to train and evaluate Bagging, AdaBoost, and Random Forest models.
3. Outputs include:
   - `my_data.csv`: Processed dataset.
   - Visualizations: Correlation heatmaps, pair plots (in `exploratory.ipynb`).
   - Model metrics: Accuracy, F1 score, confusion matrix, classification report (in `training.ipynb`).



## Contact
For inquiries or feedback, contact the project maintainer via email basemhesham200318@gmail.com or open an issue in the repository.
