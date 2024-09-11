import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

parent = [0 for i in range(n+1)]
queue = deque([1])
while queue:
    now = queue.popleft()

    for each in graph[now]:
        if parent[each] == 0:
            parent[each] = now
            queue.append(each)

for i in range(2,n+1):
    print(parent[i])