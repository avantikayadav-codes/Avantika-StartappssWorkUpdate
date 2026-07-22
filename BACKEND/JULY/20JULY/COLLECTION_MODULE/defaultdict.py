from collections import defaultdict
d=defaultdict(int)
print(d["python"])





fruits = {"apple": 2,"mango": 3}
d = defaultdict(int, fruits)
print(d["banana"])





fruits=["mango","banana","mango","banana","apple","mosambi","grapes","grapes","grapes"]
count=defaultdict(int)
for word in fruits:
    count[word]+=1
print(count)





count=defaultdict(list)
count["apple"].append(1)
count["apple"].append(1)
count["banana"].append(3)
print(count)




students = [
("Python","Avantika"),
("Python","Aman"),
("Java","Riya"),
("Python","Neha")
]
group=defaultdict(list)
for name,stu in students:
    group[name].append(stu)
print(group)




d = defaultdict(str)
print(d["name"])