class UniversityStructure:
    def __init__(self, university_name):  # Constructor should take university_name as an argument
        self.university_name = university_name
        print("Student added to the university.")

    def get_university(self):
        self.university = input("Are you a student? (yes/no): ").lower()
        if self.university == "yes":
            print(f"Welcome to {self.university_name}")
        else:
            print("You're not a student.")

# Define a new class for Student
class Student:
    def __init__(self, name, age, department, semester, university):
        # The _init_ method initializes the instance with the passed parameters
        self.name = name
        self.age = age
        self.department = department
        self.semester = semester
        self.university = university

# Create a student instance - here you should pass all arguments (name, age, etc.)
s1 = Student("Maira", 21, "Math", "6th", "GCUF")
u1 = UniversityStructure("GCUF")
u1.get_university()
# Print student's details
print("\nStudent Details:")
print("Student Name: ", s1.name)
print("Student Age: ", s1.age)
print("Student Department: ", s1.department)
print("Student Semester: ", s1.semester)
print("University Name: ", s1.university)

def get_identity(self):
    self.identity = input("Are you a student or professor? (student/professor): ").lower()
    if self.identity == "professor":
        print("What is your department?")
        # Print more details about the professor here, if necessary
    else:
        print("You're not a student.")

# Define a new class for Professor
class Professor(Student):
    def __init__(self, name, department, semester, class_timing, lecture_day):
        self.name = name
        self.department = department
        self.semester = semester
        self.class_timing = class_timing
        self.lecture_day = lecture_day

# Create a professor id
s2 = Professor("Abdullah", "Math", "6th", "9pm to 1pm", "Monday, Wednesday, Saturday")

# Print professor's details
print("\nProfessor Details:")
print("Professor Name: ", s2.name)
print("Professor Department: ", s2.department)
print("Professor Semester: ", s2.semester)
print("Professor Class_timing: ", s2.class_timing)
print("Professor Lecture Day: ", s2.lecture_day)
# courses

class Course:
    def __init__(self, course_name, course_code, course_instructor, course_schedule, course_capacity):
        self.course_name = course_name
        self.course_code = course_code
        self.course_instructor = course_instructor
        self.course_schedule = course_schedule
        self.course_capacity = course_capacity
        self.students = []
        print("Course added.")

c1 = Course("Calculus", "MATH101", "Abdullah", "Monday, Wednesday, Friday", 25)

# Print course details

print("\nCourse Details:")
print("Course Name: ", c1.course_name)
print("Course Code: ", c1.course_code)
print("Course Instructor: ", c1.course_instructor)
print("Course Schedule: ", c1.course_schedule)

# Add students to the course

def add_student(self, student):
    if len(self.students) < self.course_capacity:
        self.students.append(student)
        print(f"{s1.name} has been added to {self.course_name}.")
    else:
        print(f"{self.course_name} is full.")

# Add student to the course

add_student(c1, s1)

# Print the current list of students in the course

print("\nCurrent Students in the Course:")
for student in c1.students:
    print(student.name)


