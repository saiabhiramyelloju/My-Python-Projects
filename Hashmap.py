students = {
    'Abhiram': 100,
    'Ravi': 50,
    'Neha': 80
}

name = input("enter student name: ")
print("Marks:", students.get(name, "Student not found"))
input("Press enter to close....")