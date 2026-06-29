try:
    n=int(input("Enter number: "))
    print("Answer:",100/n)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")