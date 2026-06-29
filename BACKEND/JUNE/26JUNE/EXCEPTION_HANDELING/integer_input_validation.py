try:
    n=int(input("Enter an integer: "))
    print("You entered:",n)
except ValueError:
    print("Invalid Input")