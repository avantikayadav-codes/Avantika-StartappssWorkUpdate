"""8.	Create a class hierarchy for University → Department → Student. 
Show how data flows through constructors using super()."""

class University:
    def __init__(self,name,roll):
        print("Start")
        self.name="Gurman"
        self.roll=102
        print("stop")
    def u(self):
        print("University")
        print("Name:",self.name)
        print("roll:",self.roll)

class Department(University):
    def __init__(self,name,roll):
        print("department start")
        self.name=name
        self.roll=roll
        super().__init__(name,roll)
        print("Department stop")
    def u(self):
        super().u()
        print("Department")
        print("Name:",self.name)
        print("roll:",self.roll)

class Student(University):
    def __init__(self,name,roll):
        super().__init__(name,roll)
        print("DONE")
    def u(self):
        super().u()
        print("Student")
        print("Name:",self.name)
        print("roll:",self.roll)
obj=Student("Avantika",101)
obj.u()

obj=Department("Avantika",101)
obj.u()
