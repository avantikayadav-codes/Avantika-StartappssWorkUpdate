try:
    marks=int(input("Enter Marks: "))
    if marks<0:
        raise Exception("Marks cannot be negative")
    elif marks>100:
        raise Exception("Marks cannot exceed 100")
    print("Valid Marks")
except Exception as e:
    print(e)