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
