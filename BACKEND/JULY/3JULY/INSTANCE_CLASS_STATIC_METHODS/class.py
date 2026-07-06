class Employee:
    company="Google"

    @classmethod
    def update_company(cls,new_company):
        cls.company=new_company

obj=Employee()

print(Employee.company)
Employee.update_company("Microsoft")
print(Employee.company)