from datetime import date, timedelta

class Student:
    """Class to represent a student in a school or university system."""
    student_count = 0

    def __init__(self, student_id, name, date_of_birth, courses=None):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth  # Expecting a `datetime.date` object
        self.courses = courses if courses else []  # List of enrolled courses
        self.enrollment_date = date.today()
        Student.student_count += 1
        print(f"Student {self.name} (ID: {self.student_id}) enrolled on {self.enrollment_date}. "
              f"Total students: {Student.student_count}")

    def calculate_age(self):
        """Calculates and returns the student's age."""
        today = date.today()
        # Date of Birth: 2000-12-15
        # Today's Date: 2024-12-10
        # Age Calculation:
        # Year difference: 2024 - 2000 = 24
        # Since today is before the birth date (12-10 < 12-15), the age is adjusted to 24 - 1 = 23.
        age = today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
        return age

    def enroll_course(self, course_name):
        """Enrolls the student in a new course."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has been enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def drop_course(self, course_name):
        """Drops a course for the student."""
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} has dropped {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def get_student_info(self):
        """Returns a dictionary with all student details."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.calculate_age(),
            "enrollment_date": self.enrollment_date,
            "courses": self.courses,
        }

    def __del__(self):
        Student.student_count -= 1
        print(f"Student {self.name} (ID: {self.student_id}) record deleted. "
              f"Total students: {Student.student_count}")


# Example usage
def manage_students():
    # Creating student instances
    student1 = Student("S001", "Alice", date(2002, 5, 15))
    student2 = Student("S002", "Bob", date(2001, 8, 22), ["Mathematics", "Physics"])

    # Enrolling in courses
    student1.enroll_course("Mathematics")
    student1.enroll_course("Computer Science")
    student1.enroll_course("Mathematics")  # Attempt duplicate enrollment

    # Dropping a course
    student2.drop_course("Physics")
    student2.drop_course("Biology")  # Attempt to drop a non-enrolled course

    # Displaying student details
    print(student1.get_student_info())
    print(student2.get_student_info())

    # Deleting a student
    del student1
    print(f"Currently active students: {Student.student_count}")

if __name__ == "__main__":
    manage_students()
