def upscale_grades(students_grades):
    """
    Upscale grades by adding 1 to each grade less than or equal to 9.
    Grades of 10 remain the same.
    """
    # Using dictionary comprehension
    return {name: (grade + 1 if grade <= 9 else grade) for name, grade in students_grades.items()}

def filter_passed(students_grades):
    """
    Filter out students who passed (grade >= 5).
    """
    # Using dictionary comprehension
    return {name: grade for name, grade in students_grades.items() if grade >= 5}

def categorize_grades(students_grades):
    """
    Categorize students based on their grades into passed, failed, and honors.
    Honors is considered a grade of 10.
    """
    passed = {name: grade for name, grade in students_grades.items() if 5 <= grade < 10}
    failed = {name: grade for name, grade in students_grades.items() if grade < 5}
    honors = {name: grade for name, grade in students_grades.items() if grade == 10}
    return passed, failed, honors

def calculate_average(students_grades):
    """
    Calculate the average grade.
    """
    if students_grades:
        return sum(students_grades.values()) / len(students_grades)
    return 0

def main():
    """
    Main function to demonstrate the usage of dictionary comprehensions 
    and map/filter-like operations to transform and filter a list of student grades.
    """
    # Original dictionary of students with their grades
    students_grades = {
        "Alice": 7,
        "Bob": 5,
        "Charlie": 9,
        "David": 10,
        "Eve": 3,
        "Frank": 6,
        "Grace": 8,
        "Heidi": 4,
        "Ivan": 10,
        "Judy": 2
    }

    print("Original student grades:", students_grades)

    # Upscaling grades
    upscaled_grades = upscale_grades(students_grades)
    print("\nUpscaled grades (list comprehension):")
    for name, grade in upscaled_grades.items():
        print(f"{name}: {grade}")

    # Filtering passed students
    passed_grades = filter_passed(students_grades)
    print("\nPassed students (list comprehension):")
    for name, grade in passed_grades.items():
        print(f"{name}: {grade}")

    # Categorizing students based on their grades
    passed, failed, honors = categorize_grades(students_grades)
    print("\nPassed students:")
    for name, grade in passed.items():
        print(f"{name}: {grade}")

    print("\nFailed students:")
    for name, grade in failed.items():
        print(f"{name}: {grade}")

    print("\nHonors students:")
    for name, grade in honors.items():
        print(f"{name}: {grade}")

    # Calculating average grade
    average_grade = calculate_average(students_grades)
    print(f"\nAverage grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()
