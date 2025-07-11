# USA Housing Price Prediction (Multi-Feature)

This project demonstrates a predictive analysis of housing prices using the `USA_Housing.csv` dataset. The script preprocesses the data, builds a linear regression model with multiple features, evaluates the model's performance, and saves the trained model for future predictions.

## Project Overview 📘

- **Dataset Used:** USA_Housing.csv
- **Objective:** Predict house prices based on features such as `Avg. Area Income`, `Avg. Area House Age`, and `Avg. Area Number of Rooms`.
- **Visualization:** Pairplot, Correlation Heatmap, and Actual vs. Predicted Scatter Plot.
- **Machine Learning Algorithm:** Linear Regression
- **Persistence:** Save and reload models using `joblib`.

### :computer: Script Highlights
```python
# Example code snippet:
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms']]
y = USAHousing['Price']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Training the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
```

## Key Features 🌟
- **Exploratory Data Analysis (EDA):** Visualizations to understand data relationships.
- **Model Training:** Build a linear regression model using three features.
- **Performance Metrics:** Evaluate the model using MAE, MSE, RMSE, and R².
- **Model Persistence:** Save the trained model and reuse it for predictions.

## Dependencies 🔧
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `joblib`

## Usage Example 📋

### Train the Model:
```bash
python predict_housing_prices_multifeature.py
```
### Predict New Prices:
```python
from joblib import load
loaded_model = load('linear_model_selected_features.joblib')
new_data = np.array([80000, 7, 7]).reshape(1, -1)
price_predicted = loaded_model.predict(new_data)
print(f"Predicted Price: ${price_predicted[0]:,.2f}")
```

## Outputs 📊
1. **Pairplot Visualization:** Shows relationships between features (Saved as `pairplot.png`).
![image](https://github.com/user-attachments/assets/8ea3baf3-4365-41b5-a6f2-d55cb3b09071)

2. **Correlation Heatmap:** Displays feature correlations (Saved as `correlation_heatmap.png`).
![image](https://github.com/user-attachments/assets/8e55627b-de26-47c6-b83c-8a53ae3d2c4f)

3. **Scatter Plot:** Compares Actual vs. Predicted values (Saved as `predictions_vs_actuals_selected_features.png`).
![image](https://github.com/user-attachments/assets/35b34164-b373-4b70-8e51-5493fd218201)

### Example Metrics:
- **Mean Absolute Error (MAE):** 12345.67
- **Mean Squared Error (MSE):** 567890123.45
- **Root Mean Squared Error (RMSE):** 23845.67
- **R-squared (R²):** 0.89

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

