import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D # type: ignore


"""
Conv2D Layer
Extracts features from the input image by learning spatial hierarchies using filters.

MaxPooling2D Layer
Reduces the spatial dimensions, preserving the most important features and reducing overfitting.

Flatten Layer
Converts the 2D feature maps into a 1D vector for input into dense layers.

Dense Hidden Layer
Learns higher-level patterns in the data with 128 neurons and ReLU activation.

Output Layer
Maps the learned features to the 10 output classes with softmax for multi-class classification.
"""

# Step 2: Load the Dataset
# Load the MNIST dataset using Keras. This will automatically split the data into training and testing sets.
# Load the dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape data for CNN input
# 0 - 255
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32') / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32') / 255

# One-hot encode the labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# Step 3: Build the Model
# Create a Convolutional Neural Network (CNN) model for digit classification.
# Define the CNN model
model = Sequential()

# Add an input layer
# Input explicitly defines the shape of the input data.
# - shape=(28, 28, 1): Input images are 28x28 pixels with 1 channel for grayscale.
model.add(Input(shape=(28, 28, 1)))

# Add a convolutional layer
# Conv2D creates a convolution kernel that is convolved with the input image to produce output tensors.
# - 32: Number of filters (kernels) to use (output depth of the convolutional layer).
# - (3, 3): Size of the convolution filter (3x3 kernel).
# - activation='relu': Apply the ReLU activation function to add non-linearity.
model.add(Conv2D(32, (3, 3), activation='relu'))

# Add a max-pooling layer
# MaxPooling2D reduces the spatial dimensions of the feature maps, retaining the most important information.
# - (2, 2): Pooling window size (2x2). It takes the maximum value in every 2x2 window, reducing computation and overfitting.
model.add(MaxPooling2D((2, 2)))

# Add a flattening layer
# Flatten transforms the 2D feature maps into a 1D vector (needed before passing to dense layers).
# This prepares the data for the fully connected (dense) layers.
model.add(Flatten())

# Add a dense (fully connected) hidden layer
# - 128: Number of neurons in this dense layer.
# - activation='relu': Apply the ReLU activation function for non-linearity.
# This layer learns complex patterns from the flattened feature map.
model.add(Dense(128, activation='relu'))

# Add the output layer
# - 10: Number of neurons, corresponding to the 10 output classes (digits 0-9).
# - activation='softmax': Use the softmax activation to output probabilities for each class.
# The class with the highest probability will be the predicted digit.
model.add(Dense(10, activation='softmax'))  # Output layer for 10 classes (digits 0-9)

# Compile the model
# - optimizer='adam': Adam optimizer for efficient training.
# - loss='categorical_crossentropy': Cross-entropy loss function for multi-class classification.
# - metrics=['accuracy']: Track accuracy during training and evaluation.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
# This gives an overview of the model architecture, including the number of parameters in each layer.
model.summary()


# Step 4: Train the Model
# Fit the model on the training data.
# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=200, validation_split=0.2)


# Step 5: Evaluate the Model
# After training, evaluate the model's performance on the test set.
# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_accuracy:.4f}')


# Step 6: Make Predictions
# Use the trained model to make predictions on new data.
# Make predictions
predictions = model.predict(x_test)


import os

# Ensure the output directory for saving plots
output_dir = "mnist_plots"
os.makedirs(output_dir, exist_ok=True)

# Display some predictions and save the plots
for i in range(3):  # Plot 3 random predictions
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f'Predicted: {np.argmax(predictions[i])}, True: {np.argmax(y_test[i])}')
    plt.axis('off')
    plt.savefig(os.path.join(output_dir, f"example_{i+1}.png"))
    plt.show()

# Find and plot 3 misclassified examples
# predictions = [[0.1, 0.9, 0.0], [0.8, 0.1, 0.1], [0.0, 0.2, 0.8]]
# y_test = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]

# Iteration:
# For i=0: np.argmax(predictions[0]) = 1, np.argmax(y_test[0]) = 1 → Correct
# For i=1: np.argmax(predictions[1]) = 0, np.argmax(y_test[1]) = 0 → Correct
# For i=2: np.argmax(predictions[2]) = 2, np.argmax(y_test[2]) = 0 → Misclassified

# Output:
# misclassified_indices = [2]

misclassified_indices = [i for i in range(len(x_test)) if np.argmax(predictions[i]) != np.argmax(y_test[i])]

for j, idx in enumerate(misclassified_indices[:3]):  # Plot the first 3 misclassified examples
    plt.imshow(x_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f'Misclassified - Predicted: {np.argmax(predictions[idx])}, True: {np.argmax(y_test[idx])}')
    plt.axis('off')
    plt.savefig(os.path.join(output_dir, f"misclassified_{j+1}.png"))
    plt.show()