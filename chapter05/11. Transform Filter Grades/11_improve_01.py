def upscale_grades(grades):
    """
    Upscale grades by adding 1 to each grade less than or equal to 9.
    Grades of 10 remain the same.
    """
    # Using list comprehension
    upscaled = [grade + 1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_passed(grades):
    """
    Filter out students who passed (grade >= 5).
    """
    # Using list comprehension
    passed = [grade for grade in grades if grade >= 5]
    return passed

def categorize_grades(grades):
    """
    Categorize grades into passed, failed, and honors.
    Honors is considered a grade of 10.
    """
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return passed, failed, honors

def calculate_average(grades):
    """
    Calculate the average grade.
    """
    return sum(grades) / len(grades) if grades else 0

def main():
    """
    Main function to demonstrate the usage of list comprehensions and map/filter functions 
    to transform and filter a list of grades in a realistic classroom scenario.
    """
    grades = [7, 5, 9, 10, 3, 6, 8, 4, 10, 2]

    # Upscaling grades
    upscaled_grades = upscale_grades(grades)
    print("Original grades:", grades)
    print("Upscaled grades (list comprehension):", upscaled_grades)

    # Filtering passed students
    passed_grades = filter_passed(grades)
    print("Passed grades (list comprehension):", passed_grades)

    # Categorizing grades
    passed, failed, honors = categorize_grades(grades)
    print("Passed students:", passed)
    print("Failed students:", failed)
    print("Honors students:", honors)

    # Calculating average grade
    average_grade = calculate_average(grades)
    print(f"Average grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()
