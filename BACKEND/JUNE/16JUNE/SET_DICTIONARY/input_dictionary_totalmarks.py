#input_dictionary_totalmarks.py
a={}
n=int(input("Enter total number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    a[name]=marks
print(a)

print("Total no. obtained by students are: ",sum(a.values()))
print("Average no. obtained by students are: ",sum(a.values())/len(a))
topper = max(a, key=a.get)
print("Topper: ",topper)
print("Marks: ",a[topper])
# print("The topper is: ",max(a.values()))
