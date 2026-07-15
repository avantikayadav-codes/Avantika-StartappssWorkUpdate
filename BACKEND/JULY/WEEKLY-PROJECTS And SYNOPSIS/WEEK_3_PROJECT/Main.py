import authentication
import hodprofile
import teacherprofile
import loggingfile
import logging

print("=============================\nWelcome to School Management\n=============================")
while True:
    print("Which admin you want to use\n1. HOD \n2. TEACHER\n3. Exit")
    while True:
        try:
            n=int(input("Enter choice:"))
            break
        except Exception as e:
            logging.exception(e)
            print("Please enter numbers onlyy")
    if n==1:
        while True:
            print("Do you want to Register or Login?\n1. Login \n2. Register\n3. Exit")
            while True:
                try:
                    m=int(input("Enter choice:"))
                    break
                except Exception as e:
                    logging.exception(e)
                    print("Please enter numbers onlyy")
            if m==1:
                if authentication.login("HOD"):
                    hodprofile.hod()
            elif m==2:
                authentication.registration("HOD")
            elif m==3:
                print("Exited from HOD Admin")
                break
            else:
                print("Invalid option!")

    elif n==2:
         while True:
            print("Do you want to Register or Login?\n1. Login \n2. Register\n3. Exit")
            while True:
                try:
                    m=int(input("Enter choice:"))
                    break
                except Exception as e:
                    logging.exception(e)
                    print("Please enter numbers onlyy")
            if m==1:
                if authentication.login("TEACHER"):
                    teacherprofile.teacher()
            elif m==2:
                authentication.registration("TEACHER")
            elif m==3:
                print("Exited from TEACHER Admin")
                break
            else:
                print("Invalid option!")

    elif n==3:
        print("Thank You for using Student Management!")
        break

    else:
        print("Please Enter the valid choice!")