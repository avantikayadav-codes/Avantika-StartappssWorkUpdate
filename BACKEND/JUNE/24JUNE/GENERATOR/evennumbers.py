def even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
m=int(input("Enter nth number: "))
a=even(m)
for i in a:
    print(i)
