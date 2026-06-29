employees={
    "Rahul":50000,
    "Amit":60000,
    "Neha":70000
}
try:
    name=input("Enter employee name: ")
    print("Salary:",employees[name])
except KeyError:
    print("Employee Not Found")