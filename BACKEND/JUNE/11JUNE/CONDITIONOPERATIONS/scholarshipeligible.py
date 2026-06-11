marks=float(input("Enter the marks: "))
attend=float(input("Enter Attendence: "))

if marks>=70:
    if attend>=75:
        print("Eligible for Scholarship!")
    else:
        print("Attendence is low, Scholarship not approved")
else:
    print("Marks low, Scholarship not approved")
