# A = int(input("Enter No. A: "))
# B = int(input("Enter No. B: "))
# C = int(input("Enter No. C: "))
# D = int(input("Enter No. D: "))
# E = int(input("Enter No. E: "))
# if (A>B and A>C and A>D and A>E):
#     print("A is the greater")
# elif (B>C and B>D and B>E):
#     print("B is greater")
# elif (C>D and C>E):
#     print("C is greater")
# elif(D>E):
#     print("D is greater")
# else:
#     print("E is greater")



# n=int(input("Enter the number of elements:"))
# list=[]
# for i in range(n):
#     val=int(input(f"enter the {i} number: "))
#     list.append(val)
# biggest=list[0]
# for i in range(1,n):
#         if list[i]>biggest:
#             biggest=list[i]
# print("Biggest NO. is:", biggest)


#0,10,20,30,5
largest=int(input("Enter number 1: "))
for i in range(2,6):
     a=int(input(f"Enter number {i}: "))
     if a>largest:
          largest=a
print("Largest no. is", largest)
