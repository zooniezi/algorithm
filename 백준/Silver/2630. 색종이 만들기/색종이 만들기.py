import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result_0 = 0
result_1 = 0
def make_paper(x,y,n):
    color = arr[x][y]
    global result_0, result_1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                make_paper(x,y,n//2)
                make_paper(x+n//2, y, n//2)
                make_paper(x,y+n//2, n//2)
                make_paper(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result_0+=1
    else:
        result_1+=1
make_paper(0,0,N)
print(result_0)
print(result_1)
