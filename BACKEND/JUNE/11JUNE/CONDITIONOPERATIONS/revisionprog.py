#Insurance eligibility: Age 18-60,M, Non-smoker, BMI between 18-30
#Insurance eligibility: Age 16-50,F, Non-smoker, BMI between 18-30

Gender=input("Enter Gender(M/F): ")
Age=int(input("Enter Age: "))

if Gender=="F":
    if Age>=18 and Age<=50:
        smoke=input("Do you smoke?(Y/N): ")
        BMI=int(input("Enter Your BMI: "))
        if smoke=="N":
            if BMI>=18 and BMI<=30:
                print("Eligible for insurance")
            else:
                print("BMI Issue")
        else:
            print("Person smokes, not eligible")
    else:
        print("Age issue")
else:
    if Gender=="M":
        if Age>=18 and Age<=60:
            smoke=input("Do you smoke?(Y/N): ")
            if smoke=="N":
                BMI=int(input("Enter Your BMI: "))
                if BMI>=18 and BMI<=30:
                    print("Eligible for insurance")
                else:
                    print("BMI Issue")
            else:
                print("Person smokes, not eligible")
        else:
            print("Age issue")
    else:
        print("Gender OR Age not defined properly")      
