# ✨ Factorial Iterator Script 🔢

This script demonstrates how to create a custom iterator class in Python to generate factorials up to a given number. The `FactoIterator` class implements the iterator protocol with `__iter__` and `__next__` methods.

## Script Overview 📘

The script defines a `FactoIterator` class that generates factorials up to a specified number. The `main` function demonstrates the usage of this iterator by generating factorials up to 5.

### :computer: Script Code

```python
class FactoIterator:
    """
    An iterator class that generates factorials up to a given number n.
    """
    def __init__(self, n):
        """
        Initialize the iterator with the given number n.
        
        Parameters:
        n (int): The number up to which factorials are generated.
        """
        self.n = n
        self.result = 1
        self.order = 1
    
    def __iter__(self):
        """
        Return the iterator object itself.
        
        Returns:
        self (FactoIterator): The iterator object itself.
        """
        return self
    
    def __next__(self):
        """
        Return the next factorial in the sequence.
        
        Returns:
        int: The next factorial in the sequence.
        
        Raises:
        StopIteration: When the sequence is complete.
        """
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result

def main():
    """
    Main function to demonstrate the usage of the FactoIterator.
    """
    # Create a FactoIterator object to generate factorials up to 5
    facto_iter = FactoIterator(5)

    # Get the first factorial using the next() function
    a = next(facto_iter)
    print(a)  # Expected output: 1 (1!)

    # Iterate through the remaining factorials using a for loop
    for factorial in facto_iter:
        print(factorial)

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
2. Save the script as `13_factorial_iterator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `13_factorial_iterator.py`.
5. Run the script with: `python 13_factorial_iterator.py`.

## Usage Example 📋
Execute the script to see how the `FactoIterator` class works. The script will demonstrate iterating over a sequence of factorials up to a given number.

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
