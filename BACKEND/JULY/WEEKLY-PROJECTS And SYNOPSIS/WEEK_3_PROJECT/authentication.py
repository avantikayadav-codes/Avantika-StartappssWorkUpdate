import csv
import hashlib


Fieldname=["Role","Username","Password"]
def registration(role):
    username=input("Enter username:")
    password=input("Enter password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("Admin.csv","a+",newline="") as file:
        write=csv.DictWriter(file,fieldnames=Fieldname)
        if file.tell()==0:
            write.writeheader()
        write.writerow({"Role":role,"Username":username,"Password":hashed_password})
    print("Registration Successful!")


def login(role):
    username=input("Enter username:")
    password=input("Enter password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("Admin.csv","r",newline="") as file:
        read=csv.DictReader(file)
        for row in read:
            if(row["Role"]==role and row["Username"]==username and row["Password"]==hashed_password):
                print("Login Successful!")
                return True
        else:
            print("Invalid Username or Password!")
            return False










