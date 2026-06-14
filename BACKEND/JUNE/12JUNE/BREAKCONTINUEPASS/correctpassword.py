count=3
while count>0:
    pin=int(input("Enter pin: "))
    if pin==12345:
        print("Correct Pin!")
        break
    count-=1
else:
    print("Wrong pin!, Try after 30 minutes")