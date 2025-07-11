# K-Nearest Neighbors (KNN) Classification

This project demonstrates the implementation of a K-Nearest Neighbors (KNN) classification model on a dataset named `Classified Data`. The script preprocesses the data, finds the optimal k value, evaluates the model, and visualizes the results.

## Project Overview 📘

- **Dataset Used:** Classified Data (CSV file with a target column named `TARGET CLASS`)
- **Objective:** Classify data into target classes using the KNN algorithm.
- **Visualization:** Error rate vs. k value, Confusion Matrix, and Classification Report heatmap.
- **Machine Learning Algorithm:** K-Nearest Neighbors (KNN)

### :computer: Script Highlights
```python
# Example code snippet for scaling and training the KNN model
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, df['TARGET CLASS'], test_size=0.30, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train, y_train)
```

## Key Features 🌟
- **Standardization:** Standardize features for improved KNN performance.
- **Optimal k Selection:** Identify the optimal number of neighbors by observing the error rate.
- **Visualization:** Heatmaps for Confusion Matrix and Classification Report.
- **Evaluation Metrics:** Evaluate using precision, recall, f1-score, and accuracy.

## Dependencies 🔧
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## Usage Example 📋

### Train and Evaluate the Model:
```bash
python knn_classification.py
```

### Key Visualizations:
1. **Error Rate vs. k Value:**
   - Saved as `plots/error_rate_vs_k.png`
![image](https://github.com/user-attachments/assets/d8e4a503-9ebf-4f4c-8fa0-76e831be6e18)

2. **Confusion Matrix:**
   - Saved as `plots/confusion_matrix_k13.png`
![image](https://github.com/user-attachments/assets/68860e58-4005-4394-8e21-0e4499eef621)

3. **Classification Report Heatmap:**
   - Saved as `plots/classification_report_k13.png`
![image](https://github.com/user-attachments/assets/8495f815-a3a8-4a72-84b0-d119ab883cc3)

### Example Outputs:
- **Confusion Matrix:**
  Displays true vs. predicted labels for k=13.
- **Classification Report:**
  Shows precision, recall, and f1-score for each class.

```plaintext
Classification Report:
              precision    recall  f1-score   support

           0       0.95      0.94      0.94       150
           1       0.93      0.95      0.94       150

    accuracy                           0.94       300
   macro avg       0.94      0.94      0.94       300
weighted avg       0.94      0.94      0.94       300
```

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