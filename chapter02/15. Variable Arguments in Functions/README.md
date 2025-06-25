# 🔧 Python Function with Variable Arguments Demonstration ✨

Welcome to the Python Function with Variable Arguments Demonstration! This script showcases the use of the `*args` feature in Python to handle a variable number of arguments in a function. It’s a practical guide to writing flexible and reusable functions.

## Script Overview 📘

The script demonstrates:
- Using `*args` to pass a variable number of arguments to a function.
- Handling edge cases like no arguments provided.
- Joining arguments into a formatted string for output.

### 💻 Script Code

```python
def print_cities(*cities):
    # Check if any cities are provided
    if not cities:
        print("No cities provided")
    else:
        # Join and print the cities separated by commas
        print("Cities:", ", ".join(cities))

def main():
    # Example calls to print_cities
    print_cities("Athens", "London", "Paris")  # Cities: Athens, London, Paris
    print_cities("Athens")  # Single city
    print_cities()  # No cities provided

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Variable Arguments**: Learn how to use `*args` to handle an arbitrary number of arguments in a function.
- **Edge Case Handling**: Manage scenarios where no arguments are provided.
- **String Formatting**: Use `join` to create a clean and formatted string from a list of arguments.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `15_variable_args_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `15_variable_args_demo.py`.
5. Run the script with the command: `python 15_variable_args_demo.py`.

## Usage Example 📋

Executing the script demonstrates how to use `*args` to handle varying numbers of arguments. The outputs showcase examples of printing multiple cities, a single city, or handling cases where no arguments are provided.

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