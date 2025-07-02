# 🧮 Factorial Calculation Script 🔢

Welcome to the Factorial Calculation Script! This script demonstrates how to calculate the factorial of a given positive integer using a recursive approach.

## Script Overview 📘

The script defines a function `factorial` that calculates the factorial of a given integer `n` using recursion. It includes base cases for `0!` and `1!`, and uses the recursive relationship `n! = n * (n-1)!` for `n > 1`.

### :computer: Script Code

```python
# Factorial Calculation
# Definition: n! (n factorial) is the product of all positive integers from 1 to n.
# Recursive relationship: n! = n * (n-1)! for n > 1.
# Base cases:
# 0! = 1 : The factorial of 0 is defined as 1 by convention.
# 1! = 1 : The factorial of 1 is also 1, establishing the base case for recursive multiplication.

def factorial(n: int) -> int:
    """
    Calculate the factorial of integer n.

    Parameters:
    n (int): The integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given integer.
    """
    if n < 0: return 0
    if n in (0, 1): return 1
    return n * factorial(n - 1)

def main():
    # Get user input for the value of n
    n = int(input("Enter a positive integer to find its Factorial number: "))
    print(f"{n}! = {factorial(n):,}")

if __name__ == '__main__':
    main()
```

## Key Features 🌟

- **Recursive Calculation**: Learn how to calculate the factorial of a number using recursion.
- **Base Cases Handling**: Understand how to handle base cases in a recursive function.
- **User Input**: Discover how to capture and process user input in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `11_factorial_rec_calculation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `11_factorial_rec_calculation.py`.
5. Run the script with: `python 11_factorial_rec_calculation.py`.

## Usage Example 📋

Execute the script and enter a positive integer when prompted. The script will calculate the factorial of the given integer and display the result.

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
