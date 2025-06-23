# ✨ Python Magic Methods Demo 🪄

This README accompanies a Python script that demonstrates the use of Python's magic methods, specifically `__add__`, for performing arithmetic operations. This example is useful for understanding how Python handles operator overloading, which allows objects of custom classes to interact with built-in operators like +.

## Script Overview 📘

The script initializes two integers and demonstrates two ways to perform addition: using the standard + operator and the magic method `__add__`. This provides insight into how Python's dunder methods, or double underscore methods, work under the hood to enable such operations.

### :computer: Script Code

```python
# Initialize two integer variables
a = 10
b = 20

# Perform addition and store the result in a variable
result = a + b
# Print the result of the addition
print("a + b =", result)

# Print a separator line for clarity in output
print("---------")

# Display the data type of variable 'a'
print("Type of a:", type(a))

# Using the magic method __add__() to perform the addition
# Magic methods in Python are special methods which add "magic" to your classes.
# __add__ is one of these magic methods that allows the object of the class to use the + operator.
magic_result = a.__add__(b)
# Print the result obtained using the magic method
print("a + b =", magic_result)
```

## Key Features 🌟

- **Operator Overloading**: Shows how Python allows custom behavior for standard operations like addition.
- **Understanding Magic Methods**: Introduces magic methods and their role in enabling interactions between Python objects and operators.
- **Practical Demonstration**: Offers practical examples of how to use these methods in everyday coding.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `09_ints_out_of_the_box.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `09_ints_out_of_the_box.py`.
5. Run the script with: `python 09_ints_out_of_the_box.py`.

## Usage Example 📋

Upon execution, the script will demonstrate two different ways to perform addition, highlighting how magic methods facilitate the use of the + operator for custom types.

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
