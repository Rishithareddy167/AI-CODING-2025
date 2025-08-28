class StudentRecord:
    def __init__(self, name, id, courses=None):
        if courses is None:
            courses = []
        self.student_name = name
        self.student_id = id
        self.courses = courses
    
    def add_course(self, course):
        self.courses.append(course)
    
    def get_summary(self):
        return f"Student: {self.student_name}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"


class Department:
    def __init__(self, dept_name, students=None):
        self.dept_name = dept_name
        if students is None:
            students = []
        self.students = students

    def enroll_student(self, student):
        self.students.append(student)

    def department_summary(self):
        return f"Department: {self.dept_name}, Total Students: {len(self.students)}"


s1 = StudentRecord("Alice", 101, ["Math", "Science"])
d1 = Department("Computer Science")
d1.enroll_student(s1)
print(s1.get_summary())
print(d1.department_summary())

