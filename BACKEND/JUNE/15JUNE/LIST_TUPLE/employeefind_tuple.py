#employeefind_tuple.py


a=[]
for i in range(1,6):
    b=input(f"enter employee {i} name: ")
    a.append(b)
tup=tuple(a)

find=input("Enter employee name to find: ")
for i in range(len(tup)):
    if find==tup[i]:
        print("Employee found!")
        break
else:
    print("Employee name not found!")