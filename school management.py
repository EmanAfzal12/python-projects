class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            new_student = Student(student_id, name, age, grade)
            self.students[student_id] = new_student
            print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    def run(self):
        while True:
            print("\nSchool Management System")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                grade = input("Enter Student Grade: ")
                self.add_student(student_id, name, age, grade)
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                student_id = input("Enter Student ID to delete: ")
                self.delete_student(student_id)
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
       
