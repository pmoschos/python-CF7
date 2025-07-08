# ✨ Understanding Tuples and Mutability in Python 🔄

This script demonstrates the properties of tuples in Python and how the mutability of their elements can be leveraged. Tuples are unmodifiable, but if they contain mutable elements, those elements can be modified.

## Script Overview 📘

The script showcases the creation of tuples, attempts to modify immutable elements, and modifies mutable elements within a tuple. It also highlights how the IDs of the tuple elements change or remain the same before and after modification.

### :computer: Script Code

```python
def main():
    """
    Main function to demonstrate tuple properties and mutability of its elements.
    """
    # Creating a tuple
    g = 1, 2, 3, 5

    # Printing the type of g to show that it is a tuple
    print("Type of g:", type(g))  # Output: <class 'tuple'>

    # Tuple mutability test
    # Tuples are unmodifiable, but if they contain mutable elements, those elements can be changed.
    my_tuple = (1, 2, [3, "CF"], "Hello")

    # Attempt to change an unmodifiable element of the tuple (this will raise an error)
    try:
        my_tuple[2] = [1, 2, 3]
    except TypeError as e:
        print(f"Error: {e}")  # Output: 'tuple' object does not support item assignment

    # Accessing and printing the second element of the tuple
    print("Second element of my_tuple:", my_tuple[1])  # Output: 2

    # Printing the id and value of each item in the tuple before modification
    print("\nBefore modification:")
    for item in my_tuple:
        print(id(item), ":", item)

    # Modifying the first element of the list inside the tuple
    my_tuple[2][0] = 300

    # Printing the modified tuple
    print("\nAfter modification:")
    print("Modified my_tuple:", my_tuple)  # Output: (1, 2, [300, 'CF'], 'Hello')

    # Printing the id and value of each item in the tuple after modification
    print("\nIDs and values after modification:")
    for item in my_tuple:
        print(id(item), ":", item)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Tuple Properties**: Learn about the immutable nature of tuples in Python.
- **Mutability of Elements**: Understand how mutable elements within a tuple can be modified.
- **ID Tracking**: See how the IDs of tuple elements change or remain the same before and after modification.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `24_unmodifiable_tuples.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `24_unmodifiable_tuples.py`.
5. Run the script with: `python 24_unmodifiable_tuples.py`.

## Usage Example 📋
Execute the script to see how tuples behave with mutable and immutable elements. The script will demonstrate attempts to modify tuple elements and show the changes in IDs and values of the elements before and after modification.

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
