"""6.
Implement Stack using deque.
Methods
push()
pop()
peek()
is_empty()
"""

from collections import deque
d=deque([1,2,3])
d.append(4)
d.appendleft(0)
d.pop()
d.popleft()
print(d.index(3))
print(d)

