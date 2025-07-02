# Factorial Calculation
# Definition: n! (n factorial) is the product of all positive integers from 1 to n.
# Recursive relationship: n! = n * (n-1)! for n > 1.
# Base cases:
# 0! = 1 : The factorial of 0 is defined as 1 by convention.
# 1! = 1 : The factorial of 1 is also 1, establishing the base case for recursive multiplication.

def factorial(n: int) -> int:
    """
    Calculate the factorial of integer n.
    """
    if n < 0: return 0
    if n in (0, 1): return 1
    return n * factorial(n - 1)


def main():
    # Get user input for the value of n
    n = int(input("Enter a positive integer to find its Factorial number: "))
    print(f"{n}! = {factorial(n):,}")


if __name__ == '__main__':
    main()
