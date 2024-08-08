import sys
from collections import deque

input = sys.stdin.readline

col,row,height = map(int, input().split())

tomato = []

#input data
for _ in range(height):
  now_tomato = []
  for __ in range(row):
    now_tomato.append(list(map(int, input().split())))
  tomato.append(now_tomato)

#상하좌우전후
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

stack = deque([])

for h in range(height):
  for x in range(row):
    for y in range(col):
      if tomato[h][x][y] == 1:
        stack.append([h,x,y])
while stack:
  now = stack.popleft()
  for i in range(6):
    new_h = now[0]+dx[i]
    new_x = now[1]+dy[i]
    new_y = now[2]+dz[i]
    if 0<=new_h<height and 0<=new_x<row and 0<=new_y<col:
      if tomato[new_h][new_x][new_y] == 0:
        tomato[new_h][new_x][new_y] = tomato[now[0]][now[1]][now[2]]+1
        stack.append([new_h,new_x,new_y])
    else:
      continue


riped = True
max_day = tomato[0][0][0]
for h in range(height):
  for x in range(row):
    for y in range(col):
      if tomato[h][x][y] == 0:
        print(-1)
        riped = False
        break
      else:
        max_day = max(max_day, tomato[h][x][y])
    if not riped:
      break
  if not riped:
    break    

if riped:
  print(max_day-1)