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