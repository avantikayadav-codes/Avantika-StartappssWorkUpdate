A=input("Enter username: ")
B=int(input("Enter password: "))

if A=="Admin":
    if B==1234:
        print("Successfull Login!")
    else:
        print("Password Incorrect")
else:
    print("Username not correct")
