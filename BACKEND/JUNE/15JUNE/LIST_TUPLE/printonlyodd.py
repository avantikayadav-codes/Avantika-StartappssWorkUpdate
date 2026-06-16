n=int(input("Enter length of list: "))
a=[]

for i in range(1,n+1):
    b=int(input(f"Enter element {i}: "))
    if b%2==0:
        continue
    else:
        a.append(b)
print("Odd Numbers in list are: ",a)