# 📇 Department ID Generator Script 🆔

Welcome to the Department ID Generator Script! This script demonstrates how to generate unique IDs for students based on their department using nested functions and nonlocal variables.

## Script Overview 📘

The script defines a `department_id_generator` function that creates a unique ID generator for a specified department. It uses a nested function to increment and format the IDs. The `main` function creates ID generators for different departments and demonstrates their usage.

### :computer: Script Code

```python
def department_id_generator(department):
    """
    Generate unique IDs for students based on department.

    Parameters:
    department (str): The name of the department.

    Returns:
    function: A function that generates unique IDs for the given department.
    """
    last_id = 0  # Initialize the last_id to zero

    def generate_id():
        """
        Generate a unique ID for a student in the department.

        Returns:
        tuple: A tuple containing the unique ID as a string and the last_id as an integer.
        """
        nonlocal last_id  # Declare last_id as nonlocal to modify it within the nested function
        last_id += 1  # Increment the last_id
        return f"{department}-{last_id}", last_id  # Return the formatted ID and last_id
    
    return generate_id  # Return the nested function

def main():
    # Create ID generators for Python and Android departments
    python_id_gen = department_id_generator("Python")
    android_id_gen = department_id_generator("Android")

    # Generate and print IDs using the Python ID generator
    print(python_id_gen())  # Expected output: ('Python-1', 1)
    print(python_id_gen())  # Expected output: ('Python-2', 2)

    # Generate and print IDs using the Android ID generator
    print(android_id_gen())  # Expected output: ('Android-1', 1)

    # Generate and print another ID using the Python ID generator
    print(python_id_gen())  # Expected output: ('Python-3', 3)

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Reduce Function**: Learn how to use the reduce function to aggregate all elements in a range.
- **Lambda Function**: Discover how to define and use lambda functions for concise and readable code.
- **Factorial Calculation**: Understand how to calculate the factorial of a given integer using the reduce function and handle intermediate results.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses the built-in functools module)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `04_closure.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_closure.py`.
5. Run the script with: `python 04_closure.py`.

## Usage Example 📋
Execute the script to see how the reduce function can be used to calculate the factorial of a given integer. The script will demonstrate this operation and print both the intermediate and final results.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
