class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [Student("Alice", "001", 3.9), Student("Bob", "002", 3.7), Student("Charlie", "003", 4.0)]
students2 = [Student("David", "004", 3.5), Student("Eve", "005", 3.8), Student("Frank", "006", 3.6)]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Students sorted by CGPA (Descending) - List 1:")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

print("\nStudents sorted by CGPA (Descending) - List 2:")
for student in sorted_students2:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")