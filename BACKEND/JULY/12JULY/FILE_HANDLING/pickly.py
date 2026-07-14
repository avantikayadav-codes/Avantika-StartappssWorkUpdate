import pickle
student = {"id":102,"name":"Avantika"}
with open("student.pkl","+ab") as file:
    pickle.dump(student,file)
    file.seek(0)
    print(pickle.load(file))
