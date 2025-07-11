# 🎭 Object Matching with 'match' Statement 🔍

Welcome to the Object Matching Script! This Python script demonstrates the use of the `match` statement to process different types of objects. The program supports `Dog`, `Cat`, and `Bird` classes, and uses pattern matching to identify and describe each animal appropriately.

## Script Overview 📘

The script includes:
- An `Animal` base class and its subclasses `Dog`, `Cat`, and `Bird` to represent different animals.
- A `describe_animal` function that uses the `match` keyword to provide descriptions based on the object type.
- A main block that tests the functionality with various animal instances.

### :computer: Script Code

```python
class Animal:
    """Base class for all animals."""
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    """Class representing a Dog."""
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    """Class representing a Cat."""
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class Bird(Animal):
    """Class representing a Bird."""
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly


def describe_animal(animal):
    """
    Describes the given animal using the 'match' keyword.

    Args:
        animal: An instance of an Animal or its subclasses.
    """
    match animal:
        # Case for matching a Dog instance
        case Dog(name=name, breed=breed):
            print(f"This is a dog named {name}. It is a {breed} breed.")
        
        # Case for matching a Cat instance
        case Cat(name=name, color=color):
            print(f"This is a cat named {name}. It has a beautiful {color} color.")
        
        # Case for matching a Bird instance that can fly
        case Bird(name=name, can_fly=True):
            print(f"This is a bird named {name}. It can fly!")
        
        # Case for matching a Bird instance that cannot fly
        case Bird(name=name, can_fly=False):
            print(f"This is a bird named {name}. Unfortunately, it cannot fly.")
        
        # Default case for unknown animals
        case _:
            print("Unknown animal.")


# Test cases to help students understand pattern matching with classes
if __name__ == "__main__":
    # Creating instances of different animals
    buddy = Dog("Buddy", "Golden Retriever")
    whiskers = Cat("Whiskers", "black")
    tweety = Bird("Tweety", True)
    penguin = Bird("Pingu", False)
    unknown_animal = Animal("Mystery")

    # Describing each animal
    describe_animal(buddy)          # Should describe Buddy, the Golden Retriever
    describe_animal(whiskers)       # Should describe Whiskers, the black cat
    describe_animal(tweety)         # Should describe Tweety, the bird that can fly
    describe_animal(penguin)        # Should describe Pingu, the bird that cannot fly
    describe_animal(unknown_animal) # Should indicate that the animal is unknown
```

## Key Features 🌟

- **Pattern Matching**: Demonstrates Python's `match` statement to identify and describe objects dynamically.
- **Object-Oriented Design**: Utilizes a hierarchy of classes to represent different animal types.
- **Dynamic Dispatch**: Provides a clean and flexible approach to handle various subclasses dynamically.

## Technical Requirements 🔧

- **Python Version**: Python 3.10 or later (required for the `match` statement).
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.10 or later is installed on your machine.
2. Save the script as `13_object_matching.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `13_object_matching.py`.
5. Run the script with: `python 13_object_matching.py`.

## Usage Example 📋

Execute the script to describe different animals:

1. **Dog Example:**
    ```python
    buddy = Dog("Buddy", "Golden Retriever")
    describe_animal(buddy)
    # Output: This is a dog named Buddy. It is a Golden Retriever breed.
    ```

2. **Cat Example:**
    ```python
    whiskers = Cat("Whiskers", "black")
    describe_animal(whiskers)
    # Output: This is a cat named Whiskers. It has a beautiful black color.
    ```

3. **Bird Example (Can Fly):**
    ```python
    tweety = Bird("Tweety", True)
    describe_animal(tweety)
    # Output: This is a bird named Tweety. It can fly!
    ```

4. **Bird Example (Cannot Fly):**
    ```python
    penguin = Bird("Pingu", False)
    describe_animal(penguin)
    # Output: This is a bird named Pingu. Unfortunately, it cannot fly.
    ```

5. **Unknown Animal Example:**
    ```python
    unknown_animal = Animal("Mystery")
    describe_animal(unknown_animal)
    # Output: Unknown animal.
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

