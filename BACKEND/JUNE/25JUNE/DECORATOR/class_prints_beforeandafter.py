class Decorator:
    def __init__(self,func):
        self.func=func

    def __call__(self):
        print("function started")
        rult=self.func()
        print("function ended")
        return rult

@Decorator
def a():
    print("Hello World!")
a()