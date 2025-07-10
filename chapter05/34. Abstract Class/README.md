# 🛡️ Abstract Classes Demo Script 🔄

This Python script demonstrates the use of abstract base classes (ABCs) to define APIs for two different contexts: a Student DAO (Data Access Object) and an Inventory system. The script provides concrete implementations of these abstract classes and showcases their functionality through example usage.

---

## Script Overview 📘

The script defines two abstract classes:

1. **AbstractStudentDAO**: Defines the interface for a Student DAO, with methods to insert, update, delete, and retrieve students.
2. **ABCInventory**: Defines the interface for an Inventory system, with methods to add and remove items.

Concrete implementations (`StudentImpl` and `Inventory`) are provided to demonstrate the functionality of these abstract classes. The script also includes an `Item` class to represent inventory items.

### :computer: Script Code

```python
from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Defines the Student DAO API"""

    @abstractmethod
    def insert(self, student):
        """Insert a new student"""
        raise NotImplementedError()

    @abstractmethod
    def update(self, student_id, student):
        """Update an existing student"""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, student_id):
        """Delete a student"""
        raise NotImplementedError()

    @abstractmethod
    def getOne(self, student_id):
        """Get a student by ID"""
        raise NotImplementedError()

class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student['id']
        self.students[student_id] = student
        print(f"Inserted student with ID: {student_id}")

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with ID: {student_id}")
        else:
            print(f"Student with ID: {student_id} not found")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with ID: {student_id}")
        else:
            print(f"Student with ID: {student_id} not found")

    def getOne(self, student_id):
        return self.students.get(student_id, None)

class ABCInventory(ABC):

    @abstractmethod
    def add_item(self, item):
        """Add an item to the inventory"""
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        """Remove an item from the inventory"""
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory"""
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item_name_to_remove):
        """Remove an item from the inventory by name"""
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item)
                print(f"Removed item: {item_name_to_remove}")
                return
        print(f"Item not found: {item_name_to_remove}")

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Example usage
def main():
    # Student implementation example
    student_dao = StudentImpl()
    student_dao.insert({'id': 1, 'name': 'John Doe'})
    student_dao.update(1, {'id': 1, 'name': 'John Smith'})
    student = student_dao.getOne(1)
    print(f"Retrieved student: {student}")
    student_dao.delete(1)
    student = student_dao.getOne(1)
    print(f"Retrieved student after deletion: {student}")

    # Inventory implementation example
    inventory = Inventory()
    item1 = Item("Laptop")
    item2 = Item("Phone")
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.remove_item("Laptop")
    inventory.remove_item("Tablet")  # This will print "Item not found: Tablet"

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Abstract Base Classes**: Demonstrates the use of `ABC` and `abstractmethod` to define clear APIs.
- **Concrete Implementations**: Provides practical implementations for both the Student DAO and Inventory systems.
- **Polymorphism**: Ensures consistent behavior through standardized interfaces.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `34_abstract_class.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `34_abstract_class.py`.
5. Run the script with:

   ```bash
   python 34_abstract_class.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Inserted student with ID: 1
Updated student with ID: 1
Retrieved student: {'id': 1, 'name': 'John Smith'}
Deleted student with ID: 1
Retrieved student after deletion: None
Added item: Laptop
Added item: Phone
Removed item: Laptop
Item not found: Tablet
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