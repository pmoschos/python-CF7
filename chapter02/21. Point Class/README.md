# 📐 Python Class for 2D Point Operations Demonstration ➕

Welcome to the Python Class for 2D Point Operations Demonstration! This script showcases how to define and utilize a class in Python, using the `Point` class as an example to demonstrate object-oriented programming in handling 2D space calculations. It's an ideal resource for anyone new to Python or those teaching programming concepts related to classes and object interactions.

## Script Overview 📘

The script demonstrates how to define a `Point` class with methods for initializing, displaying, and calculating the distance between points. The usage of the math library to handle calculations exemplifies integrating Python's built-in libraries in custom classes.

### :computer: Script Code

```python
import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x=0, y=0):
        """
        Initialize a Point object with the specified x and y coordinates.

        Args:
            x (float): The x-coordinate of the point. Defaults to 0.
            y (float): The y-coordinate of the point. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the Point object.

        Returns:
            str: A string representation of the Point object in the format (x, y).
        """
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): Another Point object to calculate the distance to.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Distance between points: {p1.distance_to(p2)}")

    # Updating the point coordinates directly
    p1.x = 15
    p1.y = 25
    print(f"Updated p1: {p1}")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Class Definition and Object Manipulation**: Learn how to define classes in Python, instantiate objects, and modify object attributes.
- **Euclidean Distance Calculation**: Understand how to implement mathematical formulas within methods to calculate distances between points.
- **Integration with Python Libraries**: Discover how to leverage Python's built-in `math` library to perform complex mathematical operations.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: `math` library used for mathematical operations.

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `21_point_class_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `21_point_class_demo.py`.
5. Run the script with: `python 21_point_class_demo.py`.

## Usage Example 📋
Execute the script to create Point objects, calculate the distance between them, and update their coordinates. This practical demonstration helps understand the implementation and utility of Python classes in simulating real-world entities and relationships.

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