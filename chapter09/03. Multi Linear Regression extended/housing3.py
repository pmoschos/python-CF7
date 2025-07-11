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
# axis=0: Removes items vertically (rows).
# axis=1: Removes items horizontally (columns).
# This removes the Address column from the DataFrame
USAHousing = USAHousing.drop('Address', axis=1)

# extra:
# USAHousing = USAHousing.drop([0, 1], axis=0)
# This removes the rows with indices 0 and 1.

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

# Define features (X) and target (y)
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 
                'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 
                'Area Population']]
y = USAHousing['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Create and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Display model coefficients
print("\nModel Intercept:", linear_model.intercept_)
coeff_df = pd.DataFrame(linear_model.coef_, X.columns, columns=['Coefficient'])
print("\nModel Coefficients:")
print(coeff_df)

# Make predictions on the test set
predictions = linear_model.predict(X_test)

# Plot and save the scatter plot of True vs Predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, color='red', alpha=0.6, label='Predictions')
plt.plot(y_test, y_test, color='blue', label='Ideal Fit')
plt.title('Actual vs Predicted House Prices')
plt.xlabel('True Values (y_test)')
plt.ylabel('Predicted Values')
plt.legend()
plt.savefig('predictions_vs_actuals.png')
plt.show()

# Evaluate model performance using metrics
print("\nPerformance Metrics:")
print("Mean Absolute Error (MAE):", metrics.mean_absolute_error(y_test, predictions))
print("Mean Squared Error (MSE):", metrics.mean_squared_error(y_test, predictions))
print("Root Mean Squared Error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print("R-squared (R2):", r2_score(y_test, predictions))

# Save the trained model for future use
dump(linear_model, 'linear_model.joblib')

# Demonstrate loading the model and predicting on new data
loaded_linear_model = load('linear_model.joblib')
# 80000: Represents the Average Area Income.
# 7: Represents the Average Area House Age.
# 7: Represents the Average Area Number of Rooms.
# 4: Represents the Average Area Number of Bedrooms.
# 25000: Represents the Area Population.
# .reshape(1, -1): This reshapes the 1D array into a 2D array with a shape of (1, 5)
# 1: The number of rows (one data point).
# 5: The number of columns (five features).
new_data = np.array([80000, 15, 7, 4, 25000]).reshape(1, -1)
# new_data = np.array([80000, 7, 7, 4, 25000]).reshape(1, 5)

price_predicted = loaded_linear_model.predict(new_data)
print(f"\nPredicted house price for new data: ${price_predicted[0]:,.2f}")