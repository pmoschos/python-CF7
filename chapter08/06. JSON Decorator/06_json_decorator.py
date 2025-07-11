import json
from datetime import date, timedelta
from typing import Any, Type

def add_json_support(cls: Type) -> Type:
    """
    Decorator to add JSON support to a class by adding a `to_json` method.
    
    Args:
        cls (Type): The class to be extended with JSON support.
        
    Returns:
        Type: The class with the added `to_json` method.
    """
    def to_json(self) -> str:
        """
        Convert the object's attributes to a JSON string.
        
        Returns:
            str: A JSON representation of the object's attributes.
        """
        return json.dumps(self.__dict__, default=str)
    
    cls.to_json = to_json
    return cls

@add_json_support
class Product:
    """
    A class representing a product with a name and price.
    
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

def main() -> None:
    """
    Main function to demonstrate JSON support for the Product class.
    """
    product = Product("Laptop", 1200)
    print(product.to_json())  # Output: {"name": "Laptop", "price": 1200}

    # Demonstrating support for additional types
    product_with_date = Product("Smartphone", 800)
    product_with_date.launch_date = date.today()
    print(product_with_date.to_json())  # Handles date serialization

if __name__ == "__main__":
    main()
