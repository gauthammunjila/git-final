# Program to store information on students

students = []   # list to hold student records

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    
    # store details in dictionary
    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }
    students.append(student)

# Display all students
print("\n------ Student Information ------")
for s in students:
    print(f"Roll No: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")
    # Program to store information on students

students = []   # list to hold student records

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    
    # store details in dictionary
    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }
    students.append(student)

# Display all students
print("\n------ Student Information ------")
for s in students:
    print(f"Roll No: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")