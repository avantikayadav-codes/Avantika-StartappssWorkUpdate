"""2.	Create a multilevel inheritance example using Person → Employee → Manager.
 Add different methods at each level and demonstrate method access."""

class Person:
    def per():
        print("This is person class")
class Employee(Person):
    def emp():
        print("This is employee class")
class Manager(Employee):
    def man():
        print("This is manager class")
obj=Manager
obj.man()
obj.emp()
obj.per()