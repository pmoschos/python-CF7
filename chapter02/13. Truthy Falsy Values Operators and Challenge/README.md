# ✅ Python Truthy and Falsy Values Demonstration ❌

Welcome to the Python Truthy and Falsy Values Demonstration! This script explores Python's truthy and falsy values, conditional expressions, tuple manipulations, and the use of the `enumerate` function. It’s an excellent guide for understanding core Python concepts and practical usage.

## Script Overview 📘

The script demonstrates:
- Recognizing falsy values in Python.
- Conditional expressions with concise range checks.
- Modifying tuples by combining immutable and mutable sequences.
- Using the `enumerate` function to iterate with custom indices.

### 💻 Script Code

```python
# Falsy - Truthy Values
# Examples of falsy values: 0, 0.0, 0j, "", [], {}, (), set(), False, None

# Define an empty dictionary and check its type
empty_dict = {}  # <class 'dict'>
print(type(empty_dict))

# Conditional expression: checking if a value lies within a range
# Example: 0 < a < 10

# Define a value for `a`
a = 5

# Using and operator
if a > 0 and a < 10:
    print("Valid num")

# Using chained comparison for the same logic
if 0 < a < 10:
    print("Valid num")

# Challenge: Modifying a tuple
students = ("Alice", "Bob", "Charlie")

# Replace the first element by converting tuple to list and back
students = tuple(["Panagiotis"] + list(students)[1:])
print(students)

# Using enumerate() for custom iteration
students = ["Alice", "Bob", "Charlie", "David"]

# Enumerate with a custom start index
for index, value in enumerate(students, start=100):
    print(f"{index} : {value}")
```

## Key Features 🌟

- **Falsy and Truthy Values**: Identify common falsy values in Python and their behaviors in conditional expressions.
- **Range Checking**: Learn the benefits of concise chained comparisons for checking ranges.
- **Tuple Manipulation**: Modify immutable tuples by leveraging type conversion.
- **Enumerate Function**: Use `enumerate` for indexed iteration with custom starting indices.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `truthy_falsy_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `truthy_falsy_demo.py`.
5. Run the script with the command: `python truthy_falsy_demo.py`.

## Usage Example 📋

Executing the script demonstrates the identification of falsy values, effective range checks, tuple modification, and the use of `enumerate` for custom-indexed iteration. These examples provide practical insights into Python's versatility.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

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