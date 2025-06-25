# 🚀 Python Main Application Script (`app.py`) 🖥️

Welcome to the Python Main Application Script Demonstration! This script demonstrates how to use functions imported from another module in a Python application. It's an ideal resource for anyone new to Python or those teaching programming concepts related to module interaction and function calls.

## Script Overview 📘

The script includes a function import from `my_calculations.py` and uses it to perform an addition. The main focus is to show how to integrate and utilize external functions within an application.

### :computer: Script Code

```python
# import my_calculations
from my_calculations import my_add_function as my_add, num1

num2 = 10

# res = my_calculations.my_add_function(num2, my_calculations.num1)
# res = my_add_function(num1, num2)
res = my_add(num1, num2)
print(res) # 110
print(__name__)
```

## Key Features 🌟
- **Function Importing**: Learn how to import and alias functions from different modules.
- **Using Imported Functions**: Demonstrates using imported functions to perform operations.
- **Print Statements**: Shows effective ways of integrating dynamic print statements for displaying results.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (Assuming `my_calculations.py` is part of the same project)

## Installation and Setup 🚀
This script can be executed in any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Place both `app.py` and `my_calculations.py` in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `app.py`.
5. Run the script with: `python app.py`.

## Usage Example 📋
Running the script will display the sum of two numbers and the name of the module. This demonstrates how functions can be modularized and reused across different parts of a Python application.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>