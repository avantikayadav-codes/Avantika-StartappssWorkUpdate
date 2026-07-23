from dataclasses import dataclass,field

@dataclass
class student:
    name: str
    marks: int
    section: str =field(default="A")
    skills: list =field(default_factory=list)
    result: str =field(init=False)  
    def __post_init__(self):
        self.skills.extend(["volleyball","handball"])
        self.result="pass" if self.marks>=40 else "Fail"

ob=student("Avantika",90)
# ob.skills.extend(["volleyball","handball"])
obj=student("Gurman",80)
obj2=student("Ananya",30)
print(ob)
print(obj)
print(obj2)