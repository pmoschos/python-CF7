# 🧭 Point Class Demo Script 📍

This Python script demonstrates the use of the `Point` class, which encapsulates a 2D point with coordinates (x, y). It showcases object-oriented principles such as encapsulation, operator overloading, and property management.

---

## Script Overview 📘

The script defines a `Point` class with the following features:

1. **Encapsulation**: Uses private attributes (`__x`, `__y`) to store coordinates.
2. **Operator Overloading**: Supports addition (`+`), equality comparison (`==`), and summing a list of points (`sum`).
3. **Properties**: Provides getter and setter methods for `x` and `y` coordinates.
4. **Dynamic Usability**: Demonstrates operations like modifying coordinates, adding points, and checking equality.

Additionally, the script includes a utility function, `do_add`, to demonstrate generic addition.

### :computer: Script Code

```python
class Point:
    def __init__(self, x, y):
        """
        Initialize a point with coordinates (x, y).
        """
        self.__x = x
        self.__y = y
    
    def __str__(self):
        """
        Return a string representation of the point.
        """
        return f"({self.__x}, {self.__y})"
    
    def __add__(self, other):
        """
        Add a point or a number to the current point.
        """
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y + other)
        else:
            raise TypeError(f"Unsupported operand types for +: 'Point' and {type(other).__name__}")
    
    def __radd__(self, other):
        """
        Add the current point to a number (for right-side addition).
        """
        return self.__add__(other)
    
    def __eq__(self, other):
        """
        Check if two points are equal.
        """
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
    
    @property
    def x(self):
        """
        Get the x-coordinate of the point.
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the point.
        """
        self.__x = value
    
    @property
    def y(self):
        """
        Get the y-coordinate of the point.
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the point.
        """
        self.__y = value

def do_add(a, b):
    """
    Add two objects using the + operator.
    """
    return a + b

def main():
    """
    Main function to demonstrate the usage of the Point class and do_add function.
    """
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print("p1 + p2 =", p1 + p2)  # (4, 6)
    print("p1 + 10 =", p1 + 10)  # (11, 12)
    print("sum([p1, p2]) =", sum([p1, p2]))  # (4, 6)
    print("p1 == Point(1, 2) =", p1 == Point(1, 2))  # True
    print("p1 == 'Hello' =", p1 == "Hello")  # False

    print("do_add(Point(10, 20), Point(5, 5)) =", do_add(Point(10, 20), Point(5, 5)))  # (15, 25)

    # Accessing private fields via properties
    print("p1 x-coordinate:", p1.x)  # 1
    print("p1 y-coordinate:", p1.y)  # 2

    # Modifying private fields via setters
    p1.x = 100
    p1.y = 200
    print("Modified p1:", p1)  # (100, 200)

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Encapsulation**: Protects attributes with private naming conventions.
- **Operator Overloading**: Enhances usability with custom `+` and `==` operators.
- **Property Management**: Provides controlled access to private attributes.
- **Flexible Addition**: Supports adding points to other points or numbers.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `31_point_class.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `31_point_class.py`.
5. Run the script with:

   ```bash
   python 31_point_class.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
p1 + p2 = (4, 6)
p1 + 10 = (11, 12)
sum([p1, p2]) = (4, 6)
p1 == Point(1, 2) = True
p1 == 'Hello' = False
do_add(Point(10, 20), Point(5, 5)) = (15, 25)
p1 x-coordinate: 1
p1 y-coordinate: 2
Modified p1: (100, 200)
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