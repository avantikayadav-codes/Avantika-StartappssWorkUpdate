n=int(input("Enter no. to check armstrong: "))
armstrong=0
check=n

count=0
a=n
while a>0:
    count+=1
    a=a//10


while n>0:
    multi=1
    digit=n%10
    m=count
    while m>0:
        multi*=digit
        m-=1
    armstrong+=multi
    n=n//10

if (check==armstrong):
    print("No. is armstrong")
else:
    print("Not armstrong")