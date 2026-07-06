class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __lt__(self,other):
        return self.salary<other.salary

obj1=Employee("Avantika",50000)
obj2=Employee("Rahul",60000)

print(obj1<obj2)