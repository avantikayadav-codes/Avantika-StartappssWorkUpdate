"""1.	Create a Vehicle class with a start() method. 
Create Car, Bike, and Truck classes that inherit from Vehicle and add their own methods."""


class Vehicle:
    def start():
        print("The Vehicle is:")

class Car(Vehicle):
    def ca():
        print("Car")
class Bike(Vehicle):
    def ba():
        print("Bike")
class Truck(Vehicle):
    def tr():
        print("Truck")
        
obj1=Car
obj1.start()
obj1.ca()

obj2=Bike
obj2.start()
obj2.ba()

obj3=Truck
obj3.start()
obj3.tr()