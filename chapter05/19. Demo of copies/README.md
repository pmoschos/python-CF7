# 🛠️ Deep and Shallow Copy Demonstration in Python 🔄

This script demonstrates the differences between shallow and deep copies in Python. By using various methods to copy a list, including both shallow and deep copying, we can observe how modifications to the original list affect its copies.

## Script Overview 📘

The script creates an original list containing nested lists and demonstrates four methods to copy it: shallow copy using slicing, shallow copy using the `copy` method, shallow copy using the `list` constructor, and deep copy using the `copy` module. The effects of modifying the original list on its copies are then observed.

### :computer: Script Code

```python
import copy

def main():
    ages = [1, [2, 3, 4], 5]  # Original list with nested list

    # Method 1: Shallow copy using list slicing
    ages_slice = ages[:]
    # Method 2: Shallow copy using the list's copy method
    ages_cp = ages.copy()
    # Method 3: Shallow copy using the list constructor
    ages_list = list(ages)
    # Method 4: Deep copy using the 'copy' module
    ages_dcp = copy.deepcopy(ages)

    # Print the original list and its copies before modification
    print("Original list:", ages)
    print("Shallow copy (slicing):", ages_slice)
    print("Shallow copy (copy method):", ages_cp)
    print("Shallow copy (list constructor):", ages_list)
    print("Deep copy:", ages_dcp)

    # Modify the original list
    ages[0] = 100  # Change a non-nested element
    ages[1][0] = 200  # Change a nested element

    # Print the original list and its copies after modification
    print("\nAfter modifying the original list:")
    print("Original list:", ages)
    print("Shallow copy (slicing, nested list should change):", ages_slice)
    print("Shallow copy (copy method, nested list should change):", ages_cp)
    print("Shallow copy (list constructor, nested list should change):", ages_list)
    print("Deep copy (should not change):", ages_dcp)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Shallow Copy**: Learn how to create shallow copies using slicing, the `copy` method, and the `list` constructor.
- **Deep Copy**: Understand how to create deep copies using the `copy` module.
- **Modification Effects**: Observe how modifications to the original list affect shallow and deep copies differently.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, except the built-in `copy` module

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `19_demo_of_copies.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `19_demo_of_copies.py`.
5. Run the script with: `python 19_demo_of_copies.py`.

## Usage Example 📋
Execute the script to see how different copying methods work. The script will print the original list and its copies before and after modifying the original list, highlighting the differences between shallow and deep copies.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
