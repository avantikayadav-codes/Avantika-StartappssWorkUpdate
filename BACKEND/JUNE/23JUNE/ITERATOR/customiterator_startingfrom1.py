class yoyo:
    def __init__(self):
        self.current=1

    def __iter__(self):
        return self
    
    def __next__(self):
        value=self.current
        self.current+=1
        return value
    
a=yoyo()
for i in a:
    print(i)