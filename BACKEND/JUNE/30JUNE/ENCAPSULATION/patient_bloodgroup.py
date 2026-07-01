"""Patient
Create a Patient class.
Private Attributes
•	__blood_group
Methods
•	get_blood_group()
•	set_blood_group()
Condition:
•	Allow only valid blood groups.
"""

bloods=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
class Patient:
    def __init__(self,bg):
        self.__bloodgroup=bg
    def set_blood_group(self,bld):
        if bld in bloods:
            self.__bloodgroup.append(bld)
            print("Blood accepted:",self.__bloodgroup)
        else:
            print("Invalid Blood group")
    def get_blood_group(self):
        return self.__bloodgroup
a=Patient(["A+","A-"])
b=input("Enter blood group to add:")
a.set_blood_group(b)
print(a.get_blood_group())