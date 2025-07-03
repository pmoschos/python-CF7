import functools

def calculate(args):
    """
    Generate functions to perform arithmetic operations on a list of numbers.

    Parameters:
    args (list of int/float): List of numbers to perform operations on.

    Returns:
    tuple: Four functions (plus, minus, mul, div) that perform addition, subtraction,
           multiplication, and division respectively.
    """
    def plus():
        """Return the sum of the numbers in the list."""
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        """Return the result of subtracting the numbers in the list."""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        """Return the product of the numbers in the list."""
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        """Return the result of dividing the first number by the sum of the rest of the numbers."""
        if not 0 in args[1:]:  # Ensure there are no zeros in the denominator
            return args[0] / sum(args[1:])
        else:
            return "Division by zero error"

    return plus, minus, mul, div

def main():
    """
    Main function to demonstrate the usage of calculate.
    """
    ints_list = [26, 5, 4, 3, 2, 1]

    # Generate arithmetic operation functions for ints_list
    add_func, minus_func, mul_func, div_func = calculate(ints_list)

    # Print results of each operation
    print("add_func:", add_func())  # Expected output: 41 (sum of 26 + 5 + 4 + 3 + 2 + 1)
    print("minus_func:", minus_func())  # Expected output: 11 (26 - 5 - 4 - 3 - 2 - 1)
    print("mul_func:", mul_func())  # Expected output: 3120 (26 * 5 * 4 * 3 * 2 * 1)
    print("div_func:", div_func())  # Expected output: 2.0 (26 / (5 + 4 + 3 + 2 + 1))

if __name__ == "__main__":
    main()
