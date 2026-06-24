class ite:
    def __init__(self,employees):
        self.current=employees
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(employees):
            raise StopIteration
        value=self.current[self.index]
        self.index+=1
        return value, self.index
        
    

employees = ["John", "Mike", "Sara", "Alex"]
a=ite(employees)
for i in a:
    print(i)
print(len(employees))
