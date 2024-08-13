col, row = map(int,input().split())

board = [[0 for i in range(col)] for i in range(row)]

n = int(input())

for x in range(n):
    check, num = map(int, input().split())
    if check:
        for i in range(row):
            for j in range(num,col):
                board[i][j]+=2**x
    else:
        for i in range(num,row):
            for j in range(col):
                board[i][j]+=2**x

board_check = {}
for i in range(row):
    for j in range(col):
        if board[i][j] in board_check:
            board_check[board[i][j]]+=1
        else:
            board_check[board[i][j]]=1

max_surface = max(board_check.values())

print(max_surface)
