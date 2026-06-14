n=int(input("Enter number to check digits: "))
count=0
while n>0:
    count+=1
    n=n//10
print(f"The digits in no. are {count}")