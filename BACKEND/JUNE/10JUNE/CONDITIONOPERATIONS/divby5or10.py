a=int(input("Enter number: "))

if a%5==0:
    if a%10==0:
        print("Divisible by 5 and 10")
    else:
        print("divisible by 5 but not 10")
else:
    print("Not divisible by both")

