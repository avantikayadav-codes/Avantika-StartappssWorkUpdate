def dec1(func):
    def wrapper():
        print("hello its decorator 1 start")
        func()
        print("hello its decorator 1 end")
    return wrapper

def dec2(func):
    def wrapper():
        print("hello its decorator 2 start")
        func()
        print("hello its decorator 2 end")
    return wrapper

def dec3(func):
    def wrapper():
        print("hello its decorator 3 start")
        func()
        print("hello its decorator 3 end")
    return wrapper


@dec1
@dec2
@dec3
def a():
    print("hello world!")
a()