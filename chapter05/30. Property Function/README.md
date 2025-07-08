# 🎓 Person Class Demo Script 🔄

This Python script demonstrates the use of encapsulation, property management, and dynamic attributes using a `Person` class. It showcases how to create and manage properties dynamically while adhering to object-oriented programming principles.

---

## Script Overview 📘

The script defines a `Person` class with the following capabilities:

1. **Encapsulation**: Demonstrates private attributes using a leading underscore convention (`_name`).
2. **Property Management**: Implements a property for the `name` attribute with getter, setter, and deleter methods.
3. **Dynamic Attributes**: Allows dynamic addition of attributes to instances (e.g., adding a `friends` list dynamically).

### :computer: Script Code

```python
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
```

---

## Key Features 🌟

- **Encapsulation**: Protects class attributes with private naming conventions.
- **Dynamic Attributes**: Supports adding attributes to instances dynamically (e.g., `friends` list).
- **Property Usage**: Implements getter, setter, and deleter methods for controlled access and modification.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `30_property_function.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `30_property_function.py`.
5. Run the script with:

   ```bash
   python 30_property_function.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Getting name: John
Setting name: Jane
Getting name: Jane
Deleting name
Name attribute has been deleted

Printing friends:
 - Bob
 - Alice
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

