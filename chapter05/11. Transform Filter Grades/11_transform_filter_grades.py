def main():
    """
    Main function to demonstrate the usage of list comprehensions and map/filter functions 
    to transform and filter a list of grades.
    """
    grades = [7, 5, 9, 10, 3]

    # Map (Transforms the data of the list) using list comprehension
    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
    print("Final grades (list comprehension):", upscaled_grades)

    # Map (Transforms the data of the list) using map() function
    upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
    print("Final grades (map()):", upscaled_grades2)

    # Filter using list comprehension
    passed_grades = [grade for grade in grades if grade >= 5]
    print("Passed (list comprehension):", passed_grades)

    # Filter (Based on a predicate) using filter() function
    passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
    print("Passed (filter()):", passed_grades2)

    # Show that filter returns an iterator
    print("Filter object:", filter(lambda grade: grade >= 5, grades))

if __name__ == "__main__":
    main()
