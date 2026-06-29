def func(b):
    cache={}
    def wrapper(*args):
  
        if args in cache:
            print("Result from cache",cache[args])
            return cache[args]

        result=b(*args)
        cache[args]=result
        print("result calculated",result)
        # return result
    return wrapper


@func
def a(n):
    return n*n
a(5)
a(10)
a(15)
a(5)
a(10)
a(15)
