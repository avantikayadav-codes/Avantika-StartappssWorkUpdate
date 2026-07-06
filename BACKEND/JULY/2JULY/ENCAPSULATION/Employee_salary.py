"""3. Employee Salary
Create an Employee class.
Private Attributes
•	__employee_id
•	__salary
Methods
•	get_salary()
•	set_salary()
Condition:
•	Salary cannot be negative.
"""


class Employee:
    def __init__(self,Emp,salary):
        self.__employee_id=Emp
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,sal):
        self.__salary=sal
        return self.__salary
a=Employee(101,50000)
print(a.get_salary())
s=int(input("Enter updated salary:"))
print(a.set_salary(s))