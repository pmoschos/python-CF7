class Base:
    def __init__(self):
        self.__private = "I am private"
        self._protected = "I am protected"
        self.public = "I am public"
    
    def __private_method(self):
        return "This is a private method"
    
    def get_private(self):
        return self.__private
    
    def call_private_method(self):
        return self.__private_method()

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "I am private in Derived"

    def get_derived_private(self):
        return self.__private

def main():
    print("Base Class:")
    base = Base()
    print(base.public)             # Accessing public attribute
    print(base._protected)         # Accessing protected attribute
    print(base.get_private())      # Accessing private attribute via public method
    print(base.call_private_method())  # Calling private method via public method

    print("\nDerived Class:")
    derived = Derived()
    print(derived.public)          # Accessing public attribute in derived class
    print(derived._protected)      # Accessing protected attribute in derived class
    print(derived.get_private())   # Accessing private attribute in base class via public method
    print(derived.get_derived_private())  # Accessing private attribute in derived class

    print("\nName Mangling:")
    # Demonstrating name mangling
    print(derived._Base__private)  # Accessing base class private attribute directly
    print(derived._Base__private_method())  # Calling base class private method directly

if __name__ == "__main__":
    main()