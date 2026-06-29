import time
def dec(n):
    def fu(func):
        def wrapper():
            for i in range(n):
                start = time.time() 
                func()
                end = time.time()     
            print("Execution Time:", end - start, "seconds")
        return wrapper
    return fu

@dec(5)
def a():
    print("hello")
a()