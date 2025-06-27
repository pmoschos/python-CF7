# 🌀 Python Fibonacci Number Calculation 🔄

Welcome to the Python Fibonacci Number Calculation script! This script calculates the nth Fibonacci number based on user input. It's an ideal resource for understanding loops, sequence generation, and user input handling in Python.

## Script Overview 📘

The script prompts the user to enter an integer \( n \) and calculates the nth Fibonacci number using an iterative approach.

### :computer: Script Code

```python
def main():
    # Prompt the user to input an integer and convert it to an int
    n = int(input("Please insert an int: "))

    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1

    # Iterate from 2 to n to calculate the nth Fibonacci number
    for i in range(2, n + 1):
        # Store the current value of 'a' in a temporary variable
        temp = a
        # Update 'a' to be the value of 'b'
        a = b
        # Update 'b' to be the sum of the old 'a' (now in 'temp') and 'b'
        b = temp + b

    # Print the nth Fibonacci number
    print(f"The {n}th Fibonacci number is {b}")

# If this script is being run directly (as opposed to being imported as a module),
# call the main function
if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Fibonacci Sequence**: Learn how to calculate the nth Fibonacci number using an iterative approach.
- **User Input Handling**: Discover how to capture and use user input in Python.
- **Loop and Sequence Generation**: Understand how to use loops to generate a sequence of numbers.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `11_fibonacci_calculator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `11_fibonacci_calculator.py`.
5. Run the script with: `python 11_fibonacci_calculator.py`.

## Usage Example 📋

Execute the script and enter a positive integer when prompted. The script will calculate the nth Fibonacci number and print the result.

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
