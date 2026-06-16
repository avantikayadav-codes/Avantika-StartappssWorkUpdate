#Reportcard.py

subjects = ("Maths", "English", "Science", "Hindi", "SS")
marks = [90, 85, 78, 88, 92]

for a,b in zip(subjects,marks):
    print(f"{a} : {b}")
print()
print("Total Marks: ",sum(marks))
print("Average Marks: ",sum(marks)/len(marks))
print("Highest Marks: ",max(marks))
print("Lowest Marks: ",min(marks),"\n")
av=sum(marks)/len(marks)
if av>35:
    print("RESULT: PASS")
else:
    print("RESULT: FAIL")