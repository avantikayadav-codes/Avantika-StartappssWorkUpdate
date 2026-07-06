class addition:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return self.num + other.num
obj=addition(10)
obj1=addition(20)

print(obj+obj1)