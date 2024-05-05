class Person:
    def __init__(self, name, age, gender, role):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role

    def introduce(self):
        return f"Hello, my name is {self.name}. I am a {self.role}."

class Faculty(Person):
    def __init__(self, name, age, gender, department, role='faculty'):
        super().__init__(name, age, gender, role)
        self.department = department

    def teach(self):
        return f"I am teaching {self.department} students."

class Staff(Person):
    def __init__(self, name, age, gender, department, role='staff'):
        super().__init__(name, age, gender, role)
        self.department = department

    def assist(self):
        return f"I am assisting in {self.department} department."

class Student(Person):
    def __init__(self, name, age, gender, major, year, role='student'):
        super().__init__(name, age, gender, role)
        self.major = major
        self.year = year

    def study(self):
        return f"I am studying {self.major} as a {self.year} student."

# Example usage:
faculty_member = Faculty("Dr. Smith", 45, "Male", "Computer Science")
staff_member = Staff("Jane Doe", 30, "Female", "Admissions")
student = Student("John Doe", 20, "Male", "Biology", "Junior")

print(faculty_member.introduce())  # Output: Hello, my name is Dr. Smith. I am a faculty.
print(faculty_member.teach())      # Output: I am teaching Computer Science students.

print(staff_member.introduce())    # Output: Hello, my name is Jane Doe. I am a staff.
print(staff_member.assist())       # Output: I am assisting in Admissions department.

print(student.introduce())         # Output: Hello, my name is John Doe. I am a student.
print(student.study())             # Output: I am studying Biology as a Junior student.
