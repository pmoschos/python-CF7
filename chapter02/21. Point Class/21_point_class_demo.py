import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x=0, y=0):
        """
        Initialize a Point object with the specified x and y coordinates.

        Args:
            x (float): The x-coordinate of the point. Defaults to 0.
            y (float): The y-coordinate of the point. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the Point object.

        Returns:
            str: A string representation of the Point object in the format (x, y).
        """
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            other (Point): Another Point object to calculate the distance to.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Distance between points: {p1.distance_to(p2)}")

    # Updating the point coordinates directly
    p1.x = 15
    p1.y = 25
    print(f"Updated p1: {p1}")

if __name__ == "__main__":
    main()