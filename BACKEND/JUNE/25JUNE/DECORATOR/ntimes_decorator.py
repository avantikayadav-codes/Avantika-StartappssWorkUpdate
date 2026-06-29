def dec(n):
    def fu(func):
        def wrapper(*args):
            for i in range(n):
                func(*args)
        return wrapper
    return fu

@dec(5)
def a():
    print("hello")
a()