class Person:
    """
    A class to represent a person with a name property.
    Demonstrates encapsulation, property management, and dynamic attributes.
    """
    def __init__(self, name):
        self._name = name  # Private attribute

    def get_name(self):
        """
        Getter for the 'name' property.
        Returns the name if it exists, or a message if it has been deleted.
        """
        if not hasattr(self, '_name'):
            return "Name attribute has been deleted"
        print("Getting name", end=': ')
        return self._name

    def set_name(self, value):
        """
        Setter for the 'name' property.
        Ensures the name is a string before setting it.
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name", end=': ')
        self._name = value

    def del_name(self):
        """
        Deleter for the 'name' property.
        Deletes the name attribute and notifies the user.
        """
        print("Deleting name")
        del self._name

    # Create property using property() function
    name = property(get_name, set_name, del_name, "This is the 'name' property")

def main():
    """
    Main function to demonstrate the functionality of the Person class.
    Includes examples of using properties and dynamically adding attributes.
    """
    # Create a Person instance
    p = Person("John")

    # Access and modify the 'name' property
    print(p.name)       # Getting name -> John
    p.name = "Jane"     # Setting name
    print(p.name)       # Getting name -> Jane
    del p.name          # Deleting name
    print(p.name)       # Attempt to get name after deletion

    # Add a new dynamic property to the Person instance
    p.friends = []  # Initialize an empty list for friends
    p.friends.append("Bob")
    p.friends.append("Alice")

    # Display the friends list
    print(f"\nPrinting friends:")
    for friend in p.friends:
        print(f" - {friend}")
    print()

if __name__ == "__main__":
    main()
