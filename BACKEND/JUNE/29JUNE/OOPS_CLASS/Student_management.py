"""
Attributes (8)
•	student_id
•	name
•	age
•	gender
•	class_name
•	section
•	roll_number
•	marks
Methods (5)
•	study()
•	attend_class()
•	take_exam()
•	show_result()
•	show_profile()
"""


class Student:
    def __init__(self,student_id,name,age,gender,class_name,section,roll_number,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.gender=gender
        self.class_name=class_name
        self.section=section
        self.roll_number=roll_number
        self.marks=marks

    def study(self):
        return self.name, "is studying in", self.class_name

    def attend_class(self):
        return self.name, "is attending class in", self.class_name

    def take_exam(self):
        return self.name, "is taking class in", self.class_name

    def show_result(self):
        if self.marks<=30:
            print("Fail")
        else:
            print("Pass")
        return "Student id:", self.student_id, "Student name:", self.name,"Student marks:", self.marks

    def show_profile(self):
        print(self.student_id,"\n", self.name,"\n", self.age,"\n", self.gender,"\n", self.class_name,"\n", self.section,"\n", self.roll_number,"\n", self.marks)

obj=Student(101,"Gurman",23,"Male","Python class","A",2738,70)
print(obj.study())
print(obj.attend_class())
print(obj.take_exam())
print(obj.show_result())
obj.show_profile()
