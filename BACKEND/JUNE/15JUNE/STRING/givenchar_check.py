#givenchar_check.py

str=input("Enter string to check character: ")
for i in str:
    if "k"==i:
        print("Given character K found")
        break
else:
    print("Given character k not found")