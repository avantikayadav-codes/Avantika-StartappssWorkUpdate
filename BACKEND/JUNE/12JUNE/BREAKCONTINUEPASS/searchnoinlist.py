#searchnoinlist.py

n=int(input("Enter the total no. of elements in list: "))
list=[]
for i in range(1,n+1):
    n=int(input("Enter the elements: "))
    list.append(n)

find=int(input("Enter the element to find: "))
for i in range(len(list)):
    if list[i]==find:
        print("Element found!")
        break
else:
    print("Element not found")