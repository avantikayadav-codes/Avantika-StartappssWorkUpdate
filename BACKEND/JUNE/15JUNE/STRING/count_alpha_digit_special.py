#count_alpha_digit_special.py


string=input("Enter a string: ")
alph=0
digit=0
spec=0
for i in string:
    if i.isalpha():
        alph+=1
    if i.isdigit():
        digit+=1
    else:
        spec+=1
print("Alphabets are:- ",alph)
print("Digits are:- ",digit)
print("Special characters are:- ",spec)