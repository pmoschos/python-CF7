# 🧮 Python String Formatting and Math Module Demo 🔢

This README outlines a Python script that demonstrates various techniques of string formatting including Python 2 style, Python 3 `str.format()` method, and modern Python 3 f-strings. Additionally, it shows basic usage of the `math` module to access mathematical constants.

## Script Overview 📘

The script covers fundamental operations like importing modules, string concatenation, and string formatting in different Python versions. It's designed to help beginners understand how to properly handle data types and output formatting in Python.

### :computer: Script Code

```python
import math  # Import the math module to access mathematical constants and functions

# Define string and integer variables
name = "Alice"
age = 20

# Print a simple string
print("CF")
# Print the mathematical constant PI from the math module
print("PI =", math.pi)

# Demonstrate string concatenation
print("String Concatenation")
# This line would cause a TypeError because you cannot concatenate string and integer directly
# print(name + " is" + age + " years old.")  # Incorrect way, commented out
print(name + " is " + str(age) + " years old.")  # Correct by converting age to a string
print("-------------------------")

# Demonstrate old Python 2 style string formatting using the % operator
print("Python 2 style")
print("PI = %6.2f" % math.pi)  # Format PI to two decimal places with padding
print("%s is %d years old" % (name, age))  # Use placeholders for string and integer
print("-------------------------")

# Demonstrate Python 3 style string formatting using the str.format() method
print("Python 3 style using string format")
print("Age is {0:2d}".format(age))  # Format age with 2-digit padding
print("PI = {0:.3f}".format(math.pi))  # Format PI to three decimal places
# Explanation of the '0' in format: It refers to the first argument passed to format()
print("PI = {0:.3f} and age = {1}".format(math.pi, age))  # Multiple placeholders
print("-------------------------")

# Print combining text and variables using format and specifying the print end character
print("{0} is {1}".format(name, age), end=" ")
print("years old.")

# Using string formatting for alignment and padding
print("{0:*^10}:{1:>20}".format(name, age))  # Center name with asterisks, right-align age
print("{0:*^10}:{1:<20}".format(name, age), end="|")  # Left-align age, end print with '|'
print("-------------------------")

# Demonstrate modern Python 3 style string interpolation using f-strings
print("Python 3 style using f-strings")
print(f"{name} is {age} years old.")  # Embed expressions inside string literals directly
```

## Key Features 🌟
- **String Formatting:** Introduces multiple methods for string formatting, including Python 2 `%` style, Python 3 `format()`, and f-strings.
- **Math Module Usage:** Demonstrates how to utilize constants from the `math` module.
- **Data Type Handling:** Shows how to convert integers to strings for correct string concatenation.

## Technical Requirements 🔧
- **Python Version:** Python 3.x ![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
- **External Libraries:** None required ![Libraries](https://img.shields.io/badge/libraries-none-important)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `04_math_demo.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_math_demo.py`.
5. Run the script with: `python 04_math_demo.py`.

## Usage Example 📋
The output of the script will show how each variable is formatted differently depending on the method used, providing a visual understanding of string formatting options in Python.

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