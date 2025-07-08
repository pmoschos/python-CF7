def main():
    """
    Main function to demonstrate finding the key with the minimum value in a dictionary.
    This example finds the student with the lowest grade, the alphabetically smallest name,
    and the shortest name by length.
    """
    # Define a dictionary with students and their corresponding grades
    student_grades = {
        'Alice': 85,
        'Bob': 72,
        'Charlie': 90,
        'David': 68
    }

    # Handle edge case: empty dictionary
    if not student_grades:
        print("No student data available.")
        return

    # Find the student with the lowest grade
    student_with_lowest_grade = min(student_grades, key=student_grades.get)
    print(f"Student with the lowest grade: {student_with_lowest_grade} (Grade: {student_grades[student_with_lowest_grade]})")

    # Find the student with the smallest name alphabetically
    student_with_smallest_name = min(student_grades)
    print(f"Student with the smallest name (alphabetically): {student_with_smallest_name}")

    # Find the student with the shortest name by length
    student_with_shortest_name = min(student_grades, key=len)
    print(f"Student with the shortest name: {student_with_shortest_name} (Length: {len(student_with_shortest_name)})")

if __name__ == "__main__":
    main()
