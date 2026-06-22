from functools import reduce
"""
1.	Filter even numbers.
2.	Square them.
3.	Find their sum.
"""
nums = [1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x:x%2==0,nums))
print(a)

b=list(map(lambda x:x**2,nums))
print(b)

c=reduce(lambda x,y:x+y,nums)
print(c)