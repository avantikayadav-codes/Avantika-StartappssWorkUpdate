def counter(func):
    def wrapper():
        wrapper.count += 1
        print("Called", wrapper.count, "times")
        return func()
    wrapper.count = 0
    return wrapper
@counter
def hello():
    print("Hello")
hello()
hello()
hello()
print("Final Count:", hello.count)



def counter(func):
    print("Counter called")
    def wrapper():
        print("Wrapper called")
        func()
    return wrapper
@counter
def hello():
    print("Hello")
hello()
hello()
hello()