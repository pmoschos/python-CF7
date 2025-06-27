# 🔢 Python Armstrong Number Checker 🏗️

Welcome to the Python Armstrong Number Checker! This script checks if a given number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## Script Overview 📘

The script prompts the user to enter an integer, checks if it is an Armstrong number, and prints the result.

### :computer: Script Code

```python
def is_armstrong_number(n):
    """
    Checks if a number is an Armstrong number.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return n == total

def main():
    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Armstrong Number Check**: Learn how to check if a number is an Armstrong number.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Loop and Math Operations**: Understand how to use loops and mathematical operations to determine if a number meets the Armstrong criteria.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_armstrong_checker.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_armstrong_checker.py`.
5. Run the script with: `python 08_armstrong_checker.py`.

## Usage Example 📋

Execute the script and enter an integer when prompted. The script will check if the number is an Armstrong number and print the result.

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
