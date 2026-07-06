from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")


obj1 = Car()
obj2 = Bike()

obj1.start()
obj2.start()