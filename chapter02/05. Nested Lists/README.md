# 🗂️ Python Nested List Demonstration 🛠️

Welcome to the Python Nested List Demonstration! This script introduces the concept of lists containing various data types, including nested lists, and demonstrates operations such as iteration and indexing. It’s a practical resource for exploring Python’s list handling capabilities.

## Script Overview 📘

The script demonstrates:
- How to iterate over a list containing multiple data types.
- Accessing elements in nested lists using indexing.
- Reversing slices of lists.
- Iterating over nested lists to find specific elements.

### 💻 Script Code

```python
# A list containing elements of various data types
items = [1, 2, 3.14, True, "Hello CF6 friends"]

# Iterating through the list and printing each item
for item in items:
    print(item, end=" ")
print()

# A nested list with sublists
nest_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Printing the entire nested list
print(f"nested list: {nest_list}")  # [[1, 2], [3, 4], [5, 6]]

# Accessing the first sublist in the nested list
print(f"first nested list: {nest_list[0]}")  # [1, 2]

# Accessing an element in the second sublist
print(f"first element of second nested list: {nest_list[1][0]}")  # 3

# Accessing and reversing slices of nested lists
print(f"first nested list: {nest_list[1]}, {nest_list[0]}")  # [3, 4], [1, 2]
print(f"first nested list: {nest_list[:2][::-1]}")  # [[3, 4], [1, 2]]

# Iterating over nested lists and finding the last even number
for outer_item in nest_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:  # Check if the number is even
            result = inner_item

# Printing the final even number found
print("Final even num:", result)
```

## Key Features 🌟

- **Dynamic Iteration**: Explore lists containing diverse data types.
- **Nested List Indexing**: Learn how to access sublists and their elements using indices.
- **List Slicing and Reversing**: Understand how to manipulate slices of lists, including reversing.
- **Multi-Level Iteration**: Traverse nested lists to process elements based on conditions.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `05_nested_list_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `05_nested_list_demo.py`.
5. Run the script with the command: `python 05_nested_list_demo.py`.

## Usage Example 📋

Executing the script demonstrates how to work with lists and nested lists effectively. It outputs the elements of the main list, showcases nested list indexing, and identifies the last even number within a nested list.

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

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

