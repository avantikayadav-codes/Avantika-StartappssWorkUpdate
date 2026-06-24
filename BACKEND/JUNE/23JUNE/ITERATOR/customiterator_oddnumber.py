class ite:
    def __init__(self):
        self.current=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=21:
            raise StopIteration
        
        value=self.current
        self.current+=1
        return value
    
        

a=ite()
for i in a:
    print(i)