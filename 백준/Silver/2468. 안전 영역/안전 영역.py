from collections import deque

import sys

input = sys.stdin.readline

n = int(input())
graph = []
check_min = []
check_max = []

for i in range(n):
    now = list(map(int, input().split()))
    check_min.append(min(now))
    check_max.append(max(now))

    graph.append(now)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

mini = min(check_min)
maxi = max(check_max)

maxsafezones = 0
for water_height in range(mini, maxi+1):
    cnt = 0
    safezone = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > water_height:
                safezone[i][j] = 1

    for i in range(n):
        for j in range(n):
            if safezone[i][j] == 1:
                queue = deque([(i,j)])
                while queue:
                    now = queue.pop()
                    if safezone[now[0]][now[1]] == 1:
                        safezone[now[0]][now[1]] = 2
                    for direction in range(4):
                        next_x = now[0]+dx[direction]
                        next_y = now[1]+dy[direction]
                        if 0<=next_x<n and 0<=next_y<n:
                            if safezone[next_x][next_y] == 1:
                                queue.append((next_x,next_y))
                cnt += 1
    if cnt >= maxsafezones:
        maxsafezones = cnt

if maxsafezones == 0:
    print(1)
else:   
    print(maxsafezones)