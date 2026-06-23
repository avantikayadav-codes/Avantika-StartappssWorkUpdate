a=["my","name","is","avantika","and","i","love","python"]
b={i:sum(1 for j in i if j in "aeiou")for i in a}
print(b)