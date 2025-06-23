# 🔄 Python Logical Operators Demo 🤔

This README accompanies a Python script that demonstrates the use of logical operators `or` and `and` for variable assignment and conditional checking. This example is crucial for understanding control flow mechanisms and decision-making processes in programming.

## Script Overview 📘

The script utilizes logical operators to perform conditional assignments and checks, showcasing how to simplify code logic and make variable assignments based on conditions. It demonstrates efficient ways to handle variables that might not always contain data and how to verify the presence of valid data before proceeding.

### :computer: Script Code

```python
# Define a string variable for the name
name = "Bob"

# Demonstrate the use of the `or` logical operator for variable assignment
print("====== or ======")
# Use `or` to assign "User" to valid_user if the left-hand side (None in this case) is falsy
valid_user = None or "User"
# Output: Hello User
print("Hello", valid_user)
print()

# If `name` has a truthy value, it will be assigned to valid_user; otherwise, "User" would be assigned
valid_user = name or "User"
# Output: Hello Bob
print("Hello", valid_user)
print()

# Demonstrate the use of the `and` logical operator for conditional checking
print("====== and ======")

# Define a string variable for the email
email = "bob@example.com"
# Use `and` to check that email is not empty and assign the email to valid_email if it's true
valid_email = email and email != ""
# Output: Valid Email: bob@example.com
print("Valid Email:", valid_email)

# EXTRA: Conditional output based on the value of valid_email
if valid_email:
    # If valid_email is truthy, print a greeting and the email address
    print(f"Hello {valid_user}, your email is {email}")
else:
    # If valid_email is falsy, prompt the user to provide a valid email address
    print(f"Hello {valid_user}, please provide a valid email address.")
```

## Key Features 🌟

- **Logical Operators**: Teaches the practical use of `or` and `and` for making decisions in code.
- **Conditional Assignment**: Shows how to assign values to variables based on conditions, enhancing code readability and efficiency.
- **Data Validation**: Demonstrates methods for ensuring the validity of data before use, which is crucial in preventing errors in applications.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `13_short_circuit_demo.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `13_short_circuit_demo.py`.
5. Run the script with: `python 13_short_circuit_demo.py`.

## Usage Example 📋

Upon execution, the script will display various outcomes based on logical evaluations, illustrating their utility in everyday programming tasks.

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
