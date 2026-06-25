def infi(n):
    while True:
        yield n
        n+=1
n=1
a=infi(n)
for i in a:
    print(i)