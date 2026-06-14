n=int(input("Enter no. for fibonacci series:- "))
a,b=0,1
print(a)
print(b)
while 0<n-2:
    c=a+b
    print(c)
    a,b=b,c
    n-=1
