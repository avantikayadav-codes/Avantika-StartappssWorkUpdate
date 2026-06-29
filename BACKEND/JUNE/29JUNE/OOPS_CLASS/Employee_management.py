class Employee:
    def __init__(self,employee_id,name,department,designation,salary,email,joining_date,experience):
        self.employee_id=employee_id
        self.name=name
        self.department=department
        self.designation=designation
        self.salary=salary
        self.email=email
        self.joining_date=joining_date
        self.experience=experience

    def login(self):
        print(self.name,"logged in successfully")

    def apply_leave(self):
        days=int(input("Enter leave days: "))
        print(self.name,"applied for",days,"days leave")

    def calculate_salary(self):
        bonus=float(input("Enter Bonus: "))
        total=self.salary+bonus
        print("Total Salary =",total)

    def show_details(self):
        print("Employee ID :",self.employee_id)
        print("Name :",self.name)
        print("Department :",self.department)
        print("Designation :",self.designation)
        print("Salary :",self.salary)
        print("Email :",self.email)
        print("Joining Date :",self.joining_date)
        print("Experience :",self.experience,"Years")


obj=Employee(
    101,
    "Avantika",
    "IT",
    "Python Developer",
    50000,
    "avantika@gmail.com",
    "15-06-2026",
    2
)

obj.login()
obj.apply_leave()
obj.calculate_salary()
obj.show_details()