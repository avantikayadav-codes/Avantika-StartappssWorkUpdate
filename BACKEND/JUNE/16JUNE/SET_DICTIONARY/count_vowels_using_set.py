#count_vowels_using_set.py

a=set()
count=0
print("Enter strings 1 to 10 in set to find total vowels in it: ")
for i in range(1,11):
    b=input()
    a.add(b)
    for j in b:
        if j in ("aeiou"):
            count+=1
print("Total no. of vowels in whole set is: ",count)