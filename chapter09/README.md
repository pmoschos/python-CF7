# 👩‍💻📊 Simple Machine Learning Projects 🧑‍💻📈

![Total Views](https://views.whatilearened.today/views/github/pmoschos/python-CF7.svg)![Python](https://img.shields.io/badge/language-Python-blue.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/pmoschos/python-CF7) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview 🌟

This repository contains advanced Python scripts that demonstrate various machine learning techniques for housing price prediction, classification, and digit recognition. These scripts serve as a practical resource for understanding data preprocessing, model training, evaluation, and visualization techniques.

---

## Repository Contents 📂

<table>
  <tr>
    <td>01. <a href="https://github.com/pmoschos/python-CF7/tree/main/chapter09/01.%20Simple%20Linear%20Regression" title="Linear regression with single feature for housing price prediction.">Housing Price Prediction (Single Feature)</a></td>
  </tr>
  <tr>
    <td>02. <a href="https://github.com/pmoschos/python-CF7/tree/main/chapter09/02.%20Multi%20Linear%20Regression" title="Linear regression with multiple features for housing price prediction.">Housing Price Prediction (Multiple Features)</a></td>
  </tr>
  <tr>
    <td>03. <a href="https://github.com/pmoschos/python-CF7/tree/main/chapter09/03.%20Multi%20Linear%20Regression%20extended" title="Linear regression with all features for housing price prediction.">Housing Price Prediction (All Features)</a></td>
  </tr>
  <tr>
    <td>04. <a href="https://github.com/pmoschos/python-CF7/tree/main/chapter09/04.%20Classification%20ClassifiedData" title="K-Nearest Neighbors classification with error rate analysis.">KNN Classification</a></td>
  </tr>
  <tr>
    <td>05. <a href="https://github.com/pmoschos/python-CF7/tree/main/chapter09/05.%20MNIST%20Dataset" title="Convolutional Neural Network for MNIST digit classification.">MNIST CNN Classification</a></td>
  </tr>
</table>


### 1. Housing Price Prediction with Single Feature (`housing.py`) 🏠
- **Objective:** Predict house prices based on the `Avg. Area Income`.
- **Techniques:** Linear regression with a single feature.
- **Visualization:** Pairplot, Correlation Heatmap, Actual vs Predicted Scatter Plot.
- **Key Features:**
  - Simple linear regression to predict house prices.
  - Model evaluation using MAE, MSE, RMSE, and R² metrics.
- **Outputs:**
  - Pairplot: `pairplot.png`
  - Correlation Heatmap: `correlation_heatmap.png`
  - Scatter Plot: `predictions_vs_actuals_income.png`

### 2. Housing Price Prediction with Multiple Features (`housing2.py`) 📈
- **Objective:** Predict house prices using `Avg. Area Income`, `Avg. Area House Age`, and `Avg. Area Number of Rooms`.
- **Techniques:** Linear regression with multiple features.
- **Visualization:** Scatter Plot for predicted vs actual values.
- **Key Features:**
  - Multivariate regression to enhance predictive accuracy.
  - Coefficients for each feature to interpret feature importance.
- **Outputs:**
  - Scatter Plot: `predictions_vs_actuals_selected_features.png`

### 3. Comprehensive Housing Price Prediction (`housing3.py`) 🏘️
- **Objective:** Use all relevant features (`Avg. Area Income`, `Avg. Area House Age`, `Avg. Area Number of Rooms`, `Avg. Area Number of Bedrooms`, and `Area Population`) for prediction.
- **Techniques:** Linear regression with complete feature set.
- **Visualization:** Scatter Plot for predicted vs actual values.
- **Key Features:**
  - A comprehensive model incorporating multiple factors affecting house prices.
  - Coefficient insights for all features.
- **Outputs:**
  - Scatter Plot: `predictions_vs_actuals.png`

### 4. K-Nearest Neighbors (KNN) Classification (`knn_classification.py`) 📊
- **Objective:** Classify data points using the KNN algorithm.
- **Dataset:** Classified Data (with a target column `TARGET CLASS`).
- **Techniques:** Data standardization, optimal `k` selection, and model evaluation.
- **Visualization:**
  - Error Rate vs K Value: `error_rate_vs_k.png`
  - Confusion Matrix: `confusion_matrix_k13.png`
  - Classification Report Heatmap: `classification_report_k13.png`
- **Key Features:**
  - Identify optimal `k` for accurate predictions.
  - Classification evaluation using confusion matrix and precision-recall metrics.

### 5. MNIST Digit Classification with CNN (`mnist_cnn.py`) 🔢
- **Objective:** Recognize handwritten digits (0-9) using a Convolutional Neural Network (CNN).
- **Techniques:** Data preprocessing, CNN architecture design, training, and evaluation.
- **Visualization:**
  - Correct Predictions: `mnist_plots/example_1.png`, `example_2.png`, etc.
  - Misclassified Examples: `mnist_plots/misclassified_1.png`, `misclassified_2.png`, etc.
- **Key Features:**
  - Efficient digit recognition using CNN.
  - Visualization of misclassified examples for model improvement.

---

## Educational Value 🎓
- **Beginner-Friendly:** Understand the fundamentals of machine learning and deep learning.
- **Advanced Insights:** Gain insights into feature engineering, model evaluation, and visualization techniques.

---

## Getting Started 🚀

### Prerequisites
- Python 3.x
- Required libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `keras`, `tensorflow`.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/pmoschos/python-CF6
   ```
2. Navigate to the folder:
   ```bash
   cd python-CF6
   ```
3. Run any script:
   ```bash
   python <script_name.py>
   ```

---

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>