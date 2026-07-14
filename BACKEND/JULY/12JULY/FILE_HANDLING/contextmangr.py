with open("new2.txt","a+") as file:
    file.write("\nHello")
    file.seek(0)
    print(file.read())