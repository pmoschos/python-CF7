# 📅 Python Month Check Script 📆

Welcome to the Python Month Check Script! This script checks if a user-provided three-letter month abbreviation is in a predefined list of months. It demonstrates two different ways to perform the check and handle user input in Python.

## Script Overview 📘

The script prompts the user to enter a three-letter month abbreviation and checks if it exists in the predefined list of months. It uses two different methods to perform this check.

### :computer: Script Code

```python
def main():
    months = ["Jan", "Feb", "Mar"]
    input_month = input("Please insert 3 letters for a month: ")
    
    # 1st way
    found = False
    for month in months:
        if month.casefold() == input_month.casefold():
            found = True
            break
    
    print(f"Input month found: {input_month}"
          if found else f"Month: {input_month} not found") 
    
    # 2nd way
    for month in months:
        if month.casefold() == input_month.casefold():
            print(f"Input month found: {input_month}")
            break
    else:
        print(f"Month: {input_month} not found")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **String Comparison**: Learn how to compare strings in a case-insensitive manner using `casefold()`.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Loop and Conditional Statements**: Understand different methods for checking the presence of an item in a list.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `15_break_app.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `15_break_app.py`.
5. Run the script with: `python 15_break_app.py`.

## Usage Example 📋

Execute the script and enter a three-letter month abbreviation when prompted. The script will check if the month exists in the predefined list and print the result.

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
