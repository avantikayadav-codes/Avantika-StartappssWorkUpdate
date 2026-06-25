# def dupli(a):
#     c=set(a)
#     for i in c:
#         yield i
# a=[1,2,3,4,1,2,3,34,5,5,6,7,8,9,10,1,2,3,4,5]
# b=dupli(a)
# for i in b:
#     print(i)


def dupli(a):
    b=[]
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)
    for j in b:
        yield j
a=[1,2,3,4,1,2,3,34,5,5,6,7,8,9,10,1,2,3,4,5]
b=dupli(a)
for i in b:
    print(i)