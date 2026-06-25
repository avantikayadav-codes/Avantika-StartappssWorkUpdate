def nval(n):
    for i in range(1,n+1):
        yield(i)

n=int(input("Enter the nth number:"))
a=nval(n)
for i in a:
    print(i)