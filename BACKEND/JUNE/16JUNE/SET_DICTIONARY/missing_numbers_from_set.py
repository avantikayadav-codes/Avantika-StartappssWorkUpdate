#missing_numbers_from_set.py

expected_set={1,2,3,4,5,6,7,8,9,10}

a=set()
print("Enter any 10 elements to compare with expected set: ")
for i in range(1,11):
    b=int(input())
    a.add(b)

print("Expected values missing from set:",expected_set-a)
