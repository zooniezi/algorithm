import sys
from collections import deque
input = sys.stdin.readline

board_size = int(input())
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
num_apple = int(input())
for i in range(num_apple):
    x,y = map(int, input().split())
    board[x-1][y-1] = 2


num_change_direction = int(input())
directions = []
for i in range(num_change_direction):
    info = list(map(str, input().split()))
    info[0] = int(info[0])
    directions.append(info)


def change_direction(rotation, direction_num):
    if rotation == 'L':
        return (direction_num-1)%4
    if rotation == 'D':
        return (direction_num+1)%4


now_time = 0
now_direction = [[0,1],[1,0],[0,-1],[-1,0]]

board[0][0]=1
snake = deque([[0,0]])
head = [0,0]
tail = [0,0]
now = 0

while True:
    now_time+=1
    now_head = [head[0]+now_direction[now][0], head[1]+now_direction[now][1]]
    if 0<=now_head[0]<board_size and 0<=now_head[1]<board_size:
        if board[now_head[0]][now_head[1]] == 1:
            break
        else:
            if board[now_head[0]][now_head[1]] == 2:
                board[now_head[0]][now_head[1]] = 1
                snake.append([now_head[0],now_head[1]])
            else:
                board[now_head[0]][now_head[1]] = 1
                snake.append([now_head[0],now_head[1]])
                board[snake[0][0]][snake[0][1]] = 0
                snake.popleft()
            head = now_head
    else:
        break
    
    if directions and now_time == directions[0][0]:
        now = change_direction(directions[0][1], now)
        directions.pop(0)


print(now_time)
