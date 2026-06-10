a=int(input("Enter No. A: "))
b=int(input("Enter No. B: "))
c=int(input("Enter No. C: "))

if (a>b and a>c):
    print("A is greater")
elif (b>c and b>a):
    print("B is greater")
else:
    print("C is greater")