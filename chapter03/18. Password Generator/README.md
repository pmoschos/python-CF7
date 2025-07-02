# 🔑 Python Random Password Generator 🗝️

Welcome to the Python Random Password Generator script! This script generates a random password based on the user-specified length. It includes uppercase and lowercase letters, digits, and special characters to ensure a strong and secure password.

## Script Overview 📘

The script prompts the user to enter the desired password length and generates a random password. The user can continue generating passwords or quit the program.

### :computer: Script Code

```python
# Import necessary modules
import string
import random

# Create a list of characters that includes uppercase and lowercase letters, digits, and special characters
characters = list(string.ascii_letters + string.digits + " !@#$%^&*")

def generate_password():
    """
    Generate a random password based on the user-specified length.
    """
    try:
        # Prompt the user for the desired password length and convert it to an integer
        password_length = int(input("Give the password length: "))
        
        # Ensure the password length is a positive integer
        if password_length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a valid integer.")
        return

    # Shuffle the characters to ensure randomness
    random.shuffle(characters)
    
    # Initialize an empty list to store the password characters
    password = []

    # Randomly select characters from the shuffled list and append them to the password list
    for i in range(password_length):
        password.append(random.choice(characters))
    
    # Shuffle the password list to ensure the characters are randomly ordered
    random.shuffle(password)
    
    # Join the list of characters into a single string to form the final password
    password = "".join(password)
    
    # Print the generated password
    print(f"\nGenerated password: {password}")

def main():
    """
    Main function to control the password generation process.
    """
    while True:
        # Prompt the user if they want to create a password or quit
        option = input("\nDo you want to create a password? ('y' or 'q' for quit): ")

        # If the user wants to create a password, call the generate_password function
        if option.lower() == 'y':
            generate_password()
        # If the user wants to quit, print a goodbye message and break the loop
        elif option.lower() == 'q':
            print("Goodbye")
            break
        # Handle invalid inputs
        else:
            print("Wrong input")

# If the script is run directly, call the main function
if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Password Generation**: Learn how to generate a random password with uppercase and lowercase letters, digits, and special characters.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Loop and Conditional Statements**: Understand how to use loops and conditional statements to control program flow.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `18_password_generator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_password_generator.py`.
5. Run the script with: `python 18_password_generator.py`.

## Usage Example 📋

Execute the script and follow the prompts to generate a random password. You can continue generating passwords or quit the program as needed.

## 📢 Stay Updated

Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License

🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧

Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
