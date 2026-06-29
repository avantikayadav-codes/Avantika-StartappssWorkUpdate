class ATM:
    def __init__(self,account_number,card_number,pin,balance,account_holder,bank_name,branch,ATM_location):
        self.account_number=account_number
        self.card_number=card_number
        self.pin=pin
        self.balance=balance
        self.account_holder=account_holder
        self.bank_name=bank_name
        self.branch=branch
        self.ATM_location=ATM_location

    def withdraw_cash(self):
        amount=int(input("Enter amount to withdraw: "))
        if amount<=self.balance:
            self.balance-=amount
            print("Cash Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def deposit_cash(self):
        amount=int(input("Enter amount to deposit: "))
        self.balance+=amount
        print("Amount Deposited Successfully")

    def check_balance(self):
        print("Current Balance =",self.balance)

    def change_pin(self):
        new_pin=int(input("Enter New PIN: "))
        self.pin=new_pin
        print("PIN Changed Successfully")

    def mini_statement(self):
        print("Account Number :",self.account_number)
        print("Account Holder :",self.account_holder)
        print("Bank Name :",self.bank_name)
        print("Branch :",self.branch)
        print("ATM Location :",self.ATM_location)
        print("Current Balance :",self.balance)


obj=ATM(
    123456789,
    9876543210123456,
    1234,
    50000,
    "Avantika",
    "Punjab National Bank",
    "Indore",
    "Vijay Nagar"
)

obj.withdraw_cash()
obj.deposit_cash()
obj.check_balance()
obj.change_pin()
obj.mini_statement()