#removeduplicate.py

list=[]
update=[]
n=int(input("Enter length of list: "))
print("Enter the elements: ")
for i in range(1,n+1):
    element=int(input())
    list.append(element)

for i in list:
    if i not in update:
        update.append(i)
    else:
        continue
print("List after removing duplicates: ",update)




