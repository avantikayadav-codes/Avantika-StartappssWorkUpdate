"""Login
   │
   ▼
HOD Menu

Login
Add Student
Update Student
Delete Student
Search Student
View All Students
Logout"""

def hod():
    import csv
    import loggingfile
    import logging

    while True:
        print("\n===== HOD MENU =====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. View All Students")
        print("6. Logout")

        while True:
            try:
                choice=int(input("Enter choice:"))
                break
            except Exception as e:
                logging.exception(e)
                print("Please enter numbers onlyy")

        if choice == 1:
            class Add_Student:
                def __init__(self,email,name,age,gender,clas,section,roll):
                    self.email=email
                    self.name=name
                    self.age=age
                    self.gender=gender
                    self.clas=clas
                    self.section=section
                    self.roll=roll

                def addstudentfile(self):
                    fieldname = ["Email", "Name", "Age", "Gender", "Class", "Section", "Roll"]
                    data ={"Email":self.email, "Name":self.name, "Age":self.age, "Gender":self.gender, "Class":self.clas, "Section":self.section, "Roll":self.roll}
                    with open("student.csv","a+",newline="") as file:
                        write=csv.DictWriter(file,fieldnames=fieldname)
                        if file.tell() == 0:
                            write.writeheader()
                        write.writerow(data)
            while True:
                email = input("Enter Email: ")
                if ("@" in email and ".com" in email):
                    break
                else:
                    print("Invalid Email!")
            while True:
                name = input("Enter Name: ")
                if name.isalpha():
                    break
                else:
                    print("Name should contain only alphabets.")
            while True:
                try:
                    age=int(input("Enter Age:"))
                    if 3 <= age <= 20:
                        break
                    else:
                        print("Invalid age for school, Enter again!")
                except Exception as e:
                    logging.exception(e)
                    print("Enter Age properly! Only numbers allowed")

            while True:
                    gender = input("Enter Gender (M/F): ").upper()
                    if gender in ["M", "F"]:
                        break
                    else:
                        print("Enter only M or F.")
            while True:
                try:
                    clas = int(input("Enter Class (1-12): "))
                    if 1 <= clas <= 12:
                        break
                    else:
                        print("Class must be between 1 and 12.")
                except Exception as e:
                    logging.exception(e)
                    print("Enter only Numbers!")

            while True:
                section = input("Enter Section: ").upper()
                if section in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Section must be A, B, C or D.")
            while True:
                try:
                    roll = int(input("Enter Roll Number: "))
                    if roll > 0:
                        break
                    else:
                        print("Roll Number must be greater than 0.")
                except Exception as e:
                    logging.exception(e)
                    print("Enter only Numbers!")

            obj=Add_Student(email,name,age,gender,clas,section,roll)
            obj.addstudentfile()


        elif choice == 2:
            class Delete_Student:
                def delete(self):
                    while True:
                        try:
                            roll = int(input("Enter roll no. to delete the student:"))
                            break
                        except Exception as e:
                            logging.exception(e)
                            print("Enter Only Numbers!")
                    data=[]
                    found=False
                    with open("student.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        for row in read:
                            if row["Roll"]!=str(roll):
                                data.append(row)
                            else:
                                found=True
                    if found:
                        fieldname = ["Email", "Name", "Age", "Gender", "Class", "Section", "Roll"]
                        with open("student.csv","w", newline="") as file:
                            write=csv.DictWriter(file,fieldnames=fieldname)
                            write.writeheader()
                            write.writerows(data)
                        print("Data Deleted Successfully!")
                    else:
                        print("Roll Number Not found!")
            obj=Delete_Student()
            obj.delete()


        elif choice == 3:
            class Update_Student:
                def update(self):
                    while True:
                        try:
                            roll = int(input("Enter roll no. of student whose detail to update:"))
                            break
                        except Exception as e:
                            logging.exception(e)
                            print("Enter Only Numbers!")

                    data=[]
                    found=False
                    with open("student.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        for row in read:
                            if row["Roll"]!=str(roll):
                                data.append(row)
                            else:
                                found=True
                                while True:
                                    print("Enter the section you want to update:-\n",
                                            "1. Email\n", "2. Age\n", "3. Class\n", "4. Section\n", "5. Exit")
                                    while True:
                                        try:
                                            choice=int(input("Enter choice:"))
                                            break
                                        except Exception as e:
                                            logging.exception(e)
                                            print("Please enter numbers onlyy")
                                    if choice == 1:
                                        while True:
                                            email = input("Enter Email to update: ")
                                            if ("@" in email and ".com" in email):
                                                row["Email"]=email
                                                break
                                            else:
                                                print("Invalid Email!")

                                    elif choice == 2:
                                        while True:
                                            try:
                                                age=int(input("Enter Age to update:"))                                       
                                                if 3 <= age <= 20:
                                                    row["Age"]=age
                                                    break
                                                else:
                                                    print("Invalid age for school, Enter again!")
                                            except Exception as e:
                                                logging.exception(e)
                                                print("Enter Age properly! Only numbers allowed")

                                    elif choice == 3:
                                        while True:
                                            try:
                                                clas = int(input("Enter Class (1-12) to update: "))                                       
                                                if 1 <= clas <= 12:
                                                    row["Class"]=clas
                                                    break
                                                else:
                                                    print("Class must be between 1 and 12.")
                                            except Exception as e:
                                                logging.exception(e)
                                                print("Enter only Numbers!")

                                    elif choice == 4:        
                                        while True:
                                            section = input("Enter Section to update: ").upper()                                    
                                            if section in ["A", "B", "C", "D"]:
                                                row["Section"]=section
                                                break
                                            else:
                                                print("Section must be A, B, C or D.")

                                    elif choice == 5:
                                        print("Exited from update menu")
                                        break

                                    else:
                                        print("Invalid Choice!")
                                data.append(row)

                    if found:
                        fieldname = ["Email", "Name", "Age", "Gender", "Class", "Section", "Roll"]
                        with open("student.csv","w", newline="") as file:
                            write=csv.DictWriter(file,fieldnames=fieldname)
                            write.writeheader()
                            write.writerows(data)
                        print("Data Updated Successfully!")
                    else:
                        print("Roll Number Not found, Can't update!")
            obj=Update_Student()
            obj.update()


        elif choice == 4:
            class Search_Student:
                def search(self):
                    while True:
                        try:
                            roll = int(input("Enter roll no. to find the student:"))
                            break
                        except Exception as e:
                            logging.exception(e)
                            print("Enter Only Numbers!")

                    with open("student.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        for row in read:
                            if row["Roll"]==str(roll):
                                print("Student record Found!")
                                print(row)
                                break
                        else:
                            print("Roll Number Not found!")
            obj=Search_Student()
            obj.search()


        elif choice == 5:
            class View_all_Student:
                def view(self):
                    with open("student.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        print("Student record:-")
                        for row in read:
                            print(row)
            obj=View_all_Student()
            obj.view()


        elif choice == 6:
            print("Logged Out Successfully")
            break

        
        else:
            print("Invalid Choice")

        
































                
  
                
                










        








