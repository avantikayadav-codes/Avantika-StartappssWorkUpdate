"""Find the most common word in a paragraph using Counter."""
from collections import Counter

para="Hiii, My name is Avantika and currently i am working as a python developer" \
"I enjoy programming and i also enjoy shopping, My friend name is gurman, he also work with me"
li=para.split()
c=Counter(li)
print(c.most_common(3))