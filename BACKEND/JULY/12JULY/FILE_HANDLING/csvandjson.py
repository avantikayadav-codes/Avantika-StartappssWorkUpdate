import csv
import json

# Sample Data
students = [{"id": 101, "name": "Avantika", "age": 22},{"id": 102, "name": "Rahul", "age": 21},{"id": 103, "name": "Priya", "age": 23}]


# Export to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
    writer.writeheader()
    writer.writerows(students)

# Export to JSON
with open("students.json", "w") as file:
    json.dump(students, file)

print("Data exported successfully!")