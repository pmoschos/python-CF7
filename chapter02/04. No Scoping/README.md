# 🎲 Python Random Numbers Demonstration 🎰

Welcome to the Python Random Numbers Demonstration! This script illustrates how to generate random integers, store them in a list, and find specific elements based on conditions, such as identifying the last even number. It’s an ideal introduction to Python’s `random` module and basic list operations.

## Script Overview 📘

The script demonstrates:
- How to use the `random.randint` method to generate random integers.
- Appending elements to a list dynamically.
- Iterating over a list to identify and store elements based on a condition.

### 💻 Script Code

```python
import random

# Initialize an empty list to store random numbers
random_numbers = []

# Use a for loop to generate 10 random integers
for _ in range(10):  # Loop runs 10 times
    num = random.randint(1, 100)  # Generate a random integer between 1 and 100
    random_numbers.append(num)  # Append the generated number to the list

# Print the generated list of random numbers
print(random_numbers)

# Find the last even number in the list
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        even = num  # Store the current even number

# Print the last number in the list (regardless of even or odd)
print(f"The last item of the list: {num}")

# Print the last even number encountered in the loop
print(f"The last 'even' item of the list: {even}")
```

## Key Features 🌟

- **Random Number Generation**: Learn how to use the `random` module to generate integers dynamically.
- **List Manipulation**: Understand how to append elements to a list during iteration.
- **Condition-Based Filtering**: See how to identify and store elements based on conditions, such as checking for even numbers.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses Python’s built-in `random` module).

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `04_no_scoping_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_no_scoping_demo.py`.
5. Run the script with the command: `python 04_no_scoping_demo.py`.

## Usage Example 📋

Executing the script generates a list of 10 random integers between 1 and 100. It then identifies and displays the last even number from the list, along with the final element of the list.

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>