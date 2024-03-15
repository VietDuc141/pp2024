import math

class MarksManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def calculate_gpa(self, student):
        gpa = 0
        total_credits = 0
        for course_id, mark in student.marks.items():
            credit = 3 
            gpa += mark * credit
            total_credits += credit
        return gpa / total_credits
