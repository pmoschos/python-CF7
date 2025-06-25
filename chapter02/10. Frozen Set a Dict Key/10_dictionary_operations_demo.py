# Define a dictionary with diverse key-value pairs
sym = {
    frozenset({1, 2, 3}): "Hello",  # Immutable frozenset as a key
    "key1": "value1",  # String key with string value
    "key2": 10,  # String key with integer value
    3: [1, 2, 3],  # Integer key with list value
    4: {1: "one", 2: "two"}  # Integer key with nested dictionary as value
}

# Print the entire dictionary
print(sym)