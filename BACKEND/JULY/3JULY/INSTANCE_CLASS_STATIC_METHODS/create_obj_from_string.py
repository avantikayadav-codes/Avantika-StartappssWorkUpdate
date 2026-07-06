class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,data):
        name,age=data.split(",")
        return cls(name,int(age))

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

obj=Student.from_string("Rahul,22")
obj.display()