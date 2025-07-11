# @classmethod:

# First argument is cls, which refers to the class.
# Can access and modify class-level data.
# Useful for factory methods and class-level operations.

# @staticmethod:

# No implicit first argument (self or cls).
# Cannot access or modify class or instance data.
# Useful for utility functions related to the class.

class Employee:
    _total_employees = 0  # This is a class variable

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        Employee._total_employees += 1  # Increment the class variable

    @classmethod
    def total_employees(cls):
        """
        Class method to get the total number of employees created.
        """
        return cls._total_employees

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        """
        Static method to calculate the annual bonus based on salary and bonus percentage.
        """
        return salary * (bonus_percentage / 100)

    def full_name(self):
        """
        Instance method to return the full name of the employee.
        """
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self, raise_percentage):
        """
        Instance method to apply a raise to the employee's salary.
        """
        self.salary += self.salary * (raise_percentage / 100)
        return self.salary

def main():
    # Creating employee instances
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Jane", "Smith", 60000)

    # Getting the total number of employees created
    total_emps = Employee.total_employees()
    print(f"Total employees created: {total_emps}")  # Output: Total employees created: 2

    # Calculating annual bonus
    bonus = Employee.calculate_bonus(emp1.salary, 10)
    print(f"Annual bonus for {emp1.full_name()}: {bonus}")  # Output: Annual bonus for John Doe: 5000.0

    bonus = Employee.calculate_bonus(emp2.salary, 15)
    print(f"Annual bonus for {emp2.full_name()}: {bonus}")  # Output: Annual bonus for Jane Smith: 9000.0

    # Applying raises
    emp1_new_salary = emp1.apply_raise(5)
    print(f"New salary for {emp1.full_name()} after a 5% raise: {emp1_new_salary}")  # Output: New salary for John Doe after a 5% raise: 52500.0

    emp2_new_salary = emp2.apply_raise(10)
    print(f"New salary for {emp2.full_name()} after a 10% raise: {emp2_new_salary}")  # Output: New salary for Jane Smith after a 10% raise: 66000.0

if __name__ == "__main__":
    main()
