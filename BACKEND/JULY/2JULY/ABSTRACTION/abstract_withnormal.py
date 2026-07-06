from abc import ABC, abstractmethod

class Person(ABC):

    def display(self):
        print("Welcome")

    @abstractmethod
    def work(self):
        pass


class Student(Person):

    def work(self):
        print("Student Studies")


obj = Student()

obj.display()
obj.work()