class Employee:
    def __init__(self,name,i,salary):
        self.__name=name
        self.__id=i
        self.__salary=salary
    
    @property
    def emp_details(self):
        return self.__name,self.__id,self.__salary
    @emp_details.setter
    def emp_details(self,salary):
        self.__salary=salary
    @emp_details.deleter
    def emp_details(self):
        print("Employee deleted")
        del self.__name
        del self.__id
        del self.__salary
    

obj=Employee("Avantika",101,60000)
print(obj.emp_details)
obj.emp_details=80000
print(obj.emp_details)
del obj.emp_details

