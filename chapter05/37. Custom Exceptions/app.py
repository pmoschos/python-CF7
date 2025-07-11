from store import * # Inventory, Item, OutOfStockError

def main():
    """
    Main function to demonstrate the functionality of the inventory system.
    """
    # Create an inventory
    inventory = Inventory()
    
    # Add items to inventory
    inventory.add_item(Item("Apple", 10))
    inventory.add_item(Item("Banana", 5))
    inventory.add_item(Item("Apple", 5))  # Increase quantity of existing item
    
    # Print current inventory
    print("Current inventory:")
    inventory.print_items()
    
    # Remove an item from inventory
    print("\nRemoving an Apple...")
    inventory.remove_item("Apple")
    inventory.print_items()
    
    # Try to remove an item not in inventory
    try:
        inventory.remove_item("Orange")
    except ValueError as e:
        print(e)
    
    # Try to remove more items than available
    try:
        for _ in range(20):
            inventory.remove_item("Banana")
    except OutOfStockError as e:
        print(e)

if __name__ == "__main__":
    main()