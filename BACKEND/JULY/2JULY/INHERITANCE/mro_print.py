"""9.	Create a hybrid inheritance example and print the MRO using ClassName.mro()."""
class c1:
    def c():
        print("Hello1")

class c2(c1):
    def c():
        print("Hello2")

class c3(c1):
    def c():
        print("Hello3")

class c4(c2,c3):
    def c():
        print("Hello4")

class c5(c1):
    def c():
        print("Hello5")
obj=c5
print(c4.mro())