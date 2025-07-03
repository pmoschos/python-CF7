# 🚗 Garage Simulation Using Deque and Class 🔄

This script demonstrates how to simulate cars arriving and leaving a garage using Python's `collections.deque` class and object-oriented programming principles. The `deque` class is used for its efficient appending and popping operations, and a `Garage` class is created to manage the cars in the garage.

## Script Overview 📘

The script defines a `Garage` class with methods to handle cars arriving, leaving, and finding their positions within the garage. The `main` function simulates various actions within the garage.

### :computer: Script Code

```python
from collections import deque

class Garage:
    def __init__(self, capacity):
        self.garage = deque()
        self.capacity = capacity

    def car_arrives(self, car):
        if len(self.garage) < self.capacity:
            self.garage.append(car)
            print(f"{car} arrived. Current state of the garage: {list(self.garage)}")
        else:
            print(f"{car} cannot arrive. Garage is full. Current state of the garage: {list(self.garage)}")

    def car_leaves(self):
        if self.garage:
            car = self.garage.popleft()
            print(f"{car} left. Current state of the garage: {list(self.garage)}")
            return car
        else:
            print("No cars in the garage to leave.")
            return None

    def find_car(self, car):
        if car in self.garage:
            position = list(self.garage).index(car) + 1
            print(f"{car} is in the garage at position {position}.")
        else:
            print(f"{car} is not in the garage.")

def main():
    """
    Main function to simulate cars arriving and leaving a garage using deque.
    """
    garage_capacity = 5
    garage = Garage(garage_capacity)

    # Simulate some cars arriving in the garage
    garage.car_arrives("Car 1")
    garage.car_arrives("Car 2")
    garage.car_arrives("Car 3")
    garage.car_arrives("Car 4")

    # Simulate a car leaving the garage (FIFO)
    last_car_left = garage.car_leaves()

    # Simulate more cars arriving in the garage
    garage.car_arrives("Car 5")
    garage.car_arrives("Car 6")  # This should fail due to capacity

    # Simulate more cars leaving the garage
    garage.car_leaves()
    garage.car_leaves()
    garage.car_leaves()

    # Attempt to leave when garage might be empty
    garage.car_leaves()
    garage.car_leaves()
    garage.car_leaves()  # This should print an error message

    # Find specific cars
    garage.find_car("Car 2")
    garage.find_car("Car 6")

    # Print the last car that left the garage
    if last_car_left:
        print("Last car which left the garage:", last_car_left)
    else:
        print("No cars have left the garage yet.")

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Deque Usage**: Learn how to use the `deque` class from the `collections` module for efficient FIFO operations.
- **Class Implementation**: Discover how to encapsulate functionality using a class to manage the garage.
- **Simulating Processes**: Understand how to simulate real-world processes, such as cars arriving and leaving a garage.
- **Finding Elements**: See how to find the position of an element within a `deque`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses the built-in `collections` module)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `09_garage_simulation.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `09_garage_simulation.py`.
5. Run the script with: `python 09_garage_simulation.py`.

## Usage Example 📋
Execute the script to see how the `Garage` class and `deque` can be used to simulate a garage. The script will demonstrate cars arriving and leaving the garage, printing the current state of the garage, and finding specific cars.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
