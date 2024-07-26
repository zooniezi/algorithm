import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
num_of_edges = int(input())

graph = [[] for i in range(n+1)]
chon = [0 for i in range(n+1)]
for i in range(num_of_edges):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)


check = deque([a])
chon[a] = 0
already_visited = []

while check:
    now = check.popleft()
    #종료 조건 설정
    if now == b:
        break
    if now not in already_visited:
        already_visited.append(now)
        for each in graph[now]:
            check.append(each)
            if chon[each] == 0:
                chon[each] = chon[now]+1

if chon[b] == 0:
    print(-1)
else:
    print(chon[b])
