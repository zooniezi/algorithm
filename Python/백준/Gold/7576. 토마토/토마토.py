import sys
from collections import deque
input = sys.stdin.readline

#input
col, row = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(row)]



#make graph
dx = [0,0,1,-1]
dy = [1,-1,0,0]


check = deque([])
for i in range(row):
    for j in range(col):
        if tomato[i][j] == 1:
            check.append([i,j])
        else:
            continue

while check:
    now = check.popleft()
    graph = []
    for d in range(4):
        if 0<=now[0]+dx[d]<row and 0<=now[1]+dy[d]<col and tomato[now[0]+dx[d]][now[1]+dy[d]] != -1:
                graph.append([now[0]+dx[d],now[1]+dy[d]])
    for connected in graph:
        if tomato[connected[0]][connected[1]] == 0:
            tomato[connected[0]][connected[1]] = tomato[now[0]][now[1]] + 1
            check.append([connected[0],connected[1]])


max_tomato = tomato[0][0]
done = True
for i in range(row):
    for j in range(col):
        if tomato[i][j] == 0:
            done = False
        if tomato[i][j] > max_tomato:
            max_tomato = tomato[i][j]
if done:
    if max_tomato == 1:
        print(0)
    else:
        print(max_tomato-1)
else:
    print(-1)