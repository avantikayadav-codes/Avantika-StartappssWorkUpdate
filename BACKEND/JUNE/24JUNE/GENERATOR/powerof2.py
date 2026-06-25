def timer(n):
    for i in range(1,n+1):
        yield(2**i)

n=int(input("Enter the nth number:"))
a=timer(n)
for i in a:
    print(i)