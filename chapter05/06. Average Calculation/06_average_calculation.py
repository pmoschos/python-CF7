def avg(*args):
    """
    Calculate the average of the given numbers.

    Parameters:
    *args (float or int): A variable number of arguments which are the numbers to average.

    Returns:
    float: The average of the numbers. Returns 0 if no arguments are provided.
    """
    # 1st approach
    # if not len(args):
    #    return 0
    # sum = 0
    # for arg in args:
    #     sum += arg
    # return sum / len(args)

    # 2nd approach
    # if not args: return 0
    # return sum(args) / len(args)

    # 3rd approach
    return sum(args) / len(args) if args else 0

def main():
    """
    Main function to demonstrate the usage of avg function.
    """
    # Define a list of integers
    my_ints = [10, 5, 9]
    
    # Calculate and print the average using the avg function
    print("Average of my_ints:", avg(*my_ints))  # Expected output: 8.0

    # Calculate and print the average of different sets of numbers
    print("Average of 1, 2, 3:", avg(1, 2, 3))  # Expected output: 2.0
    print("Average of 5, 10, 15:", avg(5, 10, 15))  # Expected output: 10.0
    print("Average of no numbers:", avg())  # Expected output: 0

if __name__ == "__main__":
    main()
