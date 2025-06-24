# 📖 Python Dictionary CRUD Functions Demonstration 🔍

Welcome to the Python Dictionary CRUD Functions Demonstration! This script showcases various methods for manipulating dictionaries in Python, including creating, reading, updating, and deleting elements. It's an ideal resource for anyone new to Python or those teaching programming concepts related to dictionary operations.

## Script Overview 📘

The script demonstrates how to populate a dictionary, access elements by key, handle safe deletion, and iterate through dictionary elements. This provides a comprehensive look at dictionary management techniques in Python.

### :computer: Script Code

```python
# Dictionary CRUD functions

# Initial dictionary of products
products = {1: "apples", 2: "bananas", 10: "honey", 3: "melons"}
print("Initial products:", products)

# Create: Insert a new item
products[3] = "oranges"
print("\nAfter inserting key 3 with value 'oranges':", products)

# Read: Access elements by key
product_10 = products.get(10, "Not Found")
print("\nProduct with key 10:", product_10)

# Update: Change the value of an existing item
products[2] = "milk"
print("\nAfter updating key 2 to 'milk':", products)

# Delete: Remove an item by key using del
del products[1]
print("\nAfter deleting key 1:", products)

# Delete: Remove an item by key using pop() and handle potential KeyError
removed_product = products.pop(3, "Not Found")
print("\nAfter popping key 3:", products)
print("Popped product:", removed_product)

# Delete: Remove the last inserted item using popitem()
key, value = products.popitem()
print("\nAfter popping the last item inserted:", products)
print(f"Popped item - Key: {key}, Value: {value}")

# Check for key existence
key_to_check = 2
if key_to_check in products:
    print(f"\nKey {key_to_check} exists in products.")
else:
    print(f"\nKey {key_to_check} does not exist in products.")

# Iterating through keys
print("\nIterating through keys:")
for key in products.keys():
    print(f"Key: {key}, Value: {products[key]}")

# Iterating through values
print("\nIterating through values:")
for value in products.values():
    print(f"Value: {value}")

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in products.items():
    print(f"Key: {key}, Value: {value}")
```

## Key Features 🌟
- **Dictionary Creation and Modification**: Learn how to initialize and modify dictionaries in Python.
- **Safe Element Access and Removal**: Understand different methods for safely accessing and removing elements from dictionaries.
- **Iterating Over Dictionaries**: Discover techniques for iterating over keys, values, and key-value pairs in dictionaries.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `09_dictionary_crud_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `09_dictionary_crud_demo.py`.
5. Run the script with: `python 09_dictionary_crud_demo.py`.

## Usage Example 📋
Execute the script to see how various dictionary operations are performed in the console. This will help you understand the practical applications of dictionary manipulation in Python programming.

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