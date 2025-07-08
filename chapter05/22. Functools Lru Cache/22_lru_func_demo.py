from functools import lru_cache

# We use lru_cache to cache the results of the Fibonacci function
# maxsize: This parameter defines the maximum number of results to cache. When the cache exceeds this size, 
# the least recently used items are discarded. If maxsize is set to None, the cache can grow without bound.
# typed: If typed is set to True, arguments of different types will be cached separately. For example, 
# f(3) and f(3.0) will be treated as distinct calls with separate cache entries.
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    Return the nth Fibonacci number, with caching.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)

def fibonacci_with_logging(n):
    """
    Return the nth Fibonacci number with logging to show when each calculation is made.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if fibonacci_cached.cache_info().hits > 0:
        print(f"Cache hit for Fibonacci({n})")
    else:
        print(f"Calculating Fibonacci({n})")
    return fibonacci_cached(n)


def main():
    # Reset cache info
    fibonacci_cached.cache_clear()

    # Using the function with caching and logging to calculate Fibonacci numbers
    fibonacci_numbers = [fibonacci_with_logging(n) for n in range(10)]
    print(fibonacci_numbers) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

if __name__ == '__main__':
    main()