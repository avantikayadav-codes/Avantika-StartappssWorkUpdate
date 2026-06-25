def fact(n):
    for i in range(1,n+1):
        m=1
        for j in range(1,i+1):
            m*=j
        yield m
n=int(input("Enter nth term for factorial: "))
a=fact(n)
for i in a:
    print(i)