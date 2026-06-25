def timer(n):
    for i in range(n,-1,-1):
        yield(i)

n=int(input("Enter the nth number:"))
a=timer(n)
for i in a:
    print(i)