def flatten(a):
    for i in a:
        for j in i:
            yield j



a=[[1,2],[3,4],[5,6],[7,8],[9,10]]
c=flatten(a)
for i in c:
    print(i)