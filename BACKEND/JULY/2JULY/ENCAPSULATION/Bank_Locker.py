"""Bank Locker
Use private attributes and @property.
Condition:
•	Locker number cannot be changed after creation.
"""


class BankLocker:
    def __init__(self,no):
        self.__locker=no
    @property
    def locker(self):
        print("Locker Number:")
        print(self.__locker)

obj=BankLocker(101)
obj.locker
obj.locker=500

print("-------------------------------------------")

class BankLocker:
    def __init__(self,no):
        self.__locker=no
    @property
    def locker(self):
        print("Locker Number:")
        print(self.__locker)
    @locker.setter
    def locker(self,n):
        self.__locker=n
        print("Updated Locker Number:")
        print(self.__locker)

obj=BankLocker(101)
obj.locker
obj.locker=501
obj.locker