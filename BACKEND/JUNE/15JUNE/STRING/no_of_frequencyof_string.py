#no_of_frequencyof_string.py

str=input("Enter the string to count frequency: ")
dictt={}
for i in str:
    if i in dictt:
        dictt[i]+=1
    else:
        dictt[i]=1
print(dictt)
