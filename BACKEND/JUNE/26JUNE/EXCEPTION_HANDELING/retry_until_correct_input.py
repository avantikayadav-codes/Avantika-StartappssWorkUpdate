while True:
    try:
        n=int(input("Enter an integer: "))
        print("You entered:",n)
        break
    except ValueError:
        print("Invalid Input")