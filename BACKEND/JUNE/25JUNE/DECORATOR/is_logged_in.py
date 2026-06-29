is_logged_in=True

def a(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Can not login")
    return wrapper

@a
def fu():
    print("function Executed")
fu()