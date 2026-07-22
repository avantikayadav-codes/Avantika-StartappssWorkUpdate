"""9.
Combine three dictionaries using ChainMap.
Priority
User
↓
Company
↓
System
"""

from collections import ChainMap
user={101:"Avantika",102:"Gurman",103:"Arya"}
company={"IT":"Startappss","BANK":"sbi"}
a=ChainMap(user,company)
print(a)