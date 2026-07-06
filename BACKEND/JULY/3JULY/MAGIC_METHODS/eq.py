class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __eq__(self,other):
        return self.roll==other.roll

obj1=Student("Avantika",101)
obj2=Student("Rahul",101)

print(obj1==obj2)