def func():
    cache={}
    def inner(n):
        if n in cache:
            print(cache[n])
            return
        if n<=1:
            cache[n]=n
        else:
            cache[n]=inner_value(n-1)+inner_value(n-2)
        print(cache[n])
    def inner_value(n):
        if n in cache:
            return cache[n]
        if n<=1:
            cache[n]=n
        else:
            cache[n]=inner_value(n-1)+inner_value(n-2)
        return cache[n]
    return inner
a=func()
a(6)
a(6)