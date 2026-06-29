def func():
    x=10
    def inner():
        nonlocal x
        x+=5
        print(x)
    return inner
a=func()
a()
a()
a()