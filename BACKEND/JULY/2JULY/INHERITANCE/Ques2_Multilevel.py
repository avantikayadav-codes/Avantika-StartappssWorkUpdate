class Inheri:
    def __init__(self,name):
        self.name=name
    def cat(self):
        print("Meowwww")
        print(self.name)
class Inheri1(Inheri):
    def __init__(self,name):
        self.name=name
    def dog(self):
        print("Bhauu")
        print(self.name)
class Inheri2(Inheri1):
    def __init__(self,name):
        self.name=name
    def lion(self):
        print("wewewewe")
        print(self.name)
        
obj=Inheri2("ABC")
obj.cat()
obj.dog()
obj.lion()

#Multilevel → Parent → Child → Grandchild
