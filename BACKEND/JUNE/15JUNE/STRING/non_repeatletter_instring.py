#non_repeatletter_instring.py


inp=input("Enter a string: ")
count=1
for i in inp:
    if inp.count(i)==1:
        print("First Non-repeated char is:",i)
        break
else:
    print("Every character is repeated")