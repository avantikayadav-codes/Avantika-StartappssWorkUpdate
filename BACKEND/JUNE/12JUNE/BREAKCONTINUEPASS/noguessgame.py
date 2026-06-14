#noguessgame.py

print("--------------------------------\nWelcome to number Guessing game!\n You got only 5 Moves\n--------------------------------")

count=5
while count>0:
    n=int(input("Guess the number: "))
    if n==25:
        print("Correct guess! YOU WONNN:)")
        break
    if n<25:
        print("The number is Greater then ",n)
    if n>25:
        print("The number is small then ",n)
    count-=1
    print("Your are close!!!")
else:
    print("OOPSSS! Out of moves:(")