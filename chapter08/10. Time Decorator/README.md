# ⏱️ Method Timer Decorator Example ⚙️

Welcome to the Method Timer Decorator Example Script! This Python script demonstrates how to use decorators to log the execution time of all methods in a class. It applies the decorator to a `Calculator` class to measure and log the time taken by its `add` and `multiply` methods.

## Script Overview 📘

The script includes:
- A `add_method_timer` decorator that wraps methods of a class to log their execution time.
- A `Calculator` class with methods for addition and multiplication, both simulated with delays to demonstrate timing.
- A `main` function to demonstrate the functionality of the decorated class.

### :computer: Script Code

```python
import time
from typing import Type, Callable

def add_method_timer(cls: Type) -> Type:
    """
    Decorator to log the execution time of methods in a class.

    Args:
        cls (Type): The class to decorate.

    Returns:
        Type: The decorated class with timing functionality added to its methods.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):  # Check if the attribute is a method
            original_method = attr_value

            def timed_method(self, *args, **kwargs):
                """
                Wrapper to log execution time of a method.

                Args:
                    self: The instance of the class.
                    *args: Positional arguments for the method.
                    **kwargs: Keyword arguments for the method.

                Returns:
                    The result of the original method.
                """
                start_time = time.time()
                result = original_method(self, *args, **kwargs)
                end_time = time.time()
                print(f"Method {attr_name} took {end_time - start_time:.4f} seconds.")
                return result

            # Set the wrapped method in place of the original
            setattr(cls, attr_name, timed_method)
    return cls

@add_method_timer
class Calculator:
    """
    A simple calculator class with methods for addition and multiplication.
    """
    def add(self, a: int, b: int) -> int:
        """
        Simulate addition with a delay.

        Args:
            a (int): First number.
            b (int): Second number.

        Returns:
            int: Sum of a and b.
        """
        time.sleep(0.5)  # Simulate delay
        return a + b

    def multiply(self, a: int, b: int) -> int:
        """
        Simulate multiplication with a delay.

        Args:
            a (int): First number.
            b (int): Second number.

        Returns:
            int: Product of a and b.
        """
        time.sleep(0.3)  # Simulate delay
        return a * b

def main() -> None:
    """
    Main function to demonstrate the functionality of the Calculator class
    with execution time logging for its methods.
    """
    calc = Calculator()

    # Demonstrate addition with execution time logging
    print(f"Addition Result: {calc.add(2, 3)}")  # Logs execution time for add

    # Demonstrate multiplication with execution time logging
    print(f"Multiplication Result: {calc.multiply(4, 5)}")  # Logs execution time for multiply

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Class-Level Decoration**: Demonstrates how to apply decorators to all methods of a class dynamically.
- **Execution Time Logging**: Logs the time taken to execute methods, providing insights into performance.
- **Simulation of Delays**: Uses `time.sleep` to simulate computational delays and illustrate timing functionality.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `10_time_decorator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_time_decorator.py`.
5. Run the script with: `python 10_time_decorator.py`.

## Usage Example 📋

Execute the script to see how the decorator logs the execution time of methods:

1. **Addition Example:**
    ```python
    calc = Calculator()
    print(f"Addition Result: {calc.add(2, 3)}")
    # Logs: Method add took 0.5000 seconds.
    ```

2. **Multiplication Example:**
    ```python
    print(f"Multiplication Result: {calc.multiply(4, 5)}")
    # Logs: Method multiply took 0.3000 seconds.
    ```

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