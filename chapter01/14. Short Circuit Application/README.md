# 📥 Python Input Handling and Logical Operations Demo 📤

This README accompanies a Python script that demonstrates how to handle user input effectively and utilize logical operators to make dynamic variable assignments based on user input. This example is valuable for anyone learning how to interact with users through the command line and handle conditional logic in Python.

## Script Overview 📘

The script prompts the user for a username and email address, then uses logical operations to ensure that valid information is provided before proceeding. It illustrates the use of the `or` operator for providing default values and the `and` operator combined with `or` for creating context-specific user messages based on input validity.

### :computer: Script Code

```python
# Prompt the user to enter a username and store it in a variable
username = input(f"Enter your username: ")

# Prompt the user to enter an email address and store it in a variable
email = input("Enter your email: ")

# Using the 'or' logical operator to assign a fallback value
# If 'username' is truthy (non-empty), use it; otherwise, use the fallback value "User"
valid_user = username or "User"

# Repeat the operation to reinforce the example (this line could be omitted as it's redundant)
valid_user = username or "User"

# Use a combination of 'and' and 'or' to construct an output message
# 'email and f"your email is {email}"' evaluates to the email message if 'email' is non-empty
# If 'email' is empty, the expression after 'or' is used, asking for a valid email address
print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid email address.")))
```

## Key Features 🌟

- **User Input Handling**: Demonstrates the capturing and handling of user input.
- **Logical Operations for Validation**: Shows how to use `or` and `and` for input validation and message construction.
- **Dynamic User Feedback**: Provides immediate feedback based on the validity of the user's input.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `14_short_circuit_app.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `14_short_circuit_app.py`.
5. Run the script with: `python 14_short_circuit_app.py`.

## Usage Example 📋

Upon execution, the script will interact with the user, requesting username and email details, and based on the provided information, it will give appropriate feedback, emphasizing the importance of input validation in user interfaces.

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
