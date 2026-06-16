#tuple_sum_max_min.py

lst=[]
print("Enter 10 elements in tuple: ")
for i in range(1,11):
    a=int(input())
    lst.append(a)
tup=tuple(lst)

print("Max element is: ",max(tup))
print("Min element is: ",min(tup))
print("Sum of element is: ",sum(tup))