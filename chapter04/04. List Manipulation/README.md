# 🔄 Python List Manipulation Script 🛠️

Welcome to the Python List Manipulation Script! This script demonstrates how to manipulate lists in Python, including appending elements to a list and handling lists with mixed data types.

## Script Overview 📘

The script defines a function `append_to_list` that appends an element to a given list. It also shows how to handle lists containing elements of various types, including other lists.

### :computer: Script Code

```python
from typing import List, Any

# Define a list containing elements of mixed types, including another list
my_list = [1, 2, "Hello", [3, 4, 5]]

def append_to_list(li: List[Any], element: Any) -> None:
    """
    Appends an element to the provided list.

    Parameters:
    li (List[Any]): The list to which the element will be appended.
    element (Any): The element to append to the list.
    """
    # Append the specified element to the list
    li.append(element)

# Call the function to append "CF" to 'my_list'
append_to_list(my_list, "CF")

# Iterate through each item in the list and print it
for item in my_list:
    print(item, end=", ")  # Output each element of the list
print()
```

## Key Features 🌟

- **List Manipulation**: Learn how to append elements to a list in Python.
- **Mixed Data Types**: Discover how to handle lists containing elements of various data types, including nested lists.
- **Function Definition**: Understand how to define and use functions with type annotations to manipulate lists.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `04_list_manipulation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_list_manipulation.py`.
5. Run the script with: `python 04_list_manipulation.py`.

## Usage Example 📋

Execute the script to see how to append elements to a list and handle lists with mixed data types. The script will demonstrate these operations by printing each element of the modified list.

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