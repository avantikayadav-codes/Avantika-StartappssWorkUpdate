def prime(n):
    for i in range(2,n+1):
            if all(i % j != 0 for j in range(2, i)):
                yield i

m=int(input("Enter n term for prime:"))
a=prime(m)
for i in a:
    print(i)