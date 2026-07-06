"""3.	Implement multiple inheritance using Father and Mother classes. 
Create a Child class that inherits from both and accesses methods from each parent."""

class Father:
    def fa(self):
        print("I'm Father")
class Mother:
    def ma(self):
        print("I'm Mother")
class Child(Father,Mother):
    def ch(self):
        print("I'm Child")

ob=Child()
ob.ch()
ob.ma()
ob.fa()