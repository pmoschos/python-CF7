# 📜 Simple Iterator Class in Python 🔄

This script demonstrates how to create a custom iterator class in Python. The `SimpleIterator` class allows iteration over a list of elements, providing a practical example of implementing the iterator protocol.

## Script Overview 📘

The script defines a `SimpleIterator` class with methods to initialize the iterator, return the iterator object itself, and return the next item from the data. It also includes a `main` function to demonstrate the usage of the iterator.

### :computer: Script Code

```python
class SimpleIterator:
    def __init__(self, data):
        """
        Initialize the iterator with the given data.

        Parameters:
        data (list): The list of elements to iterate over.
        """
        self.data = data
        self.index = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
        self (SimpleIterator): The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the data. Raise StopIteration when the data is exhausted.

        Returns:
        int/float/str: The next item from the data.

        Raises:
        StopIteration: When there are no more items to return.
        """
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def main():
    """
    Main function to demonstrate the usage of the SimpleIterator.
    """
    numbers = [10, 20, 30, 40, 50]

    # Create an instance of SimpleIterator
    iterator = SimpleIterator(numbers)

    # Use the iterator in a for loop
    for number in iterator:
        print(number)

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Custom Iterator Class**: Learn how to create a custom iterator class in Python.
- **Iterator Protocol**: Understand the iterator protocol with `__iter__` and `__next__` methods.
- **Iterable Objects**: See how to make objects iterable and use them in a `for` loop.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `12_simple_iterator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `12_simple_iterator.py`.
5. Run the script with: `python 12_simple_iterator.py`.

## Usage Example 📋
Execute the script to see how the `SimpleIterator` class works. The script will demonstrate iterating over a list of numbers using the custom iterator.

## 📢 Stay Updated
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
