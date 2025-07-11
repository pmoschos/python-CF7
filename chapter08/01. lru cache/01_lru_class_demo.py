from functools import lru_cache

class FibonacciCache:
    """
    A wrapper around functools.lru_cache to add professional logging
    for cache hits and misses.
    """

    def __init__(self, maxsize=None):
        self.cache = lru_cache(maxsize=maxsize)(self._fibonacci)
        self.hits = 0
        self.misses = 0

    def _fibonacci(self, n):
        """The actual Fibonacci calculation."""
        if n <= 1:
            return n
        return self.cache(n - 1) + self.cache(n - 2)

    def __call__(self, n):
        """
        Handle the cache hit/miss tracking and return the Fibonacci number.
        """
        if n in self.cache.cache_parameters():
            self.hits += 1
            print(f"Cache hit for Fibonacci({n})")
        else:
            self.misses += 1
            print(f"Calculating Fibonacci({n})")
        return self.cache(n)

    def cache_info(self):
        """
        Return cache statistics (hits, misses, and lru_cache info).
        """
        info = self.cache.cache_info()
        return {
            "hits": self.hits,
            "misses": self.misses,
            "cache_info": info,
        }

    def cache_clear(self):
        """Clear the cache and reset hit/miss counters."""
        self.cache.cache_clear()
        self.hits = 0
        self.misses = 0


# Instantiate the cache-enabled Fibonacci function
fibonacci = FibonacciCache()


def main():
    # Reset cache before calculation
    fibonacci.cache_clear()

    # Calculate Fibonacci numbers with logging
    results = []
    for i in range(5):
        print(f"\n---fibonacci({i})---")
        results.append(fibonacci(i))
        print("\n-> Fibonacci Sequence:", results)

    # Display cache statistics
    stats = fibonacci.cache_info()
    print(
        f"Cache Statistics: Hits - {stats['hits']}, Misses - {stats['misses']}, "
        f"Cache Info - {stats['cache_info']}"
    )


if __name__ == '__main__':
    main()
