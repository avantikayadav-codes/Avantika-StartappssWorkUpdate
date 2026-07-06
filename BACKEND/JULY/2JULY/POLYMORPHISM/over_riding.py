"""Create an Animal class with a sound() method. Create Dog and Cat subclasses that override the sound() method."""

class Animal:
    def sound(self):
        print("Animal")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("Bark")

def func(a):
    a.sound()
func(Cat())
func(Dog())


Animals=[Dog(),Cat()]
for i in Animals:
    i.sound()