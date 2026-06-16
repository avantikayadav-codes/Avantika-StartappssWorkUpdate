#printgreaterthan50.py

a=[]

for i in range(1,11):
    b=int(input(f"Enter no. {i} : "))
    if b>50:
        a.append(b)
print(a)


