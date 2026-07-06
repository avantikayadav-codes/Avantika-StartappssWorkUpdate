# class Father:
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print("Hello i'm father")
#         print(self.name)

# class Mother:
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print("Hello i'm Mother")
#         print(self.name)

# class Child(Father,Mother):
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print("Hello i'm child")
#         print(self.name)

# obj=Child("yoyo")
# obj.m1()





# class GrandParent:
#     def __init__(self):
#         print("GrandParent Constructor")
# class Parent(GrandParent):
#     def __init__(self):
#         print("Parent Start")
#         super().__init__()
#         print("Parent End")
class Child():
    def __init__(self,name):
        print("Child Start")
        # super().__init__()
        self.name=name
        print(self.name)
        print("Child End")
obj = Child("hii")
obj.__init__