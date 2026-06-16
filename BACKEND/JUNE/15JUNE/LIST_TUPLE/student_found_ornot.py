#student_found_ornot.py

a=[]

for i in range(1,6):
    student=input(f"Enter name of student {i}: ")
    a.append(student)

found=input("Enter the name of students to find in list: ")
for i in range(len(a)):
    if found==a[i]:
        print("Student Found!")
        break
else:
    print("Student not found!")