choice=int(input("Please enter the choice:\n1. Addition\n2. Substraction\n3. multiply\n4. divide\n"))


A=float(input("Enter no. A: "))
B=float(input("Enter no. B: "))

if choice==1:
    print("Result: ",A+B)
elif choice==2:
    print("Result: ",A-B)
elif choice==3:
    print("Result: ",A*B)
else:
    print("Result: ",A//B)