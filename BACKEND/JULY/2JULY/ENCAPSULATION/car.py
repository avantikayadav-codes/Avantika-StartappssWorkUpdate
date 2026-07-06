"""Car
Create a Car class.
Private Attributes
•	__speed
Methods
•	accelerate()
•	brake()
•	get_speed()
Condition:
•	Speed cannot be negative.
"""

class car:
    def __init__(self,speed):
        self.__speed=speed
    def set_accelerate(self,s):
        if self.__speed<0:
            print("Value Cant be negative")
        else:
            self.__speed+=s  
            print("Accelerated!!! Current speed:",self.__speed)   
    def brake(self):
        if self.__speed>15:
            print("Brakes!!! speed decresed, current speed:",self.__speed-5)
        else:
            print("Can not press brake, their is no speed")
    def get_speed(self):
        print("Current speed:",self.__speed)
sp=int(input("Enter speed of car:"))
a=car(sp)
s=int(input("Enter speed to accelerate:"))
a.set_accelerate(s)
a.brake()
a.get_speed()
