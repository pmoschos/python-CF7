class Point:
    """
    A class to represent a point in 2D space.

    Attributes:
    ----------
    x : float
        x-coordinate of the point
    y : float
        y-coordinate of the point
    """
    def __init__(self, x, y):
        """
        Initializes the Point with x and y coordinates.
        
        Parameters:
        ----------
        x : float
            x-coordinate of the point
        y : float
            y-coordinate of the point
        """
        self.__x = x
        self.__y = y
    
    def __str__(self):
        """Returns the string representation of the Point."""
        return f"({self.__x}, {self.__y})"
    
    def __add__(self, other):
        """
        Adds two Point objects or a Point object and a number.

        Parameters:
        ----------
        other : Point or float
            The Point or number to be added to this Point

        Returns:
        -------
        Point
            A new Point object that is the sum of the two points
        """
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y + other)
        else:
            raise TypeError(f"Unsupported operand types for +: 'Point' and {type(other).__name__}")
    
    def __radd__(self, other):
        """Handles the case when the addition is performed with the Point object on the right."""
        return self.__add__(other)
    
    def __sub__(self, other):
        """
        Subtracts a Point object or a number from this Point.

        Parameters:
        ----------
        other : Point or float
            The Point or number to be subtracted from this Point

        Returns:
        -------
        Point
            A new Point object that is the difference of the points
        """
        if isinstance(other, Point):
            return Point(self.__x - other.__x, self.__y - other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x - other, self.__y - other)
        else:
            raise TypeError(f"Unsupported operand types for -: 'Point' and {type(other).__name__}")
    
    def __rsub__(self, other):
        """Handles the case when the subtraction is performed with the Point object on the right."""
        if isinstance(other, (int, float)):
            return Point(other - self.__x, other - self.__y)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """
        Multiplies this Point by a number.

        Parameters:
        ----------
        other : float
            The number to multiply with this Point

        Returns:
        -------
        Point
            A new Point object that is the product of the point and the number
        """
        if isinstance(other, (int, float)):
            return Point(self.__x * other, self.__y * other)
        else:
            raise TypeError(f"Unsupported operand types for *: 'Point' and {type(other).__name__}")
    
    def __rmul__(self, other):
        """Handles the case when the multiplication is performed with the Point object on the right."""
        return self.__mul__(other)
    
    def __eq__(self, other):
        """
        Checks if two Point objects are equal.

        Parameters:
        ----------
        other : Point
            The Point to compare with this Point

        Returns:
        -------
        bool
            True if the points are equal, False otherwise
        """
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False

    def __ne__(self, other):
        """
        Checks if two Point objects are not equal.

        Parameters:
        ----------
        other : Point
            The Point to compare with this Point

        Returns:
        -------
        bool
            True if the points are not equal, False otherwise
        """
        return not self.__eq__(other)
    
    @property
    def x(self):
        """Gets the x-coordinate of the point."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the point."""
        self.__x = value
    
    @property
    def y(self):
        """Gets the y-coordinate of the point."""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the point."""
        self.__y = value

def add_points(point1, point2):
    """
    Adds two Point objects.

    Parameters:
    ----------
    point1 : Point
        The first point
    point2 : Point
        The second point

    Returns:
    -------
    Point
        The sum of the two points
    """
    return point1 + point2

def are_equals(point1, point2):
    """
    Checks if two Point objects are equal.

    Parameters:
    ----------
    point1 : Point
        The first point
    point2 : Point
        The second point

    Returns:
    -------
    bool
        True if the points are equal, False otherwise
    """
    return point1 == point2
