from functools import reduce
nums=[1,2,3,4]
i=reduce(lambda a,b:a*b,nums)
print(i)