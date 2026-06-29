try:
    n=int(input("Enter Number: "))
    result=100/n
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Answer:",result)
finally:
    print("Execution Finished")