class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.age, self.name)


s1 = Student("Avantika", 22)
# s2 = Student("Avantika", 22)

#but what if object print krna ho? without printing with return thats where we use repr
# and what if we want to compare 2 objects? we can't do s1==s2 cause it will gonna compare the memory not values
#so thats where we use eq 



from dataclasses import dataclass
@dataclass
class Student:
    name: str
s1 = Student("Avantika")
s2 = Student("Avantika")
print(s1)
print(s1 == s2)