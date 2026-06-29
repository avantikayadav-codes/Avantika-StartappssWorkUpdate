def fun(fu):
    def wrapper(*args):
        print("func name:",fu.__name__)
        print(args)
        return fu(*args)
    return wrapper
dict={}
for i in range(5):
    j=input("Enter name")
    dict[i]=j

@fun
def a(*args):
    print("hello")
    print(args)
a(dict)
# @fun
# def a(name,age):
#     print("hello")
# a(name="Avantika",age=22)






print("--------------------------------------------------")








def logger(func):
    def wrapper(*args, **kwargs):
        print("Function Name:", func.__name__)
        print("Positional Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper
@logger
def student(name, age):
    print("Hello", name, age)
student(name="Avantika", age=22)
