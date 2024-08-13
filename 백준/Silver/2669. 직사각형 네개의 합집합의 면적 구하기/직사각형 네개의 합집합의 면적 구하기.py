coordinate = [[0 for i in range(100)] for i in range(100)]
cnt = 0

square = []
for i in range(4):
    square.append(list(map(int, input().split())))

for i in range(4):
    now_square = square[i]
    for x in range(now_square[0],now_square[2]):
        for y in range(now_square[1],now_square[3]):
            coordinate[x][y] = 1


for i in range(100):
    for j in range(100):
        if coordinate[i][j] == 1:
            cnt+=1
        
print(cnt)