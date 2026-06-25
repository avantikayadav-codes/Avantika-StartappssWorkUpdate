def cumul(a):
    m=0
    for i in a:
        m+=i
        yield m

a=[1,2,3,4,5,6,7,8,9,10]
b=cumul(a)

for i in b:
    print(i)