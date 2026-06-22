from functools import reduce
words=['Python',
       'is',
       'awesome']

a=reduce(lambda x,y:x+" "+" "+y,words)
print(a)