class Inheri:
    def __init__(self,name):
        self.name=name
    def cat(self):
        print("Meowwww")
        print(self.name)
class Inheri1(Inheri):
    def dog(self):
        print("Bhauu")
        
obj=Inheri1("ABC")
obj.cat()
obj.dog()


#Single → One Parent → One Child
