import csv
import json
import logging

logging.basicConfig(filename="error.log",level=logging.ERROR,format="%(asctime)s:%(levelname)s:%(message)s")

try:
    with open("student.csv","r") as file:
        data=list[(csv.DictReader(file))]   #python object
    
    with open("student.json","w") as file:
        json.dump(data,file,indent=4)  #JSON

    with open("student.json","r") as file:
        pr=json.load(file)

    print(pr)
except Exception:
    logging.exception("Exception while coverting csv to json")







