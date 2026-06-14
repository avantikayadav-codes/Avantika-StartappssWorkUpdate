a=int(input("Enter No. to find sum: "))
sum=0

# normal sum
# for i in range(1,a+1,1):
#     sum += i
# print("sum of ",a," = ",sum)

#even no.
for i in range(2,a+1,2):
    sum += i
print("sum of ",a," = ",sum)