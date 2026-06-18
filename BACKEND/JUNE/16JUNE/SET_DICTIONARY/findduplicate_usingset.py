#findduplicate_usingset.py


a=[10,10,20,30,40,50,20,40,60]
b=set()
c=set()
for i in a:
    if i in b:
        c.add(i)
    else:
        b.add(i)
print("Duplicates are: ",c)

