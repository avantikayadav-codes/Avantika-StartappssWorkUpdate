#countloweranduppercase.py

a=input("Enter a string: ")
count1=0
count2=0
for i in a:
    if i.isupper():
        count1+=1
    if i.islower():
        count2+=1
print("Upper case letters in string is: ",count1)
print("Lower case letters in string is: ",count2)