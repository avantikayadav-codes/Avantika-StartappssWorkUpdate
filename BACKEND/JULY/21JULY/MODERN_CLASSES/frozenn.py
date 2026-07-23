from dataclasses import dataclass,field

@dataclass(frozen=True)
class student:
    name: str
    marks: int
    section: str =field(default="A") 
    skills: list =field(default_factory=list) 
    def __post_init__(self):
        if self.marks>=40:
            print("Pass")
        else:
            print("Fail")
        
ob=student("Avantika",90)
print(ob)
obj=student("Gurman",80)
print(obj)
obj2=student("Ananya",30)
print(obj2)