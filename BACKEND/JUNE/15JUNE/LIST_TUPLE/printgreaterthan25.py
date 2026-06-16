#printgreaterthan25.py

a=[]
print("Enter 10 numbers: ")
for i in range(1,11):
    b=int(input())
    a.append(b)

new_list=[]
for i in a:
    if i>25:
        new_list.append(i)
print("New list with greater than 25 is: ",new_list)