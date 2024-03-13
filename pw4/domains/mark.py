import math
import numpy as np

class MarksManager:
    def __init__(self):
        self.students = []
        self.courses = []
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
