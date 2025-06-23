# 🔢 Python Integer Range Display Demo ↔️

This README accompanies a Python script that demonstrates how to retrieve and display the maximum and minimum integer values in Python using the `sys` module. This is particularly useful for understanding the capabilities and limitations of integer handling in different system architectures (32-bit vs 64-bit).

## Script Overview 📘

The script uses the `sys.maxsize` attribute to determine the maximum integer value the system can handle, which reflects the integer size that Python's `int` type can manage without overflow on a given platform.

### :computer: Script Code

```python
import sys

# Largest integer 
max_int = sys.maxsize
print("Max int:", max_int)

# Smallest integer 
min_int = -sys.maxsize - 1
print("Min int:", min_int)

# For a 64-bit system, you would get:
# Max size: 9223372036854775807
# Max int: 9223372036854775807
# Min int: -9223372036854775808

# For a 32-bit system, you would get:
# Max size: 2147483647
# Max int: 2147483647
# Min int: -2147483648
```

## Key Features 🌟

- **System Architecture Awareness**: Shows differences in integer sizes between 32-bit and 64-bit systems.
- **Practical Use of `sys` Module**: Utilizes the system-specific parameters to determine data types' limits.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `07_min_max_int.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `07_min_max_int.py`.
5. Run the script with: `python 07_min_max_int.py`.

## Usage Example 📋

Upon execution, the script will display the maximum and minimum integer values for the system, providing insight into the data type limits influenced by system architecture.

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
