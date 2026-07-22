"""12.
Find duplicate words in a text using Counter.
"""

from collections import Counter
para="Hiii, My name is Avantika and currently i am working as a python developer" \
"I enjoy programming and i also enjoy shopping, My friend name is gurman, he also work with me, My name is good"
li=para.split()
c=Counter(li)
dict={}
for word,freq in c.items():
    if freq>1:
        dict[word]=freq
print(dict)
