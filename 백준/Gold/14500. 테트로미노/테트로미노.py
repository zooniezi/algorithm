row, col = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(row)]


iblock = [(0,0),(1,0),(2,0),(3,0)]
iblock2 = [(0,0),(0,1),(0,2),(0,3)]

oblock = [(0,0),(0,1),(1,0),(1,1)]

jblock = [(0,0),(1,0),(2,0),(2,-1)]
jblock1 = [(0,0),(1,0),(2,0),(2,1)]
jblock2 = [(0,0),(0,1),(0,2),(-1,2)]
jblock3 = [(0,0),(0,1),(0,2),(1,2)]
jblock4 = [(0,0),(0,1),(0,2),(-1,0)]
jblock5 = [(0,0),(0,1),(0,2),(1,0)]
jblock6 = [(0,0),(1,0),(2,0),(0,1)]
jblock7 = [(0,0),(1,0),(2,0),(0,-1)]

sblock = [(0,0),(1,0),(1,1),(2,1)]
sblock1 = [(0,0),(0,1),(-1,1),(-1,2)]

zblock = [(0,0),(1,0),(1,-1),(2,-1)]
zblock1 = [(0,0),(0,1),(1,1),(1,2)]

tblock = [(0,0),(0,1),(0,2),(1,1)]
tblock1 = [(0,0),(0,1),(0,2),(-1,1)]
tblock2 = [(0,0),(1,0),(2,0),(1,1)]
tblock3 = [(0,0),(1,0),(2,0),(1,-1)]

tetromino = [iblock, iblock2, oblock, jblock, jblock1,jblock2,jblock3,jblock4,jblock5,jblock6,jblock7, sblock,sblock1, zblock,zblock1, tblock,tblock1,tblock2,tblock3]

maxsum = 0
for i in range(row):
    for j in range(col):
        for block in tetromino:
            available = True
            nowsum = 0
            for coor in range(4):
                if 0<=i+block[coor][0]<row and 0<=j+block[coor][1]<col:
                    nowsum+=matrix[i+block[coor][0]][j+block[coor][1]]
                    continue
                else:
                    available = False
                    break
            if available:
                if maxsum < nowsum:
                    maxsum = nowsum

print(maxsum)

