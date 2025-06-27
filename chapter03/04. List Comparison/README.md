# 🔄 Python List Comparison Demonstration 📋

Welcome to the Python List Comparison Demonstration! This script compares two lists for identity and equality. It's an ideal resource for anyone new to Python or those teaching programming concepts related to object identity and equality.

## Script Overview 📘

The script defines two lists, compares them for identity (whether they are the same object) and equality (whether they have the same contents), and prints the results.

### :computer: Script Code

```python
def compare_lists(list1, list2):
    """
    Compares two lists for identity and equality.

    Args:
    list1 (list): The first list to compare.
    list2 (list): The second list to compare.

    Returns:
    None
    """
    # Check if the lists are the same object (identity)
    print(f"{list1} is {list2}: {list1 is list2}")

    # Check if the lists have the same contents (equality)
    print(f"{list1} == {list2}: {list1 == list2}")

def main():

    # Hint: when I have not overloaded the magic method for equality (__eq__()) 
    # then with == they are compared using their id's (identity)

    # Define the lists
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    # Compare the lists
    compare_lists(my_list, your_list)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Object Identity**: Learn how to check if two lists are the same object using the `is` keyword.
- **Equality Check**: Understand how to check if two lists have the same contents using the `==` operator.
- **Function Usage**: Discover how to define and use functions in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `04_list_comparison_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_list_comparison_demo.py`.
5. Run the script with: `python 04_list_comparison_demo.py`.

## Usage Example 📋

Execute the script to compare two lists for identity and equality, and observe the printed results to understand how Python handles object identity and equality checks.

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
