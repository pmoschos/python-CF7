# 🏬 Inventory Management Script 🛒

This Python script demonstrates inventory management using object-oriented principles. It allows adding, removing, and managing items in an inventory, including custom exception handling for out-of-stock scenarios.

---

## Script Overview 📘

The script defines the following classes and functionalities:

1. **Custom Exception**:
   - **`OutOfStockError`**: Raised when attempting to remove an item that is out of stock.

2. **Item Class**:
   - Represents an inventory item with attributes for `name` and `quantity`.
   - Supports equality checks and hashable behavior for inventory management.

3. **Inventory Class**:
   - Manages a collection of items, allowing for adding, removing, and printing items.
   - Handles scenarios where items are out of stock or not found in the inventory.

### :computer: Script Code

```python
class OutOfStockError(Exception):
    """
    Custom exception to be raised when an item is out of stock.
    """
    def __init__(self, item_name):
        super().__init__(f"{item_name} is out of stock")

class Item:
    """
    Represents an item in the inventory.
    
    Attributes:
        name (str): The name of the item.
        quantity (int): The quantity of the item in stock.
    """
    def __init__(self, name, quantity):
        """
        Initializes the item with a name and quantity.
        
        Parameters:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
        """
        self.name = name
        self.quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the item.
        """
        return f"{self.name}, {self.quantity}"
    
    def __eq__(self, other):
        """
        Checks equality based on the item name.
        
        Parameters:
            other (Item): The other item to compare.
        
        Returns:
            bool: True if the item names are the same, False otherwise.
        """
        if not isinstance(other, Item):
            return False
        return self.name == other.name
    
    def __hash__(self):
        """
        Returns a hash value for the item based on its name.
        
        Returns:
            int: The hash value of the item name.
        """
        return hash(self.name)

class Inventory:
    """
    Represents an inventory of items.
    
    Attributes:
        items (list): A list of items in the inventory.
    """
    def __init__(self):
        """
        Initializes the inventory with an empty list of items.
        """
        self.items = []
    
    def add_item(self, item):
        """
        Adds an item to the inventory. If the item already exists, its quantity is updated.
        
        Parameters:
            item (Item): The item to add.
        """
        for existing_item in self.items:
            if existing_item == item:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)
    
    def remove_item(self, item_name_to_remove):
        """
        Removes an item from the inventory. If the item is not found or out of stock, raises an error.
        
        Parameters:
            item_name_to_remove (str): The name of the item to remove.
        
        Returns:
            Item: The item with updated quantity after removal.
        
        Raises:
            ValueError: If the item is not found in the inventory.
            OutOfStockError: If the item is out of stock.
        """
        # Check if the item exists in the inventory
        if Item(item_name_to_remove, None) not in self.items:
            raise ValueError(f"{item_name_to_remove} is not in the inventory")
        
        # Find the item and update its quantity
        for item in self.items:
            if item == Item(item_name_to_remove, None):
                if item.quantity > 0:
                    item.quantity -= 1
                    return Item(item.name, item.quantity)
                else:
                    raise OutOfStockError(item.name)

    def print_items(self):
        """
        Prints all items in the inventory.
        """
        for item in self.items:
            print(item)

# Example usage
def main():
    # Initialize inventory
    inventory = Inventory()

    # Add items to the inventory
    inventory.add_item(Item("Laptop", 10))
    inventory.add_item(Item("Phone", 5))
    inventory.add_item(Item("Laptop", 5))  # Update quantity of existing item

    # Print current inventory
    print("Current Inventory:")
    inventory.print_items()

    # Remove items and handle exceptions
    try:
        print("\nRemoving items:")
        print(inventory.remove_item("Laptop"))  # Should decrease quantity by 1
        print(inventory.remove_item("Tablet"))  # Should raise ValueError
    except ValueError as ve:
        print(ve)
    except OutOfStockError as ose:
        print(ose)

    # Remove all Laptops
    print("\nRemoving all Laptops:")
    while True:
        try:
            print(inventory.remove_item("Laptop"))
        except OutOfStockError as ose:
            print(ose)
            break

    # Print updated inventory
    print("\nUpdated Inventory:")
    inventory.print_items()

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Custom Exceptions**: Handles out-of-stock scenarios with the `OutOfStockError` exception.
- **Dynamic Item Management**: Supports adding, updating, and removing inventory items.
- **Error Handling**: Manages scenarios where items are not found or cannot be removed.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `store.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `store.py`.
5. Run the script with:

   ```bash
   python store.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Current Inventory:
Laptop, 15
Phone, 5

Removing items:
Laptop, 14
Tablet is not in the inventory

Removing all Laptops:
Laptop, 13
...
Laptop is out of stock

Updated Inventory:
Phone, 5
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