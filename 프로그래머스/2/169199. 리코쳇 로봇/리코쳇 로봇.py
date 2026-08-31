from collections import deque

def solution(board):
    queue = deque([])
    lenx = len(board)
    leny = len(board[0])
    startx, starty, goalx, goaly = 0,0,0,0
    
    for i in range(lenx):
        for j in range(leny):
            if board[i][j] == 'R':
                startx = i
                starty = j
                queue.append((i,j,0))
            if board[i][j] == 'G':
                goalx = i
                goaly = j
                
    visited = [[-1 for i in range(len(board[0]))]for j in range(len(board))]
    visited[startx][starty] = 0
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    
    while queue:
        nowx, nowy, num_move = queue.popleft()
        print(nowx,nowy)
        for i in range(4):
            dx = x[i]
            dy = y[i]
            tempx, tempy = nowx, nowy
            while True:
                if tempx+dx<0 or tempx+dx>=lenx or tempy+dy<0 or tempy+dy>=leny:
                    break
                if board[tempx+dx][tempy+dy] == 'D':
                    break
                tempx = tempx+dx
                tempy = tempy+dy
            if tempx == goalx and tempy == goaly:
                return (num_move+1)
                
            if visited[tempx][tempy] == -1:
                visited[tempx][tempy] = num_move+1
                queue.append((tempx,tempy,num_move+1))
            
    answer = -1
    return answer