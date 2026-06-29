def func(fu):
    def wrapper(*args):
        try:
            if args[0]>=0:
                print("square is:",fu(*args))
            else:
                raise Exception("Value is negative")
        except Exception as e:
            print(e)

    return wrapper




@func
def a(n):
    return n*n
a(2)
a(-2)