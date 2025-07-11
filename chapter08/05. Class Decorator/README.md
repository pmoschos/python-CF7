# 🔢 Instance Counter Decorator Script ♻️

This Python script demonstrates how to use a decorator to add an instance counter to a class. It tracks the number of active instances dynamically and adjusts the count when instances are created or destroyed.

---

## Script Overview 📘

### Function: `add_instance_counter`

1. **Purpose**:
   - Adds a counter to track the number of instances of a class.

2. **Key Features**:
   - Modifies the `__init__` method to increment the counter when an instance is created.
   - Modifies the `__del__` method to decrement the counter when an instance is deleted.
   - Adds a class method `get_instance_count` to retrieve the current instance count.

3. **Reusable Decorator**:
   - Can be applied to any class to add instance tracking functionality.

### Example Class: `Person`

1. **Attributes**:
   - `name`: The name of the person.

2. **Behavior**:
   - Uses the `add_instance_counter` decorator to track the number of active `Person` instances.

### :computer: Script Code

```python
def add_instance_counter(cls):
    """Decorator to add an instance counter to a class."""
    cls._instance_count = 0

    # Original constructor
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        cls._instance_count += 1
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init

    # Original destructor
    original_del = getattr(cls, "__del__", None)

    def new_del(self):
        cls._instance_count -= 1
        if original_del:
            original_del(self)

    cls.__del__ = new_del

    # Method to access the instance count
    def get_instance_count(cls):
        return cls._instance_count

    cls.get_instance_count = classmethod(get_instance_count)
    return cls

@add_instance_counter
class Person:
    def __init__(self, name):
        self.name = name

def main():
    # Create instances
    p1 = Person("Alice")
    p2 = Person("Bob")
    p3 = Person("Charlie")

    print(f"Number of 'Person' instances: {Person.get_instance_count()}")  # Output: 3

    # Delete instances
    del p1
    print(f"Number of 'Person' instances after deleting p1: {Person.get_instance_count()}")  # Output: 2

    del p2
    print(f"Number of 'Person' instances after deleting p2: {Person.get_instance_count()}")  # Output: 1

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Dynamic Instance Tracking**:
  - Tracks the number of active instances in real-time.
  - Automatically updates the count when instances are created or destroyed.

- **Reusable Decorator**:
  - Easily applies instance tracking to any class with minimal changes.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses Python’s standard library).

---

## Installation and Setup 🚀

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `05_class_decorator.py`.
3. Run the script:

   ```bash
   python 05_class_decorator.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Number of 'Person' instances: 3
Number of 'Person' instances after deleting p1: 2
Number of 'Person' instances after deleting p2: 1
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

