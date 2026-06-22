def student(**kwargs):
    count=0
    for i,j in kwargs.items():
        count+=1
        print(i,":",j)
    print("Number of argumnets passed are: ",count)

student(name="Avantka",Age=22,Subject="Python")