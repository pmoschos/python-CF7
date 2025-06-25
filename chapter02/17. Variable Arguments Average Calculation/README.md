# 📊 Python Average Calculation Function Demonstration ➗

Welcome to the Python Average Calculation Function Demonstration! This script showcases a flexible function that calculates the average of any number of numerical inputs and formats the result to two decimal places. It's an ideal resource for anyone learning Python or those teaching programming concepts related to arithmetic operations and string formatting.

## Script Overview 📘

The script includes a function called `get_average` which can take a variable number of numerical arguments and returns their average formatted as a string. This example teaches how to utilize variadic parameters in Python functions to handle input flexibility.

### :computer: Script Code

```python
def get_average(*numbers):
    """
    Calculate the average of a list of numbers and format the result to 2 decimal places.

    Parameters:
    *numbers: A variable number of numeric arguments.

    Returns:
    str: The formatted average of the input numbers.
    """
    if not numbers:
        return "No numbers provided."
    
    average = sum(numbers) / len(numbers)
    return "{:.2f}".format(average)

def main():
    # Example set of numbers
    numbers = [10, 20, 15]
    
    average = get_average(*numbers)
    print(f"The average of {numbers} is {average}")
    
    # Handling empty input
    average3 = get_average()
    print(f"Average with no input: {average3}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Variadic Parameters**: Learn how to handle functions with a variable number of arguments, allowing for flexibility in how many items can be processed at a time.
- **Arithmetic Operations**: Understand how to perform arithmetic calculations and use them in practical applications.
- **String Formatting**: Discover how to format strings in Python to control how text and numbers are displayed.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `17_varargs_avg_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `17_varargs_avg_demo.py`.
5. Run the script with: `python 17_varargs_avg_demo.py`.

## Usage Example 📋
Execute the script to see how the function calculates the average of provided numbers and formats the output. This will help you understand the practical applications of arithmetic functions and variadic parameters in Python programming.

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