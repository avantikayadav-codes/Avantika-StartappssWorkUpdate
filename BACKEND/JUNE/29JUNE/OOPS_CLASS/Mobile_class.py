class Mobile:
    def __init__(self,brand,model,ram,storage,battery,camera,processor,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.storage=storage
        self.battery=battery
        self.camera=camera
        self.processor=processor
        self.price=price

    def call(self):
        number=input("Enter phone number: ")
        print("Calling",number,"...")

    def send_message(self):
        number=input("Enter phone number: ")
        message=input("Enter message: ")
        print("Message sent to",number)

    def take_photo(self):
        print("Photo Captured Successfully")

    def charge(self):
        print("Mobile Charging...")

    def show_specification(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("RAM :",self.ram)
        print("Storage :",self.storage)
        print("Battery :",self.battery)
        print("Camera :",self.camera)
        print("Processor :",self.processor)
        print("Price :",self.price)


obj=Mobile(
    "Samsung",
    "Galaxy S25",
    "12 GB",
    "256 GB",
    "5000 mAh",
    "200 MP",
    "Snapdragon 8 Elite",
    85000
)

obj.call()
obj.send_message()
obj.take_photo()
obj.charge()
obj.show_specification()