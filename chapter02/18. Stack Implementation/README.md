# 🗃️ Python Stack Operations Demonstration 🛠️

Welcome to the Python Stack Operations Demonstration! This script showcases various methods for manipulating a list used as a stack in Python, including pushing, popping, and viewing elements. It's an excellent resource for anyone new to Python or those teaching programming concepts related to stack operations.

## Script Overview 📘

The script demonstrates how to use a list as a stack where elements are added and removed according to the Last-In, First-Out (LIFO) principle. The program includes functions to push items to the stack, pop items from the stack, and view the stack's current contents. It also handles user interactions through a simple menu-driven interface.

### :computer: Script Code

```python
# Importing the regular expression module to handle string matching and searching.
import re

# Initialize an empty list to use as a stack.
stack = []
# Variable to store numbers (though unused in this initial declaration).
num = 0

# Function to push an item onto the stack.
def push(list, item):
    list.append(item)  # Append the item to the end of the list (stack).

# Function to pop an item from the stack.
def pop(list):
    if list:  # Check if the list (stack) is not empty.
        return list.pop()  # Remove and return the last item from the list (stack).
    else:
        print("Stack is empty")  # Print a message if the stack is empty.

# Function to print the current state of the stack.
def print_stack(list):
    if list:  # Check if the list (stack) is not empty.
        print("Current stack:", list)  # Print the current items in the stack.
    else:
        print("Stack is empty")  # Print a message if the stack is empty.

# Function to print the menu options.
def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print stack")
    print("4. q\Q for Quit")

# Function to get the user's choice.
def get_choice():
    return input("Please provide a choice\n")  # Prompt the user for input and return it.

# Main function that runs the program.
def main():
    choice = 0  # Variable to store the user's menu choice.
    num = 0  # Variable to store the number to be pushed onto the stack.
    out_num = 0  # Variable to store the number popped from the stack.

    # Infinite loop to keep the program running until the user chooses to quit.
    while True:
        print_menu()  # Display the menu options.
        choice = get_choice()  # Get the user's choice.

        if not choice:  # If the user does not enter anything.
            continue  # Skip to the next iteration of the loop.

        # If the user wants to quit, check for 'q' or 'Q'.
        if choice == 'q' or choice == 'Q':
            break  # Exit the loop and end the program.

        # Define a pattern to check if the input choice is a single digit.
        # r: Raw string literal
        # ^: Asserts position at the start of the string.
        # \d: Matches any digit (0-9).
        # \d+: Matches any digit (0-9) These digits can be 1 or more.
        # $: Asserts position at the end of the string.
        pattern = r'^\d$'
        valid = re.match(pattern, choice)  # Use regex to validate the choice.

        if not valid:  # If the choice is not valid (not a single digit).
            print("Error in choice")
            continue  # Skip to the next iteration of the loop.

        choice = int(choice)  # Convert the valid choice to an integer.

        # Match the choice with the possible options using the match-case statement (Python 3.10+).
        match choice:
            case 1:
                num = input("Please insert a number:")  # Prompt the user to enter a number.
                pattern = r'^\d+$'  # Define a pattern to check if the input is a positive integer.
                valid = re.match(pattern, num)  # Use regex to validate the number.

                if not valid:  # If the number is not valid (not a positive integer).
                    print("Error")
                    continue  # Skip to the next iteration of the loop.

                num = int(num)  # Convert the valid number to an integer.
                push(stack, num)  # Push the number onto the stack.
                print(str(num) + " inserted")  # Print a message indicating the number was inserted.
            
            case 2:
                out_num = pop(stack)  # Pop the top number from the stack.
                if out_num is not None:  # Check if there was a number to pop.
                    print("You got:", out_num)  # Print the popped number.
            
            case 3:
                print_stack(stack)  # Print the current state of the stack.
            
            case _:  # Default case for any other input.
                print("Not valid choice")

# If this script is run as the main program, execute the main function.
if __name__ == "__main__":
    main()

```

## Key Features 🌟
- **Stack Manipulation**: Learn how to use list operations to simulate stack behavior in Python.
- **User Interaction**: Understand how to create a simple text-based user interface for interacting with the stack.
- **Error Handling**: Discover how to handle common mistakes such as popping from an empty stack.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None required, uses standard Python libraries.

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `18_my_stack.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_my_stack.py`.
5. Run the script with: `python 18_my_stack.py`.

## Usage Example 📋
Execute the script and follow the on-screen prompts to push to the stack, pop from the stack, or view the stack's contents. This will help you understand the practical applications of stack operations in Python programming.

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