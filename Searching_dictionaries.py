students = []

for i in range(5):
    student = {}
    student["roll_number"] = input("Enter the roll number: ")
    student["name"] = input("Enter the name: ")
    student["total_marks"] = int(input("Enter the total marks: "))

    students.append(student)

s_name=input("Enter the student name")
for student in students:
    if(student["name"]==s_name):
        print("Roll no.: ", student["roll_number"])
        print("Total marks: ", student["total_marks"])

sum=0
for student in students:
    sum+=student["total_marks"]

print("Average: ", sum/len(students))
