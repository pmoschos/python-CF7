# 🏷️ Python Rectangle Square Check Demonstration ✅

Welcome to the Python Rectangle Square Check Demonstration! This script checks if a given rectangle is a square based on user input. It's an ideal resource for anyone new to Python or those teaching programming concepts related to conditional statements and user input handling.

## Script Overview 📘

The script prompts the user to enter the length and width of a rectangle, checks if the rectangle is a square, and prints the result.

### :computer: Script Code

```python
def is_square(length, width):
    """
    Checks if a rectangle is a square.

    Args:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    bool: True if the rectangle is a square, False otherwise.
    """
    return length == width

def main():
    # Get user input for the length and width of the rectangle
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter valid integers for length and width.")
        return

    # Check if the rectangle is a square and print the result
    if is_square(length, width):
        print("The rectangle is a square.")
    else:
        print("The rectangle is not a square.")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **User Input Handling**: Learn how to capture and validate user input in Python.
- **Conditional Statements**: Understand how to use conditional statements to make decisions in code.
- **Function Usage**: Discover how to define and use functions in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `03_rectangle_square_check.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_rectangle_square_check.py`.
5. Run the script with: `python 03_rectangle_square_check.py`.

## Usage Example 📋

Execute the script and enter the length and width of a rectangle when prompted. The script will then determine if the rectangle is a square and print the result.

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
