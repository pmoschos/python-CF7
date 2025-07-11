def add_validation(cls):
    """
    Decorator to add validation for attributes during initialization.
    Specifically checks for negative values in the `age` attribute.

    Args:
        cls: The class to which validation is added.

    Returns:
        The modified class with validation in its constructor.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        """
        New initializer with validation for negative age values.

        Args:
            self: The instance being created.
            *args: Positional arguments passed to the original initializer.
            **kwargs: Keyword arguments passed to the original initializer.

        Raises:
            ValueError: If `age` is negative.
        """
        # Validate 'age' in positional arguments
        if len(args) >= 2 and isinstance(args[1], (int, float)) and args[1] < 0:
            raise ValueError("Age cannot be negative.")

        # Validate 'age' in keyword arguments
        if 'age' in kwargs and kwargs['age'] < 0:
            raise ValueError("Age cannot be negative.")

        # Call the original initializer
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@add_validation
class Person:
    """
    A class representing a person with a name and age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person. Must be non-negative.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def main() -> None:
    """
    Main function to demonstrate the functionality of the Person class with validation.
    """
    try:
        # Valid case
        p1 = Person("Alice", 25)
        print(f"Created Person: {p1.name}, Age: {p1.age}")

        # Invalid case (negative age)
        p2 = Person("Bob", -5)  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Invalid case with keyword argument (negative age)
        p3 = Person(name="Charlie", age=-10)  # This will also raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
