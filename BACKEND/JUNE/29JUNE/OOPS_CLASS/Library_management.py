"""
Attributes (8)
•	book_id
•	title
•	author
•	publisher
•	genre
•	price
•	total_pages
•	available_copies
Methods (5)
•	issue_book()
•	return_book()
•	show_details()
•	update_price()
•	check_availability()
"""

class library:
    def __init__(self,bookid,title,author,publisher,genre,price,pages,copies):
        self.book_id=bookid
        self.title=title
        self.author=author
        self.publisher=publisher
        self.genre=genre
        self.price=price
        self.total_pages=pages
        self.available_copies=copies

    def issue_book(self):
        if self.available_copies>0:
            print("Book Issues!")
            self.available_copies-=1
        print("Available copies:",self.available_copies)


    def return_book(self):
            print("Book Returned!")
            self.available_copies+=1
            print("Available copies:",self.available_copies)

    def show_details(self):
        print(f"---Book Details---\n{self.book_id}\n{self.title}\n{self.author}\n{self.publisher}\n{self.genre}\n{self.price}\n{self.total_pages}\n{self.available_copies}")

    def update_price(self):
        n=int(input("Enter the updated price:"))
        self.price=n
        print("Updated price of Book:",self.price)

    def check_availability(self):
        if self.available_copies>0:
            print("Books Available for issue!")
        else:
            print("Not available")


obj1=library(1,"yoyo book","Avantika","Gurman","Comedy",520,400,2)
while True:
    print("Choose Menu:")
    print("1. issue_book\n2. return_book\n3. show_details\n4. update_price\n5. check_availability\n6. Exit")
    n=int(input())
    if n==1:
        obj1.issue_book()
    elif n==2:
        obj1.return_book()
    elif n==3:
        obj1.show_details()
    elif n==4:
        obj1.update_price()
    elif n==5:
        obj1.check_availability()
    elif n==6:
        break

    else:
        print("Enter Right choice for menu!")