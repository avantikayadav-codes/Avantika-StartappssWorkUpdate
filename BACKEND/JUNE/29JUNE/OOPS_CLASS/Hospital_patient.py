class Patient:
    def __init__(self,patient_id,name,age,gender,disease,doctor_name,room_number,blood_group):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.gender=gender
        self.disease=disease
        self.doctor_name=doctor_name
        self.room_number=room_number
        self.blood_group=blood_group

    def checkup(self):
        print(self.name,"is under checkup")

    def admit(self):
        print(self.name,"has been admitted successfully")

    def discharge(self):
        print(self.name,"has been discharged")

    def take_medicine(self):
        medicine=input("Enter medicine name: ")
        print(self.name,"took",medicine)

    def show_report(self):
        print("Patient ID :",self.patient_id)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)
        print("Disease :",self.disease)
        print("Doctor Name :",self.doctor_name)
        print("Room Number :",self.room_number)
        print("Blood Group :",self.blood_group)


obj=Patient(
    101,
    "Avantika",
    22,
    "Female",
    "Viral Fever",
    "Dr. Sharma",
    205,
    "B+"
)

obj.checkup()
obj.admit()
obj.take_medicine()
obj.show_report()
obj.discharge()