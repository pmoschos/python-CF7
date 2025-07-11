# MNIST Digit Classification using CNN

This project demonstrates how to build and train a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset. The script preprocesses the data, constructs a CNN model, trains it, evaluates its performance, and visualizes predictions and misclassified examples.

## Project Overview 📘

- **Dataset Used:** MNIST (handwritten digit images)
- **Objective:** Classify digits (0-9) using a CNN.
- **Visualization:** Display predictions and misclassified examples.
- **Deep Learning Framework:** Keras with TensorFlow backend

### :computer: Script Highlights
```python
# Example code snippet for building the CNN model
model = Sequential()
model.add(Input(shape=(28, 28, 1)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
```

## Key Features 🌟
- **Data Preprocessing:**
  - Reshape and normalize input data.
  - One-hot encode target labels.
- **CNN Architecture:**
  - **Conv2D:** Extracts spatial features from images.
  - **MaxPooling2D:** Reduces spatial dimensions to prevent overfitting.
  - **Flatten:** Converts 2D feature maps to a 1D vector.
  - **Dense Layers:** Learn patterns and classify digits.
- **Training and Evaluation:**
  - Train the model with an 80-20 split for training and validation.
  - Evaluate accuracy on the test dataset.
- **Visualization:**
  - Display predictions and misclassified examples.

## Dependencies 🔧
- `numpy`
- `matplotlib`
- `keras`
- `tensorflow`

## Usage Example 📋

### Train the Model:
```bash
python mnist_cnn.py
```

### Key Outputs:
1. **Model Summary:** Overview of the CNN architecture.

![image](https://github.com/user-attachments/assets/a2c79b46-ef68-47e9-8e86-4e5b2e4f16f1)

2. **Test Accuracy:** Final accuracy on the test set (e.g., `Test accuracy: 0.98`).
3. **Prediction Visualizations:**
   - Saved as `mnist_plots/example_1.png`, `mnist_plots/example_2.png`, etc.

![image](https://github.com/user-attachments/assets/071b735a-a61e-440b-8d2c-5fe08e79494a)

4. **Misclassified Examples:**
   - Saved as `mnist_plots/misclassified_1.png`, `mnist_plots/misclassified_2.png`, etc.

![image](https://github.com/user-attachments/assets/da0972e3-dc2c-4a17-a416-72eadc9682fe)

### Example Outputs:
- **Correct Prediction Visualization:**
  Displays the true label and predicted label for correctly classified examples.
- **Misclassified Examples:**
  Highlights cases where the model's prediction differs from the true label.

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