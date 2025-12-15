# Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Ask user to enter student name
name = input("Enter the student's name: ")

# Retrieve and display marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
