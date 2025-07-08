# 📜 Logging and Timing Function Calls in Python ⏳

This script demonstrates the use of decorators to log function calls and measure their execution time. By stacking multiple decorators, we can enhance functions with additional behaviors such as logging and timing.

## Script Overview 📘

The script defines two decorators: one for logging function calls (`log_calls`) and another for measuring execution time (`measure_time`). These decorators are applied to a function that calculates Fibonacci numbers to demonstrate their usage.

### :computer: Script Code

```python
import time

def log_calls(func):
    """
    A decorator that logs the function call.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    """
    A decorator that measures the execution time of the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# The decorators are applied bottom-to-top (@measure_time first, then @log_calls).
# The execution is top-to-bottom (@log_calls executes first, then @measure_time).
@log_calls
@measure_time
def say_hello(name):
    """
    A simple function that returns a greeting.
    
    Args:
    name (str): The name to greet.
    
    Returns:
    str: The greeting message.
    """
    time.sleep(1)  # Simulate some processing delay
    return f"Hello, {name}!"

def main():
    # Using the function with multiple decorators
    print(say_hello("Alice"))
    print(say_hello("Bob"))

if __name__ == '__main__':
    main()

```

## Key Features 🌟
- **Logging Decorator**: Learn how to create and use a decorator to log function calls and their arguments.
- **Timing Decorator**: Understand how to create and use a decorator to measure the execution time of functions.
- **Decorator Stacking**: See how to stack multiple decorators to combine their functionalities.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `23_multiple_decorators.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `23_multiple_decorators.py`.
5. Run the script with: `python 23_multiple_decorators.py`.

## Usage Example 📋
Execute the script to see how logging and timing decorators enhance the function that calculates Fibonacci numbers. The script will print log messages for function calls and their execution time, followed by the Fibonacci number at the specified position.

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
