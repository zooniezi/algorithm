from collections import deque
import sys
input = sys.stdin.readline

node_num, edge_num = map(int,input().split())

graph = [[] for _ in range(node_num+1)]
for _ in range(edge_num):
    vertex1, vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

visited = []
check = deque([])
ans = 0
for node in range(1,node_num+1):
    if node not in visited:
        check.append(node)
        ans += 1
    while check:
        now_node = check.pop()
        if now_node not in visited:
            visited.append(now_node)
            for each in graph[now_node]:
                check.append(each)

    
print(ans)