from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")


class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking")


obj1 = UPI()
obj2 = CreditCard()
obj3 = NetBanking()

obj1.pay()
obj2.pay()
obj3.pay()