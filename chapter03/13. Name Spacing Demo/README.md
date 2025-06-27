# 🗺️ Python Name Spacing Script 🖋️

Welcome to the Python Name Spacing Script! This script takes a user-provided name and prints each character separated by a specified number of spaces. It's a useful exercise for understanding string manipulation and user input handling in Python.

## Script Overview 📘

The script prompts the user to enter a name and a number of spaces. It then prints the name with each character separated by the specified number of spaces.

### :computer: Script Code

```python
def name_spacing(num: int):
    """
    Prints each character of the given name separated by a specified number of spaces.
    
    Args:
    num (int): The number of spaces to insert between each character.
    """
    if not isinstance(num, int):
        print("The number of spaces must be an integer.")
        return

    if num < 0:
        print("The number of spaces must be a non-negative integer.")
        return

    name = input("Please give a name: ").strip()
    
    if not name:
        print("No name provided.")
        return

    # Create the spaced string and print it
    spaced_name = (' ' * num).join(name)
    print(spaced_name)

def main():
    # Example usage
    try:
        num = int(input("Enter the number of spaces between characters: "))
        name_spacing(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of spaces.")

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **String Manipulation**: Learn how to manipulate strings and insert spaces between characters.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Conditional Statements**: Understand how to use conditional statements to handle edge cases and invalid input.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `13_name_spacing_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `13_name_spacing_demo.py`.
5. Run the script with: `python 13_name_spacing_demo.py`.

## Usage Example 📋

Execute the script and enter a name when prompted. The script will print each character of the name separated by the specified number of spaces.

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
