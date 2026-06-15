#StudentResultManagementSystem.py

n=int(input("Enter the no. of student: "))
student=[]
marks=[]
total_mark=[]
average_mark = []
percentage_mark = []
Attendence=[]

for i in range(n):
    st=input("Enter student name: ")
    student_marks = []
    for j in range(5):
        while True:
            mr=int(input(f"Enter marks for subject {j+1}: "))
            if 0<=mr<=100:
                break
            else:
                print("Invalid Marks! enter again")
        student_marks.append(mr)
    while True:
        atten=int(input(f"Enter attendence for student {i+1}:"))
        if 0<=atten<=100:
            break
        else:
            print("Invalid attendence! enter again") 
        
    total=sum(student_marks)
    average = total / len(student_marks)
    percentage = (total / (100 * len(student_marks))) * 100
    student.append(st)
    marks.append(student_marks)
    total_mark.append(total)
    average_mark.append(average)
    percentage_mark.append(percentage)
    Attendence.append(atten)




while True: 
    print("\n\n---------------------------------\n---------------------------------\nSTUDENT RESULT MANAGEMENT SYSTEM\n"\
              "---------------------------------\n---------------------------------\n")
    print("1. Add Student\n2. View Result\n3. View Statistics\n4. Exit")
    choice=int(input("ENTER CHOICE: "))


    if choice == 1:
        n=int(input("Enter the no. of student: "))

        for i in range(n):
            st=input("Enter student name: ")
            student_marks = []
            for j in range(5):
                while True:
                    mr=int(input(f"Enter marks for subject {j+1}:"))
                    if 0<=mr<=100:
                        break
                    else:
                        print("Invalid Marks! enter again")
                student_marks.append(mr)
            while True:
                atten=int(input(f"Enter attendence for student {i+1}:"))
                if 0<=atten<=100:
                    break
                else:
                    print("Invalid attendence! enter again")
            

            total=sum(student_marks)
            average = total / len(student_marks)
            percentage = (total / (100 * len(student_marks))) * 100
            student.append(st)
            marks.append(student_marks)
            total_mark.append(total)
            average_mark.append(average)
            percentage_mark.append(percentage)
            Attendence.append(atten)


    elif choice==2:
        res=input("Enter student name to see report: ")
        for i in range(len(student)):
            if res==student[i]:
                print(f"-----------------------\n-----------------------\nRESULT CARD\n"\
                       "-----------------------\n-----------------------")
                print("Student Name:- ",student[i])
                print("Marks:-")
                count=0
                for j in range(len(marks[i])):
                    print(f"Subject {j+1} marks:- {marks[i][j]}")
                    if (marks[i][j]<25):
                        count+=1
                mini=min(marks[i])
                maxi=max(marks[i])
                print("\n")
                print("Total Marks:-",total_mark[i])
                print("Average Marks:-",average_mark[i])
                print("Percentage:-",round(percentage_mark[i],2),"\n")
                      
                print("Highest Marks:- ",maxi)
                print("Lowest Marks:- ",mini,"\n")

                print("Attendence:- ",Attendence[i])
                if(Attendence[i]<65):
                    print("Eligibility:- Not Eligible for Exam","\n")
                else:
                    print("Eligibility:- Eligible for Exam","\n")

                print("Failed subjects:-",count,"\n")

                if(percentage_mark[i]>80):
                    print("Grade: A",)
                elif(percentage_mark[i]>60):
                    print("Grade: B")
                elif(percentage_mark[i]>40):
                    print("Grade: C")
                else:
                    print("Grade: D")

                if(percentage_mark[i]<30):
                    print("Fail!")
                else:
                    print("Pass")

                if(average_mark[i]>90):
                    print("Performence: Excellent")
                elif(average_mark[i]>70):
                    print("Performence: Good")
                elif(average_mark[i]>50):
                    print("Performence: Average")
                else:
                    print("Performence: Poor")
                break
        else:
            print("Student Record Not Found!")


    elif choice==3:
        print(f"-----------------------\n-----------------------\nSTATISTICS\n"\
                "-----------------------\n-----------------------")
        
        countfail=0
        countpass=0
        topper=0
        maxx=max(percentage_mark)
        for i in range(len(student)):
            if (percentage_mark[i]<30):
                countfail+=1
            else:
                countpass+=1
            if maxx==percentage_mark[i]:
                topper=student[i]
        
        classaverage=sum(average_mark)/len(average_mark)

        tot=len(student)
        print("Total Number of students:",tot)
        print("Total Number of Passed Students:",countpass)
        print("Total Number of Failed Students:",countfail,"\n")

        print("Class Average:- ",classaverage,"\n")

        print("Topper Student:- ",topper)
        print("Topper percentage:- ",maxx)


    elif choice==4:
        break

    else:
        print("Invalid Choice!")

print("Thanks For visiting!")