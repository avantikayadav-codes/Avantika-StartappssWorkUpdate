def func(num):
    def inner(n):
        print(n*num)
    return inner
a=func(5)
a(10)
a(20)