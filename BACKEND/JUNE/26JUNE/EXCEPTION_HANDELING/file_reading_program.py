try:
    file=input("Enter file name: ")
    f=open(file,"r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File Not Found")