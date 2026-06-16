#subject_mark_listtuple.py


tuple=("Maths","English","Hindi","Sanskrit","Science")
list=[90,80,70,80,60]

for subject,marks in zip(tuple,list):
    print(f"{subject} : {marks}")