#frequency_of_wordinsentence.py

a=input("Enter the no. of string to find frequency: ")
word=a.split()
dict={}

for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1


for word,number in dict.items():
    print(f"{word} : {number}")