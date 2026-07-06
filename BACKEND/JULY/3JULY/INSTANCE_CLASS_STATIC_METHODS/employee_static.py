class Employee:

    @staticmethod
    def validate_age(age):
        if age>=18:
            return "Eligible"
        else:
            return "Not Eligible"

print(Employee.validate_age(20))
print(Employee.validate_age(15))