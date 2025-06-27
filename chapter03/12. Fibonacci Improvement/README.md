# ✨ Python Fibonacci Number Generator 🔄

Welcome to the Python Fibonacci Number Generator! This script calculates the nth Fibonacci number based on user input. It's an ideal resource for understanding sequence generation, loops, and user input handling in Python.

## Script Overview 📘

The script prompts the user to enter a non-negative integer \( n \) and calculates the nth Fibonacci number using an iterative approach.

### :computer: Script Code

```python
def fibonacci(n):
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return
    
    fib_number = fibonacci(n)
    
    print(f"The {n}th Fibonacci number is {fib_number}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Fibonacci Sequence**: Learn how to calculate the nth Fibonacci number using an iterative approach.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Loop and Sequence Generation**: Understand how to use loops to generate a sequence of numbers.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `12_fibonacci_improvement.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `12_fibonacci_improvement.py`.
5. Run the script with: `python 12_fibonacci_improvement.py`.

## Usage Example 📋

Execute the script and enter a non-negative integer when prompted. The script will calculate the nth Fibonacci number and print the result.

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
