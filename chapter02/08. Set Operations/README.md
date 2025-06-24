# 🛠️ Python Set Operations Demonstration 🔄

Welcome to the Python Set Operations Demonstration! This script showcases various methods for manipulating sets in Python, including adding items, avoiding duplicates, handling errors during item removal, and iterating over sets. It's an ideal resource for anyone new to Python or those teaching programming concepts related to set operations.

## Script Overview 📘

The script begins by creating a set with duplicate items to demonstrate automatic duplicate removal. It then proceeds through adding items to the set, attempting to remove an item safely by checking its presence first, and iterating through the set to display its contents.

### :computer: Script Code

```python
# Set demo with items in a bag
bag = {"eggs", "apples", "bananas", "eggs"}  # Duplicate "eggs" will be automatically removed
print("Initial bag contents:", bag)

# Add a new item to the set
bag.add("oranges")
print("\nAfter adding 'oranges':", bag)

bag.add("oranges")
print("\nAfter second adding 'oranges':", bag)

# Attempt to remove an item that may not be in the set
item_to_remove = "eggs2"
# bag.remove(item_to_remove) # KeyError

if item_to_remove in bag:
    bag.remove(item_to_remove)
else:
    print(f"\n'{item_to_remove}' not found in the bag.")

# Iterate through the set
print("\nIterating through the bag:")
for item in bag:
    print(item)
```

## Key Features 🌟
- **Set Creation and Automatic Duplicate Removal**: Learn how sets automatically handle duplicates and how to initialize them.
- **Safe Item Removal**: Understand how to safely remove items from a set without causing errors.
- **Iterating Over Sets**: Discover methods for iterating over set items effectively.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `08_set_operations_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `08_set_operations_demo.py`.
5. Run the script with: `python 08_set_operations_demo.py`.

## Usage Example 📋
Execute the script to see how set operations are performed in the console. This will help you understand the practical applications of set management in Python programming, particularly in situations where item uniqueness is crucial.

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