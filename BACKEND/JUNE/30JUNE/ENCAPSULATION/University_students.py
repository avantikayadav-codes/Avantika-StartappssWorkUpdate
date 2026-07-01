"""
University Student
Private Attributes
•	__cgpa
Use getter, setter, and @property.
Condition:
•	CGPA should be between 0.0 and 10.0.
"""
class University:
    def __init__(self,cgpa):
        self.__cgpa=cgpa
    def get_percent(self):
        return self.__cgpa
    def set_percent(self,n):
        if 0<n<10:
            self.__cgpa=n
        else:
            print("Invalid percentage!")
    @property
    def percent(self):
        return self.__cgpa

obj=University(7)
print(obj.get_percent())
n=int(input("Enter CGPA T0 update:"))
obj.set_percent(n)
print(obj.percent)