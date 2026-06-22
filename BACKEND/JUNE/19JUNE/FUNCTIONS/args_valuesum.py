def add(*args):
    total=sum(args)
    return total

n=int(input("Enter no. of element:"))
list=[]
for i in range(1,n+1):
    m=int(input(f"Enter element {i}:"))
    list.append(m)
print(add(*list))
