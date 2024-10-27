import json

class Student:
    def __init__(self, name, student_id, grades=[]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def has_passed(self):
        return self.calculate_average() >= 60

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades,
            "average": self.calculate_average(),
            "passed": self.has_passed()
        }

class StudentGradesSystem:
    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for student_data in data:
                    student = Student(student_data["name"], student_data["student_id"], student_data["grades"])
                    self.students.append(student)
        except FileNotFoundError:
            print("No students found.")
            pass

    def save_students(self):
        with open(self.file_path, "w") as file:
            json.dump([student.to_dict() for student in self.students], file)

    def add_student(self, student):
        self.students.append(student)
        self.save_students()
        print(f"Student '{student.name}' added.")
        
system = StudentGradesSystem()
student = Student("kamal", "A001")
student.add_grade(85)
student.add_grade(75)
student.add_grade(65)
system.add_student(student)
del student

student = Student("nimal", "A002")
student.add_grade(44)
student.add_grade(65)
student.add_grade(70)
system.add_student(student)

