#tupleof_10_countgreater50.py

a=(10,20,30,40,60,70,80,99)
count=0
for i in a:
    if i>50:
        count+=1
print(a)
print("Greater than 50 in tuple: ",count)