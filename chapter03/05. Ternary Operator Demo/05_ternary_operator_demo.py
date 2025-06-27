def compare_integers(a, b):
    """
    Compares two integers and prints the result.

    Args:
    a (int): The first integer to compare.
    b (int): The second integer to compare.

    Returns:
    None
    """
    if a == b:
        print("The numbers are equal.")
    elif a > b:
        print("The first number is greater than the second number.")
    else:
        print("The first number is less than the second number.")

def main():
    try:
        # Get user input for the two integers
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    # Compare the integers
    compare_integers(a, b)

    # 1. Ternary operator (simple example)
    result = "Positive" if a > 0 else "Non-positive"
    print(result)

    # 2. Ternary operator (extended example)
    result = (
        "The numbers are equal." if a == b else
        "The first number is greater than the second number." if a > b else
        "The first number is less than the second number."
    )
    print(result)


if __name__ == "__main__":
    main()
