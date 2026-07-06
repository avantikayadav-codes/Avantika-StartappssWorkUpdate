from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_salary():
        pass

class Fulltimeemp(Employee):
    def salary(self):
        print("Salary printed")
    def calculate_salary(self):
        print("50,000k")

class Freelancer(Employee):
    def salary(self):
        print("Salary printed")
    def calculate_salary(self):
        print("50,000k")

obj=Fulltimeemp()
obj.salary()
obj.calculate_salary()


obj1=Freelancer()
obj1.salary()
obj1.calculate_salary()