def odd(a):
    for i in a:
        if i%2!=0:
            yield i
a=[1,2,3,4,5,6,7,8,9,10]
m=odd(a)
print("Odd numbers in list are:")
for i in m:
    print(i)