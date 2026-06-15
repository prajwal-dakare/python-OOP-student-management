# Parent Class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Child Class (Inheritance)
class Result(Student):
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


# List
students = []

try:
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent {i+1}")

        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        student = Result(name, roll, marks)
        students.append(student)

except ValueError:
    print("Invalid input! Please enter numbers correctly.")

# Dictionary
student_dict = {}

for s in students:
    student_dict[s.roll_no] = s.name

print("\nDictionary Data:")
print(student_dict)

# Set
unique_names = {s.name for s in students}

print("\nUnique Student Names:")
print(unique_names)

# Tuple
college_info = ("JSPM University", "ENTC", "2026")

print("\nCollege Information:")
print(college_info)

# Display Data
for s in students:
    s.display()
    print("Grade:", s.grade())

# File Handling
try:
    with open("students.txt", "w") as file:
        for s in students:
            file.write(
                f"{s.name}, {s.roll_no}, {s.marks}, Grade: {s.grade()}\n"
            )

    print("\nStudent data saved successfully.")

except FileNotFoundError:
    print("File error occurred.")
    
