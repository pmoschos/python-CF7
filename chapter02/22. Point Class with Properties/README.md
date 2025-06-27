# ✨ Python Class Demonstration: `Point` with Magic Methods 🔮

Welcome to the Python `Point` Class Demonstration! This script introduces a `Point` class, showcasing advanced features such as encapsulation, class-level attributes, operator overloading, and property management. It’s an excellent guide for understanding object-oriented programming (OOP) in Python.

## Script Overview 📘

The script demonstrates:
- Encapsulation using private attributes.
- Operator overloading for string representation, equality, and comparison.
- Class-level attributes and methods.
- Using properties for getter and setter methods.

### 💻 Script Code

```python
class Point:
    __count = 0  # Class-level private attribute to track instances

    def __init__(self, x=0, y=0):
        self.__x = x  # Private instance attribute
        self.__y = y  # Private instance attribute
        Point.__count += 1  # Increment instance count

    def __str__(self):
        return f"({self.__x}, {self.__y})"  # String representation

    def __repr__(self):
        return f"Point(x={self.__x},y={self.__y})"  # Debug representation

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y  # Equality check
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.__x <= other.__x and self.__y < other.__y) \
                    or (self.__x < other.__x and self.__y <= other.__y)  # Comparison
        else:
            return False

    @classmethod
    def get_count(cls):
        return cls.__count  # Class method to get instance count

    # Properties for `x`
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    # Properties for `y`
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


# Main function to demonstrate usage
def main():
    p1 = Point(11, 20)
    p2 = Point(11, 20)

    print(p1 < p2)  # Demonstrating overloaded `<` operator

if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Encapsulation**: Demonstrates private attributes and controlled access through properties.
- **Operator Overloading**: Implements `__str__`, `__repr__`, `__eq__`, and `__lt__` for customized behavior.
- **Class-Level Attributes and Methods**: Uses a class attribute to track the number of instances and a class method to access it.
- **Properties**: Simplifies getter and setter methods with Python's `@property` decorator.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `22_point_class_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `22_point_class_demo.py`.
5. Run the script with the command: `python 22_point_class_demo.py`.

## Usage Example 📋

Executing the script demonstrates the creation of `Point` objects, comparisons using overloaded operators, and access to instance and class-level data. The examples highlight OOP principles and Python's flexibility with custom classes.

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