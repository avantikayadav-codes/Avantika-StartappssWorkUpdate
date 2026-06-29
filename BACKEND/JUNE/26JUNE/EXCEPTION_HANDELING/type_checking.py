def func(a,b):
    try:
        print(a+b)
    except TypeError:
        print("Incompatible Data Types")
x=input("Enter first value: ")
y=int(input("Enter second value: "))
func(x,y)