class a:
    def __init__(self,start,stop):
        self.current=start
        self.end=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=self.end+1:
            raise StopIteration
        value=self.current
        self.current+=1
        return value

b=a(5,10)
for i in b:
    print(i)