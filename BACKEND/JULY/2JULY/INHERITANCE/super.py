"""Constructor Inheritance
Create a program to demonstrate constructor inheritance using super()."""

class Mother:
    def meth():
        print("I'm Mother")
class Father:
    def meth():
        print("I'm Father")
class Child(Mother,Father):
    def meth():
        super().meth()
        print("I'm child")

ob=Child
ob.meth()
