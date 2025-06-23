# 🗣️ Python User Interaction and Data Conversion Demo 🔄

This README describes a Python script that prompts the user for personal information like name, age, height, and student status. It then processes and displays this data to provide personalized feedback based on the user's input. This example is perfect for beginners to understand user input handling, data type conversion, and basic control structures in Python.

## Script Overview 📘

The script guides the user through a series of input prompts to gather personal details and then uses conditional logic to customize the output based on whether the user identifies as a student. It also demonstrates the importance of immediate data type conversion during input to prevent type errors later in the script.

### :computer: Script Code

```python
# Request the user's name and store it in a variable
name = input("Please enter your name: ")

# Request the user's age, converting the input directly to an integer
age = int(input("Please enter your age: "))

# Request the user's height in meters, converting the input directly to a float for precision
height = float(input("Please enter your height in meters: "))

# Request a yes/no answer to determine if the user is a student, converting to lowercase and comparing to 'yes'
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

# Print a formatted greeting using the user's name
print("\nHello, {}!".format(name))

# Condition to check if the user is a student and print the corresponding status
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")
    
# Print the user's age and height, formatting the height to two decimal places
print("Your age is {}, and your height is {:.2f} meters.".format(age, height))
```

## Key Features 🌟

- **User Input**: Interactively collects data from users via console input.
- **Data Type Conversion**: Converts input data to appropriate numeric types and text immediately upon input.
- **Conditional Logic**: Uses simple if-else conditions to personalize output.
- **Formatted Output**: Provides personalized feedback that is formatted for readability.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `06_input_demo.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `06_input_demo.py`.
5. Run the script with: `python 06_input_demo.py`.

## Usage Example 📋

Upon execution, the script will prompt the user to input their name, age, height, and student status. After input, it will personalize the output based on the provided data, showing a tailored greeting and information summary.

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
