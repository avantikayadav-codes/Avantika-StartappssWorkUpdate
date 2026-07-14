class Engine():
    def __init__(self):
        self.this="petrol"

class Car():
    def __init__(self):
        self.engine=Engine()
    def metho(self):
        print(self.engine.this)

ca=Car()
ca.metho()