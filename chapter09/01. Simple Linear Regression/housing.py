import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from joblib import dump, load

# Load and inspect the dataset
USAHousing = pd.read_csv('../data/USA_Housing.csv')

# Display the first few rows of the dataset to understand its structure
print(USAHousing.head())

# Check for null values to ensure data integrity
print("\nChecking for missing values:")
print(USAHousing.isnull().sum())

# Dropping irrelevant columns (e.g., Address) for predictive modeling
USAHousing = USAHousing.drop('Address', axis=1)

# Visualize relationships between features using pairplot
sns.pairplot(USAHousing)
plt.savefig('pairplot.png')  # Save the pairplot visualization
plt.show()

# Calculate and display correlation matrix to examine feature relationships
print("\nCorrelation Matrix:")
correlation_matrix = USAHousing.corr()
print(correlation_matrix)

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# Choose one feature for linear regression: 'Avg. Area Income'
X = USAHousing[['Avg. Area Income']]
y = USAHousing['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Create and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Display model coefficients
print("\nModel Intercept:", linear_model.intercept_)
print("\nModel Coefficient for 'Avg. Area Income':", linear_model.coef_[0])

# Make predictions on the test set
predictions = linear_model.predict(X_test)

# Plot and save the scatter plot of True vs Predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, color='red', alpha=0.6, label='Predictions')
plt.plot(y_test, y_test, color='blue', label='Ideal Fit')
plt.title('Actual vs Predicted House Prices (Using Avg. Area Income)')
plt.xlabel('True Values (y_test)')
plt.ylabel('Predicted Values')
plt.legend()
plt.savefig('predictions_vs_actuals_income.png')
plt.show()

# Evaluate model performance using metrics
print("\nPerformance Metrics:")
print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_test, predictions))
print("Mean Squared Error (MSE):", metrics.mean_squared_error(y_test, predictions))
print("Root Mean Squared Error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print("R-squared (R2):", r2_score(y_test, predictions))

# Save the trained model for future use
dump(linear_model, 'linear_model_avg_area_income.joblib')

# Demonstrate loading the model and predicting on new data
loaded_linear_model = load('linear_model_avg_area_income.joblib')
new_data = np.array([80000]).reshape(1, -1)
price_predicted = loaded_linear_model.predict(new_data)
print(f"\nPredicted house price for new data (Avg. Area Income = $80,000): ${price_predicted[0]:,.2f}")