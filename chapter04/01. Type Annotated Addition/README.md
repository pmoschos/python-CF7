# 📋 Python Type-Annotated Addition Function ✅

Welcome to the Python Type-Annotated Addition Function script! This script demonstrates the use of type annotations in Python functions to ensure that parameters are of the correct type and to provide useful documentation.

## Script Overview 📘

The script defines a function `my_add` that adds two numbers and includes type annotations for its parameters and return value. The script also demonstrates how to handle type errors and use the `help()` function to display function documentation.

### :computer: Script Code

```python
# Type Annotations for Parameters (a: float | int, b: float | int):
# Return Type Annotation (-> float | int)
def my_add(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers and returns the result.

    Args:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
    int | float: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers or floats.")
    return a + b

def main():
    # Testing the function
    print(my_add(10, 20))          # Outputs: 30
    print(my_add(5, 8.3))          # Outputs: 13.3
    try:
        print(my_add("Hello ", "Coding Factory"))  # This call should raise an error
    except TypeError as e:
        print(e)  # Outputs: Both a and b must be integers or floats.
    
    print("Annotations:", my_add.__annotations__)
    print("Docs:", my_add.__doc__)

    print("--------------------------------")

    help(my_add)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Type Annotations**: Learn how to use type annotations to specify the expected types of function parameters and return values.
- **Error Handling**: Discover how to handle and raise exceptions in Python.
- **Function Documentation**: Understand how to use docstrings to document your functions and use the `help()` function to display this documentation.

## Technical Requirements 🔧

- **Python Version**: Python 3.10 or higher is recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.10 or higher is installed on your machine.
2. Save the script as `01_type_annotated_addition.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `01_type_annotated_addition.py`.
5. Run the script with: `python 01_type_annotated_addition.py`.

## Usage Example 📋

Execute the script to see type annotations in action. The script will demonstrate correct usage, error handling, and display function annotations and documentation.

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