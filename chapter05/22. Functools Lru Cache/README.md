# 🌀 Fibonacci Sequence with LRU Cache 🔄

This script demonstrates the use of the Least Recently Used (LRU) cache in Python to optimize the calculation of Fibonacci numbers. By caching the results of expensive function calls, LRU caching improves performance and reduces redundant calculations.

## Script Overview 📘

The script uses the `functools.lru_cache` decorator to cache the results of the `fibonacci_cached` function, which calculates Fibonacci numbers. Additionally, it includes a logging function to indicate when a cached result is used.

### :computer: Script Code

```python
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
```

## Key Features 🌟
- **LRU Cache**: Learn how to use the `functools.lru_cache` decorator to cache function results and improve performance.
- **Fibonacci Calculation**: Understand the implementation of a recursive function to calculate Fibonacci numbers.
- **Logging**: See how logging can be added to provide feedback on when cached results are used.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in `functools` module

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `22_lru_func_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `22_lru_func_demo.py`.
5. Run the script with: `python 22_lru_func_demo.py`.

## Usage Example 📋
Execute the script to see how LRU caching optimizes the calculation of Fibonacci numbers. The script will print messages indicating cache hits and calculations, followed by the first 10 Fibonacci numbers.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
