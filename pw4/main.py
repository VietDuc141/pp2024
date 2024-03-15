from input import Input_Manage
from output import Output_Manage
from domains.student import Student
from domains.course import Course
from domains.mark_manager import MarksManager

def main():
    mask = MarksManager()
    Input_Manage.input_students(mask)
    Input_Manage.input_courses(mask)
    while True:
        print("1. Input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks for a given course")
        print("5. Calculate average GPA for a given student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            Input_Manage.input_marks(mask)
        elif choice == '2':
            Output_Manage.list_students(mask)
        elif choice == '3':
            Output_Manage.list_courses(mask)
        elif choice == '4':
            Output_Manage.show_marks(mask)
        elif choice == '5':
            student_id = input("Enter student ID: ")
            found = False
            for student in mask.students:
                if student.id == student_id:
                    found = True
                    print("Average GPA:", mask.calculate_gpa(student))
                    break
            if not found:
                print("Student not found.")
            pass
        elif choice == '6':
            break
        else:
            print("Invalid choice") 

if __name__ == "__main__":
    main()
