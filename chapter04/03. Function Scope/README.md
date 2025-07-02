# 📚 Python Function Scope and Parameters Script ✨

Welcome to the Python Function Scope and Parameters Script! This script demonstrates how function parameters and local variables work in Python, including how modifications within a function do not affect the original arguments.

## Script Overview 📘

The script defines a function `add_numbers` that adds two integers. It also shows how modifying a parameter inside the function does not change the original variable outside the function.

### :computer: Script Code

```python
a = 10
b = 20

def add_numbers(x: int, y: int) -> int:
    """
    Adds two integers and returns the sum.

    Parameters:
    x (int): The first integer.
    y (int): The second integer.

    Returns:
    int: The sum of the two integers.
    """
    x = 100  # Clearly distinguish local modification
    return x + y

def main():
    # Use the function and display results
    result = add_numbers(a, b)
    print(result)  # Output will be 120
    print(a)       # Output will be 10, demonstrating that 'a' is unchanged

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Function Parameters**: Learn how to use function parameters and understand their scope.
- **Local Variables**: Discover how modifying a parameter inside a function affects only the local copy.
- **Function Return Values**: Understand how to return values from a function and use them in your code.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `03_function_scope.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_function_scope.py`.
5. Run the script with: `python 03_function_scope.py`.

## Usage Example 📋

Execute the script to see how function parameters and local variables work in Python. The script will demonstrate that modifying a parameter inside a function does not affect the original variable outside the function.

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