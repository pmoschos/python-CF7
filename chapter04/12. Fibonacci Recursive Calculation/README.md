# 🔄 Fibonacci Sequence Calculation Script 🌀

Welcome to the Fibonacci Sequence Calculation Script! This script demonstrates how to calculate the nth Fibonacci number using a recursive approach.

## Script Overview 📘

The script defines a function `fibo` that calculates the nth Fibonacci number using recursion. It includes base cases for `Fibonacci(0) = 0` and `Fibonacci(1) = 1`, and uses the recursive relationship `Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)` for `n > 1`.

### :computer: Script Code

```python
# Fibonacci sequence
#
# Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# Fibonacci(0) = 0
# Fibonacci(1) = 1

def fibo(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    
    Args:
    n (int): The position in the Fibonacci sequence to calculate.
    
    Returns:
    int: The nth Fibonacci number.
    
    Comments:
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.
    """
    # Base cases: fibo(0) = 0, fibo(1) = 1
    if n in (0, 1):
        return n
    # Recursive case: fibo(n) = fibo(n-1) + fibo(n-2)
    return fibo(n - 1) + fibo(n - 2)

def main():
    # Get user input for the value of n
    n = int(input("Enter a positive integer to find its Fibonacci number: "))
    print(f"fibo({n}) = {fibo(n)}")

if __name__ == '__main__':
    main()
```

## Key Features 🌟

- **Recursive Calculation**: Learn how to calculate the nth Fibonacci number using recursion.
- **Base Cases Handling**: Understand how to handle base cases in a recursive function.
- **User Input**: Discover how to capture and process user input in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `12_fibonacci_rec_calculation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `12_fibonacci_rec_calculation.py`.
5. Run the script with: `python 12_fibonacci_rec_calculation.py`.

## Usage Example 📋

Execute the script and enter a positive integer when prompted. The script will calculate the Fibonacci number at the given position and display the result.

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
