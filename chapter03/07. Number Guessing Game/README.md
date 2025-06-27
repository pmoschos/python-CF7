# 🎯 Python Number Guessing Game 🎲

Welcome to the Python Number Guessing Game! This script allows users to guess a randomly generated secret number within a specified range. The user receives feedback on their guesses, helping them to determine how close they are to the secret number.

## Script Overview 📘

The script generates a random secret number and prompts the user to guess the number within a limited number of tries. The user is informed if their guess is "Hot" (close to the secret number) or "Cold" (far from the secret number). The game continues until the user guesses the number or reaches the maximum number of attempts.

### :computer: Script Code

```python
import random

def get_user_guess():
    """
    Prompts the user to input a guess and returns it as an integer.
    Handles ValueError if input is not a valid integer.
    """
    while True:
        try:
            return int(input("Please insert an int: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_guess(secret, guess):
    """
    Checks the user's guess against the secret number and prints the appropriate message.
    
    Args:
    secret (int): The secret number to guess.
    guess (int): The user's guess.
    
    Returns:
    bool: True if the guess is correct, False otherwise.
    """
    if guess == secret:
        print("Bingo! Secret number:", secret)
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False

def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number, guess):
            break
        tries += 1
    
    if tries == MAX_TRIES:
        print("You reached the max number of tries:", MAX_TRIES)

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Random Number Generation**: Learn how to generate a random number within a specified range using the `random` module.
- **User Input Handling**: Discover how to capture and validate user input in Python.
- **Conditional Feedback**: Understand how to provide feedback based on how close the user's guess is to the secret number.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `07_number_guessing_game.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `07_number_guessing_game.py`.
5. Run the script with: `python 07_number_guessing_game.py`.

## Usage Example 📋

Execute the script and follow the prompts to guess the secret number. The script will inform you if your guess is correct, "Hot," or "Cold," and continue until you guess the number or reach the maximum number of attempts.

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
