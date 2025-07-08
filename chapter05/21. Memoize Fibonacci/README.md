# 🎯 Memoization in Python 🧠

This script demonstrates the use of memoization in Python to optimize the calculation of Fibonacci numbers. Memoization is a technique used to cache the results of expensive function calls and reuse them when the same inputs occur again, improving performance.

## Script Overview 📘

The script defines a memoization decorator that caches the results of the `fibonacci` function. This reduces the number of redundant calculations, making the computation of Fibonacci numbers more efficient.

### :computer: Script Code

```python
def memoize(func):
    """
    A simple memoization decorator to cache results of the function.
    """
    cache = {}
    
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for Fibonacci({n})")
        else:
            print(f"Calculating Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    # Using the decorated function to calculate Fibonacci numbers
    print([fibonacci(n) for n in range(10)]) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

if __name__ == '__main__':
    main()
```

## Key Features 🌟
- **Memoization**: Learn how to use a memoization decorator to cache function results and improve performance.
- **Fibonacci Calculation**: Understand the implementation of a recursive function to calculate Fibonacci numbers.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `21_memoize_fibonacci.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `21_memoize_fibonacci.py`.
5. Run the script with: `python 21_memoize_fibonacci.py`.

## Usage Example 📋
Execute the script to see how memoization optimizes the calculation of Fibonacci numbers. The script will print messages indicating cache hits and calculations, followed by the first 10 Fibonacci numbers.

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
