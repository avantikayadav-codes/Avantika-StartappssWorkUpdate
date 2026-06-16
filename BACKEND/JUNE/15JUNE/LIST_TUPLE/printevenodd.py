n=int(input("Enter length of list: "))
a=[]
count=0
count1=0
for i in range(1,n+1):
    b=int(input(f"Enter element {i}: "))
    a.append(b)
    if b%2==0:
        count+=1
    else:
        count1+=1
    
print("Even Numbers in list are: ",count)
print("Odd Numbers in list are: ",count1)