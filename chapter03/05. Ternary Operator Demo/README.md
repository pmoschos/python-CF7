# 🔢 Python Integer Comparison Demonstration ✅

Welcome to the Python Integer Comparison Demonstration! This script compares two integers provided by the user and prints the result. It also demonstrates the use of ternary operators in Python.

## Script Overview 📘

The script prompts the user to enter two integers, compares them, and prints the result. It also includes examples of using ternary operators for simple conditional expressions.

### :computer: Script Code

```python
def compare_integers(a, b):
    """
    Compares two integers and prints the result.

    Args:
    a (int): The first integer to compare.
    b (int): The second integer to compare.

    Returns:
    None
    """
    if a == b:
        print("The numbers are equal.")
    elif a > b:
        print("The first number is greater than the second number.")
    else:
        print("The first number is less than the second number.")

def main():
    try:
        # Get user input for the two integers
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    # Compare the integers
    compare_integers(a, b)

    # 1. Ternary operator (simple example)
    result = "Positive" if a > 0 else "Non-positive"
    print(result)

    # 2. Ternary operator (extended example)
    result = (
        "The numbers are equal." if a == b else
        "The first number is greater than the second number." if a > b else
        "The first number is less than the second number."
    )
    print(result)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Integer Comparison**: Learn how to compare two integers and print the result using conditional statements.
- **Ternary Operator**: Understand how to use ternary operators for simple conditional expressions in Python.
- **User Input Handling**: Discover how to capture and validate user input in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `05_ternary_operator_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `05_ternary_operator_demo.py`.
5. Run the script with: `python 05_ternary_operator_demo.py`.

## Usage Example 📋

Execute the script and enter two integers when prompted. The script will compare the integers and print the result, demonstrating both traditional conditional statements and ternary operators.

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
