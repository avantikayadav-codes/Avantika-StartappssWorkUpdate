def func():
    msg="Python is Awesome"
    def inner():
        print(msg)
    return inner
a=func()
a()