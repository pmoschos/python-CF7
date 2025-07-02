# 📜 Python Generic Functions Script 🖋️

Welcome to the Python Generic Functions Script! This script demonstrates the use of generic functions with type annotations, providing a robust way to work with sequences and other types in Python.

## Script Overview 📘

The script includes several generic functions to handle sequences and various types. It also demonstrates the usage of these functions with different data types and scenarios.

### :computer: Script Code

```python
from typing import Sequence, TypeVar, List, Any, Optional

# Declare Generic Type Variable
T = TypeVar('T')

# More descriptive TypeVar names based on the intended type constraints
Number = TypeVar('Number', int, float)  # Used for numbers

# Generic function to get the first element of a sequence
def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence.
    If the sequence is empty, raises a ValueError.

    Args:
    seq (Sequence[T]): The sequence from which to get the first element.

    Returns:
    T: The first element of the sequence.
    """
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[0]

# Generic function to get the last element of a sequence
def last(seq: Sequence[T]) -> T:
    """
    Returns the last element of a sequence.
    If the sequence is empty, raises a ValueError.

    Args:
    seq (Sequence[T]): The sequence from which to get the last element.

    Returns:
    T: The last element of the sequence.
    """
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[-1]

def count_truthy(elements: List[Any]) -> int:
    """
    Counts how many elements in the list are truthy.

    Args:
    elements (List[Any]): A list of elements.

    Returns:
    int: The count of truthy elements in the list.
    """
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    """
    Returns the length of a string. Returns 0 if the string is None.

    Args:
    s (Optional[str]): The string or None.

    Returns:
    int: The length of the string, or 0 if None.
    """
    return len(s) if s is not None else 0

def main() -> None:
    # Demonstrate first and last functions
    numbers = [10, 20, 30, 40, 50]
    print("First number:", first(numbers))
    print("Last number:", last(numbers))

    try:
        print("First in empty list:", first([]))  # Should raise an error
    except ValueError as e:
        print(e)

    # Demonstrate count_truthy function
    mixed_values = [0, True, False, 'hello', '', None, 22]
    print("Truthy count:", count_truthy(mixed_values))

    # Demonstrate len_str function
    print("Length of 'hello world':", len_str("hello world"))
    print("Length of None:", len_str(None))

    # Incorrect usage: Passing a string where a sequence of numbers or similar type expected
    words = "This is a test string"
    print("First character (expected to pass):", first(words))  # This is fine as strings are sequences

    # ERROR: Argument 1 to "first" has incompatible type "int"; expected "Sequence[Never]"  [arg-type]
    # print("First element using an int (expected to fail):", first(123))  # This should cause a type error

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Generic Functions**: Learn how to create and use generic functions to handle various data types.
- **Type Annotations**: Discover how to use type annotations to specify expected types and ensure type safety.
- **Error Handling**: Understand how to raise and handle exceptions in Python functions.

## Technical Requirements 🔧

- **Python Version**: Python 3.10 or higher is recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.10 or higher is installed on your machine.
2. Save the script as `02_generic_functions.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `02_generic_functions.py`.
5. Run the script with: `python 02_generic_functions.py`.

## Usage Example 📋

Execute the script to see generic functions in action. The script will demonstrate correct usage, error handling, and display function annotations and documentation.

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