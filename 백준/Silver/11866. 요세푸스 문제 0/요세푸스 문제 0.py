from collections import deque

n, k = map(int, input().split())

arr = []
queue = deque()

for i in range(n):
    queue.append(i+1)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, arr)), end="")
print(">")