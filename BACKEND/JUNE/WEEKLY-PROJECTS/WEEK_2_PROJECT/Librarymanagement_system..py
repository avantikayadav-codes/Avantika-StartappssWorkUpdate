#Librarymanagement_system..py

print("------------------------------------------\n           WELCOME TO LIBRARY\n"\
      "------------------------------------------")
books = {
    "The Alchemist": "Paulo Coelho",
    "Rich Dad Poor Dad": "Robert Kiyosaki",
    "Atomic Habits": "James Clear",
    "Think and Grow Rich": "Napoleon Hill",
    "The Psychology of Money": "Morgan Housel",
    "Ikigai": "Hector Garcia",
    "Wings of Fire": "A.P.J. Abdul Kalam",
    "The Power of Your Subconscious Mind": "Joseph Murphy",
    "The Monk Who Sold His Ferrari": "Robin Sharma",
    "Do Epic Shit": "Ankur Warikoo",
    "Harry Potter and the Philosopher's Stone": "J.K. Rowling",
    "The Hobbit": "J.R.R. Tolkien",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "The Catcher in the Rye": "J.D. Salinger",
    "The Kite Runner": "Khaled Hosseini",
    "A Thousand Splendid Suns": "Khaled Hosseini",
    "The Da Vinci Code": "Dan Brown"
}

def b():
    for key,value in books.items():
        if key==n:
            print(f"Book Found!\n Book Name-{key} : Author-{value}")
            break
    else:
        print("Book not found:(")



while True:
    print("Select An Option: \n1. Add Book\n2. View Books\n3. Search Book\n4. Issue Book\n5. Return Book\n6. Delete Book\n7. Exit")
    n=int(input("Enter Any one choice: "))
    if n==1:
        m=int(input("Enter No. of books to add: "))
        for i in range(1,m+1):
            book=input("Enter Book name: ")
            author=input("Enter author name: ")
            books[book]=author
        print("Book Added Successfully!")


    elif n==2:
        print("-----------\n  BOOKS\n-----------")
        print(books)


    elif n==3:
        n=input("Enter Book Name correctly to find Book:")
        b()


    elif n==4:
        n=input("Enter Book Name correctly to find Book for issue:")
        b()
        m=int(input("Enter No. of days to issue a Book: "))
        if m>30:
            print("You Can not issue a Book more than 30 days!")
        else:
            print("Book Issued! Please collect book ")


    elif n==5:
        n=input("Enter Book Name correctly to return Book:")
        for key,value in books.items():
            if key==n:
                print(f"Book Found!\n Book Name-{key} : Author-{value}")
                break
        else:
            print("The Book is not from this Library")
        m=int(input("Enter how much days its been from date of issue:"))
        if m<=30:
            print("Book returned Successfully!")
        else:
            print("You kept Book for more than 30 days, Please Pay the fine!")


    elif n==6:
        n=input("Enter Book Name correctly to delete a Book:")
        for key,value in books.items():
            if key==n:
                del books[key]
                break
        else:
            print("The Book is not from this Library")
        print("Books after deleting the book:",books)


    elif n==7:
        break

    else:
        print("choice not valid!")
print("Thank you for using libraray!\n           Have a Nice Day:)")
