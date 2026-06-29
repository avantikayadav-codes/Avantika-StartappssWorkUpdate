class BankAccount:
    def __init__(self,account_number,account_holder,bank_name,branch,balance,account_type,IFSC,mobile_number):
        self.account_number=account_number
        self.account_holder=account_holder
        self.bank_name=bank_name
        self.branch=branch
        self.balance=balance
        self.account_type=account_type
        self.IFSC=IFSC
        self.mobile_number=mobile_number

    def deposit(self):
        amount=int(input("Enter amount to deposit: "))
        self.balance+=amount
        print("Amount Deposited Successfully")
        print("Current Balance =",self.balance)

    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if amount<=self.balance:
            self.balance-=amount
            print("Amount Withdrawn Successfully")
            print("Remaining Balance =",self.balance)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance =",self.balance)

    def transfer_money(self):
        amount=int(input("Enter amount to transfer: "))
        if amount<=self.balance:
            self.balance-=amount
            print("Money Transferred Successfully")
            print("Remaining Balance =",self.balance)
        else:
            print("Insufficient Balance")

    def print_statement(self):
        print("Account Number :",self.account_number)
        print("Account Holder :",self.account_holder)
        print("Bank Name :",self.bank_name)
        print("Branch :",self.branch)
        print("Balance :",self.balance)
        print("Account Type :",self.account_type)
        print("IFSC :",self.IFSC)
        print("Mobile Number :",self.mobile_number)


obj=BankAccount(
    123456789,
    "Avantika",
    "Punjab National Bank",
    "Indore",
    50000,
    "Saving",
    "PUNB12345",
    9876543210
)

obj.deposit()
obj.withdraw()
obj.check_balance()
obj.transfer_money()
obj.print_statement()