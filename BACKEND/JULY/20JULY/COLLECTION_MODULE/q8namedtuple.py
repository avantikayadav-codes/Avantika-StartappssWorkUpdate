"""Create a namedtuple for Student.
Fields
id
name
salary
Print all students earning more than ₹50,000.
"""

from collections import namedtuple
student=namedtuple("student","id,name,salary")
o1=student(101,"Avantika",70000)
o2=student(102,"Vaishali",40000)
o3=student(103,"Garima",60000)
list=[o1,o2,o3]
for i in list:
    if i.salary>50000:
        print(i)