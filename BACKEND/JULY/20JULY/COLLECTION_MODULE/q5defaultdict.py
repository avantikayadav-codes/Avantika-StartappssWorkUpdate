"""Count how many employees belong to each department using defaultdict."""
from collections import defaultdict
group=[
("Rahul","IT"),
("Aman","HR"),
("Rohit","IT"),
("Arya","HR"),
]
dict=defaultdict(int)
for name,depart in group:
    dict[depart]+=1
print(dict)
