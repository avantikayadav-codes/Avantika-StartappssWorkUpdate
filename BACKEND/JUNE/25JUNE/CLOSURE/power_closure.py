def func(power):
    def inner(n):
        print(n**power)
    return inner
square=func(2)
cube=func(3)
fourth=func(4)
square(5)
cube(5)
fourth(5)