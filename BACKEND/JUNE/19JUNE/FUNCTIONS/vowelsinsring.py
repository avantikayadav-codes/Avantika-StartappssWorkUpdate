def vow(n):
    count=0
    for i in n:
        if i in "aeiouAEIOU":
            count+=1
    return count
    
n=input("Enter a string: ")
print("No. of vowels are: ",vow(n))