"""9. Movie Ticket
Create a MovieTicket class.
Private Attributes
•	__seat_number
•	__price
Methods
•	book_ticket()
•	cancel_ticket()
•	get_ticket_details()
"""

class MovieTicket:
    def __init__(self,seatno,price):
        self.__seatnum=seatno
        self.__price=price

    def book_ticket(self):
        print("Available tickets:",self.__seatnum,"please enter to book!")
        n=int(input())
        if n in self.__seatnum:
            self.__seatnum=n
            print("Ticket booked")
        else:
            print("Invalid ticket number")

    def cancel_ticket(self):
        print("tickets cancelled!")
    def get_ticket_details(self):
        print("Ticket details:")
        return self.__seatnum,":" ,self.__price
a=MovieTicket([1,2,3,4,5],100)
a.book_ticket()
a.cancel_ticket()
print(a.get_ticket_details())






















class Bank:
    def __init__(self,no):
        self.__locker=no
    @property
    def locker(self,n): 
        self.__locker=n
        return self.__locker 

obj=Bank(101)
print(obj.locker)
obj.locker(500)
print(obj.locker)