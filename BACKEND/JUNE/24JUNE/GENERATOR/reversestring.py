def reverse(n):
    a=n[::-1]
    for i in a:
        yield i
n=["hi","my","name"]
m=reverse(n)
for i in m:
    print(i)