#correctusernamepass.py


count=3
while count>0:
    user=input("Enter username: ")
    pin=int(input("Enter password: "))
    if (user=="Admin" and pin==12345):
        print("Successfull Login!")
        break
    count-=1
    print("Please Try again-")
else:
    print("Wrong username OR password! Account blocked")