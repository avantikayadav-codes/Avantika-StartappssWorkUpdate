atmpin=12345
count=3
while count>0:
    pin=int(input("Enter pin: "))
    if pin==atmpin:
        print("Correct Pin!")
        money=float(input("Enter the Amount in your bank:"))
        A=int(input("Enter the task:\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n"\
            "4. Exit\n-"))
        if A==1:
            print("Your Balance", money)
        elif A==2:
            B=float(input("Enter the Amount you want to deposit:"))
            C=B+money
            print("Deposit Success!\nYour Balance: ",C)
        elif A==3:
            if money>100:
                B=float(input("Enter the amount you want to withdraw: "))
                if B<money:
                    C=money-B
                    print("Withdraw Success!\nAvailable Balance: ",C)
                else:
                    print("Insufficient funds!")
            else:
                print("Insufficient funds!")
        elif A==4:
            pass
        print("Thanks for using bank!")
        break
    count-=1
else:
    print("Wrong Atm Pin, Try after 1 hour")

