words = ["python", "java", "c++", "javascript"]

li = [sum(1 for ch in l if ch in "aeiou") for l in words]
print(li)