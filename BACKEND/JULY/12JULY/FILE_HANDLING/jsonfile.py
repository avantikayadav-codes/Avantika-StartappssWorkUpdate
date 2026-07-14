import json
student= {"id": 1, "name": "Avantika"},{"id": 2, "name": "Nishta"}
with open("stu_record.json","a",newline="") as file:
    json.dump(student,file,indent=4)
    print(json.load(file))


# import json
# with open("stu_record.json", "r") as f:
#     data = json.load(f)

# data.append({"ID": 102, "Name": "Nishta"})

# with open("student.json", "w") as f:
#     json.dump(data, f, indent=4)