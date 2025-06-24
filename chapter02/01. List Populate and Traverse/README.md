# 📋 Python List CRUD Functions Demonstration 🔄

Welcome to the Python List CRUD Functions Demonstration! This script showcases various methods for manipulating lists in Python, including creating, reading, updating, and deleting elements. It’s an excellent guide for newcomers to Python or educators teaching fundamental list operations.

## Script Overview 📘

The script demonstrates how to populate a list, iterate over it to read values and indices, and emphasizes the behavior of loop variables in Python.

### 💻 Script Code

```python
# Populate a list
ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

# Read: Iterating over a list and accessing both the index and the value
print("\nIterating with index and value:")
for index, value in enumerate(ages):  # (index, value)
    print(f"Index: {index}, Value: {value}")

# Iterating with enhanced for loop
print("\nIterating with enhanced for loop:")
for age in ages:
    print(age, end=" ")
print()

# Python's loop variables persist after the loop ends
print(f"\nVariable 'age' after the loop: {age}")
```

## Key Features 🌟

- **List Creation**: Understand how to initialize and populate lists in Python.
- **List Reading**: Learn different methods for iterating over lists while accessing indices and values.
- **Variable Scope in Loops**: Observe how Python handles loop variables and their persistence outside the loop.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `01_list_populate_traverse.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `01_list_populate_traverse.py`.
5. Run the script with the command: `python 01_list_populate_traverse.py`.

## Usage Example 📋

Running the script demonstrates various list operations, helping you explore and understand their functionality. The output will include initial list population, iteration examples, and more, offering hands-on learning about Python list operations.

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