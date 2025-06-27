# 🔑 Python Message Decryption Script 🔐

Welcome to the Python Message Decryption Script! This script decrypts a message by removing all numeric characters from a given string. It's an ideal resource for understanding string manipulation and character filtering in Python.

## Script Overview 📘

The script defines a function to decrypt a message by removing numeric characters and then demonstrates its usage with an example message.

### :computer: Script Code

```python
def decrypt_message(message):
    """
    Decrypts a message by removing all numeric characters.

    Args:
    message (str): The encrypted message containing alphanumeric characters.

    Returns:
    str: The decrypted message with numeric characters removed.
    """
    # Remove numeric characters using list comprehension and join
    # Spoiler... hehe
    # return ''.join([char for char in message if not char.isnumeric()])
    decrypt_message = ""
    for char in message:
        if not char.isnumeric():
            decrypt_message += char
    return decrypt_message

def main():
    strange_message = "432H3525el523l52o5 523C532F52"
    decrypted_message = decrypt_message(strange_message)
    print(decrypted_message)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **String Manipulation**: Learn how to manipulate strings and remove specific characters.
- **Character Filtering**: Discover how to filter out numeric characters from a string.
- **Function Definition**: Understand how to define and use functions in Python.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `14_decrept_message.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `14_decrept_message.py`.
5. Run the script with: `python 14_decrept_message.py`.

## Usage Example 📋

Execute the script to see the decrypted message printed in the console. The script will remove all numeric characters from the provided message.

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
