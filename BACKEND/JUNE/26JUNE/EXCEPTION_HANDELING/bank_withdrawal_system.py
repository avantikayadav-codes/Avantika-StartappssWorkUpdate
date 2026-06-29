class BalanceError(Exception):
    pass
balance=10000
try:
    amount=int(input("Enter Withdrawal Amount: "))
    if amount>balance:
        raise BalanceError("Insufficient Balance")
    balance-=amount
    print("Remaining Balance:",balance)
except BalanceError as e:
    print(e)