row=int(input("Enter no. of row.: "))
column=int(input("Enter no. of column: "))

matrix=[]
for i in range(0,row,1):
    temp=[]
    for j in range(0,column,1):
        value=int(input(f"enter value of row {i} and column {j}: "))
        temp.append(value)
    matrix.append(temp)

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")