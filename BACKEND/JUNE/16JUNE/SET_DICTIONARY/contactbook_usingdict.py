#contactbook_usingdict.py

a={}

n=int(input("Enter the number of contacts: "))
for i in range(1,n+1):
    name=input(f"Enter contact {i}: ")
    numbers=int(input("Enter contact number: "))
    addresss=input("Enter Address: ")
    a[name]={"number":numbers,"address":addresss}
print(a)