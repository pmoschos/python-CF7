# 🌀 Fibonacci with Cache and Logging Script ✨

This Python script demonstrates an enhanced implementation of the Fibonacci sequence calculation using `functools.lru_cache` with added functionality for professional logging of cache hits and misses.

---

## Script Overview 📘

The script includes:

1. **`FibonacciCache` Class**:
   - A custom wrapper around `functools.lru_cache`.
   - Tracks cache hits and misses with detailed logging.
   - Provides methods for cache statistics and clearing the cache.

2. **Fibonacci Calculation**:
   - Uses recursion with caching to calculate Fibonacci numbers efficiently.

3. **Cache Management**:
   - Includes functionality to reset the cache and track statistics for optimized performance.

### :computer: Script Code

```python
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
```

---

## Key Features 🌟

- **Efficient Fibonacci Calculation**:
  - Uses caching to avoid redundant calculations.
  - Significantly improves performance for large inputs.

- **Professional Logging**:
  - Tracks cache hits and misses.
  - Logs each calculation step for detailed insights.

- **Cache Management**:
  - Provides methods to view and reset cache statistics.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `01_lru_class_demo.py`.
3. Run the script:

   ```bash
   python 01_lru_class_demo.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Cache hit for Fibonacci(0)
---fibonacci(0)---

-> Fibonacci Sequence: [0]
Calculating Fibonacci(1)
---fibonacci(1)---

-> Fibonacci Sequence: [0, 1]
Calculating Fibonacci(2)
---fibonacci(2)---

-> Fibonacci Sequence: [0, 1, 1]
Calculating Fibonacci(3)
---fibonacci(3)---

-> Fibonacci Sequence: [0, 1, 1, 2]
Calculating Fibonacci(4)
---fibonacci(4)---

-> Fibonacci Sequence: [0, 1, 1, 2, 3]
Cache Statistics: Hits - 3, Misses - 2, Cache Info - CacheInfo(hits=3, misses=2, maxsize=None, currsize=5)
```

---

## 📲 Contact and Contribution

### Contact 📧
- **Author**: Panagiotis Moschos
- **Email**: pan.moschos86@gmail.com
- **GitHub**: [pmoschos](https://github.com/pmoschos)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>

