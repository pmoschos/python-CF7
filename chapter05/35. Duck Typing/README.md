# 🚗 Vehicle Polymorphism Demo Script 🔧

This Python script demonstrates polymorphism in object-oriented programming by defining a `Vehicle` class and multiple subclasses, each implementing the `drive` method differently. It also includes an unrelated class (`Hoverboard`) that exhibits similar behavior and a subclass (`Boat`) that does not fully implement the abstract behavior.

---

## Script Overview 📘

The script defines the following classes and methods:

1. **`Vehicle` Abstract Class**: Serves as a base class with an unimplemented `drive` method.
2. **Concrete Subclasses**:
   - **`Car`**: Implements the `drive` method to simulate driving a car.
   - **`Bicycle`**: Implements the `drive` method to simulate riding a bicycle.
3. **Unrelated Class**:
   - **`Hoverboard`**: Implements a `drive` method but does not inherit from `Vehicle`.
4. **Incomplete Subclass**:
   - **`Boat`**: Extends `Vehicle` but does not implement the `drive` method, demonstrating what happens when a subclass does not meet its contract.
5. **Polymorphic Function**: `drive_vehicle` calls the `drive` method of any object passed to it, demonstrating Python’s duck typing.

### :computer: Script Code

```python
class Vehicle:
    def drive(self):
        # print("Driving...")
        raise NotImplementedError("Subclasses should implement this!")

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bicycle(Vehicle):
    def drive(self):
        print("Riding a bicycle")

# A class that does not extend Vehicle but has a drive method
# The behavior of a class in Python is more important than the type of the instance.
class Hoverboard:
    def drive(self):
        print("Hovering on a hoverboard")

# A class that extends Vehicle but does not implement the drive method
class Boat(Vehicle):
    def sail(self):
        print("Sailing a boat")

# Polymorphic method
def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can't drive.")

def main():
    # Instances of each class
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = Hoverboard()
    my_boat = Boat()

    # Calling the drive_vehicle function with different objects
    drive_vehicle(my_car)        # Output: Driving a car
    drive_vehicle(my_bicycle)    # Output: Riding a bicycle
    drive_vehicle(my_hoverboard) # Output: Hovering on a hoverboard

    try:
        drive_vehicle(my_boat)       # Output: Boat can't drive.
    except NotImplementedError as e:
        print(e)

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Polymorphism**: Demonstrates how different objects respond to the same method call.
- **Duck Typing**: Highlights that behavior is more important than inheritance in Python.
- **Abstract Base Class**: Uses an abstract method to enforce a contract on subclasses.
- **Error Handling**: Safely handles cases where the contract is not fulfilled.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `35_duck_typing.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `35_duck_typing.py`.
5. Run the script with:

   ```bash
   python 35_duck_typing.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Driving a car
Riding a bicycle
Hovering on a hoverboard
Boat can't drive.
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

