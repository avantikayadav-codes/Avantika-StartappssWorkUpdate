#Longest_string_find_in_sentence.py

a=input("Enter the sentence: ")
word=a.split()

longest=word[0]
for i in word:
    if len(i)>len(longest):
        longest=i
print("Longest word: ",longest)



# longest=word[0]
# for i in range(len(word)):
#     if len(word[i])>len(longest):
#         longest=word[i]
# print("Longest word: ",longest)
