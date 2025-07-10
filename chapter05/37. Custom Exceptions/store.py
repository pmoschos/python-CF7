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