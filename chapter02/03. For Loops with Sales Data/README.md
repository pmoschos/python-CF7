# 🔢 Python Loops and Range Demonstration ↔️

Welcome to the Python Loops and Range Demonstration! This script dives into the versatile `range` function and showcases a variety of loop constructs, including nested loops, control flow with `break` and `continue`, and `else` blocks. Additionally, it highlights conditional checks in lists, offering practical insights for Python developers.

## Script Overview 📘

The script provides examples of how to:
- Use the `range` function with various parameters.
- Implement basic loops, conditional loops, and nested loops.
- Utilize control flow statements (`break`, `continue`) effectively.
- Work with lists and conditional membership checks.

### 💻 Script Code

#### Part 1: Range and Loops

```python
# The range function returns an object of class range.
# range(10)
# It generates a sequence of numbers starting from 0 by default and increments by 1
a = range(10)
print(f"a : {a}")  # Output: a : range(0, 10)
print(f"type(a): {type(a)}")  # Output: type(a): <class 'range'>

# Basic loop from 0 to 9
print("Loop from 0 to 9:")
for i in range(10):
    print(i, end=' ')
print("\n")

# Loop with a start, stop, and step
print("Loop from 1 to 9 with step of 3:")
for i in range(1, 10, 3):
    print(i, end=' ')
print("\n")

# Loop with a break statement
print("Loop from 0 to 9, breaking at 5:")
for i in range(10):
    if i == 5:  # Breaks the loop when i equals 5
        break
    print(i, end=' ')
print("\n")

# Loop with a continue statement
print("Loop from 0 to 9, skipping 5:")
for i in range(10):
    if i == 5:  # Skips the iteration when i equals 5
        continue
    print(i, end=' ')
print("\n")

# Loop with a break statement and else block
print("Loop from 0 to 9, breaking at 5, with else block:")
for i in range(10):
    if i == 5:
        break  # Break prevents else block from running
    print(i, end=' ')
else:
    print("Loop ended normally")
print("\n")

# Loop with an else block executing after normal completion
print("Loop from 0 to 9, with else block (no break):")
for i in range(10):
    print(i, end=' ')
else:
    print("\nLoop ended normally")
print()

# Nested loops example
print("Nested loops example (multiplication table):")
for i in range(1, 4):  # Outer loop iterates over rows
    for j in range(1, 4):  # Inner loop iterates over columns
        print(f"{i} * {j} = {i * j}", end=' | ')
    print()
print()

# Using range with negative step
print("Loop from 10 to 1, decrementing by 2:")
for i in range(10, 0, -2):  # Negative step decrements the range
    print(i, end=' ')
print("\n")

# Demonstrating that a for loop does not have its own scope in Python
# Iterate over a range of numbers and print each number
for num in range(10):
    print(num, end=' ')
print("\n-----")

# The variable num is still accessible here, outside the for loop
print("After the loop, num is still accessible")
print(f"num = {num}")
```

#### Part 2: Conditional Checks in Lists

```python
# List of fruits:
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Banana"

for fruit in fruits:
    if fruit == fruit_to_check:  # Check if current fruit matches target
        print(f"{fruit_to_check} is in list")
        break
else:
    print(f"{fruit_to_check} is not in list")

print("Why do Python devs never get lost?")
print("Because they always know where 'in' is!")

# Using 'in' for a simpler membership check
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in list")
else:
    print(f"{fruit_to_check} is not in list")

# One-liner conditional check
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list!")
```

## Key Features 🌟

- **Range and Loops**: Master basic and advanced usage of the `range` function.
- **Control Flow**: Understand how `break`, `continue`, and `else` blocks enhance loops.
- **Nested Loops**: Learn how to work with loops inside loops for multi-dimensional operations.
- **Membership Checks**: Simplify checks for list elements using `in` and conditional statements.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `03_loops_and_conditions_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_loops_and_conditions_demo.py`.
5. Run the script with the command: `python 03_loops_and_conditions_demo.py`.

## Usage Example 📋

Executing the script provides a comprehensive walkthrough of various loop constructs and their applications. The output will include range demonstrations, conditional flows, nested loop multiplication tables, and membership checks in lists.

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>

