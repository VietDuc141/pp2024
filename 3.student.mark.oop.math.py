import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

class MarksManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter course ID: ")
        for course in self.courses:
            if course.id == course_id:
                course_name = course.name
                break
        else:
            print("Invalid course ID")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} ({course_name}): "))
            mark = math.floor(mark * 10) / 10
            student.marks[course_id] = mark

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"{course.id}: {course.name}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student.id}: {student.name}")

    def show_marks(self):
        course_id = input("Enter course ID: ")
        for course in self.courses:
            if course.id == course_id:
                course_name = course.name
                break
        else:
            print("Invalid course ID")
            return

        print(f"Marks for {course_name}:")
        for student in self.students:
            if course_id in student.marks:
                mark = student.marks[course_id]
                print(f"{student.name}: {mark}")
            else:
                print(f"{student.name}: N/A")

    def calculate_gpa(self, student):
        gpa = 0
        total_credits = 0
        for course_id, mark in student.marks.items():
            credit = 3  
            gpa += mark * credit
            total_credits += credit
        return gpa / total_credits

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

if __name__ == '__main__':
    marks_manager = MarksManager()
    marks_manager.main()
