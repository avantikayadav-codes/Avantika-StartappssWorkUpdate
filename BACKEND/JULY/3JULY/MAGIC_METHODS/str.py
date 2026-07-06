class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return f"student name is {self.name} and the id is {self.id}"

obj=student("Avantika",101)
print(obj)
print(obj.name)