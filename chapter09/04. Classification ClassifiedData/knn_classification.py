import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import os

# Ensure output directory for plots
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Load the dataset
# Assuming the dataset "Classified Data" is a CSV file with a column index.
df = pd.read_csv("../data/secret_data", index_col=0)

# Display the first few rows of the dataset to understand its structure
print("Dataset Head:")
print(df.head())

# Standardizing the features
# We need to scale the features for KNN to perform better, as it is distance-based.
scaler = StandardScaler()

# Fit the scaler to the data, excluding the target variable ('TARGET CLASS')
scaler.fit(df.drop('TARGET CLASS', axis=1))

# Transform the data to have a mean of 0 and a standard deviation of 1
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

# Create a DataFrame for the scaled features for better understanding
# The columns are the same as the original feature columns.
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print("\nScaled Features Head:")
print(df_feat.head())

# Splitting the dataset into training and testing sets
# X (features) and y (target variable) are separated.
X_train, X_test, y_train, y_test = train_test_split(
    scaled_features,  # Independent variables
    df['TARGET CLASS'],  # Dependent variable
    test_size=0.30,  # 30% of the data for testing
    random_state=42  # Ensures reproducibility
)

# Finding the optimal k value by observing the error rate for k values from 1 to 40
error_rate = []  # List to store error rates for each k value

# Loop over a range of k values to find the one with the lowest error rate
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)  # Set the current k value
    knn.fit(X_train, y_train)  # Train the model with the current k
    pred_i = knn.predict(X_test)  # Predict the test data
    error_rate.append(np.mean(pred_i != y_test))  # Calculate the error rate

# Plot the error rate against the k values
plt.figure(figsize=(12, 8))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=8, label='Error Rate')
plt.title('Error Rate vs. K Value', fontsize=16)
plt.xlabel('K Value', fontsize=14)
plt.ylabel('Error Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "error_rate_vs_k.png"))
plt.show()

# Choosing the optimal k value (e.g., k=13 from the error rate analysis)
knn = KNeighborsClassifier(n_neighbors=13)

# Retrain the KNN model using the optimal k value
knn.fit(X_train, y_train)

# Predict using the optimal k value
pred = knn.predict(X_test)

# Evaluate the model again with the optimal k value
print('WITH K=13')
conf_matrix = confusion_matrix(y_test, pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=["Class 0", "Class 1"], yticklabels=["Class 0", "Class 1"])
plt.title("Confusion Matrix (k=13)", fontsize=16)
plt.xlabel("Predicted Label", fontsize=14)
plt.ylabel("True Label", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "confusion_matrix_k13.png"))
plt.show()

# Plot the classification report
report = classification_report(y_test, pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

plt.figure(figsize=(10, 6))
sns.heatmap(report_df.iloc[:-1, :-1], annot=True, cmap="coolwarm", cbar=False, fmt='.2f')
plt.title("Classification Report (k=13)", fontsize=16)
plt.xlabel("Metrics", fontsize=14)
plt.ylabel("Classes", fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "classification_report_k13.png"))
plt.show()

print('\nClassification Report:')
print(classification_report(y_test, pred))
