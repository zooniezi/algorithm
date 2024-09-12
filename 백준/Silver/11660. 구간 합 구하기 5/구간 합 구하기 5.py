import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

sums = [[0 for i in range(n)] for i in range(n)]

sums[0][0] = arr[0][0]
for i in range(1,n):
    sums[0][i] = arr[0][i]+sums[0][i-1]
    sums[i][0] = arr[i][0]+sums[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        sums[i][j] = arr[i][j]+sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]


for i in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    x1-=1
    x2-=1
    y1-=1
    y2-=1
    total = sums[x2][y2]
    if x1>0:
        total-=sums[x1-1][y2]
    if y1>0:
        total-=sums[x2][y1-1]
    if x1>0 and y1>0:
        total += sums[x1-1][y1-1]
    print(total)