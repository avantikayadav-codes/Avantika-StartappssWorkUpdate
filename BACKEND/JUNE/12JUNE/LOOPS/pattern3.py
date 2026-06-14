for i in range(0,5,1):
    for j in range(0,i+1):
        print("*",end=" ")
    for k in range(0,2*(5-i)):
        print(" ",end=" ")
    for l in range(0,i+1):
        print("*",end=" ")
    print()

for i in range(0,5,1):
    for j in range(0,5-i):
        print("*",end=" ")
    for k in range(0,i+1):
        print("   ",end=" ")
    for l in range(0,5-i):
        print("*",end=" ")
    print()