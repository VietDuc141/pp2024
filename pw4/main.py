from output import Output_Manage
from domains.mark_manager import MarksManager
from input import Input_Manage

def main():
    mark = MarksManager()
    inp = Input_Manage()
    outp = Output_Manage()
    
    inp.input_students()
    inp.input_courses()
    while True:
        print("1. Input marks")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks for a given course")
        print("5. Calculate average GPA for a given student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            inp.input_marks()
        elif choice == '2':
            outp.list_students()
        elif choice == '3':
            outp.list_courses()
        elif choice == '4':
            outp.show_marks()
        elif choice == '5':
            student_id = input("Enter student ID: ")
            found = False
            for student in mark.students:
                if student.id == student_id:
                    found = True
                    print("Average GPA:", mark.calculate_gpa(student))
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
