from dataclasses import dataclass,field

@dataclass(frozen=True)
class student:
    name: str
    marks: int
    section: str =field(default="A") 
    skills: list =field(default_factory=list) 
    result: str =field(init=False)
    def __post_init__(self):
        object.__setattr__(self,"result","Pass" if self.marks >= 40 else "Fail")
        object.__setattr__(self,"skills",["Volleyball","Handball","Cricket"])
        
ob=student("Avantika",90)
print(ob)
obj=student("Gurman",80)
print(obj)
obj2=student("Ananya",30)
print(obj2)
print(obj!=obj2)














# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s = Student("Avantika",22)
# print(s.name)