def factorial(n):
    num=1
    while n>0:
        num*=n
        n-=1
    return num
n=int(input("Enter Number to find factorial: "))
# fact=factorial(n)
print(factorial(n))
