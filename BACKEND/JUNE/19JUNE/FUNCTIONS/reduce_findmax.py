from functools import reduce
nums=[10,45,23,67,12]
a=reduce(lambda x,y:x if x>y else y,nums)
print(a)