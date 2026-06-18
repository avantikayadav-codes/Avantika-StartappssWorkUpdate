a={}
n=int(input("Enter No. of employees: "))

for i in range(1,n+1):
    employee=input(f"Employee {i} name: ")
    interest=input("Enter interest: ")
    a[employee]=interest
print(a)

b={}
for emp,intrst in a.items():
    if intrst not in b:
        b[intrst]=[emp]
    else:
        b[intrst].append(emp)
print(b)
