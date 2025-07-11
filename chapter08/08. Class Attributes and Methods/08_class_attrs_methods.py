class Student:
    school_name = "Example High School"  # Class attribute

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def update_grade(self, new_grade):
        """Updates the student's grade."""
        self.grade = new_grade
        print(f"Grade updated to {self.grade}")

    def is_adult(self):
        """Checks if the student is an adult (age >= 18)."""
        return self.age >= 18

    def display_info(self):
        """Displays the student's information."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


print(Student.__dict__.items())

print("\nClass Attributes and Methods:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    print(f"{attr_name:<15}: {attr_value}")

print("\nClass Methods:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    if callable(attr_value):
        print(f"{attr_name:<15}: {attr_value}")

print("\nClass Attributes:")
print("-" * 30)
for attr_name, attr_value in Student.__dict__.items():
    if not callable(attr_value) and not attr_name.startswith("__"):
        print(f"{attr_name:<15}: {attr_value}")