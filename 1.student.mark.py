def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(num_students):
        student = {}
        student['id'] = input("Enter student ID: ")
        student['name'] = input("Enter student name: ")
        student['dob'] = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append(student)
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course = {}
        course['id'] = input("Enter course ID: ")
        course['name'] = input("Enter course name: ")
        courses.append(course)
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID: ")
    for course in courses:
        if course['id'] == course_id:
            course_name = course['name']
            break
    else:
        print("Invalid course ID")
        return
    for student in students:
        mark = input(f"Enter mark for {student['name']} ({course_name}): ")
        student.setdefault('marks', {})[course_id] = mark

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_marks(students, courses):
    course_id = input("Enter course ID: ")
    for course in courses:
        if course['id'] == course_id:
            course_name = course['name']
            break
    else:
        print("Invalid course ID")
        return
    print(f"Marks for {course_name}:")
    for student in students:
        if course_id in student.get('marks', {}):
            mark = student['marks'][course_id]
            print(f"{student['name']}: {mark}")
        else:
            print(f"{student['name']}: N/A")

def main():
    students = input_students()
    courses = input_courses()
    while True:
        print("1. Input marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            input_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_marks(students, courses)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()