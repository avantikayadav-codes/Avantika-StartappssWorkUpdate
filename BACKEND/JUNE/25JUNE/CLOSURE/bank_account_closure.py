def func():
    balance=0
    def inner(choice,amount=0):
        nonlocal balance
        if choice=="deposit":
            balance+=amount
            print("Balance:",balance)
        elif choice=="withdraw":
            if amount<=balance:
                balance-=amount
                print("Balance:",balance)
            else:
                print("Insufficient Balance")
        elif choice=="check":
            print("Balance:",balance)
    return inner
a=func()
a("deposit",1000)
a("withdraw",300)
a("check")