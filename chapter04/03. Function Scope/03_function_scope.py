a = 10
b = 20

def add_numbers(x: int, y: int) -> int:
    """
    Adds two integers and returns the sum.

    Parameters:
    x (int): The first integer.
    y (int): The second integer.

    Returns:
    int: The sum of the two integers.
    """
    x = 100  # Clearly distinguish local modification
    return x + y


def main():
    # Use the function and display results
    result = add_numbers(a, b)
    print(result)  # Output will be 120
    print(a)       # Output will be 10, demonstrating that 'a' is unchanged

if __name__ == "__main__":
    main()