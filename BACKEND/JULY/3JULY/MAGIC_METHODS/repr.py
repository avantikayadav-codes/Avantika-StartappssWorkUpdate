class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __repr__(self):
        return f"student({self.name} ,{self.id})"

obj=student("Avantika",101)
print(obj)
print(obj.name)