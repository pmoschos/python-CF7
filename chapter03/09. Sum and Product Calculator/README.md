# ➕ Python Sum and Product Calculation ✖️

Welcome to the Python Sum and Product Calculation script! This script calculates the sum and product of all numbers from 1 to a user-specified upper bound. It's an ideal resource for understanding loops, mathematical operations, and user input handling in Python.

## Script Overview 📘

The script prompts the user to enter a positive integer as the upper bound, calculates the sum and product of all numbers from 1 to the upper bound, and prints the results.

### :computer: Script Code

```python
def calculate_sum_and_product(upper_bound):
    """
    Calculates the sum and product of numbers from 1 to upper_bound.
    
    Args:
    upper_bound (int): The upper limit of the range.
    
    Returns:
    tuple: A tuple containing the sum and product.
    """
    total_sum = 0
    total_product = 1

    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i
    
    return total_sum, total_product

def main():
    try:
        upper_bound = int(input("Please insert a positive int: "))
        if upper_bound <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    
    total_sum, total_product = calculate_sum_and_product(upper_bound)
    
    print(f"Sum (1 - {upper_bound}): {total_sum:,}")
    print(f"Product (1 - {upper_bound}): {total_product:,}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Sum Calculation**: Learn how to calculate the sum of numbers within a specified range.
- **Product Calculation**: Understand how to calculate the product of numbers within a specified range.
- **User Input Handling**: Discover how to capture and validate user input in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `09_sum_and_product.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `09_sum_and_product.py`.
5. Run the script with: `python 09_sum_and_product.py`.

## Usage Example 📋

Execute the script and enter a positive integer when prompted. The script will calculate the sum and product of all numbers from 1 to the upper bound and print the results.

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
