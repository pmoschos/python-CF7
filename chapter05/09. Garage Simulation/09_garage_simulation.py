from collections import deque

def display_garage(garage: deque) -> None:
    """
    Displays the current state of the garage.

    Parameters:
    garage (deque): The deque representing the garage.

    Returns:
    None
    """
    if garage:
        print("\nCurrent cars in the garage:")
        for i, car in enumerate(garage, 1):
            print(f"{i}. {car}")
    else:
        print("\nThe garage is empty.")

def add_car_to_garage(garage: deque, max_capacity: int) -> None:
    """
    Adds a car to the garage if there is available space.

    Parameters:
    garage (deque): The deque representing the garage.
    max_capacity (int): The maximum number of cars the garage can hold.

    Returns:
    None
    """
    if len(garage) < max_capacity:
        car_name = input("Enter the name or ID of the car: ")
        garage.append(car_name)
        print(f"{car_name} has entered the garage.")
    else:
        print("The garage is full! Cannot add more cars.")

def remove_car_from_garage(garage: deque) -> None:
    """
    Removes the first car from the garage if it is not empty.

    Parameters:
    garage (deque): The deque representing the garage.

    Returns:
    None
    """
    if garage:
        car_left = garage.popleft()
        print(f"{car_left} has left the garage.")
    else:
        print("The garage is empty! No cars to remove.")

def main() -> None:
    """
    Main function to simulate cars arriving and leaving a garage using deque.

    The program allows users to:
    1. Add a car to the garage.
    2. Remove the first car from the garage.
    3. Display the current state of the garage.
    4. Exit the simulation.

    Returns:
    None
    """
    garage = deque()  # Create a deque to represent the garage
    max_capacity = 5  # Maximum number of cars the garage can hold

    while True:
        print("\nOptions:")
        print("1. Add a car to the garage")
        print("2. Remove the first car from the garage")
        print("3. Display the garage state")
        print("4. Exit")

        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        match choice:
            case 1:
                add_car_to_garage(garage, max_capacity)

            case 2:
                remove_car_from_garage(garage)

            case 3:
                display_garage(garage)

            case 4:
                print("Exiting the program. Goodbye!")
                break

            case _:
                print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
