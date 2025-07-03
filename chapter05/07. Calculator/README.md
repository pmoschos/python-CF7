# 🧮 Arithmetic Operations on a List of Numbers 🔢

This script demonstrates how to generate functions to perform arithmetic operations on a list of numbers. The operations include addition, subtraction, multiplication, and division.

## Script Overview 📘

The script defines a `calculate` function that generates four functions: `plus`, `minus`, `mul`, and `div`. Each function performs a specific arithmetic operation on the provided list of numbers.

### :computer: Script Code

```python
import functools

def calculate(args):
    """
    Generate functions to perform arithmetic operations on a list of numbers.

    Parameters:
    args (list of int/float): List of numbers to perform operations on.

    Returns:
    tuple: Four functions (plus, minus, mul, div) that perform addition, subtraction,
           multiplication, and division respectively.
    """
    def plus():
        """Return the sum of the numbers in the list."""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        """Return the result of subtracting the numbers in the list."""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        """Return the product of the numbers in the list."""
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        """Return the result of dividing the first number by the sum of the rest of the numbers."""
        if not 0 in args[1:]:  # Ensure there are no zeros in the denominator
            return args[0] / sum(args[1:])
        else:
            return "Division by zero error"

    return plus, minus, mul, div

def main():
    """
    Main function to demonstrate the usage of calculate.
    """
    ints_list = [26, 5, 4, 3, 2, 1]

    # Generate arithmetic operation functions for ints_list
    add_func, minus_func, mul_func, div_func = calculate(ints_list)

    # Print results of each operation
    print("add_func:", add_func())  # Expected output: 41 (sum of 26 + 5 + 4 + 3 + 2 + 1)
    print("minus_func:", minus_func())  # Expected output: 11 (26 - 5 - 4 - 3 - 2 - 1)
    print("mul_func:", mul_func())  # Expected output: 3120 (26 * 5 * 4 * 3 * 2 * 1)
    print("div_func:", div_func())  # Expected output: 2.0 (26 / (5 + 4 + 3 + 2 + 1))

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Variable-Length Arguments**: Learn how to define and use functions with variable-length argument lists in Python.
- **Default Parameters**: Discover how to use default values for function parameters.
- **Keyword Arguments**: Understand how to use keyword arguments to pass additional information to a function.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses the built-in functools module)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `07_calculator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `07_calculator.py`.
5. Run the script with: `python 07_calculator.py`.

## Usage Example 📋
Execute the script to see how the functions for arithmetic operations work on a list of numbers. The script will demonstrate the sum, difference, product, and division of the provided list of numbers.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
