class Animals:
    def __init__(self,name):
        self.name=name
    def dog(self):
        print("bhau")

class Dog(Animals):
    def cat(self):
        print("meowwwww")

class Cat(Animals):
    def lion(self):
        print("roarrrrr")

obj1=Dog("AAAA")
obj1.dog()
obj1.cat()

obj2=Cat("BBBB")
obj2.dog()
obj2.lion()

#Hierarchical → One Parent → Multiple Children