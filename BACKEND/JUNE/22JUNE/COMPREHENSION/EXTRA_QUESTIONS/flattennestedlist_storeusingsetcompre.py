nested = [[1, 2], [3, 4], [5, 6],[5,2],[8,4]]

a={a for i in nested for a in i}
print(a)