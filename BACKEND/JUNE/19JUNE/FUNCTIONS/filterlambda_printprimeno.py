a=range(1,51)
i=list(filter(lambda x:x>1 and all(x%i!=0 and i!=x for i in range(2,x)),a))
print(i)