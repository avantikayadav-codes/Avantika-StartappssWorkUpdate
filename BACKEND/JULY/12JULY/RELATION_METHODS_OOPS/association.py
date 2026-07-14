class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self,teacher):
        print(f"{self.name} is learning from {teacher.name}")


t = Teacher("Mr. Sharma")
s = Student("Avantika")

s.learn(t)
