# 🧮 Python Factorial Calculation 🔢

Welcome to the Python Factorial Calculation script! This script calculates the factorial of a user-specified non-negative integer. It's an ideal resource for understanding loops, mathematical operations, and user input handling in Python.

## Script Overview 📘

The script prompts the user to enter a non-negative integer, calculates the factorial of the number, and prints the result.

### :computer: Script Code

```python
def calculate_factorial(n):
    """
    Calculates the factorial of a given number.
    
    Args:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return
    
    factorial = calculate_factorial(n)
    
    print(f"{n}! = {factorial:,}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Factorial Calculation**: Learn how to calculate the factorial of a given number using loops.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Error Handling**: Understand how to handle invalid input and provide appropriate feedback to the user.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `10_factorial_calculator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_factorial_calculator.py`.
5. Run the script with: `python 10_factorial_calculator.py`.

## Usage Example 📋

Execute the script and enter a non-negative integer when prompted. The script will calculate the factorial of the number and print the result.

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
