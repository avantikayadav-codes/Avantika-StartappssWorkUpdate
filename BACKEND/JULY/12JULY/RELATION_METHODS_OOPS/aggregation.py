class Engine():
    def __init__(self):
        self.this="petrol"

class Car():
    def __init__(self,engine):
        self.engine=engine
    def metho(self):
        print(self.engine.this)

eng=Engine()
ca=Car(eng)
ca.metho()