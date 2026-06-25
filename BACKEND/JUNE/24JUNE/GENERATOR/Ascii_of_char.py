def asc(a):
    for i in a:
        yield ord(i)

a="Hi my name is avantika"
b=asc(a)
for i in b:
    print(i)