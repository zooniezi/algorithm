import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

ans = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    stack = []
    stack.append(i)
    visited = []
    while stack:
        now = stack.pop()
        for x in range(n):
            if graph[now][x] == 1:
                if x not in visited:
                    stack.append(x)
                    ans[i][x] = 1
                    visited.append(x)

for i in range(n):
    print(*ans[i])
