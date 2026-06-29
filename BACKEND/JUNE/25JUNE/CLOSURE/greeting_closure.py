def func(name):
    def inner():
        print("Hello",name)
    return inner
a=func("Avantika")
a()