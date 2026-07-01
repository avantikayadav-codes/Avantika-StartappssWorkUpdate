""" Employee Age
Create an Employee class using @property.
Condition:
•	Age must be between 18 and 60.
"""


class EmployeeAge:
    def __init__(self,age):
        self.__age=age
    @property
    def emp(self):
        return self.__age
    @emp.setter
    def emp(self,n):
        if 18<n<60:
            self.__age=n
        else:
            print("Invalid age!")
ob=EmployeeAge(30)
print(ob.emp)
n=int(input("enter updated age of employee:"))
ob.emp=n
print(ob.emp)