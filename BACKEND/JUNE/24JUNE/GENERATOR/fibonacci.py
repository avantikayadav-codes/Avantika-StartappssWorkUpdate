def fibo(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b

        
n=int(input("Enter n for fibonacci: "))
a=fibo(n)
for i in a:
    print(i)