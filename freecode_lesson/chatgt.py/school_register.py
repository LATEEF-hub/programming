







class Student:
    def __init__(self, name, grade, attendance):
        self.name = name
        self.grade = grade
        self.attendance = attendance

class SchoolRegister:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def list_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Grade: {student.grade}, Attendance: {student.attendance}%")

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

if __name__ == "__main__":
    register = SchoolRegister()

    student1 = Student("John Doe", 10, 95)
    student2 = Student("Jane Doe", 9, 88)

    register.add_student(student1)
    register.add_student(student2)

    print("Listing all students:")
    register.list_students()

    search_result = register.search_student("John Doe")
    if search_result:
        print(f"\nSearch result: {search_result.name}")
    else:
        print("\nStudent not found.")

    register.remove_student(student1)

    print("\nAfter removing John Doe:")
    register.list_students()
    