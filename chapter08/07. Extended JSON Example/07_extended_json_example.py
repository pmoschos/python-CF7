import json
from datetime import date, timedelta
from typing import Type, Any, List

def add_json_support(cls: Type) -> Type:
    """
    Decorator to add JSON support with handling for non-serializable types.
    Adds a `to_json` method to the decorated class.
    
    Args:
        cls (Type): The class to be decorated.

    Returns:
        Type: The decorated class with `to_json` support.
    """
    def to_json(self) -> str:
        """
        Converts the object's attributes to a JSON string, handling custom types.
        
        Returns:
            str: JSON representation of the object.
        """
        def custom_serializer(obj: Any) -> Any:
            if isinstance(obj, (date, timedelta)):
                return obj.isoformat()  # Convert to ISO 8601 string
            raise TypeError(f"Type {type(obj)} not serializable")

        return json.dumps(self.__dict__, default=custom_serializer)
    
    cls.to_json = to_json
    return cls

@add_json_support
class Product:
    """
    A class representing a product with a name and price.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

@add_json_support
class Student:
    """
    A class representing a student with an ID, name, and date of birth.
    
    Attributes:
        student_id (str): Unique identifier for the student.
        name (str): Full name of the student.
        date_of_birth (date): Date of birth.
        courses (List[str]): List of enrolled courses.
        enrollment_date (date): Date of enrollment, defaults to today.
    """
    def __init__(self, student_id: str, name: str, date_of_birth: date, courses: List[str] = None) -> None:
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.courses = courses if courses else []  # List of enrolled courses
        self.enrollment_date = date.today()

def main() -> None:
    """
    Main function to demonstrate JSON serialization for Product and Student classes.
    """
    # Creating a product instance
    product = Product("Laptop", 1200)
    print("Product JSON:", product.to_json())

    # Creating student instances
    student1 = Student("S001", "Alice", date(2002, 5, 15))
    student2 = Student("S002", "Bob", date(2001, 8, 22), ["Mathematics", "Physics"])
    
    print("Student 1 JSON:", student1.to_json())
    print("Student 2 JSON:", student2.to_json())

    # Edge case: Unsupported type
    try:
        class UnsupportedType:
            pass

        unsupported_instance = UnsupportedType()
        unsupported_instance.to_json = add_json_support(type(unsupported_instance))
        print("Unsupported Type JSON:", unsupported_instance.to_json())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
