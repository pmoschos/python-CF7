def memoize(func):
    """
    A simple memoization decorator to cache results of the function.
    """
    cache = {}
    
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for Fibonacci({n})")
        else:
            print(f"Calculating Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    # Using the decorated function to calculate Fibonacci numbers
    print([fibonacci(n) for n in range(10)]) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

if __name__ == '__main__':
    main()