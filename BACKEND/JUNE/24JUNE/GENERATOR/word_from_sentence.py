def word(m):
    for i in m:
        yield i

n=input("Enter a Sentence:")
m=n.split()
a=word(m)
for i in a:
    print(i)