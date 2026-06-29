def func():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner
a=func()
a()
a()
a()