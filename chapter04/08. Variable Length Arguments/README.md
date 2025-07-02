# 🌀 Python Functions with Variable-Length Arguments Script ✨

Welcome to the Python Functions with Variable-Length Arguments Script! This script demonstrates how to define functions that can handle an arbitrary number of arguments, providing flexibility in how values are passed and processed.

## Script Overview 📘

The script defines two functions: `my_add` and `my_avg`. The `my_add` function calculates the sum of an arbitrary number of integers, while the `my_avg` function calculates the average of an arbitrary number of integers.

### :computer: Script Code

```python
def my_add(*args: int) -> int:
    """
    Calculate the sum of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    int: The sum of the provided integers.
    """
    return sum(args)  # Utilizing Python's built-in sum function for efficiency and readability.

def my_avg(*args: int) -> float:
    """
    Calculate the average of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    float: The average of the provided integers. Returns 0 if no arguments are provided to avoid division by zero.
    """
    if not args:  # Check if args is empty to prevent division by zero.
        return 0
    return sum(args) / len(args)  # Using built-in sum function and len function for concise code.

def main():
    # List of ages to be averaged
    ages = [27, 35, 42, 18, 20]
    # Printing the average of a list of ages using unpacking argument lists
    print("Average age:", my_avg(*ages))

    # Directly passing numbers to calculate their average
    print("Average of 1, 2, 3, 4, 5:", my_avg(1, 2, 3, 4, 5))

    # Example to demonstrate handling with no inputs
    print("Average with no inputs:", my_avg())  # Should return 0

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Variable-Length Arguments**: Learn how to define and use functions with variable-length argument lists in Python.
- **Sum Calculation**: Discover how to calculate the sum of an arbitrary number of integers.
- **Average Calculation**: Understand how to calculate the average of an arbitrary number of integers and handle cases with no inputs.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_variable_length_arguments.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_variable_length_arguments.py`.
5. Run the script with: `python 08_variable_length_arguments.py`.

## Usage Example 📋

Execute the script to see how variable-length arguments work in Python functions. The script will demonstrate summing and averaging an arbitrary number of integers, including handling cases with no inputs.

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