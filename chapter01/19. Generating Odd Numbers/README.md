# 📏 Python Range Demonstration ➡️

Welcome to the Python Range Demonstration! This script demonstrates the efficiency of the `range()` function in Python for generating sequences of numbers, specifically showing how to generate odd numbers efficiently compared to a more traditional approach.

## Script Overview 📘

The script contrasts two methods for generating odd numbers up to 21:
1. A traditional Java-like style that checks each number.
2. A Python-optimized style using `range()` with step increments.

### :computer: Script Code

```python
# Python 2 vs Python 3 range functionality discussion
# Python 2: `range()` returned a list, not memory efficient
# Python 3: `range()` returns a range object, which is much more memory efficient

# Print odd numbers from 1 to 21 using a traditional Java-style approach in Python
print("Java style")
for i in range(22):
    if i % 2 != 0:
        print(i, end=' ')
print()

# Print odd numbers from 1 to 21 using Python's efficient range with step parameter
print("Python style")
for i in range(1, 22, 2):
    print(i, end=' ')
print()
```

## Key Features 🌟

- **Java Style vs Python Style**: Compare the traditional loop-and-check method with Python's efficient range stepping.
- **Efficiency of Python's `range()`**: Understand how Python's `range()` can be used to simplify code and improve memory usage when iterating over large ranges.
- **Odd Number Generation**: Learn a specific use case of `range()` for generating odd numbers effectively.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `19_odd_numbers_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `19_odd_numbers_demo.py`.
5. Run the script with: `python 19_odd_numbers_demo.py`.

## Usage Example 📋

Execute the script to observe how each approach outputs odd numbers up to 21 in the console. This will help you grasp the practical applications of efficient number generation in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

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