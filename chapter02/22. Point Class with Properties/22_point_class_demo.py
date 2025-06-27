class Point:
    __count = 0  # Class-level private attribute to track instances

    def __init__(self, x=0, y=0):
        self.__x = x  # Private instance attribute
        self.__y = y  # Private instance attribute
        Point.__count += 1  # Increment instance count

    def __str__(self):
        return f"({self.__x}, {self.__y})"  # String representation

    def __repr__(self):
        return f"Point(x={self.__x},y={self.__y})"  # Debug representation

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y  # Equality check
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.__x <= other.__x and self.__y < other.__y) \
                    or (self.__x < other.__x and self.__y <= other.__y)  # Comparison
        else:
            return False

    @classmethod
    def get_count(cls):
        return cls.__count  # Class method to get instance count

    # Properties for `x`
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    # Properties for `y`
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


# Main function to demonstrate usage
def main():
    p1 = Point(11, 20)
    p2 = Point(11, 20)

    print(p1 < p2)  # Demonstrating overloaded `<` operator

if __name__ == "__main__":
    main()