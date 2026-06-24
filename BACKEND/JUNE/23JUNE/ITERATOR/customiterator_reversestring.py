text = "Python"

class py:
    def __init__(self,text):
        self.current=text
        self.index=-1

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index<=-(len(text)+1):
            raise StopIteration
        
        value=self.current[self.index]
        self.index-=1
        return value,self.index

a=py(text)
for i in a:
    print(i)