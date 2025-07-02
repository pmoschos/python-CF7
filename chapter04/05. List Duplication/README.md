# ✏️ Python List Duplication and Modification Script 📝

Welcome to the Python List Duplication and Modification Script! This script demonstrates how list duplication works in Python and how modifying elements affects the original and duplicated lists.

## Script Overview 📘

The script initializes a list with mixed data types, including a nested list. It then demonstrates how duplicating and modifying the list affects its elements and their memory addresses.

### :computer: Script Code

```python
# Initialize a list with mixed types, including a nested list
my_list = [1, 2, "Hello", [3, 4, 5]]

# Print each item in the new list and its memory address
# This helps to understand which items are the same objects (sharing the same memory address)
print("At the start:")
for item in my_list:
    print(f"{item} : {id(item)}")

# Create a new list by repeating the original list twice
new_list = my_list * 2
print("\nDuplicated list:", new_list)
print("---------------")

# Modify the first element of the new list
new_list[0] = 100
print("\nModified first element of new_list:", new_list)
print("---------------")

# Modify an element within the nested list inside new_list
# This shows how changes to mutable objects inside lists affect all references
new_list[3][0] = 300
print("\nModified nested list within new_list:", new_list)
print("---------------")

# Print each item in the new list and its memory address
# This helps to understand which items are the same objects (sharing the same memory address)
print("\nAt the end:")
for item in new_list:
    print(f"{item} : {id(item)}")
```

## Key Features 🌟

- **List Duplication**: Learn how to duplicate lists using the `*` operator in Python.
- **Element Modification**: Discover how modifying elements in a list affects the original and duplicated lists.
- **Memory Address Printing**: Understand how to print memory addresses of list elements to identify shared objects.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `05_list_duplication.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `05_list_duplication.py`.
5. Run the script with: `python 05_list_duplication.py`.

## Usage Example 📋

Execute the script to see how list duplication and element modification work in Python. The script will demonstrate these operations by printing each element of the original and modified lists along with their memory addresses.

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