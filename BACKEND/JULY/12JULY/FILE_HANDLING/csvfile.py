import csv
# a=[[105,"Nishta",23],[106,"Ambika",23]]
a=[
    {"ID":108, "Name":"Ram", "Age":21},
    {"ID":109, "Name":"Priya", "Age":24}
]
with open("student.csv","a+",newline="") as file:
    fieldnames = ["ID", "Name", "Age"]
    read=csv.DictReader(file)
    file.seek(0)
    for i in read:
        print(i)
    # wr=csv.DictWriter(file,fieldnames=fieldnames)
    # wr.writerow({"ID":110, "Name":"Priya", "Age":24})
    # wr.writerows(a)

    
