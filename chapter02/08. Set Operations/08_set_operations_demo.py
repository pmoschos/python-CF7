# Set demo with items in a bag
bag = {"eggs", "apples", "bananas", "eggs"}  # Duplicate "eggs" will be automatically removed
print("Initial bag contents:", bag)

# Add a new item to the set
bag.add("oranges")
print("\nAfter adding 'oranges':", bag)

bag.add("oranges")
print("\nAfter second adding 'oranges':", bag)

# Attempt to remove an item that may not be in the set
item_to_remove = "eggs2"
# bag.remove(item_to_remove) # KeyError

if item_to_remove in bag:
    bag.remove(item_to_remove)
else:
    print(f"\n'{item_to_remove}' not found in the bag.")

# Iterate through the set
print("\nIterating through the bag:")
for item in bag:
    print(item)