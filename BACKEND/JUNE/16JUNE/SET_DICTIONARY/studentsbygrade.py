#studentsbygrade.py

n=int(input("Enter the number of students: "))
dict={}
for i in range(1,n+1):
    name=input("Enter name: ")
    grade=input("Enter grade: ")
    dict[name]=grade
print(dict)

grd={}
for nm,gr in dict.items():
    if gr not in grd:
        grd[gr]=[]
    grd[gr].append(nm)
print(grd)

