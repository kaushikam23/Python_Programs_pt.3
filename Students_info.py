students = []

for i in range(3):
    student = {}
    student["roll_number"] = input("Enter the roll number: ")
    student["name"] = input("Enter the name: ")
    student["total_marks"] = int(input("Enter the total marks: "))

    students.append(student)

print(students)
