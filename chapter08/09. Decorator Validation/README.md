# ✅ Person Class with Validation Decorator 🧑‍⚖️

Welcome to the Person Class Validation Example Script! This Python script demonstrates the use of a decorator to add validation logic for attributes during class initialization. It specifically checks that the `age` attribute is non-negative when creating instances of the `Person` class.

## Script Overview 📘

The script includes:
- A decorator function, `add_validation`, that validates the `age` attribute to ensure it is non-negative.
- A `Person` class that represents individuals with attributes for name and age.
- A `main` function to showcase valid and invalid uses of the `Person` class.

### :computer: Script Code

```python
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
```

## Key Features 🌟

- **Decorator Usage**: Demonstrates how to extend class behavior dynamically using decorators.
- **Validation Logic**: Adds attribute validation to ensure the `age` attribute is non-negative.
- **Error Handling**: Provides examples of how exceptions are raised and handled during invalid input cases.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `09_decorator_validation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `09_decorator_validation.py`.
5. Run the script with: `python 09_decorator_validation.py`.

## Usage Example 📋

Execute the script to see how the validation decorator enforces rules during class instantiation:

1. Creating a `Person` object with a valid age:
    ```python
    p1 = Person("Alice", 25)  # Works fine
    ```

2. Creating a `Person` object with a negative age:
    ```python
    p2 = Person("Bob", -5)  # Raises ValueError
    ```

3. Using a keyword argument with a negative age:
    ```python
    p3 = Person(name="Charlie", age=-10)  # Raises ValueError
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

