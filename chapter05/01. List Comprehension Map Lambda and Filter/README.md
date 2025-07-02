# 🔄 Squaring Numbers in a List Script 🔢

Welcome to the Squaring Numbers in a List Script! This script demonstrates various methods to square numbers in a list using Python. The methods include `list comprehension`, the `map` function with both `lambda` and `named functions`, and `filtering` even numbers before squaring.

## Script Overview 📘

The script showcases different techniques to square numbers in a list of integers. It demonstrates list comprehensions, the `map` function with a `lambda`, using a named function, and `filtering` even numbers for squaring.

### :computer: Script Code

```python
# Original list of numbers
list_of_ints = [1, 2, 3, 4, 5, 6, 7]

# 1. Using list comprehension to square each number in the list
squared_list_comprehension = [number ** 2 for number in list_of_ints]

# Printing the results
print(f"Squared numbers (list comprehension): {squared_list_comprehension}")


# 2. Using map() with a lambda function to square each number in the list
squared_map_lambda = list(map(lambda number: number ** 2, list_of_ints))

# Printing the results
print(f"Squared numbers (map with lambda): {squared_map_lambda}")


# 3. This function takes an integer and returns its square.
def square_function(num):
    return num ** 2

# Printing the results using a list comprehension with a named function
# The condition `if number == 100` will filter out all numbers since none are 100
filtered_squared_func_results = [square_function(number) for number in list_of_ints if number == 100]
print(f"Squared numbers with filter (list comprehension with function): {filtered_squared_func_results}")


# 4. Using map() with the named function to square each number in the list
squared_map_function = list(map(square_function, list_of_ints))

# Printing the results
print(f"Squared numbers (map with function): {squared_map_function}")


# 5. Filtering and squaring only even numbers using list comprehension
filtered_squared_list_comprehension = [number ** 2 for number in list_of_ints if number % 2 == 0]

# Printing the results
print(f"Filtered and squared numbers (list comprehension): {filtered_squared_list_comprehension}")


# 6. Filtering and squaring only even numbers using filter() and map()
filtered_squared_map_filter = list(map(square_function, filter(lambda x: x % 2 == 0, list_of_ints)))

# Printing the results
print(f"Filtered and squared numbers (map and filter): {filtered_squared_map_filter}")
```

# Key Features 🌟
- **List Comprehension**: Learn how to use list comprehensions for concise and efficient code.
- **Map Function**: Discover how to use the map function with both lambda and named functions.
- **Filtering**: Understand how to filter elements in a list before applying transformations.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `01_list_compr_map_lambda_filter.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `01_list_compr_map_lambda_filter.py`.
5. Run the script with: `python 01_list_compr_map_lambda_filter.py`.

## Usage Example 📋
Execute the script to see various methods to square numbers in a list. The script will demonstrate each method and print the results.

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
