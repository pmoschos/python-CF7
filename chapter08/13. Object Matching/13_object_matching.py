# A program that uses the 'match' keyword to work with different types of objects.

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
