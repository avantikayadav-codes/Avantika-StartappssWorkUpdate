"""Group employees according to salary range.
0-20000

20001-50000

50001+
Use defaultdict.
"""
from collections import defaultdict
emp=[("Rahul",20000),("Ram",30000),("Gurman",40000),("Avantika",55000)]
dict=defaultdict(list)
for name,sal in emp:
    if 0<sal<=20000:
        dict["0-20000"].append((name,sal))
    elif 20001<sal<=50000:
        dict["20001-50000"].append((name,sal))
    elif 50001<sal:
        dict["50001+"].append((name,sal))
print(dict)