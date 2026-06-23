a=[1,2,4,5,7,5,3,3,6,8,3,4,6]
b=[34,3,6,3,7,45,7,45,7,9,44]

k=[i for i in a if i in b]
print(k)




k=[set(a) & set(b)]
print(k)