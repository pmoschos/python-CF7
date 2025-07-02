# 🧮 Factorial Calculation Using Reduce Script 🔢

Welcome to the Factorial Calculation Using Reduce Script! This script demonstrates how to calculate the factorial of a given integer using the `reduce` function from the `functools` module along with a lambda function.

## Script Overview 📘

The script prompts the user to input an integer and uses the `reduce` function to compute the factorial of that number. Additionally, it includes a version that prints intermediate multiplication results to illustrate the steps involved in the calculation.

### :computer: Script Code

```python
from functools import reduce

# Prompt the user to input an integer for which the factorial is to be calculated
n = int(input("Give an int to calc facto: "))

# Use the reduce function to calculate the factorial of the number
# The reduce function applies a rolling computation to sequential pairs of values in a range from 1 to n+1
# The lambda function provided to reduce takes two arguments x and y, multiplying them together
# Since range(1, n+1) generates numbers from 1 to n, this effectively calculates the product of all integers from 1 to n, which is the factorial

# First step: x = 1, y = 2 (Result: 1 * 2 = 2)
# Second step: x = 2 (result of previous step), y = 3 (Result: 2 * 3 = 6)
# Third step: x = 6 (result of previous step), y = 4 (Result: 6 * 4 = 24)
# Fourth step: x = 24 (result of previous step), y = 5 (Result: 24 * 5 = 120)
result = reduce(lambda x, y: x * y, range(1, n + 1))

# Output the result to the user, formatting it as n! = result
print(f"{n}! = {result}")

# Modified lambda function to print intermediate results
def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

result = reduce(print_and_multiply, range(1, n + 1))
print(f"Final result: {result}")

# Use reduce with a lambda function that includes a print statement
result = reduce(lambda x, y: print(f"{x} * {y} = {x * y}") or x * y, range(1, n + 1))
print(f"Final result: {result}")
```

# Key Features 🌟
- **Reduce Function**: Learn how to use the reduce function to aggregate all elements in a range.
- **Lambda Function**: Discover how to define and use lambda functions for concise and readable code.
- **Factorial Calculation**: Understand how to calculate the factorial of a given integer using the reduce function and handle intermediate results.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses the built-in functools module)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `18_reduce_factorial_wow.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_reduce_factorial_wow.py`.
5. Run the script with: `python 18_reduce_factorial_wow.py`.

## Usage Example 📋
Execute the script to see how the reduce function can be used to calculate the factorial of a given integer. The script will demonstrate this operation and print both the intermediate and final results.

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