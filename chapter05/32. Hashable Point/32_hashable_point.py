# Define the Point class
class Point:
    def __init__(self, x, y):
        self._x = x        
        self._y = y

    def __eq__(self, other):
        """
        Check if two Point instances are equal.
        Equality is based on x and y coordinates.
        """
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

    def __hash__(self):
        """
        Provide a hash value for Point instances.
        Hash is based on the tuple (x, y), which ensures that the hash is unique 
        for different coordinate pairs.
        """
        return hash((self._x, self._y))  # Using a tuple of (x, y) ensures immutability

    def __repr__(self):
        """
        Provide a string representation for Point instances for easier debugging and printing.
        """
        return f"Point({self._x}, {self._y})"

def main():
    # Create instances of Point
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)  # Same coordinates as p1

    # Demonstrate equality and hash behavior
    print("Comparing Points:")
    print(f"p1 == p3: {p1 == p3}")  # True, since they have the same coordinates
    print(f"p1 == p2: {p1 == p2}")  # False, since coordinates differ

    print("\nHash Values:")
    print(f"hash(p1): {hash(p1)}")  # Hash of p1
    print(f"hash(p3): {hash(p3)}")  # Hash of p3 should be the same as hash(p1)
    print(f"hash(p2): {hash(p2)}")  # Hash of p2 should be different from p1 and p3

    # Create a dictionary with Point instances as keys
    point_dict = {
        p1: "Point 1",  # Adding p1 with value "Point 1"    
        p2: "Point 2",  # Adding p2 with value "Point 2"    
        p3: "Point 3"   # p3 has the same coordinates as p1, so it should update the value of p1's key
    }

    # Display the dictionary
    print("\nDictionary Contents:")
    for key, value in point_dict.items():
        print(f"{key}: {value}")

    # Accessing the values using the Point instances
    print("\nAccessing Dictionary Values:")
    print(f"Value for p1: {point_dict[p1]}")  # Output: Point 3
    print(f"Value for p2: {point_dict[p2]}")  # Output: Point 2
    print(f"Value for p3: {point_dict[p3]}")  # Output: Point 3

if __name__ == "__main__":
    main()
