students = {
    'Alice': [85, 92, 78],
    'Bob': [79, 95, 88],
    'Charlie': [68, 72, 80],
    'Diana': [95, 98, 100],
    'Eve': [50, 60, 58]
}

def main():
    # Input validation loop
    while True:
        try:
            threshold = int(input("Please insert the threshold (integer): "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate average grades above the threshold
    average_grades = {
        student: round(sum(grades) / len(grades), 2)
        for student, grades in students.items()
        if grades and sum(grades) / len(grades) > threshold
    }

    # Display results
    if not average_grades:
        print(f"No students have an average grade greater than {threshold}.")
    else:
        print(f"\nStudents with average grade greater than {threshold}:")
        for student, avg_grade in average_grades.items():
            print(f"{student}: {avg_grade:.2f}")

if __name__ == "__main__":
    main()
