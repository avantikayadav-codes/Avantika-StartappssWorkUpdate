#marks_total_average.py

marks=[]

for i in range(1,6):
    while True:
        mark=float(input(f"Enter the marks of subject {i}: "))
        if 0<=mark<=100:
            marks.append(mark)
            break
        else:
            print("Invalid Marks!")
print("Total marks obtained: ",sum(marks))
print("Average marks obtained: ",sum(marks)/len(marks))
print("Highest marks obtained: ",max(marks))
print("Lowest marks obtained: ",min(marks))