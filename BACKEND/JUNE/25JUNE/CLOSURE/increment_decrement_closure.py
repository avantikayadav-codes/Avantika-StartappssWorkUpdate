def func():
    count=0
    def increment():
        nonlocal count
        count+=1
        print("Increment:",count)
    def decrement():
        nonlocal count
        count-=1
        print("Decrement:",count)
    return increment,decrement
inc,dec=func()
inc()
inc()
dec()
inc()