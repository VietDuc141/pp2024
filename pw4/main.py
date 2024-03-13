from input import input_students, input_courses
from domains.mark import  MarksManager
from domains.student import Student
from domains.course import Course

def main(self):
    self.input_students()
    self.input_courses()
    while True:
        print("1. Input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks for a given course")
        print("5. Calculate average GPA for a given student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            self.input_marks()
        elif choice == '2':
            self.list_students()
        elif choice == '3':
            self.list_courses()
        elif choice == '4':
            self.show_marks()
        elif choice == '5':
            student_id = input("Enter student ID: ")
            found = False
            for student in self.students:
                if student.id == student_id:
                    found = True
                    print("Average GPA:", self.calculate_gpa(student))
                    break
            if not found:
                print("Student not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice")
