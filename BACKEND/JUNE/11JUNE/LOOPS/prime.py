a=int(input("Enter Number: "))

count=0
for i in range(1,a+1):
    if a/i==int(a/i):
       count += 1

if count==2:
    print("Prime")
else:
    print("not prime")