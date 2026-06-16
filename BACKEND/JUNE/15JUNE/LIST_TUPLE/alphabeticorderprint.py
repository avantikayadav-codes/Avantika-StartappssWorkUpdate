#alphabeticorderprint.py

list=[]

print("Enter strings to sort alphabetically: ")
for i in range(1,6):
    a=input(f"enter string {i}: ")
    list.append(a)
list.sort()
print(list)