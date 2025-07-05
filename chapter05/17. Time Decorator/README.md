# ⏳ Timing Function Execution with Decorators 🔄

This script demonstrates how to measure the execution time of functions in Python using a decorator. The example functions include calculating the sum and average of integers, as well as reversing a string. The decorator adds timing functionality to these functions, allowing us to measure and print the execution time.

## Script Overview 📘

The script defines a `timer_decorator` that wraps a function to measure and print its execution time. Three example functions (`sum_function`, `average_function`, and `reverse_string`) are decorated to demonstrate the functionality.

### :computer: Script Code

```python
import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function with added timing functionality.
    """
    def inner_function(*args, **kwargs):
        """
        Wrapper function to calculate the execution time of the decorated function.

        Parameters:
        *args: Variable length argument list for the decorated function.
        **kwargs: Arbitrary keyword arguments for the decorated function.

        Returns:
        Any: The result of the decorated function.
        """
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the decorated function
        end_time = time.time()  # Record the end time
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result  # Return the result of the decorated function
    return inner_function

# Decorate the sum_function manually
def sum_function(n):
    """
    Function to calculate the sum of integers from 0 to n-1.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    int: The sum of integers from 0 to n-1.
    """
    return sum(range(n))

# Decorate the sum_function manually
sum_function = timer_decorator(sum_function)
print(sum_function(1_000_000))

# Decorate the sum_function_2 using the decorator syntax
@timer_decorator
def average_function(n):
    """
    Function to calculate the average of integers from 0 to n-1.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    float: The average of integers from 0 to n-1.
    """
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_function(1_000_000))

# Another example function decorated with the timer_decorator
@timer_decorator
def reverse_string(s):
    """
    Function to reverse a string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return "".join(reversed(s))

print(reverse_string("Coding Factory"))

def main():
    """
    Main function to demonstrate the usage of the timer_decorator.
    """
    print(sum_function(1_000_000))  # Manually decorated function
    print(average_function(1_000_000))  # Function decorated with @timer_decorator
    print(reverse_string("Coding Factory"))  # Another example function decorated with @timer_decorator

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Decorator Pattern**: Learn how to use decorators to add functionality to existing functions.
- **Time Measurement**: Understand how to measure the execution time of functions using the time module.
- **Function Wrapping**: See how to wrap functions with additional functionality while preserving their original behavior.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `17_time_decorator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `17_time_decorator.py`.
5. Run the script with: `python 17_time_decorator.py`.

## Usage Example 📋
Execute the script to see how the time taken for a function to execute is measured and printed. The script will demonstrate the timing of calculating the sum and average of numbers from 0 to `n-1` and reversing a string.

📢 Stay Updated
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
