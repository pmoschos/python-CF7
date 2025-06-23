# ✏️ Python Variables and Printing Options Demo 🖨️

This README describes a Python script that initializes three different types of variables—an integer, a float, and a string—and demonstrates various ways to format their output using the `print` function. It's a practical example for those new to Python, focusing on variable handling and custom print formatting.

## Script Overview 📘

The script performs simple variable initialization and showcases different methods of printing variables, including default space-separated printing, tab-separated, and custom end characters. This introduction to variable handling and output formatting is ideal for Python beginners.

### :computer: Script Code

```python
# Initialize an integer, a float, and a string variable
my_int = 10       # Integer value
my_float = 5.5    # Floating point number
my_str = "Hello CF!"  # String value

# Print a header message before printing values
print("Printing comma separated values:")

# Print variables separated by space (default behavior)
print(my_int, my_float, my_str)

# Print a separator line
print("-------------------------")

# Print variables separated by a tab character
print(my_int, my_float, my_str, sep="\t")

# Print another separator line
print("-------------------------")

# Print variables separated by a tab, ending the print statement with '---' followed by a new line
print(my_int, my_float, my_str, sep="\t", end="---\n")
```

## Key Features 🌟
- **Variable Initialization:** Introduces how to declare and initialize basic data types in Python.
- **Custom Print Formatting:** Demonstrates modifying the default behavior of the print function to adjust spacing and end characters.

## Technical Requirements 🔧
- **Python Version:** Python 3.x ![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
- **External Libraries:** None required ![Libraries](https://img.shields.io/badge/libraries-none-important)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `03_print_demo.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_print_demo.py`.
5. Run the script with: `python 03_print_demo.py`.

## Usage Example 📋
When executed, the script prints the initialized variables in different formats, providing visual feedback on how various print options affect the output.


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