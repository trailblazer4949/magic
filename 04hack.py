from collections import deque

q = deque(["a", "b", "c", "d", "e", "f"])

q.append(" ")
print(q)

q.append("g h i j k")
print(q)

q.popleft()
print(q)
