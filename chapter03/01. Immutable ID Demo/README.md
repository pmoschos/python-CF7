# 🔎 Python Variable ID Demonstration 🆔

Welcome to the Python Variable ID Demonstration! This script showcases how to print the memory addresses (IDs) of different variables in Python, specifically focusing on integer and string interning. It's an ideal resource for anyone new to Python or those teaching programming concepts related to memory management and variable interning.

## Script Overview 📘

The script demonstrates how to define integer and string variables and print their IDs to show how Python handles memory allocation for these variables.

### :computer: Script Code

```python
def print_id(variable_name, variable):
    """
    Prints the id of the given variable.

    Args:
    variable_name (str): The name of the variable as a string.
    variable: The variable whose id is to be printed.
    """
    print(f"id({variable_name}) = {id(variable)}")

def main():

    # Interning (όπως το String pool της Java)

    # Define integer variables
    a = 10
    b = 10

    # Define string variables
    str1 = "CF"
    str2 = 'CF'

    # Print the ids of the variables
    print_id("a", a)
    print_id("b", b)

    print_id("str1", str1)
    print_id("str2", str2)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Variable Interning**: Learn how Python handles memory allocation for integers and strings, showing the concept of interning.
- **ID Printing**: Understand how to print the memory address (ID) of variables in Python.
- **Memory Management**: Discover the behavior of Python's memory management through variable IDs.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `01_immutable_id_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `01_immutable_id_demo.py`.
5. Run the script with: `python 01_immutable_id_demo.py`.

## Usage Example 📋

Execute the script to see the memory addresses of different variables printed in the console. This will help you understand how Python handles memory allocation and variable interning.

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
