def my_add(*args: int) -> int:
    """
    Calculate the sum of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    int: The sum of the provided integers.
    """
    # result = 0
    # for arg in args:
    #   result += arg
    # return result
    return sum(args)  # Utilizing Python's built-in sum function for efficiency and readability.

def my_avg(*args: int) -> float:
    """
    Calculate the average of an arbitrary number of integers.

    Parameters:
    *args (int): A variable-length argument list of integers.

    Returns:
    float: The average of the provided integers. Returns 0 if no arguments are provided to avoid division by zero.
    """
    if not args:  # Check if args is empty to prevent division by zero.
        return 0
    return sum(args) / len(args)  # Using built-in sum function and len function for concise code.

def main():
    # List of ages to be averaged
    ages = [27, 35, 42, 18, 20]
    # Printing the average of a list of ages using unpacking argument lists
    print("Average age:", my_avg(*ages))

    # Directly passing numbers to calculate their average
    print("Average of 1, 2, 3, 4, 5:", my_avg(1, 2, 3, 4, 5))

    # Example to demonstrate handling with no inputs
    print("Average with no inputs:", my_avg())  # Should return 0

if __name__ == "__main__":
    main()
