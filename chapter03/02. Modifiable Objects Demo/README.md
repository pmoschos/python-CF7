# 🔍 Python List ID Demonstration 🆔

Welcome to the Python List ID Demonstration! This script showcases how to print the memory addresses (IDs) of lists in Python and demonstrates how list assignment works. It's an ideal resource for anyone new to Python or those teaching programming concepts related to memory management and list operations.

## Script Overview 📘

The script demonstrates how to assign lists to new variables, check if two variables point to the same object, and print the memory addresses (IDs) of the lists.

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
    # Define the original list
    original_list = [1, 2]

    # Assign the original list to a new variable
    new_list = original_list

    # Print the ids of the lists
    print_id("original_list", original_list)
    print_id("new_list", new_list)

    # Check if both variables point to the same object
    print(f"original_list is new_list: {original_list is new_list}")

    # Print the id of a new list with the same elements
    temp_list = [1, 2]
    print_id("temp_list", temp_list)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **List Assignment**: Learn how list assignment works in Python and how it affects memory addresses.
- **ID Printing**: Understand how to print the memory address (ID) of lists in Python.
- **Memory Management**: Discover the behavior of Python's memory management through list IDs and variable assignments.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `02_modifiable_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `02_modifiable_demo.py`.
5. Run the script with: `python 02_modifiable_demo.py`.

## Usage Example 📋

Execute the script to see the memory addresses of different lists printed in the console. This will help you understand how Python handles memory allocation and list assignments.

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
