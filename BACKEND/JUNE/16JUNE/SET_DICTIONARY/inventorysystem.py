#inventorysystem.py

n=int(input("Enter the number of products: "))
dict={}
for i in range(1,n+1):
    product=input("Enter product name: ")
    quantity=int(input("Enter quantity: "))
    dict[product]=quantity
print(dict)