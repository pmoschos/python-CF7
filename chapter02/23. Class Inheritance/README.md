# 🛡️ Python Class Inheritance and Encapsulation Demonstration 🔒

Welcome to the Python Class Inheritance and Encapsulation Demonstration! This script showcases advanced concepts in object-oriented programming, focusing on attribute visibility and method accessibility in Python. It's an invaluable resource for anyone learning advanced Python or teaching object-oriented programming principles.

## Script Overview 📘

The script explores how to use encapsulation to protect object attributes, and demonstrates inheritance where a derived class extends the functionality of a base class.

### :computer: Script Code

```python
class Base:
    def __init__(self):
        self.__private = "I am private"
        self._protected = "I am protected"
        self.public = "I am public"
    
    def __private_method(self):
        return "This is a private method"
    
    def get_private(self):
        return self.__private
    
    def call_private_method(self):
        return self.__private_method()

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "I am private in Derived"

    def get_derived_private(self):
        return self.__private

def main():
    base = Base()
    print(base.public)             # Accessing public attribute
    print(base._protected)         # Accessing protected attribute
    print(base.get_private())      # Accessing private attribute via public method
    print(base.call_private_method())  # Calling private method via public method

    derived = Derived()
    print(derived.public)          # Accessing public attribute in derived class
    print(derived._protected)      # Accessing protected attribute in derived class
    print(derived.get_private())   # Accessing private attribute in base class via public method
    print(derived.get_derived_private())  # Accessing private attribute in derived class

    # Demonstrating name mangling
    print(derived._Base__private)  # Accessing base class private attribute directly
    print(derived._Base__private_method())  # Calling base class private method directly
```

## Key Features 🌟
- **Class Definition and Inheritance**: Learn how to define classes and use inheritance to extend these classes.
- **Encapsulation and Access Modifiers**: Understand how to use private and protected modifiers to control access to attributes.
- **Special Methods**: Explore how to define and use special methods for object representation and comparison.
- **Attribute Access**: Learn how attribute access and method calls are managed within an inheritance hierarchy.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended.
- **External Libraries**: None required, as the demonstration uses Python's core features.

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `23_inherit_class_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `23_inherit_class_demo.py`.
5. Run the script with: `python 23_inherit_class_demo.py`.

## Usage Example 📋
Execute the script to understand how base and derived classes handle attribute accessibility and how encapsulation affects object interaction.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*
---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>