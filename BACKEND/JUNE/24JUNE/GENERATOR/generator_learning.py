def test():

 print("Hello")

 yield 5

 print("World")
 

g = test()

print(next(g))
print(next(g))