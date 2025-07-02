# 🗂️ Python List Shallow Copy Script 📋

Welcome to the Python List Shallow Copy Script! This script demonstrates how to create a shallow copy of a list and how changes to the original list affect the copied list.

## Script Overview 📘

The script defines an original list with mixed data types, including a nested list. It then creates a shallow copy of this list and demonstrates the effects of modifying elements in the original list on the shallow copy.

### :computer: Script Code

```python
# Define the original list with mixed data types including a nested list
my_list = [1, 2, "Hello", [3, 4, 5]]

# Create a shallow copy of the original list using list slicing
new_list = my_list[:]
print("Are new_list and my_list the same object:", new_list is my_list)

# Modify an immutable element (integer) in the original list
my_list[0] = 100
print("Original list after changing the first element to 100:", my_list)
print("Shallow copy after changing the first element in the original list:", new_list)
print("------------------------------------------------------------------------------------")

# Modify a mutable element (nested list) in the original list
my_list[3][0] = 300
print("Original list after modifying nested list:", my_list)
print("Shallow copy after modifying nested list in the original list:", new_list)
```

## Key Features 🌟

- **List Shallow Copy**: Learn how to create a shallow copy of a list using list slicing in Python.
- **Immutable vs Mutable Elements**: Discover how changes to immutable and mutable elements in the original list affect the shallow copy.
- **Nested Lists**: Understand the impact of modifying nested lists on both the original and copied lists.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `06_list_shallow_copy.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `06_list_shallow_copy.py`.
5. Run the script with: `python 06_list_shallow_copy.py`.

## Usage Example 📋

Execute the script to see how creating a shallow copy of a list and modifying elements in the original list affects the shallow copy. The script will demonstrate these operations by printing the original and copied lists before and after modifications.

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