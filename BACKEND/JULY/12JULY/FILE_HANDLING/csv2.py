import csv
with open("record.csv","a+") as file:
    # read=csv.DictReader(file)
    # for i in read:
    #     print(i)
    filenames=["ID","Name"]
    write=csv.DictWriter(file,fieldnames=filenames)
    write.writerow({"ID":101,"Name":"Avantika"})