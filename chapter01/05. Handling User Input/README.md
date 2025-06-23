
# 🗣️ Python User Interaction and Data Conversion Demo 🔄

This README describes a Python script that prompts the user for personal information like name, year of birth, and height, and then uses this data to perform and display calculations such as the user's age and height in meters. This example is great for beginners to understand user input handling, data type conversion, and basic arithmetic operations in Python.

## Script Overview 📘

The script guides the user through a sequence of input prompts to gather personal details and then processes these details to calculate and display the user's age and height in a more user-friendly format. It emphasizes the importance of correctly handling different data types and providing a responsive user interface.

### :computer: Script Code

```python
# Request user's name via input and store it in a variable
name = input("Please enter your name: ")
# Print a personalized greeting using the inputted name
print("Hello, " + name + "!")

# Request user's year of birth and convert it directly to an integer
# This prevents type conversion errors later in the code
year_of_birth = int(input("Please enter the year of your birth: "))

# Calculate and print the user's age using the current year minus the year of birth
# The conversion to int was originally done after input, which is now refactored to be immediate
print("You are", 2024 - year_of_birth, "years old.")   

# Request the user's height in centimeters and convert it to a float for precision
height = float(input("Please enter your height in cm: "))
# Convert height from centimeters to meters and print it
print("You are", height / 100, "meters tall")
```

## Key Features 🌟

- **User Input**: Collects user data interactively via the console.
- **Data Type Conversion**: Converts input data to appropriate numeric types for calculations.
- **Personalized Feedback**: Provides personalized output based on the user's input.

## Technical Requirements 🔧

- **Python Version**: Python 3.x
- **External Libraries**: None required

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `05_input_demo.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `05_input_demo.py`.
5. Run the script with: `python 05_input_demo.py`.

## Usage Example 📋

Upon execution, the script will prompt the user to input their name, year of birth, and height. After input, it will calculate and display the age in years and height in meters, providing immediate and customized feedback based on the provided data.

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
