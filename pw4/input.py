import math
from domains.student import  Student
from domains.course import Course
class Input_Manage:
    def input_students(manager):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            student = Student(student_id, name, dob)
            manager.students.append(student)

    def input_courses(manager):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            manager.courses.append(course)

    def input_marks(manager):
        course_id = input("Enter course ID: ")
        for course in manager.courses:
                if course.id == course_id:
                    course_name = course.name
                    break
        else:
                print("Invalid course ID")
                return

        for student in manager.students:
                mark = float(input(f"Enter mark for {student.name} ({course_name}): "))
                mark = math.floor(mark * 10) / 10  
                student.marks[course_id] = mark
        pass
