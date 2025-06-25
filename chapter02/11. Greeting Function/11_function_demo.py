def say_hello(place: str = "Coding Factory"):
    """
    Prints a greeting message.

    Args:
        place (str): The place to greet. Defaults to 'Coding Factory'.
    """
    # Print a greeting message using f-string
    print(f"Hello, {place}!")

def main():
    """
    The main function to execute the program.
    """
    # Call the say_hello function
    say_hello()

    # Print the documentation of the say_hello function
    print("\nFunction Documentation:")
    print(say_hello.__doc__)

# main()

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()