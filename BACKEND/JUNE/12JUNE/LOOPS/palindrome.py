n=int(input("Enter no. you want to reverse: "))
number=0
palin=n
while n>0:
    digit=n%10
    number=number*10+digit
    n=n//10

if(number==palin):
    print("It is palindrome no.")
else:
    print("Not palindrome")