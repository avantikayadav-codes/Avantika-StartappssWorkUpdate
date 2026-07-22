"""Find the first unique character.
apple
↓
Output
a
"""

from collections import Counter
text = "apple"
c = Counter(text)
for ch in text:
    if c[ch] == 1:
        print(ch)
        break



list=["apple","banana","list","tuple","yoyo","honey","singh"]
li=[]
for i in list:
    li.append(i[0])
print(li)