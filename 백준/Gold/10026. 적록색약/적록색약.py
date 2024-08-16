import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
color = []
for i in range(n):
    color.append(list(map(str,input().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = [[False for _ in range(n)] for _ in range(n)]
cnt_color = 0
cnt_blind = 0

for i in range(n):
    for j in range(n):
        if not check[i][j]:
            queue = deque([(i,j)])
            while queue:
                now = queue.pop()
                for d in range(4):
                    if 0<=now[0]+dx[d]<n and 0<=now[1]+dy[d]<n:
                        if color[now[0]+dx[d]][now[1]+dy[d]] == color[now[0]][now[1]]:
                            if check[now[0]+dx[d]][now[1]+dy[d]] == 0:
                                queue.append((now[0]+dx[d],now[1]+dy[d]))
                check[now[0]][now[1]] = True
            cnt_color+=1

for i in range(n):
    for j in range(n):
        if color[i][j] == 'G':
            color[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if check[i][j]:
            queue = deque([(i,j)])
            while queue:
                now = queue.pop()
                for d in range(4):
                    if 0<=now[0]+dx[d]<n and 0<=now[1]+dy[d]<n:
                        if color[now[0]+dx[d]][now[1]+dy[d]] == color[now[0]][now[1]]:
                            if check[now[0]+dx[d]][now[1]+dy[d]] == 1:
                                queue.append((now[0]+dx[d],now[1]+dy[d]))
                check[now[0]][now[1]] = False
            cnt_blind+=1


print(cnt_color, cnt_blind)