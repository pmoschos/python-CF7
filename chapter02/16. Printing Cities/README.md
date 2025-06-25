# 🏙️ Python City Printing Function Demonstration 🖨️

Welcome to the Python City Printing Function Demonstration! This script showcases a versatile function that prints a list of city names with customizable separators and end characters. It's an excellent resource for anyone learning Python or those teaching programming concepts related to handling variable numbers of arguments and advanced string formatting.

## Script Overview 📘

The script includes a function called `print_cities` which takes any number of city names as arguments and prints them using a specified separator and end character. This example teaches how to utilize variadic parameters along with keyword arguments to enhance the functionality of print statements in Python.

### :computer: Script Code

```python
def print_cities(*cities, sep=", ", end="\n"):
    """
    Print a list of cities separated by a specified separator and ending with a specified end character.

    Parameters:
    *cities (str): A variable number of city names to be printed.
    sep (str): Separator between city names. Default is ", ".
    end (str): End character after the last city. Default is "\n".
    """
    if not cities:
        print("No cities provided.", end=end)
    else:
        print("Cities:", sep.join(cities), end=end)

def main():
    # Demonstrating various calls to print_cities function
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities("New York", "Tokyo", "Berlin", "Sydney")
    print_cities()
    
    # Demonstrating custom separator and end character
    print_cities("Athens", "Paris", "London", sep=" | ", end=".")
    print("\n--------------------------")
    print("Athens", "Paris", "London", sep=" | ", end=".")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Variadic Parameters**: Learn how to handle functions with a variable number of arguments, providing flexibility in how many items can be processed at a time.
- **String Manipulation**: Understand how to manipulate strings and use string methods like `join()` to format output elegantly, along with custom separators and endings.
- **Conditional Logic**: Discover how to implement conditional checks within functions to handle different input scenarios effectively, including handling no inputs gracefully.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `16_cities_printing_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `16_cities_printing_demo.py`.
5. Run the script with: `python 16_cities_printing_demo.py`.

## Usage Example 📋
Execute the script to see how different configurations of city names are formatted and printed based on the function's parameters. This will help you understand the practical applications of handling variable-length argument lists and custom print settings in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>