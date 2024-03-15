class Output_Manage:
    def list_courses(manager):
        print("Courses:")
        for course in manager.courses:
            print(f"{course.id}: {course.name}")

    def list_students(manager):
        print("Students:")
        for student in manager.students:
            print(f"{student.id}: {student.name}")

    def show_marks(manager):
        course_id = input("Enter course ID: ")
        for course in manager.courses:
            if course.id == course_id:
                course_name = course.name
                break
        else:
            print("Invalid course ID")
            return

        print(f"Marks for {course_name}:")
        for student in manager.students:
                if course_id in student.marks:
                    mark = student.marks[course_id]
                    print(f"{student.name}: {mark}")
                else:
                    print(f"{student.name}: N/A")
        pass
