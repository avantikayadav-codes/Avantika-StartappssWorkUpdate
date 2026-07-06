"""Create Dog, Cat, and Cow classes with a sound() method. 
Store their objects in a list and use a loop to call sound() on each object."""

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

Animals=[Dog(),Cat(),Cow()]
for i in Animals:
    i.sound()