# Fibonacci sequence
#
# Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# Fibonacci(0) = 0
# Fibonacci(1) = 1

def fibo(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    
    Args:
    n (int): The position in the Fibonacci sequence to calculate.
    
    Returns:
    int: The nth Fibonacci number.
    
    Comments:
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
    usually starting with 0 and 1.
    """
    # Base cases: fibo(0) = 0, fibo(1) = 1
    if n in (0, 1):
        return n
    # Recursive case: fibo(n) = fibo(n-1) + fibo(n-2)
    return fibo(n - 1) + fibo(n - 2)

def main():
    # Get user input for the value of n
    n = int(input("Enter a positive integer to find its Fibonacci number: "))
    print(f"fibo({n}) = {fibo(n)}")

if __name__ == '__main__':
    main()