# 🔡 Python Character ASCII Value Demonstration 🆎

Welcome to the Python Character ASCII Value Demonstration! This script reads characters from the user and prints their ASCII values until the user inputs '#'. It includes two functions that demonstrate different approaches to achieving this task.

## Script Overview 📘

The script prompts the user to enter characters, prints their ASCII values, and continues to prompt until the user enters '#'. Two different methods are demonstrated for achieving this functionality.

### :computer: Script Code

```python
def process_characters():
    """
    Reads characters from the user and prints their ASCII values until the user inputs '#'.
    """
    ch = input("Please insert a char: ")

    while ch != '#':
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
    
    print("Goodbye")

def process_characters2():
    """
    Reads characters from the user and prints their ASCII values until the user inputs '#'.
    """
    while True:
        ch = input("Please insert a char (or '#' to quit): ")
        if ch == '#':
            break
        print(f"{ch}: {ord(ch)}")
    
    print("Goodbye")

def main():
    process_characters()
    process_characters2()

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Character Input**: Learn how to read characters from the user input.
- **ASCII Value Printing**: Understand how to print the ASCII values of characters using the `ord()` function.
- **Loop Control**: Discover two different approaches for controlling loops based on user input.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `06_char_ascii_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `06_char_ascii_demo.py`.
5. Run the script with: `python 06_char_ascii_demo.py`.

## Usage Example 📋

Execute the script and enter characters when prompted. The script will print the ASCII values of the entered characters until you input '#', at which point the script will terminate with a goodbye message.

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
