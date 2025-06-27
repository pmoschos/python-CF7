def fibonacci(n):
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        # Initial values: a = 2, b = 3
        # Evaluate right-hand side: b, a + b becomes (3, 2 + 3) which is (3, 5)
        # Assign the values:
        # a gets the first value of the tuple: a = 3
        # b gets the second value of the tuple: b = 5

    return b

def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return
    
    fib_number = fibonacci(n)
    
    print(f"The {n}th Fibonacci number is {fib_number}")

if __name__ == "__main__":
    main()
