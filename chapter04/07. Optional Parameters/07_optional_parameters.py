def add(a: int, b: int, c: int = 0) -> int:
    """
    Calculate the sum of two or three integers.

    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.
    c (int, optional): The third number to add, defaults to 0 if not provided.

    Returns:
    int: The sum of the provided numbers.
    """
    return a + b + c

def full_opt_add(a=0, b=0, c=0) -> int:
    """
    Calculate the sum of up to three numbers with default values.

    Parameters:
    a (int): The first number (default 0).
    b (int): The second number (default 0).
    c (int): The third number (default 0).

    Returns:
    int: The sum of the numbers.
    """
    return a + b + c

def main():
    # Demonstration of calling the function
    print(f"add(10, 20) = {add(10, 20)}")  # Outputs 30, demonstrates using the default for 'c'
    print(f"add(10, 20, 25) = {add(10, 20, 25)}")  # Outputs 55, demonstrates specifying all three parameters

    # Demonstrating the function with positional arguments
    # The numbers 1, 2, and 3 are added, expected output: 6
    print("Sum using positional arguments:", full_opt_add(1, 2, 3))

    # Demonstrating the function with keyword arguments
    # Specifying each argument by name for clarity, expected output: 6
    print("Sum using keyword arguments:", full_opt_add(c=3, a=1, b=2))

    # Demonstrating the function with default values
    # No arguments passed, so all parameters use their default value of 0, expected output: 0
    print("Sum with default values:", full_opt_add())

if __name__ == "__main__":
    main()