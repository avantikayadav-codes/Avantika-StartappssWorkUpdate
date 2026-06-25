def square(n):
    for i in n:
        yield i*i

m=[1,2,3,4,5,6,7,8,9]
a=square(m)
for i in a:
    print(i)