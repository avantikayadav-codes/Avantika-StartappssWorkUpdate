"""Bank Account
Create a BankAccount class.
Private Attributes
•	__account_number
•	__balance
Methods
•	deposit()
•	withdraw()
•	get_balance()
Condition:
•	Deposit amount must be positive.
•	Cannot withdraw more than available balance.
"""


class bank_account():
    def __init__(self,acnum,balance):
        self.__account_number=acnum
        self.__balance=balance
    def deposit(self,balance):
        print("Deposited successfull!")
        self.__balance+=balance
        print("Updated balance:",self.__balance)
    def withdraw(self,balance):
        if balance<=self.__balance:
            self.__balance-=balance
            print("Updated balance:",self.__balance)
        else:
            print("Insufficient balance!")
    def get_balance(self):
        return "Your balance is: ", self.__balance 
    
a=bank_account(12345,50000)
n=int(input("Enter balance to deposit:"))
a.deposit(n)
n=int(input("Enter balance to withdraw:"))
a.withdraw(n)
print(a.get_balance())