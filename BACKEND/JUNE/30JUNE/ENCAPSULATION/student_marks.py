"""1. Student Marks
Create a Student class.
Private Attributes
•	__name
•	__marks
Methods
•	get_name()
•	get_marks()
•	set_marks()
•	show_details()
Condition:
•	Marks should be between 0 and 100.
"""

class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if 100>marks>0:
            return marks
        else: 
            print("Marks not valid")
            
    def show_details(self):
        print(self.__name,":",self.__marks)

a=Student("Avantika",99)
print(a.get_name())
print(a.get_marks())
print(a.set_marks(50))
a.show_details()