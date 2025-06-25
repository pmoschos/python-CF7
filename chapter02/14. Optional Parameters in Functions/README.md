# 🗓️ Python Date Formatting Function Demonstration 🔢

Welcome to the Python Date Formatting Function Demonstration! This script showcases a function that formats dates into a standard "dd/mm/yyyy" string format. It's an ideal resource for anyone learning Python or those teaching programming concepts related to handling dates and string formatting.

## Script Overview 📘

The script includes a function called `get_formatted_date` which takes day, month, and year as inputs and returns the date in a formatted string. This example demonstrates the flexibility of function parameters, including default values and how they can be overridden by explicitly passing arguments.

### :computer: Script Code

```python
def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representing a date in the format "dd/mm/yyyy".

    Args:
        day (int): The day of the month. Defaults to 1.
        month (int): The month of the year. Defaults to 1.
        year (int): The year. Defaults to 2000.

    Returns:
        str: The formatted date string.
    """
    return f"{day:02d}/{month:02d}/{year:4d}"

def main():
    """
    Demonstrates various ways to call get_formatted_date function.
    """
    print(get_formatted_date())  # Default date (01/01/2000)
    print(get_formatted_date(10))  # Date with day only (10/01/2000)
    print(get_formatted_date(14, 5))  # Date with day and month (14/05/2000)
    print(get_formatted_date(14, 5, 2024))  # Custom date (14/05/2024)
    print(get_formatted_date(year=2024))  # Custom date with keyword argument (01/01/2024)
    print(get_formatted_date(year=2024, day=14, month=5))  # Custom date with all arguments (14/05/2024)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Function Definition and Defaults**: Learn how to define functions with default parameters that allow flexibility in how functions are called.
- **Date Formatting**: Understand how to manipulate and format strings in Python to display dates in a clear and conventional format.
- **Function Overloading**: Discover how to use function overloading by providing different numbers of arguments to achieve different outputs.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `14_optional_params_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `14_optional_params_demo.py`.
5. Run the script with: `python 14_optional_params_demo.py`.

## Usage Example 📋
Execute the script to see how different date configurations are formatted based on the function's parameters. This will help you understand the practical applications of function parameters and string formatting in Python programming.

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