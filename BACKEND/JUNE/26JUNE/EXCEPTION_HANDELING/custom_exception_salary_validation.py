class SalaryError(Exception):
    pass
try:
    salary=int(input("Enter Salary: "))
    if salary<20000:
        raise SalaryError("Salary must be at least 20000")
    print("Valid Salary")
except SalaryError as e:
    print(e)