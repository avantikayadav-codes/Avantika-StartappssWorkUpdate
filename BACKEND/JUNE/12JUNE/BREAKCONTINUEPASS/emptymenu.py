count=3
while count>0:
    pin=int(input("Enter pin: "))
    if pin==1234:
        print("Correct Pin!")
        money=float(input("Enter the Amount in your bank:"))
        A=int(input("Enter the task:\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n"\
            "4. Exit\n-"))
        if A==1:
            pass
        elif A==2:
            pass
        elif A==3:
            pass
        elif A==4:
            pass
        print("Thanks for using bank!")
        break
    count-=1
else:
    print("Wrong Atm Pin, Try after 1 hour")
