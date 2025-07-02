# 🔎 Filtering Even Numbers Script 🔢

Welcome to the Filtering Even Numbers Script! This script demonstrates how to filter even numbers from a list using a lambda function and the `filter` function.

## Script Overview 📘

The script defines a list of numbers and uses a lambda function with the `filter` function to create an iterator that filters out even numbers. It then demonstrates the behavior of the iterator and how to create a reusable list of even numbers.

### :computer: Script Code

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers (iterator)
even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)

print(even_numbers_iterator)
# print(*even_numbers_iterator)
# print(*even_numbers_iterator)

# Printing even numbers
for num in even_numbers_iterator:
    print(num, end=" ")

# Printing even numbers ???
for num in even_numbers_iterator:
    print(num, end=" ")

# Using filter and lambda to create a list of even numbers from the original list
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))

# Since even_numbers_list is already a list, you can directly reuse it
print("Repeated print of the even numbers list:")
print(even_numbers_list)
print(even_numbers_list)
```

## Key Features 🌟

- **Filtering with Lambda**: Learn how to filter elements in a list using a lambda function.
- **Iterator Behavior**: Discover how iterators work and how they can be exhausted after a single use.
- **Reusable Lists**: Understand how to create reusable lists from filtered results.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `14_filter_even_numbers.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `14_filter_even_numbers.py`.
5. Run the script with: `python 14_filter_even_numbers.py`.

## Usage Example 📋

Execute the script to see how to filter even numbers from a list using a lambda function. The script will demonstrate the behavior of iterators and how to create a reusable list of even numbers.

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
