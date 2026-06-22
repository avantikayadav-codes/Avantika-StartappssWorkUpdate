from functools import reduce

li=range(1,7)
a=reduce(lambda x,y:x*y,li)
print("Factorial of 6:",a)