"""Login
   │
   ▼
Teacher Menu

1. Add Marks
2. Update Marks
3. View Student
4. Display Result
5. Logout"""

def teacher():
    import csv
    import loggingfile
    import logging

    while True:

        print("\n===== TEACHER MENU =====")
        print("1. Add Marks")
        print("2. Update Marks")
        print("3. View Student")
        print("4. Display Result")
        print("5. Logout")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except Exception as e:
                logging.exception(e)
                print("Enter Only Numbers!")


        if choice == 1:
            class Add_Marks:
                def marks(self):
                    while True:
                        try:
                            roll=int(input("Enter student roll number to add their marks:"))
                            break
                        except Exception as e:
                            logging.exception(e)
                            print("Roll Number should be in numeric form only!")
                    value=False
                    with open("student.csv","r",newline="") as file:
                        read=csv.DictReader(file)
                        for row in read:
                            if row["Roll"]==str(roll):
                                value=True
                                found=False
                                fieldname=["Name","Roll","Maths","Science","English","Total","Percentage","Grade"]
                                with open("Result.csv","a+",newline="") as newfile:
                                    reader=csv.DictReader(newfile)
                                    writer=csv.DictWriter(newfile,fieldnames=fieldname)
                                    newfile.seek(0)
                                    for roww in reader:
                                        if roww["Roll"]==str(roll):
                                            found= True
                                            print("student already exists! can't add marks only update")
                                            break
                                    if not found:
                                        if newfile.tell()==0:
                                            writer.writeheader()
                                        while True:
                                            try:
                                                math=int(input("Enter Maths Marks:"))
                                                scien=int(input("Enter Science Marks:"))
                                                eng=int(input("Enter English Marks:"))
                                                if (0<=math<100 and 0<=scien<100 and 0<=eng<100):
                                                    break
                                                else:
                                                    print("Please Enter valid Marks again!")
                                            except Exception as e:
                                                print("Please Enter valid marks again:")
                                                logging.exception(e)
                                        tot=math+scien+eng
                                        per=(tot / 300) * 100
                                        if per>=90:
                                            gr="A"
                                        elif 60<=per<90:
                                            gr="B"
                                        elif 30<=per<60:
                                            gr="C"
                                        else:
                                            gr="D"
                                        data={"Name":row["Name"],"Roll":row["Roll"],"Maths":math,"Science":scien,"English":eng,"Total":tot,"Percentage":per,"Grade":gr}
                                        writer.writerow(data)
                                break
                        if not value:
                            print("No such roll Number found!")
            obj=Add_Marks()
            obj.marks()


        elif choice == 2:
            class Update_Marks:
                def update(self):
                    data=[]
                    while True:
                        try:
                            roll=int(input("Enter student roll number to update their marks:"))
                            break
                        except Exception as e:
                            logging.exception(e)
                            print("Roll Number should be in numeric form only!")
                    value=False
                    data=[]
                    with open("Result.csv","r",newline="") as newfile:
                        reader=csv.DictReader(newfile)
                        for roww in reader:
                            if roww["Roll"]==str(roll):
                                value=True
                                while True:
                                    try:
                                        math=int(input("Enter Update Maths Marks:"))
                                        scien=int(input("Enter Update Science Marks:"))
                                        eng=int(input("Enter Update English Marks:"))
                                        if (0<=math<100 and 0<=scien<100 and 0<=eng<100):
                                            roww["Maths"]=math
                                            roww["Science"]=scien
                                            roww["English"]=eng
                                            break
                                        else:
                                            print("Please Enter valid Marks again!")
                                    except Exception as e:
                                        print("Please Enter valid marks again:")
                                        logging.exception(e)
                                tot=math+scien+eng
                                roww["Total"]=tot
                                per=(tot / 300) * 100
                                roww["Percentage"]=per
                                if per>=90:
                                    gr="A"
                                    roww["Grade"]=gr
                                elif 60<=per<90:
                                    gr="B"
                                    roww["Grade"]=gr
                                elif 30<=per<60:
                                    gr="C"
                                    roww["Grade"]=gr
                                else:
                                    gr="D"
                                    roww["Grade"]=gr
                                data.append(roww)
                            else:
                                data.append(roww)
                    if value:
                        fieldname=["Name","Roll","Maths","Science","English","Total","Percentage","Grade"]
                        with open("Result.csv","w",newline="") as newfile:
                            writer=csv.DictWriter(newfile,fieldnames=fieldname)
                            if newfile.tell()==0:
                                writer.writeheader()
                            writer.writerows(data)
                    else:
                        print("Roll Number Not found!!")                                
            obj=Update_Marks()
            obj.update()


        elif choice == 3:
            class View_all_Student:
                def view(self):
                    with open("student.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        print("Student record:-")
                        for row in read:
                            print(row)
            obj=View_all_Student()
            obj.view()


        elif choice == 4:
            class Display_All_Results:
                def display(self):
                    with open("Result.csv","r", newline="") as file:
                        read=csv.DictReader(file)
                        print("Student Results:-")
                        for row in read:
                            print(row)
            obj=Display_All_Results()
            obj.display()


        elif choice == 5:
            print("Logged Out Successfully!")
            break


        else:
            print("Invalid Choice!")


