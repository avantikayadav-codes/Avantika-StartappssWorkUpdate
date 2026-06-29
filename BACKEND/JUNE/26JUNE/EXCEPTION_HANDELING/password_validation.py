password="admin123"
count=0
while count<3:
    p=input("Enter Password: ")
    if p==password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
        count+=1
if count==3:
    print("Account Locked")