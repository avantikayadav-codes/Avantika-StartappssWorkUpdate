class Student:
    def __init__(self,marks):
        self.marks=marks

    def __getitem__(self,index):
        return self.marks[index]

obj=Student([90,80,70,95])

print(obj[0])
print(obj[2])