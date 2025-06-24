# 📋 Python List Operations Demonstration 🔄

Welcome to the Python List Operations Demonstration! This script covers essential operations for manipulating Python lists, such as adding, updating, deleting, and searching for elements. It’s a comprehensive guide for mastering Python’s list methods.

## Script Overview 📘

The script demonstrates:
- How to populate a list.
- Adding single or multiple elements.
- Inserting and updating elements.
- Deleting elements by value or position.
- Searching for elements within a list.

### 💻 Script Code

```python
# Populate a list with initial values
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add a single element at the end of the list
fruits.append("Berry")
print("After adding Berry:", fruits)

# Add multiple elements at the end of the list
fruits.extend(["Grapes", "Fig"])
print("After adding Grapes and Fig:", fruits)

# Insert an element at a specific position
fruits.insert(1, "Coconut")  # Insert Coconut at position 1
print("After inserting Coconut at position 1:", fruits)

# Update the first element
fruits[0] = "Melon"
print("After updating the first element to Melon:", fruits)

# Update a slice of the list (two elements)
fruits[1:3] = ["A"]  # Replace elements at index 1 and 2
print("After updating two elements:", fruits)

# Delete an element by position using pop()
removed_item = fruits.pop(1)  # Remove the second element
print(f"Removed item: {removed_item}")
print("List after removal:", fruits)

# Delete an element by value using remove()
fruits.remove("Cherry")  # Remove the first occurrence of "Cherry"
print("List after removing Cherry:", fruits)

# Check if a removed item exists in the list
if "Cherry" in fruits:
    print("Cherry still exists in the list")
else:
    print("Cherry doesn't exist in the list")

# Search for an element in the list and get its position
pos = fruits.index("Berry")
print(f"'Berry' is at position {pos} in the list.")
```

## Key Features 🌟

- **Adding Elements**: Learn how to use `append` and `extend` to grow your list.
- **Inserting Elements**: Understand how to place elements at specific positions using `insert`.
- **Updating Elements**: Modify single or multiple elements in a list.
- **Deleting Elements**: Explore `pop` and `remove` for removing elements by position or value.
- **Searching**: Use `index` to find the position of an element.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `06_list_operations_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `06_list_operations_demo.py`.
5. Run the script with the command: `python 06_list_operations_demo.py`.

## Usage Example 📋

Executing the script demonstrates various list operations step-by-step, with outputs showcasing the state of the list after each modification. It’s an excellent way to gain hands-on experience with Python’s list methods.

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