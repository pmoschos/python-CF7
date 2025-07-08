def memoize(func):
    """
    A simple memoization decorator to cache results of the function.
    """
    cache = {}
    cache_stats = {"hits": 0, "misses": 0}

    def wrapper(n):
        if n in cache:
            cache_stats["hits"] += 1
            print(f"Cache hit for Fibonacci({n})")
        else:
            cache_stats["misses"] += 1
            print(f"Calculating Fibonacci({n})")
            cache[n] = func(n)
        return cache[n]

    # Adding a function to print cache statistics
    def get_cache_stats():
        return cache_stats

    # Attach the stats function to the wrapper for easy access
    wrapper.get_cache_stats = get_cache_stats
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
    # results = [fibonacci(n) for n in range(10)]
    # print("\nFibonacci Sequence:", results)
    results = []
    for i in range(5):
        print(f"\n---fibonacci({i})---")
        results.append(fibonacci(i))
        print("\n-> Fibonacci Sequence:", results)

    # Print cache hit/miss summary
    cache_stats = fibonacci.get_cache_stats()
    print(f"Cache Statistics: Hits - {cache_stats['hits']}, Misses - {cache_stats['misses']}")

if __name__ == '__main__':
    main()
