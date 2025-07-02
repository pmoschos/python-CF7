# ✨ Python Functions with Optional and Default Parameters Script 🔄

Welcome to the Python Functions with Optional and Default Parameters Script! This script demonstrates how to define functions with optional and default parameters in Python, providing flexibility in how arguments are supplied.

## Script Overview 📘

The script defines two functions: `add` and `full_opt_add`. The `add` function calculates the sum of two or three integers, while the `full_opt_add` function calculates the sum of up to three numbers with default values for all parameters.

### :computer: Script Code

```python
# Python Functions with Optional and Default Parameters Script

Welcome to the Python Functions with Optional and Default Parameters Script! This script demonstrates how to define functions with optional and default parameters in Python, providing flexibility in how arguments are supplied.

## Script Overview 📘

The script defines two functions: `add` and `full_opt_add`. The `add` function calculates the sum of two or three integers, while the `full_opt_add` function calculates the sum of up to three numbers with default values for all parameters.

### :computer: Script Code

```python
def add(a: int, b: int, c: int = 0) -> int:
    """
    Calculate the sum of two or three integers.

    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.
    c (int, optional): The third number to add, defaults to 0 if not provided.

    Returns:
    int: The sum of the provided numbers.
    """
    return a + b + c

def full_opt_add(a=0, b=0, c=0) -> int:
    """
    Calculate the sum of up to three numbers with default values.

    Parameters:
    a (int): The first number (default 0).
    b (int): The second number (default 0).
    c (int): The third number (default 0).

    Returns:
    int: The sum of the numbers.
    """
    return a + b + c

def main():
    # Demonstration of calling the function
    print(f"add(10, 20) = {add(10, 20)}")  # Outputs 30, demonstrates using the default for 'c'
    print(f"add(10, 20, 25) = {add(10, 20, 25)}")  # Outputs 55, demonstrates specifying all three parameters

    # Demonstrating the function with positional arguments
    print("Sum using positional arguments:", full_opt_add(1, 2, 3))  # Outputs 6

    # Demonstrating the function with keyword arguments
    print("Sum using keyword arguments:", full_opt_add(c=3, a=1, b=2))  # Outputs 6

    # Demonstrating the function with default values
    print("Sum with default values:", full_opt_add())  # Outputs 0

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Optional Parameters**: Learn how to define and use optional parameters with default values in Python functions.
- **Default Parameters**: Discover how to use default values for all function parameters.
- **Function Calls**: Understand how to call functions with positional and keyword arguments, and how default values are utilized.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `07_optional_parameters.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `07_optional_parameters.py`.
5. Run the script with: `python 07_optional_parameters.py`.

## Usage Example 📋

Execute the script to see how optional and default parameters work in Python functions. The script will demonstrate calling the functions with different numbers of arguments and display the results.

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