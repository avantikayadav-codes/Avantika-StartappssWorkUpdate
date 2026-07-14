from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    marks: int
# Instance Method
    def introduce(self):
        print(f"My name is {self.name}.")
# Instance Method
    def is_pass(self):
        return self.marks >= 40
# Instance Method
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Marks: {self.marks}")
# Class Method
    @classmethod
    def college(cls):
        print("LNCT College")
# Static Method
    @staticmethod
    def course():
        print("Python Full Stack")
# Object Creation
s1 = Student("Avantika", 22, 95)
# Accessing Attributes
print(s1.name)
print(s1.age)
print(s1.marks)
# Calling Instance Methods
s1.introduce()
print(s1.is_pass())
s1.display()
# Calling Class Method
Student.college()
# Calling Static Method
Student.course()
# Dataclass Generated __repr__()
print(s1)
