def func():
    total=0
    def inner(n):
        nonlocal total
        total+=n
        print(total)
    return inner
a=func()
a(10)
a(20)
a(30)