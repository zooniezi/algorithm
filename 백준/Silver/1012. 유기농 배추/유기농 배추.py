import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for testcase in range(t):
    m,n,seed = map(int, input().split())

    graph = [[0 for i in range(n)] for j in range(m)]


    for i in range(seed):
        row, col = map(int, input().split())
        graph[row][col] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    cnt = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] != 1:
                continue
            else:
                check = deque([(i,j)])
                already_visited = []
                while check:
                    now = check.pop()
                    already_visited.append(now)
                    graph[now[0]][now[1]] = 2
                    connected_place = []
                    for direction in range(4):
                        if 0<=now[0]+dx[direction]<m and 0<=now[1]+dy[direction]<n:
                            connected_place.append((now[0]+dx[direction],now[1]+dy[direction]))
                    for each in connected_place:
                        if each not in already_visited and graph[each[0]][each[1]] == 1:
                            check.append(each)
                cnt += 1

    print(cnt)