# Store marks of 5 students in a dictionary

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records:")

for name, marks in students.items():
    print(f"{name}: {marks}")

search_name = input("\nSearch student: ")

if search_name in students:
    print("Marks:", students[search_name])
else:
    print("Student not found")
