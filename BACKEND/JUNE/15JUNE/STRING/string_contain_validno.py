#string_contain_validno.py
count=0
a=input("Enter a string to check if it contains digit only or not: \n")
b=len(a)
for i in a:
    if i.isdigit():
        count+=1
if count==b:
    print("String is only digits!")
else:
    print("contains string")