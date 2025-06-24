# Dictionary CRUD functions

# Initial dictionary of products
products = {1: "apples", 2: "bananas", 10: "honey", 3: "melons"}
print("Initial products:", products)

# Create: Insert a new item
products[3] = "oranges"
print("\nAfter inserting key 3 with value 'oranges':", products)

# Read: Access elements by key
product_10 = products.get(10, "Not Found")
print("\nProduct with key 10:", product_10)

# Update: Change the value of an existing item
products[2] = "milk"
print("\nAfter updating key 2 to 'milk':", products)

# Delete: Remove an item by key using del
del products[1]
print("\nAfter deleting key 1:", products)

# Delete: Remove an item by key using pop() and handle potential KeyError
removed_product = products.pop(3, "Not Found")
print("\nAfter popping key 3:", products)
print("Popped product:", removed_product)

# Delete: Remove the last inserted item using popitem()
key, value = products.popitem()
print("\nAfter popping the last item inserted:", products)
print(f"Popped item - Key: {key}, Value: {value}")

# Check for key existence
key_to_check = 2
if key_to_check in products:
    print(f"\nKey {key_to_check} exists in products.")
else:
    print(f"\nKey {key_to_check} does not exist in products.")

# Iterating through keys
print("\nIterating through keys:")
for key in products.keys():
    print(f"Key: {key}, Value: {products[key]}")

# Iterating through values
print("\nIterating through values:")
for value in products.values():
    print(f"Value: {value}")

# Iterating through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in products.items():
    print(f"Key: {key}, Value: {value}")