class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Make the object iterable by returning an iterator of `data`
        return iter(self.data)

    def __getitem__(self, index):
        # Return the item at the given index
        return self.data[index]

    def __len__(self):
        # Return the length of the collection
        return len(self.data)

    def __repr__(self):
        # Return a string representation of the collection
        return f"DataCollection({self.data})"

def main():
    # Create an instance of DataCollection
    collection = DataCollection([1, 2, 3, 4])

    # Print the DataCollection object
    print("DataCollection object:", collection)  # Output: DataCollection object: DataCollection([1, 2, 3, 4])

    # Iterating over DataCollection instance
    print("Iterating over collection:")
    for item in collection:
        print(item)  # Output: 1, 2, 3, 4

    # Unpacking the DataCollection instance
    a, b, c, d = collection
    print("Unpacked values:", a, b, c, d)  # Output: 1 2 3 4

    # Indexing to access individual elements
    print("Element at index 0:", collection[0])  # Output: Element at index 0: 1
    print("Element at index 3:", collection[3])  # Output: Element at index 3: 4

    # Getting the length of the collection
    print("Length of collection:", len(collection))  # Output: Length of collection: 4

    # Demonstrating slicing (works because of __getitem__)
    print("Slice of collection:", collection[1:3])  # Output: Slice of collection: [2, 3]

if __name__ == "__main__":
    main()
