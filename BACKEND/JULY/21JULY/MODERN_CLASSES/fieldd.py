from dataclasses import dataclass,field

@dataclass
class student:
    name: str
    section: str =field(default="A") # to set default value of this var
    skills: list =field(default_factory=list) #to set default list,set,dict for this
    age: int =field(init=False)  #it means that this value is not assigned here or python is told not to include this
    #varibale rn because its value will be assigned in post init or after making an obj
ob=student("Avantika")
ob.skills.extend(["volleyball","handball"])
ob.age=20
obj=student("Gurman")
obj.age=21
print(ob)
print(obj)