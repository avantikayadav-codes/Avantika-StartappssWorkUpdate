from functools import reduce
fact = {i: reduce(lambda x,y: x*y, range(1,i+1))for i in range(1,21)}
print(fact)