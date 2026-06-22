def palin(n):
    m=(n[::-1])
    if m==n:
        print("String is palindrome")
    else:
        print("Not palindrome")


n=input("Enter a string to reverse: ")
palin(n)