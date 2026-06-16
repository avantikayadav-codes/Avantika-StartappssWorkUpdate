#vowelscount.py

string=input("Enter a string: ")
count=0
for i in string:
    if i in "aeiou":
        count+=1
print("Total vowels: ",count)