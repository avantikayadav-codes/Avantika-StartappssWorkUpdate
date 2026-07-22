"""Group students department-wise using defaultdict.
Input
[
("Rahul","IT"),
("Aman","HR"),
("Rohit","IT")
]
"""

from collections import defaultdict
group=[
("Rahul","IT"),
("Aman","HR"),
("Rohit","IT")
]

dict=defaultdict(list)
for name,branch in group:
    dict[branch].append(name)
print(dict)


