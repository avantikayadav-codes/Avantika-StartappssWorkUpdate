from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")

    def move(self):
        print("Dog Runs")


class Bird(Animal):

    def sound(self):
        print("Chirp")

    def move(self):
        print("Bird Flies")


obj1 = Dog()
obj2 = Bird()

obj1.sound()
obj1.move()

obj2.sound()
obj2.move()