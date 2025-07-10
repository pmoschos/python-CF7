# 📚 DataCollection Class Demo Script 📂

This Python script demonstrates the implementation and usage of the `DataCollection` class. The class encapsulates a collection of data, providing functionalities like iteration, indexing, slicing, and length calculation, while also offering a string representation for easy debugging.

---

## Script Overview 📘

The script defines a `DataCollection` class with the following features:

1. **Iterable Object**: Implements `__iter__` to allow iteration over the collection.
2. **Indexing and Slicing**: Implements `__getitem__` to support direct indexing and slicing.
3. **Length Calculation**: Implements `__len__` to return the number of elements in the collection.
4. **String Representation**: Implements `__repr__` for clear output during debugging.

### :computer: Script Code

```python
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
```

---

## Key Features 🌟

- **Iteration**: Supports iteration over the collection using `for` loops.
- **Indexing and Slicing**: Allows accessing specific elements or slices of the collection.
- **Unpacking**: Enables unpacking of elements directly into variables.
- **Length Retrieval**: Provides the size of the collection using `len()`.
- **Debug-Friendly**: Includes a string representation for easy debugging and informative output.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `33_iterable_data_class.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `33_iterable_data_class.py`.
5. Run the script with:

   ```bash
   python 33_iterable_data_class.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
DataCollection object: DataCollection([1, 2, 3, 4])
Iterating over collection:
1
2
3
4
Unpacked values: 1 2 3 4
Element at index 0: 1
Element at index 3: 4
Length of collection: 4
Slice of collection: [2, 3]
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