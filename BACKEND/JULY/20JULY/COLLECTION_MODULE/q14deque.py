from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
win=deque()
k=3
answer=[]
for i in range(k):
    win.append(nums[i])
answer.append(max(win))
for i in range(k,len(nums)):
    win.popleft()
    win.append(nums[i])
    answer.append(max(win))
print(answer)