def alt(a,b):
    for i,j in zip(a,b):
        yield i
        yield j

a=[1,2,3,4,5]
b=["a","b","c","d","e"]
c=alt(a,b)
for i in c:
    print(i)