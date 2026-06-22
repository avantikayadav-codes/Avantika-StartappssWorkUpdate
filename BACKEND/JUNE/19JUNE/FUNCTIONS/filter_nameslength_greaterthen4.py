names=['Ram','Shyam',
       'John','Bob',
       'Alexander']

a=list(filter(lambda x:len(x)>=4,names))
print(a)