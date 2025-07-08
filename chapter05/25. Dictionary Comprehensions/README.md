# 📜 Dictionary Comprehension in Python 🔧

This script demonstrates the use of dictionary comprehension in Python to create dictionaries from lists of numbers. It includes examples of generating dictionaries with numbers and their squares, as well as filtering for even numbers.

## Script Overview 📘

The script uses dictionary comprehensions to create dictionaries where keys are numbers and values are their squares. It also shows how to filter numbers within the comprehension and includes a function to calculate the square of a number.

### :computer: Script Code

```python
# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Using dictionary comprehension to create a dictionary of numbers and their squares
squares_dict = {number: number ** 2 for number in numbers}
# Output the result
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using dictionary comprehension to create a dictionary of even numbers and their squares
even_squares_dict = {number: number ** 2 for number in numbers if number % 2 == 0}
# Output the result
print(even_squares_dict)  # {2: 4, 4: 16}

# Returns the square of the given number
def square(number):
    """
    Return the square of the given number.
    
    Args:
    number (int): A number to be squared.
    
    Returns:
    int: The square of the number.
    """
    return number ** 2

# Using dictionary comprehension to create a dictionary of numbers and their squares
# The comprehension iterates over each number in the list 'numbers'
# For each number, it calls the 'square' function to compute the square of the number
# The number is used as the key and the square of the number as the value in the resulting dictionary
squares_dict = {number: square(number) for number in numbers}

# Output the resulting dictionary
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Key Features 🌟
- **Dictionary Comprehension**: Learn how to create dictionaries using dictionary comprehensions in Python.
- **Filtering with Comprehension**: Understand how to filter elements within a dictionary comprehension.
- **Function Integration**: See how to integrate functions within dictionary comprehensions.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `25_dictionary_comprehensions.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `25_dictionary_comprehensions.py`.
5. Run the script with: `python 25_dictionary_comprehensions.py`.

## Usage Example 📋
Execute the script to see how dictionary comprehensions can be used to create dictionaries from lists. The script will generate dictionaries with numbers and their squares, both for all numbers and filtered for even numbers.

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
