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
