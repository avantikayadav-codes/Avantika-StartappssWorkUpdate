a=[10,20,30,40,50]
try:
    n=int(input("Enter index: "))
    print(a[n])
except IndexError:
    print("Invalid Index")