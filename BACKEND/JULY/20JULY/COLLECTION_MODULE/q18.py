"""Given
sales=[
("Rahul","Laptop"),
("Rahul","Laptop"),
("Aman","Mouse"),
("Rahul","Mouse")
]
Output
Rahul
Laptop :2
Mouse :1
Aman
Mouse :1
Use
defaultdict
Counter
"""


from collections import defaultdict, Counter

sales = [
    ("Rahul", "Laptop"),
    ("Aman", "Laptop"),
    ("Rahul", "Mouse"),
    ("Aman", "Mouse"),
    ("Rahul", "Laptop"),
    ("Aman", "Mouse")
]

group = defaultdict(list)

for name, pro in sales:
    group[name].append(pro)

for name, products in group.items():
    print(name)
    c = Counter(products)
    for product, count in c.items():
        print(f"{product} : {count}")